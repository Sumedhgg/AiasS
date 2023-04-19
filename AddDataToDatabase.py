import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://aifaceattendance-263ed-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "ENG19CT0016":
        {
            "name": "Kevin Henry",
            "major": "Computer Science and Technology",
            "starting_year": 2019,
            "total_attendance": 93,
            "standing": "A",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "ENG19CT0041":
        {
            "name": "Suchitra Swain",
            "major": "Computer Science and Technology",
            "starting_year": 2019,
            "total_attendance": 93,
            "standing": "A",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },

    "ENG19CT0042":
        {
            "name": "Sumedh Hagaldivte",
            "major": "Computer Science and Technology",
            "starting_year": 2019,
            "total_attendance": 93,
            "standing": "A",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        }

}

for key, value in data.items():
    ref.child(key).set(value)
