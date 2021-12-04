import mysql.connector as connector

# Database Connector


class DBHelper:
    # Database Connector
    def __init__(self):
        self.con = connector.connect(host="localhost", port='3306', user='root',
                                     password='password', database='todolist', auth_plugin='mysql_native_password')
        query = "create table if not exists todo(priority int,task varchar(100),status varchar(200))"
        cur = self.con.cursor()
        cur.execute(query)
    


# Add tasks into the Database


    def add_task(self, priority, task):
        query = "insert into todo(priority,task,status) values ({},'{}','Pending')".format(
            priority, task)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('Added task: "'+task+'" with priority ' + str(priority))


# Fetch all todo in the database


    def fetch_all_tasks(self):
        query = "select * from todo order by priority asc"
        cur = self.con.cursor()
        cur.execute(query)
        for row in enumerate(cur, 1):
            print(str(row[0])+". " + str(row[1][1]) + " ["+str(row[1][0])+"]")


# Delete task by using priority


    def delete_task(self, priority):
        query = "delete from todo where priority={}".format(priority)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Deleted task #"+str(priority))


# Update task by using priority


    def update_task(self, priority):
        query = "update todo set status='Completed' where priority={}".format(
            priority)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Marked item as done.")

# Show Report
    def report(self):
        query2 = "select count(*) from todo where status='Pending'"
        query = "select * from todo where status='Pending' order by priority asc"
        cur = self.con.cursor(buffered=True)
        cur2 = self.con.cursor(buffered=True)
        cur2.execute(query2)
        cur.execute(query)
        for col in cur2:
            print('Pending : '+str(col[0]))
        for row in enumerate(cur, 1):
            print(str(row[0])+". " + str(row[1][1]) + " ["+str(row[1][0])+"]")
        print()
        query2 = "select count(*) from todo where status='Completed'"
        query = "select * from todo where status='Completed' order by priority asc"
        cur = self.con.cursor(buffered=True)
        cur2 = self.con.cursor(buffered=True)
        cur2.execute(query2)
        cur.execute(query)
        for col in cur2:
            print('Completed : '+str(col[0]))
        for row in enumerate(cur, 1):
            print(str(row[0])+". " + str(row[1][1]))

    # Show Usage
    def show_usage(self):
        print("Usage:-")
        print("$ ./task add 2 hello world       # Add a new item with priority 2 and text 'hello world' to the list")
        print("$ ./task ls                      # Show incomplete priority list items sorted by priority in ascending order")
        print(
            "$ ./task del NUMBER   # Delete the incomplete item with given priority number")
        print("$ ./task done NUMBER  # Mark the incomplete item with given PRIORITY_NUMBER as complete")
        print("$ ./task help                    # Show usage")
        print("$ ./task report                  # Statistics")
