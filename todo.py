from datetime import date, timedelta

def log_call(action_name):
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[LOG] About to run action: {action_name}")
            result= func(*args, **kwargs)
            print(f"[LOG] Finised  action: {action_name}")
            return wrapper
    return decorator

class TodoItem:
    
    Valid_status = ("pending", "completed", "in-progress")

    all_items =[]
    item_count = 0

def __init__(self, title, status="pending"):
    self.title = title
    self.status = status
    self.created_at = date.today()
    
@classmethod
def pending_items(cls):
    return [item for item in cls.all_items if item.status =="pending"]



class TimedTodoItem(TodoItem):
    def __init__(self, title, due_date, status="pending"):
        super().__init__(title, status)
        self.due_date = due_date
        
    def item_is_overdue(self):
        return self.status == "pending" and self.due_date < date.today()


class TodoList:
    def __init__(self, name):
        self.name =name
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)    
    
    def add_new_item(self, title):
        item = TodoItem(title)
        self.items.append(item)
        print(f"Item {item} added.")
    
    def show_items(self, order_by="created"):
        if order_by =="title":
           title_key = lambda item:item.title
           sort_key =title_key
        elif order_by =="status":
           status_key = lambda item:item.status
           sort_key =status_key
        else:
           created_key = lambda item:item.created_at
           sort_key =created_key
        
        sorted_items =sorted(self.items, key=sort_key)
        
        print(f"Items in list {self.name} sorted by {order_by}")
        for i, item in enumerate(sorted_items, start=1):
            print( f"{i}.{item}")
            
            
@log_call("add_tasks_items to TodoList")
def add_task_items (todo_list: TodoList):
    todo_list.add_new_item("Go to the market")
    todo_list.add_new_item("Redo python introduction")
    
    todo_list.add_item(
        TimedTodoItem(
            "Learn class and instance attributes.",
            due_date=date.today() + timedelta(days=1),
        )
    )
    
    todo_list.add_item(
        TimedTodoItem(
            "Learn object inheritance.",
            due_date=date.today() - timedelta(days=1),
        )
    )