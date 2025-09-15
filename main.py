from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from src.routes.auth import router

app=FastAPI()
app.include_router(router)

# @app.get("/")
# def hello():
#     return HTMLResponse('''
#               <h1>hi!</h1>          
#                         ''')
    # return JSONResponse({
    #     "sms":"helo"
    # })
    
    # return RedirectResponse("https://www.youtube.com/watch?v=uk6H-ryc1Wg")