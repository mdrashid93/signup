from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from src.routes.auth import router as auth_router
from src.routes.dashboard import router as dashboard_router

app=FastAPI()
app.include_router(auth_router)

# @app.get("/")
# def hello():
#     return HTMLResponse('''
#               <h1>hi!</h1>          
#                         ''')
    # return JSONResponse({
    #     "sms":"helo"
    # })
    
    # return RedirectResponse("https://www.youtube.com/watch?v=uk6H-ryc1Wg")