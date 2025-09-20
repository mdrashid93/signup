from fastapi import APIRouter,Request,Form
from fastapi.templating import Jinja2Templates
from supabase import create_client
from fastapi.responses import RedirectResponse,JSONResponse

router=APIRouter()
templates=Jinja2Templates(directory="templates")
db=create_client('https://whverxagwhavhndnzykn.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndodmVyeGFnd2hhdmhuZG56eWtuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTc4MzQ3NDQsImV4cCI6MjA3MzQxMDc0NH0.vyb3_1X78hmnQBj4PiYBzhPUZ-shA6J1WZga9hg4zfI')

@router.get('/')
def home():
    return RedirectResponse('/signup')

@router.get('/signup')
def signup(request:Request):
    return templates.TemplateResponse("signup.html",{'request':request})

@router.post('/api/signup')
def api_signup(request:Request,email=Form(...),password=Form(...)):
    # print(email)
    # print(password)
    result=db.auth.sign_up({
        'email':email,
        'password':password
    })
    
    if result.user:
        return JSONResponse({
            'message':'user created successfully',
            'token':result.session.access_token
        })
         


@router.get('/login')
def login(request:Request):
    return templates.TemplateResponse("login.html",{'request':request})

@router.post('/api_login')
def api_login(request:Request,email=Form(...), password=Form(...)):
    result= db.auth.sign_in_with_password({
        'email':email, 
        'password':password
    })
    
    if result.user:
        # return
        response=templates.TemplateResponse('dashboard.html',{'request':request})
        # return JSONResponse({
        #     'message':'user loggedin successfully',
        #     'token': result.session.access_token
        # })
        response.set_cookie('user_session',result.session.access_token, max_age=3600)
        return response  