from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates=Jinja2Templates(directory="Templates")
posts: list[dict] = [
    {
        "id": 1,
        "author": "Aditya J Parida",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast",
        "date_posted": "September 20, 2026"
    },
    {
        "id": 2,
        "author": "Pratyush Panda",
        "title": "Python is great for Web Development",
        "content": "Python is a great language for web development and FastAPI makes it even better",
        "date_posted": "September 19, 2026"
    }
]

@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(
        request, "home.html", {"posts": posts, "title": "Home"},
    )
@app.get("/api/posts")
def get_posts():
    return posts