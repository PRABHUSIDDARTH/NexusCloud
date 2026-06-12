from cryptography.fernet import Fernet
from app.core.config import settings

_fernet = Fernet(settings.ENCRYPTION_KEY.encode())


def encrypt(plain_text: str) -> str:
    """Encrypt a credential string before storing in DB."""
    return _fernet.encrypt(plain_text.encode()).decode()


def decrypt(cipher_text: str) -> str:
    """Decrypt a credential string retrieved from DB."""
    return _fernet.decrypt(cipher_text.encode()).decode()
