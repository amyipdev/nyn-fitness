# SPDX-License-Identifier: AGPL-3.0-or-later
#
# nyn-fitness: the dynamic recommendation fitness app
# Copyright (C) 2023 Amy Parker <amy@amyip.net>
#   				 Kevin Ramirez <thekevinramirez@csu.fullerton.edu>
#   				 Nicholas Goulart <nick.goulart@csu.fullerton.edu>
#   				 Theresa Nguyen <ttnguyen1011@csu.fullerton.edu>
#   				 Dat Lam <Dlam42@csu.fullerton.edu>
#   				 Srinidhi Chevvuri <srinidhi.chevvuri@csu.fullerton.edu>
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA or visit the
# GNU Project at https://gnu.org/licenses. The GNU Affero General Public
# License version 3 is available at, for your convenience,
# https://www.gnu.org/licenses/agpl-3.0.en.html.

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
