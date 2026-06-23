from sqlalchemy import select
from app.db.repository.base import BaseRepository
from app.models.user import User
from app.schemas.user import UserInCreate


class UserRepository(BaseRepository):

    async def create_user(self, user_data: UserInCreate) -> User:
        new_user = User(**user_data.model_dump(exclude_none=True))
        self.session.add(new_user)
        await self.session.flush()
        await self.session.refresh(new_user)
        return new_user

    async def user_exist_by_email(self, email: str) -> bool:
        result = await self.session.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none() is not None

    async def get_user_by_email(self, email: str) -> User | None:
        result = await self.session.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def get_user_by_id(self, user_id) -> User | None:
        result = await self.session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()