CREATE  TABLE `DbMysql08`.`genres` (
  `genre_id` INT NOT NULL AUTO_INCREMENT ,
  `movie_id` INT NOT NULL ,
  `genre` CHAR(20) NOT NULL ,
  PRIMARY KEY (`genre_id`) ,
  FOREIGN KEY (movie_id) REFERENCES `DbMysql08`.`movies` (movie_id),
  UNIQUE INDEX `genre_id_UNIQUE` (`genre_id` ASC) 
);
