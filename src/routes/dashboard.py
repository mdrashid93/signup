from fastapi import APIRouter,Request,Form
from fastapi.templating import Jinja2Templates
from supabase import create_client
from fastapi.responses import RedirectResponse,JSONResponse

router=APIRouter()
templates=Jinja2Templates(directory="templates")

db=create_client('https://whverxagwhavhndnzykn.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndodmVyeGFnd2hhdmhuZG56eWtuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTc4MzQ3NDQsImV4cCI6MjA3MzQxMDc0NH0.vyb3_1X78hmnQBj4PiYBzhPUZ-shA6J1WZga9hg4zfI')

@router.get('/dashboard')
def dashboard(request:Request):
    return request.cookies.get('user_session')
      
