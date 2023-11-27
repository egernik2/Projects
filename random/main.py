from cgitb import html
from urllib import response
import fastapi
import fastapi.responses
 
app = fastapi.FastAPI()
atr = fastapi.Path
Resp = fastapi.responses
 
@app.get("/")
def read_root():
    return Resp.HTMLResponse(content="<h1>Я люблю Риту!</h1>")

@app.get("/about")
def about():
    return Resp.HTMLResponse (content="<h1>Это сайтик говна<h1>")

@app.get("/users/{name}.{age}")
def users(name:str = atr(min_lenght=3), age:int = atr(ge=18, lt=111)):
    return {"user_name": name, "user_age": age}