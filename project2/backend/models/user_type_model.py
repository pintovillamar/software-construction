from backend.models.connection_pool import getcursor

class UserTypeModel:

    def user_types(self):
        with getcursor() as cur:
            cur.execute("SELECT * from user_type")
            result_set = cur.fetchall()

            data = []
            content = {}
            for result in result_set:
                content = {'id': result[0], 'name': result[1]}
                data.append(content)
                content = {}
            return data

    def user_type(self, id):
        with getcursor() as cur:
            cur.execute(f"SELECT * from user_type where ust_id = {id}")
            result_set = cur.fetchall()

            data = []
            content = {}
            for result in result_set:
                content = {'ust_id': result[0], 'name': result[1]}
                data.append(content)
                content = {}
            return data

    def create_user_type(self, name):
        with getcursor() as cur:
            cur.execute(f"INSERT INTO user_type (ust_name) VALUES ('{name}')")
            return {'message': 'User type created successfully'}

            # cur.commit()

if __name__ == "__main__":
    ut = UserTypeModel()
    print(ut.user_types())

