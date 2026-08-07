class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username_input = "#userEmail"
        self.password_input = "#userPassword"
        self.login_button = "#login"
        self.sidebar = "#sidebar"

    def open(self):
        self.page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    def enter_username(self, username):
        self.page.fill(self.username_input, username)

    def enter_password(self, password):
        self.page.fill(self.password_input, password)

    def click_login(self):
        self.page.click(self.login_button)

    def is_logged_in(self):
        return self.page.locator(self.sidebar).is_visible()


