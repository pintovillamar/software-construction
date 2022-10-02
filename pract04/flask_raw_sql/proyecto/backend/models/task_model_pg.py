from backend.models.connection_pool_pg import getcursor
#from connection_pool_pg import getcursor

class TaskModelPG:
                   
    def get_tasks(self):  
        with getcursor() as cur:
            cur.execute("SELECT * from task")
            result_set = cur.fetchall()

            data = []
            content = {}
            for result in result_set:
                content = {'id': result[0], 'title': result[1], 'description': result[2]}
                data.append(content)
                content = {}
            return data
      
    
if __name__ == "__main__":    
    tm = TaskModelPG()     

    #print(tm.get_task(1))
    #print(tm.get_tasks())
    print(tm.get_tasks())
    #print(tm.create_task('prueba 10', 'desde python'))