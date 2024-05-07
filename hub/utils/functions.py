import random,string


sys_random=random.Random()
def generate_user_id():
    return "".join(sys_random.choice(string.ascii_letters) for i in range(10))


def generate_project_id():
    return "".join(sys_random.choice(string.ascii_letters) for i in range(10))