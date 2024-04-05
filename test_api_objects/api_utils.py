from faker import Faker


def generate_random_body():
    return {
        "name": Faker().name(),
        "data": {
            "year": Faker().year(),
            "price": Faker().random_number(),
            "CPU model": Faker().word(),
            "Hard disk size": f'{Faker().random_int(1, 5)} TB'
        }
    }
