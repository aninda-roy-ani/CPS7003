from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from week5.database.university import DATABASE_PATH
from week5.tui.role_tui import RoleTUI


class MainTUI:

    def __init__(self):
        self.role_tui = RoleTUI()

    def run(self):

        while True:
            print("""
Welcome to University Management System
----------------------------------------

Select a service: 
1. Role
2. User
3. Course
4. Module
5. Tutor
[Enter 0 to exit]
            """)

            selection = input()
            print()
            if selection.isnumeric():
                selection = int(selection)
                if selection == 0:
                    print("Thank you for using this system")
                    break
                elif selection == 1:
                    self.role_tui.menu()
                else:
                    print("Wrong Input")
            else:
                print("Error Input")
                break


if __name__ == "__main__":
    # Create SQLAlchemy engine
    engine = create_engine(f"sqlite:///{DATABASE_PATH}")

    # Create session
    session = sessionmaker(bind=engine)

    # Create MainTUI
    main = MainTUI()

    # RUN
    main.run()
