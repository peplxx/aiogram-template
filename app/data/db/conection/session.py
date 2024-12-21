import ssl
from threading import Lock

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.data.config import get_settings

settings = get_settings()


class SessionManager:
    _instance = None
    _lock = Lock()

    def __init__(self) -> None:
        self.refresh()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(SessionManager, cls).__new__(cls)
                cls._instance.refresh()
            return cls._instance

    def get_session_maker(self) -> sessionmaker:
        if not hasattr(self, 'session_maker'):
            self.session_maker = sessionmaker(self.engine, class_=AsyncSession, expire_on_commit=False)
        return self.session_maker

    def default_engine(self):
        self.engine = create_async_engine(
            get_settings().database_uri,
            future=True
        )

    def refresh(self) -> None:
        self.default_engine()


def get_session() -> AsyncSession:
    session_maker = SessionManager().get_session_maker()
    return session_maker()
