import pymongo


class MongoConnect:

    def __init__(self, new_user, db_name, table_name):

        mongo_token = ""

        my_client = pymongo.MongoClient(mongo_token)
        my_test_db = my_client[db_name]
        self.my_collection = my_test_db[table_name]

        self.user_data = new_user

    def insert_to_mongo(self):
        self.my_collection.insert_one(self.user_data)
        print('inserted')

    def check_if_same_exists(self):
        i = self.my_collection.find_one(self.user_data)
        if i is not None:
            obj_id = i['_id']
            print(f'Item exists in DB. obj_id is: {obj_id}')
            return i['_id']

        else:
            print('item dose not exists in DB')
            return None

    def delete_user_from_db(self, obj_id):
        self.my_collection.remove(obj_id)
        print(f'item {obj_id} deleted from DB')




