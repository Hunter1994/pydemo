from pydantic import BaseModel, Field

# 定义 Company 模型
class Company(BaseModel):
    id: int
    username: str  # 在 Company 类中使用 'username' 字段

# 定义 CompanyDto 模型，并将 'user_name' 设置为 'username' 的别名
class CompanyDto(BaseModel):
    id: int
    user_name: str = Field(..., alias='username')  # 'user_name' 映射到 'username'

    class Config:
        # 配置 Pydantic 模型使用别名
        orm_mode = True

# 示例：将 Company 转换为 CompanyDto
company = Company(id=1, username='AcmeInc')

# 使用 Pydantic 的 `dict` 方法转换 Company 对象为字典格式
company_dict = company.dict()

# 使用 dict 中的数据创建 CompanyDto 对象（自动映射）
company_dto = CompanyDto(**company_dict)

# 输出映射后的 CompanyDto 对象
print(company_dto.json())  # 输出：{"id": 1, "user_name": "AcmeInc"}
