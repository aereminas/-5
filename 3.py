import random
import json
import string

given_names = ["Ethan", "Olivia", "Noah", "Emma", "Liam", "Ava", "Mason", "Sophia", "Jacob", "Isabella", "William", "Mia"]
family_names = ["Clark", "Lewis", "Lee", "Walker", "Hall", "Young", "King", "Wright", "Hill", "Green", "Adams", "Baker"]

password_chars = string.ascii_letters + string.digits + string.punctuation

def create_full_name():
    first_name = random.choice(given_names)
    last_name = random.choice(family_names)
    return f"{first_name} {last_name}"

def create_email(full_name):
    first, last = full_name.split()
    email_domains = ["yahoo.com", "outlook.com", "protonmail.com"]
    return f"{first.lower()}.{last.lower()}@{random.choice(email_domains)}"

def create_password(length=12):
    return ''.join(random.choice(password_chars) for _ in range(length))

def generate_profile():
    full_name = create_full_name()
    return {
        "name": full_name,
        "age": random.randint(16, 90),
        "email": create_email(full_name),
        "password": create_password()
    }

def store_and_load_profile(filename='profile.json'):
    try:
        profile_data = generate_profile()
        with open(filename, 'w') as json_file:
            json.dump(profile_data, json_file, indent=4)

        with open(filename, 'r') as json_file:
            loaded_profile = json.load(json_file)

        print("Создан профиль пользователя:")
        print(json.dumps(loaded_profile, indent=4))

    except Exception as error:
        print(f"Произошла ошибка: {error}")

store_and_load_profile()
