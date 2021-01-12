CREATE  TABLE DbMysql08.profile (
  `profile_id` INT NOT NULL ,
  `name` CHAR(50) NOT NULL ,
  `gender` TINYINT NOT NULL ,
  `age` TINYINT ,
  `main_department` CHAR(20) NOT NULL ,
  `popularity` FLOAT NOT NULL ,
  `biography` TEXT,
  `photo_link` TEXT NULL ,
  PRIMARY KEY (`profile_id`) ,
  UNIQUE INDEX `id_UNIQUE` (`profile_id` ASC),
  INDEX `popularity_index` (`popularity` ASC));
