import random
import string


def random_word(length=8):
    letters = string.ascii_letters
    return "".join(random.choices(letters, k=length))


def generate_user():
    first_name = random_word(8)
    last_name = random_word(8)
    email = f"{random_word(10).lower()}@gmail.com"

    mobile = "".join(random.choices(string.digits, k=10))

    password = f"{random_word(5)}@{random.randint(1000, 9999)}"

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "mobile": mobile,
        "occupation": random.choice(
            ["Doctor", "Student", "Engineer", "Scientist"]
        ),
        "gender": random.choice(["Male", "Female"]),
        "password": password,
    }