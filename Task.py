from db_init import database_init, execute_query, check_existence_of_table


class Task:
    def __init__(self, title, description, start_date, end_date, status, period, alarm_list):
        pass

    def _creat_table(self):
        self.connection = database_init()
        if not check_existence_of_table(self.connection, "task"):
            # TODO Add alarm to the db
            create_tasks_table = """CREATE TABLE task
(
    task_id     INT PRIMARY KEY,
    title       VARCHAR(40)  NOT NULL,
    description VARCHAR(288) NOT NULL,
    start_date  DATETIME,
    end_date    DATETIME,
    status      ENUME('Finished', 'Canceled', 'In Progress'),
    period_unite ENUME('Year', 'Month', 'Week', 'Day', 'Hour', 'Minute', 'Second'),
);
             """
