import os
import sys
import json
import uuid
from timeit import default_timer as timer

import mysql.connector

start = timer()

srcdir = os.path.dirname(os.path.realpath(__file__))

sys.path.append(f"{srcdir}/../cpp/")
import nyn_recommender

PROMPTS = [
    "Experience level [-6,6]: ",
    "Workout length (minutes-17.5)/5: ",
    "Intensity [-4,4]: ",
    "Weight-bearing [-2,2]: ",
    "Strength [-2,2]: ",
    "Team-based: [-1,1]: ",
    "Neuroplasticity [-1,1]: ",
    "Required thought [-2,2]: ",
    "Weight loss [-2,2]: ",
    "Upper body [-1,1]: ",
    "Lower body [-1,1]: ",
    "Full body [-1,1]: ",
    "Core [-1,1]: ",
    "Cardio [-1,1]: ",
    "Flexibility [-1,1]: ",
    "Balance [-1,1]: "
]

config = json.load(open(f"{srcdir}/../nyn-conf.json", "r"))
db = mysql.connector.connect(user=config["database"]["user"],
                             password=config["database"]["pwd"],
                             host=config["database"]["host"],
                             database=config["database"]["db"],
                             port=config["database"]["port"])
print("nyn workout setup v1.0")
print(f"Connected to database {config['database']['db']}@{config['database']['host']}")
print("Remember to use EMBED LINKS! (https://youtube.com/embed/videoid)")
print("Category IDs: Cardio=0, Core=1, HIIT=2\n")

ax = 0
while True:
    if input("Add new workout? y/[n] ") != "y":
        break
    wk_uuid = str(uuid.uuid4())
    wk_name = input("Workout name: ")
    descr = input("Workout description: ")
    ytlink = input("YouTube EMBED link: ")
    catid = int(input("Category ID: "))
    duration = input("Video duration (mM:SS): ")
    vect_basis = []
    for p in PROMPTS:
        vect_basis.append(float(input(p)))
    vect = json.dumps(nyn_recommender.gen_uv(vect_basis))
    
    curr = db.cursor()
    curr.execute("insert into workouts "
                 "(wk_uuid, wk_name, descr, ytlink, catid, duration, vect) "
                 "values (%s, %s, %s, %s, %s, %s, %s)",
                 (wk_uuid, wk_name, descr, ytlink, catid, duration, vect))
    db.commit()
    curr.close()
    print("Workout added successfully\n")
    ax += 1

print(f"Added {ax} workouts in {timer() - start} seconds")
