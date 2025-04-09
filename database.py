from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models import Base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = "sqlite+aiosqlite:///./digital_farm.db"

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

async def get_all_fields():
    async with AsyncSessionLocal() as session:
        result = await session.execute("SELECT * FROM fields")
        return result.fetchall()

async def get_field(field_id: int):
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            "SELECT * FROM fields WHERE id = :field_id",
            {"field_id": field_id}
        )
        return result.fetchone()

async def create_farmer(name: str, phone: str, email: str, password_hash: str):
    async with AsyncSessionLocal() as session:
        new_farmer = Farmer(
            name=name,
            phone=phone,
            email=email,
            password_hash=password_hash
        )
        session.add(new_farmer)
        await session.commit()
        return new_farmer

async def get_farmer_by_email(email: str):
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            "SELECT * FROM farmers WHERE email = :email",
            {"email": email}
        )
        return result.fetchone()
