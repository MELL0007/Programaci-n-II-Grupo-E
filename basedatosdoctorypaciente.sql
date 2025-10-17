create database clinica;
use clinica;
create table pacientes(
id_paciente int auto_increment primary key,
nombre varchar(100),
edad int,
genero varchar(10),
diagnostico varchar(150)
);
insert into pacientes(nombre,edad,genero,diagnostico) values('Juancito pinto',10,'Masculino','Ninguno');
insert into pacientes(nombre,edad,genero,diagnostico) values('Maria',16,'Masculino','Anemia');
insert into pacientes(nombre,edad,genero,diagnostico) values('Ariana',18,'Femenino','Tos seca');
insert into pacientes(nombre,edad,genero,diagnostico) values('Fabiana',18,'Masculino','Ninguno');
insert into pacientes(nombre,edad,genero,diagnostico) values('Aaron',10,'Masculino','Resfrio');
Update pacientes set diagnostico ="Anemia" where id_Paciente=1;
delete from pacientes where id_paciente=1;
select * from pacientes;
create table doctor(
id_doctor int auto_increment primary key,
nombre varchar(50),
ci varchar(10),
gmail varchar(50),
fecha_ingreso date
);
insert  into doctor (nombre,ci,gmail,fecha_ingreso) values ('Juana','1354678','juana@gmail.co','2025-10-17');
insert  into doctor (nombre,ci,gmail,fecha_ingreso) values ('Ignacio','13335368','juan@gmail.co','2025-01-17');
insert  into doctor (nombre,ci,gmail,fecha_ingreso) values ('Juana','11301217','pamela@gmail.co','2024-10-17');
insert  into doctor (nombre,ci,gmail,fecha_ingreso) values ('Natalia','12570024','arturo@gmail.co','2025-10-17');
insert  into doctor (nombre,ci,gmail,fecha_ingreso) values ('Fabiana','1354678','juan@gmail.co','2025-10-17');
insert  into doctor (nombre,ci,gmail,fecha_ingreso) values ('Niurka','1354678','ninoska@gmail.co','2025-10-17');
insert  into doctor (nombre,ci,gmail,fecha_ingreso) values ('Dayanara','1354678','luíta@gmail.co','2025-10-17');
insert  into doctor (nombre,ci,gmail,fecha_ingreso) values ('Natasha','1354678','natynatasha@gmail.co','2025-10-17');
insert  into doctor (nombre,ci,gmail,fecha_ingreso) values ('Emily','1354678','emyemy@gmail.co','2025-10-17');
Update doctor set fecha_ingreso ='2025-10-17' where id_doctor=5;
delete from doctor where id_doctor=3;
select * from doctor;



