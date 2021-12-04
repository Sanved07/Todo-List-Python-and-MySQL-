from dbhelper import DBHelper


def main():
    db = DBHelper()

    a = input().split(" ", 2)

    if a[0] == "ls":
        db.fetch_all_tasks()

    elif a[0] == 'add':
        operation = str(a[0])
        priority = int(a[1])
        task = str(a[2])
        task = task[1:-1]
        db.add_task(priority, task)

    elif a[0] == "del":
        priority = int(a[1])
        db.delete_task(priority)

    elif a[0] == "done":
        priority = int(a[1])
        db.update_task(priority)

    elif a[0] == "report":
        db.report()

    elif a[0] == "help":
        db.show_usage()

    else:
        db.show_usage()


if __name__ == "__main__":
    main()
