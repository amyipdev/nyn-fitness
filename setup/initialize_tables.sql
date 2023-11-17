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