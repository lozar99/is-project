class User:
    def __init__(self, email: str, name: str, surname: str, doctor: bool = False,
                 password: str = None, born_year: int = None):
        self.email = email
        self.name = name
        self.surname = surname
        self.doctor = doctor
        self.password = password
        self.born_year = born_year

