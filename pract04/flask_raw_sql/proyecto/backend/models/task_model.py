from backend.models.connection_pool import MySQLPool

class TaskModel:
    def __init__(self):        
        self.mysql_pool = MySQLPool()

    def get_task(self, id):    
        params = {'id' : id}      
        rv = self.mysql_pool.execute("SELECT * from task where id=%(id)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'title': result[1], 'description': result[2]}
            data.append(content)
            content = {}
        return data

    def get_tasks(self):  
        rv = self.mysql_pool.execute("SELECT * from task")  
        data = []
        content = {}
        for result in rv:
            content = {'id': result[0], 'title': result[1], 'description': result[2]}
            data.append(content)
            content = {}
        return data

    def create_task(self, title, description):    
        params = {
            'title' : title,
            'description' : description
        }  
        query = """insert into task (title, description) 
            values (%(title)s, %(description)s)"""    
        cursor = self.mysql_pool.execute(query, params, commit=True)   

        data = {'id': cursor.lastrowid, 'title': title, 'description': description}
        return data

    def delete_task(self, id):    
        params = {'id' : id}      
        query = """delete from task where id = %(id)s"""    
        self.mysql_pool.execute(query, params, commit=True)   

        data = {'result': 1}
        return data

if __name__ == "__main__":    
    tm = TaskModel()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    print(tm.delete_task(67))
    print(tm.get_tasks())
    #print(tm.create_task('prueba 10', 'desde python'))