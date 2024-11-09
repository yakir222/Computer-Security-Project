from fastapi import FastAPI
# from db.init_db import create_database
import json
import uvicorn
import os
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware

from server.api.user_routes import UserRouter
import server.api.customer_router as customer_router

def load_config():
    with open(os.path.join('server', 'config.json')) as config_file:
        return json.load(config_file)

def main():

    config = load_config()
    DATABASE_URL = config['database_url']

    app = FastAPI(middleware=[
        Middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"],)
    ])

    app.include_router(UserRouter(), prefix="/base/user")
    app.include_router(customer_router.CustomerRouter(), prefix="/base/customer")
    print(*app.routes, sep='\n')
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == '__main__':
    main()
