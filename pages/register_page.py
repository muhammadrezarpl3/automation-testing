class RegisterPage:

    def __init__(self, page):
        self.page = page
        self.first_name = "#firstName"
        self.last_name = "#lastName"
        self.email = "#userEmail"
        self.mobile = "#userMobile"
        self.occupation = '[formcontrolname="occupation"]'
        self.male_radio = 'input[formcontrolname="gender"][value="Male"]'
        self.female_radio = 'input[formcontrolname="gender"][value="Female"]'
        self.password = "#userPassword"
        self.confirm_password = "#confirmPassword"
        self.age_checkbox = 'input[formcontrolname="required"]'
        self.register_button = "#login"
        self.success_message = self.page.get_by_text(
            "Account Created Successfully",
            exact=True
        )
    def open(self):
        self.page.goto(
            "https://rahulshettyacademy.com/client/#/auth/register"
        )
        
    def register_user(self, user):
        self.page.fill(self.first_name, user["first_name"])
        self.page.fill(self.last_name, user["last_name"])
        self.page.fill(self.email, user["email"])
        self.page.fill(self.mobile, user["mobile"])
        self.page.select_option(
            self.occupation,
            label=user["occupation"]
        )
        if user["gender"] == "Male":
            self.page.check(self.male_radio)
        else:
            self.page.check(self.female_radio)
        self.page.fill(self.password, user["password"])
        self.page.fill(self.confirm_password, user["password"])
        self.page.check(self.age_checkbox)
        self.page.click(self.register_button)

    def is_registration_successful(self):
        success_message = self.page.get_by_text(
            "Account Created Successfully",
            exact=True
        )
        try:
            success_message.wait_for(
                state="visible",
                timeout=10000
            )
            return True
        except Exception:
            return False