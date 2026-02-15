from faker import Faker

fake = Faker('ru_RU')

def generate_fake_data():
    return {
        "login": fake.user_name(),
        "firstName": fake.first_name(),
        "password": fake.password(length=10),
       
        
    }