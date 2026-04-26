from sqlalchemy.orm import Session
import models

# ---------------- CREATE TASK ----------------
def create_task(db: Session, task, user_id: int):
    t = models.Task(
        title=task.title,
        description=task.description,
        owner_id=user_id
    )
    db.add(t)
    db.commit()
    db.refresh(t)
    return t


# ---------------- GET ALL TASKS FOR USER ----------------
def get_tasks(db: Session, user_id: int):
    return db.query(models.Task).filter(models.Task.owner_id == user_id).all()


# ---------------- GET SINGLE TASK ----------------
def get_task(db: Session, task_id: int, user_id: int):
    return db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.owner_id == user_id
    ).first()


# ---------------- UPDATE TASK ----------------
def update_task(db: Session, task_id: int, task_data, user_id: int):
    task = db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.owner_id == user_id
    ).first()

    if not task:
        return None

    # Optional updates
    if hasattr(task_data, "title") and task_data.title is not None:
        task.title = task_data.title
    if hasattr(task_data, "description") and task_data.description is not None:
        task.description = task_data.description
    if hasattr(task_data, "status") and task_data.status is not None:
        task.status = task_data.status

    db.commit()
    db.refresh(task)
    return task


# ---------------- DELETE TASK ----------------
def delete_task(db: Session, task_id: int, user_id: int):
    task = db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.owner_id == user_id
    ).first()

    if not task:
        return None

    db.delete(task)
    db.commit()
    return task


# ---------------- BACKGROUND TASK ----------------
def fake_email():
    print("Sending email in background...")