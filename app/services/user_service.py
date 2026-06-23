from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repository.user_repo import UserRepository
from app.schemas.user import UserInCreate, UserOutput, UserInLogin, UserWithToken
from app.core.security import get_password, verify_password, sign_jwt


class UserService:

    def __init__(self, session: AsyncSession):
        self.user_repository = UserRepository(session=session)

    async def signup(self, user_details: UserInCreate) -> UserOutput:
        if await self.user_repository.user_exist_by_email(email=user_details.email):
            raise HTTPException(status_code=400, detail="Email already registered. Please log in.")

        hashed_password = get_password(plain=user_details.password)
        user_details.password = hashed_password
        return await self.user_repository.create_user(user_data=user_details)

    async def login(self, login_details: UserInLogin) -> UserWithToken:
        user = await self.user_repository.get_user_by_email(email=login_details.email)
        if not user:
            raise HTTPException(status_code=400, detail="No account found. Please sign up.")

        if not verify_password(plain=login_details.password, hashed=user.password):
            raise HTTPException(status_code=400, detail="Invalid password. Please try again.")

        token = sign_jwt(user_id=user.id)
        return UserWithToken(token=token)

    async def get_user_by_id(self, user_id) -> UserOutput:
        user = await self.user_repository.get_user_by_id(user_id=user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user