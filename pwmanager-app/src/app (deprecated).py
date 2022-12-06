from console_io import ConsoleIO
from services.user_service import UserService

class PasswordManagerApp:
    def __init__(self):
        self._io = ConsoleIO()
        self._user_service = UserService()
        self._user = None

    def run(self):
        self.print_initial()

        while True:
            if self._user:
                self.print_home_instructions()
                command = self._io.cin("Command: ")
                if command=="1":
                    self.add_password_entry()
                elif command=="2":
                    self.delete_password_entry()
                elif command=="3":
                    self._io.newline()
                    self._user = None
                    self._io.cout("Log-out successful!")
            else:
                self.print_auth_instructions()
                command = self._io.cin("Command: ")

                if command=="1":
                    self.login()
                elif command=="2":
                    self.create_account()
                elif command=="3":
                    self._io.newline()
                    self._io.cout("Bye, see you soon!")
                    break


    def print_auth_instructions(self):
        self._io.newline()
        self._io.cout("Welcome, Press:")
        self._io.newline()
        self._io.cout("[1]	To Log-In")
        self._io.cout("[2]	To Create an Account")
        self._io.cout("[3]	To Exit")
        self._io.newline()

    def print_home_instructions(self):
        self._io.newline()
        self._io.cout(f"Welcome {self._user.username}, Press:")
        self._io.newline()
        self._io.cout("[1]	To Add a new app-password entry")
        self._io.cout("[2]	To Remove an app-password entry")
        self._io.cout("[3]	To Log-out")
        self._io.newline()
        self._io.cout("Your app-password database:")
        self.get_user_passwords()
        self._io.newline()

    def print_initial(self):
        self._io.cout("-------------------------------------------------")
        self._io.cout("|	Password Manager v1			|")
        self._io.cout("-------------------------------------------------")


    def create_account(self):
        self._io.newline()
        self._io.cout("Please input a username and password to create your account:")
        username_input = self._io.cin("Username: ")
        password_input = self._io.cin("Password: ")
        check = self._io.cin("Confirm (y/n): ")
        if(check=="" or check=="y" or check=="yes"):
            resp = self._user_service.create_account(username_input,password_input)
            self._io.newline()
            if resp=="Account created successfully":
                self._io.cout(
                    "Account created successfully, you can now log-in with your credentials!"
                    )
            else:
                self._io.cout(resp)
        else:
            self._io.cout("No worries, we will cancel that!")

    def login(self):
        self._io.newline()
        self._io.cout("Please input your username and password: ")
        username_input = self._io.cin("Username: ")
        password_input = self._io.cin("Password: ")
        user = self._user_service.authenticate(username_input,password_input)
        if user:
            self._user = user
            self._io.cout("Logged in successfully!")
        else:
            self._io.cout("Error, incorrect credentials")
        self._io.newline()

    def get_user_passwords(self):
        self._io.newline()
        self._io.cout("App - Password")
        self._io.cout("-------------------------------------------------")
        list_of_password_items = self._user_service.get_all_user_passwords()
        for item in list_of_password_items:
            self._io.cout(f"{item.app} - {item.password}")

    def add_password_entry(self):
        self._io.newline()
        self._io.cout("Please input app name and password:")
        app_input = self._io.cin("App: ")
        password_input = self._io.cin("Password: ")
        check = self._io.cin("Confirm (y/n): ")
        if check=="" or check=="y" or check=="yes":
            self._user_service.add_password(app_input,password_input)
            self._io.newline()
            self._io.cout("Password item added successfully!")
        else:
            self._io.cout("No worries, we will cancel that!")

    def delete_password_entry(self):
        self._io.newline()
        self._io.cout("Please input app name associated with entry: ")
        app_input = self._io.cin("App: ")
        check = self._io.cin("Confirm (y/n): ")
        if check=="" or check=="y" or check=="yes":
            status = self._user_service.delete_password(app_input)
            self._io.newline()
            self._io.cout(status)
        else:
            self._io.cout("No worries, we will cancel that!")