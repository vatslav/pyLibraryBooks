DROP TABLE IF EXISTS "books";
CREATE TABLE books(
	id integer primary key autoincrement,
	ISBN text unique not null,
	bbk text not null,
	autors text not null,
	title text not null,
	years date not null,
	publisher text not null,
	keywords text not null,
	city text not null,
	createTime timestamp
	);

DROP TABLE IF EXISTS "exemplars";
CREATE TABLE exemplars(
	id integer primary key autoincrement,
	classbook integer not null,
	create_time timestamp,
	FOREIGN KEY (classbook) REFERENCES books(id)
	ON DELETE RESTRICT 
	ON UPDATE CASCADE
	);
DROP TABLE IF EXISTS "getting";
CREATE TABLE getting(
	id integer primary key autoincrement,
	active boolean,
	datestart integer not null,
	dateend integer not null,
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
	id integer primary key autoincrement,
	NomberAbonement text unique not null,
	fio not null,
	adress text not null,
	telephone text,
	create_time timestamp);
DROP TABLE IF EXISTS "users";
CREATE TABLE [users] (
  [name] TEXT primary key, 
  [pass] TEXT NOT NULL, 
  [role] TEXT NOT NULL,
  create_time timestamp);
INSERT INTO "users" VALUES('Иван Ильич','f1290186a5d0b1ceab27f4e77c0c5d68','Читатель',1);
INSERT INTO "users" VALUES('Евгений Абрамы','e1671797c52e15f763380b45e841ec32','Библиотекарь',1);
INSERT INTO "users" VALUES('vfddd','9e3669d19b675bd57058fd4664205d2a','Администратор',1);
INSERT INTO "users" VALUES('иванДl2','as','Читатель',1);
INSERT INTO "users" VALUES('ssss1','3691308f2a4c2f6983f2880d32e29c84','Администратор',1);
INSERT INTO "users" VALUES('Мария Ивановна','2bfe4581ac6cf8ce4c3e7ee8f07f518b','Читатель',1);
INSERT INTO "users" VALUES('Мария Иоановна','5af57ea0892641f24c731d1e4e27cee4','Читатель',1);
INSERT INTO "users" VALUES('марк ионыч','29b177eff320a1087575b429c02643b9','Библиотекарь',1);
INSERT INTO "users" VALUES('test22','dc17d6fbbbfafbf8d4f94ea0a3c1c6f1','Читатель',1);
INSERT INTO "users" VALUES('семен ефимович','c885f743e17023ab48ed9f6ddb051e2d','Читатель',1);
INSERT INTO "users" VALUES('марк','e10adc3949ba59abbe56e057f20f883e','Администратор',1);
INSERT INTO "users" VALUES('марков','b51e8dbebd4ba8a8f342190a4b9f08d7','Администратор',1);
