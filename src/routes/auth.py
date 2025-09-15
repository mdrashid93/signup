from fastapi import APIRouter,Request,Form
from fastapi.templating import Jinja2Templates
from supabase import create_client

router=APIRouter()
templates=Jinja2Templates(directory="templates")
db=create_client('https://whverxagwhavhndnzykn.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndodmVyeGFnd2hhdmhuZG56eWtuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTc4MzQ3NDQsImV4cCI6MjA3MzQxMDc0NH0.vyb3_1X78hmnQBj4PiYBzhPUZ-shA6J1WZga9hg4zfI')

@router.get('/signup')
def signup(request:Request):
    return templates.TemplateResponse("signup.html",{'request':request})

@router.post('/api/signup')
def signup(request:Request,email=Form(...),password=Form(...)):
    print(email)
    print(password)
    result=db.auth.sign_up({
        'email':email,
        'password':password
    })
    
    if result.user:
        return 'user created successfully'

