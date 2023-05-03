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
        },

    "ENG19CT0043":
            {
                "name": "Syed Suhail Salaha",
                "major": "CST",
                "starting_year": 2019,
                "total_attendance": 93,
                "standing": "A",
                "year": 4,
                "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
            },
    "ENG18CT0035":
        {
            "name": "Venkat Vilek",
            "major": "CST",
            "starting_year": 2018,
            "total_attendance": 92,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0002":
        {
            "name": "Akash Pandey",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0003":
            {
                "name": "Alisha Chinmay",
                "major": "CST",
                "starting_year": 2019,
                "total_attendance": 62,
                "standing": "A",
                "year": 4,
                "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
            },
    "ENG19CT0005":
        {
            "name": "Anand Singh Tanwar",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0006":
        {
            "name": "Apeksha Prabhu",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0008":
        {
            "name": "Chella Sai Keerthna",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0009":
        {
            "name": "Dhanush K",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0024":
        {
            "name": "Shivansh Pandey",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0021":
        {
            "name": "Nandan Pai",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0023":
        {
            "name": "Noor Poonia",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0011":
        {
            "name": "Gaurav Gupta",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0025":
        {
            "name": "Piyush Sharma",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0026":
        {
            "name": "Preeti Nayak",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0027":
        {
            "name": "Rachana D",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0028":
        {
            "name": "Rahul K P",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0029":
        {
            "name": "Rubeen Sakeena",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0031":
        {
            "name": "Saakar Dubey",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0032":
        {
            "name": "Samarth Sharma",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0034":
        {
            "name": "Saumya Anand",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0036":
        {
            "name": "Shambhavi Jhala",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0038":
        {
            "name": "Shivam ",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0039":
        {
            "name": "Shreyas B U",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0044":
        {
            "name": "Vamshi R",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0045":
        {
            "name": "Vandana",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0046":
        {
            "name": "Vikas D",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },
    "ENG19CT0004":
        {
            "name": "Amitash M S",
            "major": "CST",
            "starting_year": 2019,
            "total_attendance": 62,
            "standing": "A",
            "year": 4,
            "last_attendance_time": now.strftime("%Y-%m-%d %H:%M:%S")
        },


}

for key, value in data.items():
    ref.child(key).set(value)

