drop database if exists ships;
create database ships;

use ships;

create table UserRole(
	id int primary key NOT NULL auto_increment,
    role_name VARCHAR(45) NOT NULL
);

create table Users(
	id int primary key not null auto_increment,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    pass VARCHAR(45) NOT NULL,
    salt int not null,
    username VARCHAR(45) NOT NULL,
    user_role int not null,
    foreign key(user_role) references UserRole(id)
);

create table Forms(
	id int primary key not null auto_increment,
    vehicle_id int not null,
    form_type VARCHAR(45) NOT NULL,
    year_of_production datetime
);

create table Application(
	id int primary key not null auto_increment,
    petitioner int not null,
    clerk int not null,
    form int not null,
    foreign key(petitioner) references Users(id),
    foreign key(clerk) references Users(id),
    foreign key(form) references Forms(id)
);

create table Document(
	id int primary key not null auto_increment,
    filename VARCHAR(45) NOT NULL,
    link VARCHAR(45) NOT NULL,
    document_type VARCHAR(45) NOT NULL,
    form int not null,
    foreign key(form) references Forms(id)
);
