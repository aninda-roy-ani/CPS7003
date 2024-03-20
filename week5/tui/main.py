from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from week5.database.university import DATABASE_PATH
from week5.tui.role_tui import RoleTUI

if __name__ == "__main__":
    # Create SQLAlchemy engine
    engine = create_engine(DATABASE_PATH)

    # Create session
    session = sessionmaker(bind=engine)

    # Instantiate RoleTUI and pass session object
    role_tui = RoleTUI(session)
    role_tui.menu()