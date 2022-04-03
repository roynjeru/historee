use historee;
create table markers (
    id int not null auto_increment,
    title varchar(80),
    latitude decimal,
    longitude decimal,
    town varchar(30),
    county varchar(30),
    state varchar(20),
    primary key (id)
);