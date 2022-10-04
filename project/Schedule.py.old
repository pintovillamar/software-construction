from psycopg2.pool import SimpleConnectionPool
from contextlib import contextmanager

dbConnection = "dbname='flaskpsql' user='postgres' host='localhost' password='Pass.123$'"

# pool define with 10 live connections
connectionpool = SimpleConnectionPool(1,10,dsn=dbConnection)

@contextmanager
def getcursor():
    con = connectionpool.getconn()
    try:
        yield con.cursor()
    finally:
        connectionpool.putconn(con)

if __name__ == "__main__":
    try:
        # with here will take care of put connection when its done
        with getcursor() as cur:
            cur.execute("select * from task")
            result_set = cur.fetchall()

        for result in result_set:
            print(result)

    except Exception as e:
        print("error in executing with exception: ", e)from psycopg2.pool import SimpleConnectionPool
from contextlib import contextmanager

dbConnection = "dbname='flaskpsql' user='postgres' host='localhost' password='Pass.123$'"

# pool define with 10 live connections
connectionpool = SimpleConnectionPool(1,10,dsn=dbConnection)

@contextmanager
def getcursor():
    con = connectionpool.getconn()
    try:
        yield con.cursor()
    finally:
        connectionpool.putconn(con)

if __name__ == "__main__":
    try:
        # with here will take care of put connection when its done
        with getcursor() as cur:
            cur.execute("select * from task")
            result_set = cur.fetchall()

        for result in result_set:
            print(result)

    except Exception as e:
        print("error in executing with exception: ", e)

class Schedule(db.Model):
    sch_id = db.Column(db.Integer, primary_key=True)
    sch_begin = db.Column(db.Time())
    sch_end = db.Column(db.Time())
    sch_day = db.Column(db.String(70))
    gru_id = db.Column(db.Integer, db.ForeignKey(Group.gru_id))

    def __init__(self, sch_begin, sch_end, sch_day, gru_id):
        self.sch_begin = sch_begin
        self.sch_end = sch_end
        self.sch_day = sch_day
        self.gru_id = gru_id

class ScheduleSchema(ma.Schema):
    class Meta:
        fields = (
            'sch_id',
            'sch_begin',
            'sch_end',
            'sch_day',
            'gru_id'
        )
    
schedule_schema = ScheduleSchema()
schedules_schema = ScheduleSchema(many=True)

db.create_all()

#ENDPOINTS

# Create a schedule
@app.route('/create_schedule', methods=['POST'])
def create_schedule():
    print(request.json)

    sch_begin = request.json['sch_begin']
    sch_end = request.json['sch_end']
    sch_day = request.json['sch_day']
    gru_id = request.json['gru_id']

    new_schedule = Schedule(sch_begin, sch_end, sch_day, gru_id)
    db.session.add(new_schedule)
    db.session.commit()

    return schedule_schema.jsonify(new_schedule)

# Get all schedules
@app.route('/schedules', methods=['POST'])
def schedules():
    all_schedules = Schedule.query.all()
    result = schedules_schema.dump(all_schedules)
    return jsonify(result)

# Get a schedule
@app.route('/schedule/<sch_id>', methods=['POST'])
def schedule(sch_id):
    result = Schedule.query.get(sch_id)
    result = schedule_schema.dump(result)
    return jsonify(result)

# Update a schedule
@app.route('/update_schedule/<sch_id>', methods=['POST'])
def update_schedule(sch_id):
    schedule = Schedule.query.get(sch_id)
    sch_begin = request.json['sch_begin']
    sch_end = request.json['sch_end']
    sch_day = request.json['sch_day']
    gru_id = request.json['gru_id']

    schedule.sch_begin = sch_begin
    schedule.sch_end = sch_end
    schedule.sch_day = sch_day
    schedule.gru_id = gru_id

    db.session.commit()
    return schedule_schema.jsonify(schedule)

# Delete a schedule
@app.route('/delete_schedule/<sch_id>', methods=['POST'])
def delete_schedule(sch_id):
    schedule = Schedule.query.get(sch_id)
    db.session.delete(schedule)
    db.session.commit()
    return schedule_schema.jsonify(schedule)