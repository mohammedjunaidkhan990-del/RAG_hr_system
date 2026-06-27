from sqlalchemy.orm import Session
from database import SessionLocal, create_tables
from models import User, LeaveBalance, Salary, Payslip, PerformanceReview
from auth import get_password_hash

def init_database():
    # Create tables
    create_tables()
    
    db = SessionLocal()
    try:
        # Create sample users
        users_data = [
            {"username": "john_doe", "password": "password123", "department": "Engineering"},
            {"username": "jane_smith", "password": "password123", "department": "HR"},
            {"username": "mike_wilson", "password": "password123", "department": "Finance"}
        ]
        
        for user_data in users_data:
            existing_user = db.query(User).filter(User.username == user_data["username"]).first()
            if not existing_user:
                user = User(
                    username=user_data["username"],
                    password=get_password_hash(user_data["password"]),
                    department=user_data["department"],
                    roles="ROLE_USER"
                )
                db.add(user)
                db.commit()
                db.refresh(user)
                
                # Add leave balance
                leave_balance = LeaveBalance(
                    user_id=user.id,
                    annual_leave=21,
                    used_annual=5,
                    sick_leave=10,
                    used_sick=2
                )
                db.add(leave_balance)
                
                # Add salary data
                salaries = [
                    {"month": "2024-03", "basic_salary": 5000.00, "allowances": 800.00, "deductions": 300.00, "net_salary": 5500.00},
                    {"month": "2024-02", "basic_salary": 5000.00, "allowances": 800.00, "deductions": 300.00, "net_salary": 5500.00},
                    {"month": "2024-01", "basic_salary": 4800.00, "allowances": 750.00, "deductions": 280.00, "net_salary": 5270.00}
                ]
                
                for salary_data in salaries:
                    salary = Salary(user_id=user.id, **salary_data)
                    db.add(salary)
                
                # Add payslip data
                payslips = [
                    {"month": "2024-03", "gross_pay": 5800.00, "tax_deducated": 580.00, "net_pay": 5220.00, "generated_date": "2024-03-31"},
                    {"month": "2024-02", "gross_pay": 5800.00, "tax_deducated": 580.00, "net_pay": 5220.00, "generated_date": "2024-02-29"},
                    {"month": "2024-01", "gross_pay": 5550.00, "tax_deducated": 555.00, "net_pay": 4995.00, "generated_date": "2024-01-31"}
                ]
                
                for payslip_data in payslips:
                    payslip = Payslip(user_id=user.id, **payslip_data)
                    db.add(payslip)
                
                # Add performance review data
                reviews = [
                    {"review_period": "Q1-2024", "rating": "Exceeds Expectations", "comments": "Excellent technical delivery and team collaboration", "reviewer": "Manager A"},
                    {"review_period": "Q4-2023", "rating": "Meets Expectations", "comments": "Consistent performance with good results", "reviewer": "Manager A"}
                ]
                
                for review_data in reviews:
                    review = PerformanceReview(user_id=user.id, **review_data)
                    db.add(review)
        
        db.commit()
        print("Database initialized with sample data!")
        
    except Exception as e:
        print(f"Error initializing database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_database()