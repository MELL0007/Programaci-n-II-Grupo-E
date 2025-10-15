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
select *from pacientes;


