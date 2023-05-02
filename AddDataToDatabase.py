import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from datetime import datetime

now = datetime.now()

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://aifaceattendance-263ed-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "ENG19CT0016":
        {
            "name": "Kevin Henry",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 93,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0041":
        {
            "name": "Suchitra Swain",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 93,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },

    "ENG19CT0042":
        {
            "name": "Sumedh Hagaldivte",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 93,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        }

}

for key, value in data.items():
    ref.child(key).set(value)

