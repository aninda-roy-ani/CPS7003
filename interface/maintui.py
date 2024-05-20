
class MainTUI:

    def start(self):
        print('''
        ST. MARY'S MED TECH HEALTHCARE
        ------------------------------
        What do you want to do?
        1. Guest Login (For Patients)
        2. Login as an existing User(For Staffs)
        3. Sign up as a New User(For Staffs)
        Enter your choice: ''')
        choice = input()
        if choice == '1':
            print()
