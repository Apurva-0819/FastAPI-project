from fastapi import FastAPI, Depends, BackgroundTasks, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database, crud, auth

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# ------------------ AUTH ------------------

@app.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return auth.create_user(db, user)


@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(database.get_db)):
    return auth.login_user(db,user)


# ------------------ TASKS (PROTECTED) ------------------

# CREATE TASK
@app.post("/tasks", response_model=schemas.TaskResponse)
def create_task(
    task: schemas.TaskCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserResponse = Depends(auth.get_current_user)
):
    new_task = crud.create_task(db, task, user_id=current_user.id)

    background_tasks.add_task(crud.fake_email, current_user.email)

    return new_task

# GET ALL TASKS
@app.get("/tasks", response_model=list[schemas.TaskResponse])
def get_tasks(
    db: Session = Depends(database.get_db),
    current_user: schemas.UserResponse = Depends(auth.get_current_user)
):
    return crud.get_tasks(db, user_id=current_user.id)


# GET SINGLE TASK
@app.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserResponse = Depends(auth.get_current_user)
):
    task = crud.get_task(db, task_id, user_id=current_user.id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


# UPDATE TASK
@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(
    task_id: int,
    task: schemas.TaskUpdate,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserResponse = Depends(auth.get_current_user)
):
    updated = crud.update_task(db, task_id, task, user_id=current_user.id)

    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")

    return updated


# DELETE TASK
@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.UserResponse = Depends(auth.get_current_user)
):
    deleted = crud.delete_task(db, task_id, user_id=current_user.id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted"}


# ------------------ BACKGROUND TASK ------------------

@app.post("/notify")
def notify(background_tasks: BackgroundTasks):
    background_tasks.add_task(crud.fake_email)
    return {"message": "Notification scheduled"}