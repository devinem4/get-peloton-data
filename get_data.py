"""get data from peloton api"""
import os
from pylotoncycle import PylotonCycle
from dotenv import load_dotenv

load_dotenv()

PELOTON_USERNAME_OR_EMAIL = os.getenv("PELOTON_USERNAME_OR_EMAIL")
PELOTON_PASSWORD = os.getenv("PELOTON_PASSWORD")

conn = PylotonCycle(PELOTON_USERNAME_OR_EMAIL, PELOTON_PASSWORD)
workouts = conn.GetRecentWorkouts(5)
