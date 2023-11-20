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

import json
import os

import mysql.connector

config = json.load(open(f"{os.path.dirname(__file__)}/../nyn-conf.json", "r"))
db = mysql.connector.connect(user=config["database"]["user"],
                             password=config["database"]["pwd"],
                             host=config["database"]["host"],
                             database=config["database"]["db"],
                             port=config["database"]["port"])

curr = db.cursor()
curr.execute("delete from tokens "
             "where curdate() > expiry_date;")
db.commit()
curr.close()
db.close()
