from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    department = Column(String, nullable=True)
    roles = Column(String, default="ROLE_USER")

class LeaveBalance(Base):
    __tablename__ = "leave_balance"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    annual_leave = Column(Integer, default=21)
    used_annual = Column(Integer, default=0)
    sick_leave = Column(Integer, default=10)
    used_sick = Column(Integer, default=0)

class Salary(Base):
    __tablename__ = "salary"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    month = Column(String, nullable=False)
    basic_salary = Column(Float, nullable=False)
    allowances = Column(Float, default=0)
    deductions = Column(Float, default=0)
    net_salary = Column(Float, nullable=False)

class Payslip(Base):
    __tablename__ = "payslip"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    month = Column(String, nullable=False)
    gross_pay = Column(Float, nullable=False)
    tax_deducated = Column(Float, default=0)
    net_pay = Column(Float, nullable=False)
    generated_date = Column(String, nullable=False)

class PerformanceReview(Base):
    __tablename__ = "performance_review"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    review_period = Column(String, nullable=False)
    rating = Column(String, nullable=False)
    comments = Column(String, nullable=True)
    reviewer = Column(String, nullable=False)