import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



class DBConnectionHandler:

    """Class that handles all database connections, engines and session."""

    def __init__(self) -> None:
        self.__user = os.environ.get("POSTGRES_USER")
        self.__password = os.environ.get("POSTGRES_PASS")
        self.__host = os.environ.get("POSTGRES_HOST")
        self.__port = os.environ.get("DB_PORT")
        self.__database = os.environ.get("POSTGRES_DATABASE")
        self.__connection_string = f"postgresql://{self.__user}:{self.__password}@{self.__host}:{self.__port}/{self.__database}"  # pylint: disable=max-line-length
        self.__engine = self.__create_database_engine()
        self.session = None

    def get_engine(self):
        """
        Return connection Engine.

        :parram - None
        :return - engine connection to Database.

        """
        return self.__engine

    def __create_database_engine(self):
        """
        creates the database engine.

        Returns:
            _type_: engine

        """
        engine = create_engine(
            self.__connection_string,
            echo=False,
            pool_size=1,
            max_overflow=0,
            pool_recycle=3600,
            pool_pre_ping=True,
            pool_use_lifo=True,
        )
        return engine

    def __enter__(self):
        """
        Context manager that will handle session, and make sure no errors
        occurr when doing it.

        Returns:
            _type_: self

        """
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine, expire_on_commit=False)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Context manager that will handle session, and make sure the session
        will be closed.

        Args:
            exc_type (_type_): default method param
            exc_val (_type_): default method param
            exc_tb (_type_): default method param

        """
        self.session.close_all()  # pylint: disable=no-member
