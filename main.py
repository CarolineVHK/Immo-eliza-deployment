from fastapi import FastAPI, HTTPException, status #(query, Path)
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date



user_dict = {"Jack":{"username":"Jack","date_":"2020-01-23","age":5, "location":"NY"}, 
             "Jan":{"username":"Jan","date_":"2020-01-23","age":15, "location":"GENT"}}




class User(BaseModel):
    username : str = Field(min_length=3, max_length=20) #return an instance of a special class from pydantic
    date_ : date
    age : int = Field(None,gt=5,lt=130) #default value None but greater than 5 and less than 23 (ge=greater equal to, le=less equal to)
    location: Optional[str] = None #make a field optional, so if not enter it goes on

class User_Update(User):
    date_ : Optional[date] = None

def ensure_username_in_dict(username: str):
    if username not in user_dict:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'username {username} not found')

app = FastAPI()
#get api: only read
@app.get('/')#decorator for the function, whatever get request is call it wil be send to the url ('/')
def first_api():
    return{'First api':'I made it!'}
#running code in terminal: uvicorn main:app --reload : means that you reload the app after each new coding
#copy the http: http://127.0.0.1:8000, adding /docs or redoc nicer view 

#adding users' path
# @app.get('/users') 
# def get_users():
#     user_list = list(user_dict.values())
#     return user_list

#path parameter:
@app.get('/users/{username}') #adding variable: always beiing requiered, even if you add default value
def get_users_path(username: str): #telling py that it needs to be a string
    ensure_username_in_dict(username)
    return user_dict[username]

#adding query parameter
@app.get('/users')
def get_users_query(limit: int = 20):  #making a default value 2, so then in api the required is gone
    user_list = list(user_dict.values())
    return user_list[:limit] #passing the values from beginning to the limit-query-parameter, appearse as a ? after users: users?limit=2

#post operation models: request/response body with pydantic model: user send and ad users data into you api
@app.post('/users')
def create_user(user: User): #define a class User: to declare what info you need about the user
    username = user.username
    if username in user_dict:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Username {username} already exsists')
    user_dict[username] = user_dict.dict() #convert data into a dictionorairy
    return {"message": f'Succesfully added new user {username}'}

#error response
#existend user:
# def check_user_exist():
#     if username in user_dict:


@app.delete('/users/{username}')
def delete_user(username: str):
    del user_dict[username]
    return {"message": f'Succesfully deleted user {username}'}



@app.put('/users')
def update_user(user: User):
    #ensure_users_exist
    username = user.username
    user_dict[username] = user_dict.dict()
    return {"message": f'Succesfully updated username {username}'}

#partial update: if not filled in, doesn't change the existant data
@app.patch('/users')
def update_user_partial(user: User_Update):
    #ensure_users_exist
    username = user.username
    user_dict[username].update(user_dict.dict(exclude_unset=True))
    return {"message": f'Succesfully updated username {username}'}


