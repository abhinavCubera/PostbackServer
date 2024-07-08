import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    db_url: str = os.getenv("DATABASE_URL", "postbackdb.cju6ymo0wzq0.ap-south-1.rds.amazonaws.com")
    db_name: str = os.getenv("DB_NAME", "postgres")
    db_username: str = os.getenv("DB_USERNAME", "postgres")
    db_password: str = os.getenv("DB_PASSWORD", "Cubera2024$")
    db_tablename: str = os.getenv("DB_TABLENAME", "postbacks")
    db_port: int = int(os.getenv("DB_PORT", 5432))

    @property
    def database_url(self) -> str:
        return f"postgresql://{self.db_username}:{self.db_password}@{self.db_url}:{self.db_port}/{self.db_name}"

settings = Settings()



# import os
# from pydantic import BaseSettings

# class Settings(BaseSettings):
#     db_url: str = os.getenv("DATABASE_URL", "postgresql://postgres:Cubera2024$@postbackdb.cju6ymo0wzq0.ap-south-1.rds.amazonaws.com/postgres")

# settings = Settings()
