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