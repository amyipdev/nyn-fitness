-- SPDX-License-Identifier: AGPL-3.0-or-later
--
-- nyn-fitness: the dynamic recommendation fitness app
-- Copyright (C) 2023 Amy Parker <amy@amyip.net>
--   				  Kevin Ramirez <thekevinramirez@csu.fullerton.edu>
--   				  Nicholas Goulart <nick.goulart@csu.fullerton.edu>
--   				  Theresa Nguyen <ttnguyen1011@csu.fullerton.edu>
--   				  Dat Lam <Dlam42@csu.fullerton.edu>
--   				  Srinidhi Chevvuri <srinidhi.chevvuri@csu.fullerton.edu>
--
-- This program is free software; you can redistribute it and/or modify it
-- under the terms of the GNU Affero General Public License as published by
-- the Free Software Foundation; either version 3 of the License, or
-- (at your option) any later version.
--
-- This program is distributed in the hope that it will be useful, but
-- WITHOUT ANY WARRANTY; without even the implied warranty of
-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
-- See the GNU Affero General Public License for more details.
--
-- You should have received a copy of the GNU Affero General Public License
-- along with this program; if not, write to the Free Software Foundation, Inc.,
-- 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA or visit the
-- GNU Project at https://gnu.org/licenses. The GNU Affero General Public
-- License version 3 is available at, for your convenience,
-- https://www.gnu.org/licenses/agpl-3.0.en.html.

create table user_info (
    user_uuid varchar(36) unique not null,
    displayname text not null,
    username text unique not null,
    password_hs text not null,
    salt varchar(32) not null,
    primary key (user_uuid)
);
create table tokens (
    user_uuid varchar(36) not null,
    token varchar(128) unique not null,
    expiry_date date not null,
    primary key (token),
    foreign key (user_uuid) references user_info(user_uuid) on delete cascade
);
create table workouts (
    wk_uuid varchar(36) unique not null,
    wk_name text unique not null,
    descr text not null,
    ytlink text not null,
    vect text not null,
    catid int not null,
    duration text not null,
    primary key (wk_uuid)
);
create table user_preferences (
    user_uuid varchar(36) unique not null,
    exp double not null,
    dur double not null,
    ins double not null,
    wbr double not null,
    sti double not null,
    tbs double not null,
    npl double not null,
    rqt double not null,
    wlf double not null,
    ubf double not null,
    lbf double not null,
    fbf double not null,
    cor double not null,
    car double not null,
    flx double not null,
    bal double not null,
    foreign key (user_uuid) references user_info(user_uuid) on delete cascade
);
create table workout_completed (
    user_uuid varchar(36) not null,
    wk_uuid varchar(36) not null,
    completion datetime not null,
    foreign key (user_uuid) references user_info(user_uuid) on delete cascade,
    foreign key (wk_uuid) references workouts(wk_uuid) on delete cascade,
    primary key (user_uuid, wk_uuid)
);