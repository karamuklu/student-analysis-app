
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from openai_client import analyze_students
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.post("/analyze", response_class=HTMLResponse)
async def analyze(request: Request, students: str = Form(...), prompt: str = Form(...)):
    try:
        student_list = []
        for line in students.strip().splitlines():
            name, grade = line.split(":")
            student_list.append({"name": name.strip(), "grade": float(grade.strip())})

        result = analyze_students(student_list, prompt)
        return templates.TemplateResponse("index.html", {"request": request, "result": result})
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "result": f"Hata: {str(e)}"})
