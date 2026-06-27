from sqlalchemy.orm import Session
from models import LeaveBalance, Salary, Payslip, PerformanceReview
from typing import Optional

class HrSqlRagService:
    def __init__(self, db: Session):
        self.db = db

    def get_leave_balance(self, user_id: int) -> str:
        leave_balance = self.db.query(LeaveBalance).filter(LeaveBalance.user_id == user_id).first()
        if not leave_balance:
            return f"No Employee with ID {user_id}"
        
        return f"LeaveBalance for Id {leave_balance.id}, annual leaves: {leave_balance.annual_leave} |used_annual {leave_balance.used_annual}| Remaining {leave_balance.annual_leave - leave_balance.used_annual}| sick leave {leave_balance.sick_leave} |used_sick {leave_balance.used_sick} |Remaining {leave_balance.sick_leave - leave_balance.used_sick}"

    def get_salary(self, user_id: int) -> str:
        salaries = self.db.query(Salary).filter(Salary.user_id == user_id).order_by(Salary.month.desc()).all()
        if not salaries:
            return f"No salary found for this Id {user_id}"
        
        result = []
        for s in salaries:
            result.append(f"Month: {s.month} | Basic: {s.basic_salary:.2f} | Allowances: {s.allowances:.2f} | Deductions: {s.deductions:.2f} | Net: {s.net_salary:.2f}")
        return "\n".join(result)

    def get_payslip(self, user_id: int) -> str:
        payslips = self.db.query(Payslip).filter(Payslip.user_id == user_id).order_by(Payslip.month.desc()).all()
        if not payslips:
            return f"No payslip for this Id {user_id}"
        
        result = []
        for p in payslips:
            result.append(f"Month: {p.month} | Gross: {p.gross_pay:.2f} | Tax: {p.tax_deducated:.2f} | Net Pay: {p.net_pay:.2f} | Generated: {p.generated_date}")
        return "\n".join(result)

    def get_review(self, user_id: int) -> str:
        reviews = self.db.query(PerformanceReview).filter(PerformanceReview.user_id == user_id).order_by(PerformanceReview.review_period.desc()).all()
        if not reviews:
            return f"No Reviews for this Id {user_id}"
        
        result = []
        for p in reviews:
            result.append(f"Period: {p.review_period} | Rating: {p.rating} | Comments: {p.comments} | Reviewer: {p.reviewer}")
        return "\n".join(result)