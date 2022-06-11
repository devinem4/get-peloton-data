from fastapi import FastAPI

import os
from dotenv import load_dotenv
from pylotoncycle import PylotonCycle


load_dotenv()

PELOTON_USERNAME_OR_EMAIL = os.getenv("PELOTON_USERNAME_OR_EMAIL")
PELOTON_PASSWORD = os.getenv("PELOTON_PASSWORD")


app = FastAPI()


@app.get("/")
def read_root():
    conn = PylotonCycle(PELOTON_USERNAME_OR_EMAIL, PELOTON_PASSWORD)
    workouts = conn.GetRecentWorkouts(5)
    return workouts
