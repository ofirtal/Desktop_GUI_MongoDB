from db_gui.control_panel import ControlPanel
from db_gui.user_input import UserInput
from mongo_connect import MongoConnect
from new_user import NewUserData


class Interface:
    """ construct main gui interface """
    def __init__(self, root):
        self.root = root
        self.root.title('CREATE A NEW USER PLEASE')
        self.users_temp_dict = {}

        self.first_name = UserInput(root, 0, 0, 'First name:')
        self.last_name = UserInput(root, 1, 0, 'Last name:')
        self.user_age = UserInput(root, 2, 0, 'Age:')
        self.user_pet = UserInput(root, 3, 0, 'Do you have a dog or cat:')

        self.gui_control_panel = ControlPanel(self.root, 4, 0, self.clear_func, self.submit_func, self.delete_from_db)

    def clear_func(self):
        """ clear all fields user see) """
        self.first_name.clear()
        self.last_name.clear()
        self.user_age.clear()
        self.user_pet.clear()

    def submit_func(self):
        """ submit new user to DB.
        firstly, it checks if a user already exists in DB.
        A user will be considered as existing if it is identical to the  Key, value  pairs given.
        Any change (extra filed, extra field data, lack of filed or empty field data) will be considered as new user.

        If user exists it will return a notice, if not it will insert it to DB
        """
        check_if_item_exists = self.check_if_user_exists_in_db(self.get_user_data_gui())
        if check_if_item_exists is None:
            MongoConnect(self.get_user_data_gui(), 'my_test_db', 'my_test_collection').insert_to_mongo()

    def delete_from_db(self):
        """Delete user from db after verifying it exists"""
        check_if_item_exists = self.check_if_user_exists_in_db(self.get_user_data_gui())
        if check_if_item_exists is not None:
            MongoConnect(self.get_user_data_gui(), 'my_test_db', 'my_test_collection')\
                .delete_user_from_db(check_if_item_exists)

    def get_user_data_gui(self):
        """Convert all user input from gui to a workable NewUserData instance"""
        user_name = self.first_name.get_user_data()
        user_last_name = self.last_name.get_user_data()
        user_age = self.user_age.get_user_data()
        user_pet = self.user_pet.get_user_data()

        return NewUserData(user_name, user_last_name, user_age, user_pet).user_data()

    @staticmethod
    def check_if_user_exists_in_db(user_data_from_gui):
        return MongoConnect(user_data_from_gui, 'my_test_db', 'my_test_collection').check_if_same_exists()
