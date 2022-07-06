import faker

fake=faker.Faker()

def get_user():
    """create one user

    Returns:
        str: a user with a first name and a last name
    """
       
    return (f"{fake.first_name()} {fake.last_name()}")    


def get_users(number_of_users: int) -> list[str]:
    """create a list of users

    Args:
        number_of_users (int): the number of users to create

    Returns:
        list [str]: list_of_users
    """
    list_of_users=[]
    for _ in range(number_of_users):
        list_of_users.append(get_user())

    return list_of_users
