from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String
from database import Base

# 定义用户返回时的数据模型
class Project(BaseModel):
    id: int
    name: str
    email: str
    age: int = None

    class Config:
        orm_mode = True  # 允许从 ORM 对象转换为 Pydantic 模型
        # 使用 alias_generator 来自动映射字段别名
        alias_generator = lambda string: string.lower()

# 定义数据库模型
class DBProject(Base):
    __tablename__ = "projects"  # 这里你应该使用一个合适的表名
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer, nullable=True)
    project_name = Column(String(200), nullable=True)

# 创建 Pydantic 模型实例
usermodel = Project(id=1, name="zhangsan", email="123@qq.com", age=18)

# 使用 Pydantic 模型的 dict 方法来传递字段，并映射到 DBProject
db = DBProject(**usermodel.model_dump())  # Pydantic 模型会自动处理别名映射
print("输出：")

print(db.name)
print(db.age)
print(db.project_name)
