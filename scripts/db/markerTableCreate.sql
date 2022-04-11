use historee;
create table historee.markers (
    id int not null auto_increment,
    hmdbID int,
    title varchar(80),
    inscription varchar(750),
    latitude decimal,
    longitude decimal,
    town varchar(30),
    county varchar(30),
    state varchar(20),
    country varchar(40),
    primary key (id),
    unique(hmdbID)
);

-- sample insert query 
insert into markers (title, latitude, longitude, town, county, state) values
('Test locatioon', 33.8790, -84.2890, 'Savannah', 'Fulton', 'Georgia');

-- truncate markers;