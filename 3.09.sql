create table if not exists barista(
id integer not null primary key auto_increment,
name_ varchar(20)
);

create table if not exists change_№(
id integer not null primary key auto_increment,
change_ int not null,
id_barista int,
foreign key (id_barista) references barista(id)
); 

create table if not exists sales(
id integer not null primary key auto_increment,
sales_05 int,
sales_02 int,
id_barista int,
foreign key (id_barista) references barista(id)
);

insert into barista(name_,id_barista) values
(ivan, 1),
(igor,2);

insert into sales( id_barista, sales_05,sales_02) values
(1, 2, 4),
(2, 0, 6);

insert into change_№(id_barista, change_) values
(1, 2),
(2, 1);

select * from sales


