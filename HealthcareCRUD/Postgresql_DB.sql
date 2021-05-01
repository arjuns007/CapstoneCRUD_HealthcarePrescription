create table patient (
	id serial primary key,
	patientname varchar(150), 
	sex char,
	dob DATE,
	phone varchar(10),
	email varchar(150),
	address varchar(350),
	disease varchar(150),
	doctor varchar(150),
	drug varchar(150),
	drugstrength varchar(150),
	drugduration varchar(150),
	prescriptionadvice varchar(150),
	remarks varchar(150)
);
create table image(
	id serial primary key,
	title varchar(150),
	image varchar(150)
)
drop table image;
drop table patient;

select * from patient;
select * from image;

delete from image;
delete from patient;
