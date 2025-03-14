from pydantic import BaseModel

# 定义用户创建时的数据模型
class UserCreate(BaseModel):
    name: str
    email: str
    age: int = None

# 定义用户返回时的数据模型
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int = None

    class Config:
        orm_mode = True  # 允许从 ORM 对象转换为 Pydantic 模型