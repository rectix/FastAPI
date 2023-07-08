from fastapi import FastAPI, Path
from typing import Annotated, Optional
from pydantic import BaseModel



class Stu(BaseModel):
    name : str   
    age:int  
    year :str  

app = FastAPI()

students = {
    1:{
        "name"  : 'hocine',
         'age'  :  22,
         'year':  "fifth"     

    },
    2:{
        "name"  : 'hinata',
         'age'  :  20,
         'year':  "fifth"     

    }
}



@app.get('/')
def home():
    return {"welcome": 'home'}


@app.get("/get_student/{student_id}")
def get_info(student_id: int = Path(description = "Student ID tha you want to view on the page ", gt=0)):
    return  students[student_id] 



@app.get("/filter_by_name/{student_id}")
def get_name(*, student_id:int,name:Optional[str] = None ):
    for student_id in students:
        if (students[student_id]['name'] == name):
            return students[student_id]

    return {"data" : "not found"}


# @app.post("new_student/{student_id}", response_model=Stu)
# def new_student(student_id:int, st:Stu):
#     if(student_id in students): 
#         return {"Error": "Student exists "}

#     students[student_id] = st
#     return students[student_id]



@app.post("/new_student/{student_id}", response_model=Stu)
def new_student(student_id:int, st:Stu):
    if(student_id in students): 
        return {"Error": "Student exists "}

    students[student_id] = st
    return students[student_id]

