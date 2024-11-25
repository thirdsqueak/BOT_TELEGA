tasks = {}

def add_task(user_id: int, task: str):
    if user_id not in tasks:
        tasks[user_id] = []
    tasks[user_id].append(task)

def list_tasks(user_id: int):
    return tasks.get(user_id, [])

def delete_task(user_id: int, task_index: int):
    if user_id in tasks and 0 <= task_index < len(tasks[user_id]):
        tasks[user_id].pop(task_index)
        return True
    return False
