create table `user`
(id int auto_increment primary key,usename varchar(100),password varchar(100), name varchar(64) not null,age int, email varchar(100),birthplace varchar(100), job varchar(100),  university varchar(100), c_prefecture varchar(100), visit varchar(100),recent_shopping varchar(100), hobby1 varchar(100), hobby2 varchar(100), hobby3 varchar(100), fav_food varchar(100),fav_movie varchar(100),fav_anime varchar(100), enter_date DATE) DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

insert into user values(NULL,'ytanaka','docomo','田中百合',22, 'ytanaka@docomo.com','滋賀県', 'エンジニア', '慶応大', '東京','アメリカ' ,'冷蔵庫','カフェ巡り',NULL, NULL , 'たこ焼き', '竜とそばかすの姫', '鬼滅の刃', '2021.09.14') ;
