
class NewUserData:

    def __init__(self, first_name, last_name, age, pet_type):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.pet = pet_type

    def user_data(self):
        data_string_for_db = {'name': self.first, 'last_name': self.last, 'age': self.age, 'pet': self.pet}
        return data_string_for_db
