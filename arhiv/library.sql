DROP TABLE IF EXISTS "books";
CREATE TABLE books(
	id integer primary key,
	autors text not null,
	title text not null,
	ISBN text not null,
	years integer,
	publisher text not null,
	keywords text not null,
	city text );
DROP TABLE IF EXISTS "exemplars";
CREATE TABLE exemplars(
	id integer primary key,
	classbook integer not null,
	FOREIGN KEY (classbook) REFERENCES books(id)
	ON DELETE RESTRICT 
	ON UPDATE CASCADE);
DROP TABLE IF EXISTS "getting";
CREATE TABLE getting(
	id primary key,
	datestart text not null,
	dateend text not null,
	idbook integer not null,
	idreader integer not null,
	foreign key (idbook) references exemplars(id)
	on delete restrict
	on update restrict,
	foreign key (idreader) references readers(id)
	on delete restrict
	on update restrict);
DROP TABLE IF EXISTS "readers";
CREATE TABLE readers(
	id integer primary key,
	NomberAbonement text unique not null,
	fio not null,
	adress text not null,
	telephone text);
DROP TABLE IF EXISTS "users";
CREATE TABLE [users] (
  [name] TEXT primary key, 
  [pass] TEXT NOT NULL, 
  [role] TEXT NOT NULL);
INSERT INTO "users" VALUES('kola','c4ca4238a0b923820dcc509a6f75849b','1');
INSERT INTO "users" VALUES('Кирилов','202cb962ac59075b964b07152d234b70','1');
