CREATE  TABLE DbMysql08.locations (
  `location_id` INT NOT NULL AUTO_INCREMENT ,
  `movie_id` INT NOT NULL ,
  `country` CHAR(56) NOT NULL ,
  PRIMARY KEY (`location_id`) ,
  FOREIGN KEY (movie_id) REFERENCES DbMysql08.movies(movie_id),
  UNIQUE INDEX `location_id_UNIQUE` (`location_id` ASC) );
