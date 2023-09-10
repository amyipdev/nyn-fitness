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