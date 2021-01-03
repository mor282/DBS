CREATE  TABLE DbMysql08.quotes(
  `quote_id` INT NOT NULL AUTO_INCREMENT ,
  `title` CHAR(209) NOT NULL ,
  `quote` MEDIUMTEXT NOT NULL ,
  PRIMARY KEY (`quote_id`) ,
  FOREIGN KEY (title) REFERENCES DbMysql08.movies(title),
  UNIQUE INDEX `quote_id_UNIQUE` (`quote_id` ASC) ,
  INDEX `title_index` (`title` ASC) );
