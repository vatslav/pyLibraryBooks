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
INSERT INTO "books" VALUES(1,'978-5--93286-210-0','01-50','Марк Лутц','Программирование на Python',2011,'O`REALLY','python, программирование','Москва','2012-07-28 11:59:27.921000');
INSERT INTO "books" VALUES(22,'0-100','ббк','Автор','Название',1001,'издательство','ключ слова','город','2012-07-28 12:14:20.470000');
INSERT INTO "books" VALUES(27,'isbn','ббк','автор','назв','год','изд','ключ','город','2012-07-30 14:42:33.107000');
INSERT INTO "books" VALUES(28,'978-93286-210-0','Нет','Дэевид Бизли','Python - пожробный справочник',2010,'Символ','python, программирование, курсовая','Москва','2012-07-30 14:50:01.512000');
INSERT INTO "books" VALUES(29,'050-12','1056210','Юрий Жуков','Основы Web-хакинга',2009,'Питер','хобби','Санкт-Питебруг','2012-07-30 14:51:39.440000');
INSERT INTO "books" VALUES(30,'1-5099','04654','Шмелев','Лето Господне',1927,'Париж-паблик','проза','Париж','2012-07-30 14:52:35.014000');
INSERT INTO "books" VALUES(31,'1-8899','04654','Прохоренок','Python 3 и PyQt',2011,'Питер','учебник, курсовая','Санкт-Питебруг','2012-07-30 14:54:13.930000');
INSERT INTO "books" VALUES(32,'0-59-2','446540-45','Лермонтов','Стихи',1995,'Детская Литература','стихи','Москва','2012-07-30 14:54:59.817000');
INSERT INTO "books" VALUES(33,'0-59-1','446540-45-2','Лермонтов','Стихи том 2',1995,'Детская Литература','стихи','Москва','2012-07-30 14:55:15.808000');
INSERT INTO "books" VALUES(34,'22-50848','232-50','Блж. Иоанн Мосх','Луг Духовный',2000,'Не известно','богословие','Екатеринбург','2012-07-30 14:56:44.293000');
INSERT INTO "books" VALUES(35,'05-5095','нет','Святой Тихон Задонский','Сокровище Духовное от мира собираемое',1945,'Московская Патриархия','богословие','Москва','2012-07-30 14:58:08.947000');
INSERT INTO "books" VALUES(61,'9','9','9','9',9,'9','99','9','2012-08-08 15:32:14.872000');
INSERT INTO "books" VALUES(62,'1','1','1','1',1,'1','11','1','2012-08-08 15:33:21.175000');
INSERT INTO "books" VALUES(63,'wsef','2','2','2',2,'2','22','2','2012-08-08 15:34:56.995000');
INSERT INTO "books" VALUES(64,'sdf','2','0','0',0,'0','00','2','2012-08-08 15:35:56.171000');
INSERT INTO "books" VALUES(65,'QWE','5','5','5',5,'5','55','5','2012-08-08 15:37:51.781000');
INSERT INTO "books" VALUES(66,'QWED','5','WEQ','5',5,'5','5','55','2012-08-08 15:38:21.935000');
INSERT INTO "books" VALUES(67,'ERTG','5','5','5',5,'5','5','55','2012-08-08 15:41:13.718000');
INSERT INTO "books" VALUES(68,'WER','5','5','5',5,'5','55','5','2012-08-08 15:41:35.833000');
INSERT INTO "books" VALUES(69,'REWFG','5','5','5',5,'5','5','5','2012-08-08 15:41:59.468000');
INSERT INTO "books" VALUES(70,'REWFG1','5','5','5',5,'5','5','5','2012-08-08 15:42:08.987000');
INSERT INTO "books" VALUES(71,'WEFR5','5','5','5',5,'5','55','5','2012-08-08 15:42:48.966000');
INSERT INTO "books" VALUES(72,'WERG5','5','5','5',5,'5','55','5','2012-08-08 15:43:09.821000');
INSERT INTO "books" VALUES(73,'QW31D','5','5','5',5,'55','5','5','2012-08-08 15:47:59.354000');
INSERT INTO "books" VALUES(74,'ew5','5','5','55',5,'5','5','5','2012-08-08 15:49:05.088000');
INSERT INTO "books" VALUES(75,'dfgv5','5','5','5',5,'5','55','5','2012-08-08 15:49:42.322000');
INSERT INTO "books" VALUES(76,'sf5','5','5','5',5,'55','5','5','2012-08-08 15:53:43.490000');
INSERT INTO "books" VALUES(77,'sdfsdf5','5','5','5',55,'5','5','5','2012-08-08 15:54:14.916000');
INSERT INTO "books" VALUES(78,'sdfvbd5','5','5','5',55,'5','5','5','2012-08-08 15:55:38.962000');
INSERT INTO "books" VALUES(79,'sdf52','5','5','5',5,'55','5','5','2012-08-08 15:56:01.385000');
INSERT INTO "books" VALUES(80,'ISBN 2','5','АВТОР"!Ё','НАЗВАНИЕ!===','ГОДЫ====','ИЗДАТЕЛЬСТВО==','КЛЮЧ СЛОВА==','ГОРОД===','2012-08-08 16:04:18.660000');
INSERT INTO "books" VALUES(81,'dcscv4','5','5','5',5,'55','5','5','2012-08-08 16:15:18.814000');
INSERT INTO "books" VALUES(82,'asd','5','5','5',5,'5','5','55','2012-08-08 16:17:50.636000');
INSERT INTO "books" VALUES(83,'asdfcsd','55','5','5',55,'5','5','5','2012-08-08 16:58:13.991000');
INSERT INTO "books" VALUES(84,'asd05','55','5','5',55,'5','5','5','2012-08-08 17:00:11.948000');
INSERT INTO "books" VALUES(85,'asd8','52','5','5',55,'5','5','5','2012-08-08 17:05:05.330000');
INSERT INTO "books" VALUES(86,'ad','sdf','asd','asd','asdasd','sd','465','sdf','2012-08-13 12:45:09.550000');
INSERT INTO "books" VALUES(87,'as23','46','4','5445',46,'4646','46','46','2012-08-13 12:46:13.913000');
INSERT INTO "books" VALUES(88,'as23qw','46','4','5445',46,'4646','46','46','2012-08-13 12:46:32.183000');
INSERT INTO "books" VALUES(89,'drfg45q','435','45','45',45,'4545','45','435','2012-08-13 12:50:26.299000');
INSERT INTO "books" VALUES(90,'dfgd45','45','45','45',45,'45','4545','45','2012-08-13 12:55:35.581000');
INSERT INTO "books" VALUES(91,'asdf3','SDF','asf','EF','SEF','SEF34','WSEF','AEF3','2012-08-13 12:59:48.291000');
DROP TABLE IF EXISTS "exemplars";
CREATE TABLE exemplars(
	id integer primary key autoincrement,
	classbook integer not null,
	create_time timestamp,
	FOREIGN KEY (classbook) REFERENCES books(id)
	ON DELETE RESTRICT 
	ON UPDATE CASCADE
	);
INSERT INTO "exemplars" VALUES(16,79,'2012-08-08 15:56:02.014000');
INSERT INTO "exemplars" VALUES(17,82,'2012-08-08 16:17:53.297000');
INSERT INTO "exemplars" VALUES(18,82,'2012-08-08 16:17:53.297000');
INSERT INTO "exemplars" VALUES(19,82,'2012-08-08 16:17:53.297000');
INSERT INTO "exemplars" VALUES(20,82,'2012-08-08 16:17:53.297000');
INSERT INTO "exemplars" VALUES(21,82,'2012-08-08 16:17:53.297000');
INSERT INTO "exemplars" VALUES(22,85,'2012-08-08 17:05:06.574000');
INSERT INTO "exemplars" VALUES(23,85,'2012-08-08 17:05:06.574000');
INSERT INTO "exemplars" VALUES(24,86,'2012-08-13 12:45:10.706000');
INSERT INTO "exemplars" VALUES(25,89,'2012-08-13 12:50:27.333000');
INSERT INTO "exemplars" VALUES(26,89,'2012-08-13 12:50:27.333000');
INSERT INTO "exemplars" VALUES(27,90,'2012-08-13 12:55:36.463000');
INSERT INTO "exemplars" VALUES(28,90,'2012-08-13 12:55:36.463000');
INSERT INTO "exemplars" VALUES(29,90,'2012-08-13 12:55:36.463000');
INSERT INTO "exemplars" VALUES(30,90,'2012-08-13 12:55:36.463000');
INSERT INTO "exemplars" VALUES(31,90,'2012-08-13 12:55:36.463000');
INSERT INTO "exemplars" VALUES(32,91,'2012-08-13 12:59:52.919000');
INSERT INTO "exemplars" VALUES(33,91,'2012-08-13 12:59:52.919000');
INSERT INTO "exemplars" VALUES(34,91,'2012-08-13 12:59:52.919000');
INSERT INTO "exemplars" VALUES(35,91,'2012-08-13 12:59:52.919000');
INSERT INTO "exemplars" VALUES(36,91,'2012-08-13 12:59:52.919000');
INSERT INTO "exemplars" VALUES(37,91,'2012-08-13 12:59:52.919000');
INSERT INTO "exemplars" VALUES(38,91,'2012-08-13 12:59:52.919000');
INSERT INTO "exemplars" VALUES(39,91,'2012-08-13 12:59:52.919000');
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
INSERT INTO "readers" VALUES(1,'a','a','a','a','2012-08-03 00:23:06.264000');
INSERT INTO "readers" VALUES(2,'m-2','Тирапулько Акакий Леонидович','Москва, д.2','5-13-55','2012-08-03 00:30:47.654000');
INSERT INTO "readers" VALUES(3,'m-25','Иванов','баристов 15','0-500','2012-08-04 11:35:20.576000');
INSERT INTO "readers" VALUES(4,'m-sdfs','srfs','wrfrg','erged','2012-08-04 11:40:12.174000');
INSERT INTO "readers" VALUES(5,'m-55','Jon Smith','xorg street, 15','5-995-50','2012-08-04 11:40:57.510000');
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
INSERT INTO "users" VALUES('ssss','3691308f2a4c2f6983f2880d32e29c84','Библиотекарь',1);
INSERT INTO "users" VALUES('Мария Ивановна','95557b1eefad2bc90276f2f87333ad76','Читатель',1);
INSERT INTO "users" VALUES('Мария Иоановна','cba8cd7c127180a69de6a601f624bb60','Читатель',1);
INSERT INTO "users" VALUES('марк ионыч','29b177eff320a1087575b429c02643b9','Библиотекарь',1);
INSERT INTO "users" VALUES('test22','dc17d6fbbbfafbf8d4f94ea0a3c1c6f1','Читатель',1);
INSERT INTO "users" VALUES('семен ефимович','c885f743e17023ab48ed9f6ddb051e2d','Читатель',1);
INSERT INTO "users" VALUES('марк','e10adc3949ba59abbe56e057f20f883e','Администратор',1);
INSERT INTO "users" VALUES('марков','b51e8dbebd4ba8a8f342190a4b9f08d7','Администратор',1);
INSERT INTO "users" VALUES('cate','4297f44b13955235245b2497399d7a93','Администратор',2);
INSERT INTO "users" VALUES('dfcdsads','ab1c4bd92574cc67ca7b20d204f02e9b','Читатель',2);
INSERT INTO "users" VALUES('asdew','df3b62927b30043c1ffa2be509f75b98','Читатель',2);
INSERT INTO "users" VALUES('jons','00b7691d86d96aebd21dd9e138f90840','Администратор',2);
