CREATE  TABLE DbMysql08.movie_crew (
  `crew_id` INT NOT NULL AUTO_INCREMENT ,
  `profile_id` INT NOT NULL ,
  `role` CHAR(50) NOT NULL ,
  `movie_id` INT NOT NULL ,
  PRIMARY KEY (`crew_id`) ,
  FOREIGN KEY (movie_id) REFERENCES DbMysql08.movies(movie_id),
  FOREIGN KEY (profile_id) REFERENCES DbMysql08.profile(profile_id),
  FOREIGN KEY (role) REFERENCES DbMysql08.department(role),
  UNIQUE INDEX `crew_id_UNIQUE` (`crew_id` ASC) ,
  INDEX `role_index` (`role` ASC) 
);
