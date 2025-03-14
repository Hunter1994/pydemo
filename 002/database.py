from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL 连接 URL
SQLALCHEMY_DATABASE_URL="mysql+pymysql://zhangdi0807:20190807@192.168.1.59:3306/salary_payment_standard_new?charset=utf8mb4"
# 创建数据库引擎
engine =create_engine(SQLALCHEMY_DATABASE_URL)
# 创建 SessionLocal 类，用于数据库会话
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
# 声明基类，用于定义模型
Base=declarative_base()
