CREATE  TABLE DbMysql08.movies(
  `movie_id` INT NOT NULL ,
  `title` CHAR(209) NOT NULL ,
  `budget` INT UNSIGNED ,
  `revenue` BIGINT UNSIGNED NOT NULL ,
  `runtime` MEDIUMINT NOT NULL ,
  `language` TINYTEXT NOT NULL ,
  `poster_link` TEXT NULL ,
  `release_year` YEAR NOT NULL ,
  `overview` MEDIUMTEXT NOT NULL ,
  PRIMARY KEY (`movie_id`) ,
  UNIQUE INDEX `movie_id_UNIQUE` (`movie_id` ASC) ,
  UNIQUE INDEX `title_UNIQUE` (`title` ASC) ,
  FULLTEXT `overview_ft_index` (`overview`),
  INDEX `budget_index` (`budget` ASC) );
  

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
  
                            
  CREATE  TABLE DbMysql08.department (
  `role` CHAR(50) NOT NULL ,
  `department` CHAR(20) NOT NULL ,
  `job_description` TEXT,
  PRIMARY KEY (`role`) ,
  UNIQUE INDEX `role_UNIQUE` (`role` ASC) );
  
                            
  CREATE  TABLE DbMysql08.locations (
  `location_id` INT NOT NULL AUTO_INCREMENT ,
  `movie_id` INT NOT NULL ,
  `country` CHAR(56) NOT NULL ,
  PRIMARY KEY (`location_id`) ,
  FOREIGN KEY (movie_id) REFERENCES DbMysql08.movies(movie_id),
  UNIQUE INDEX `location_id_UNIQUE` (`location_id` ASC) );
  
 
CREATE  TABLE DbMysql08.genres (
  `genre_id` INT NOT NULL AUTO_INCREMENT ,
  `movie_id` INT NOT NULL ,
  `genre` CHAR(20) NOT NULL ,
  PRIMARY KEY (`genre_id`) ,
  FOREIGN KEY (movie_id) REFERENCES DbMysql08.movies(movie_id),
  UNIQUE INDEX `genre_id_UNIQUE` (`genre_id` ASC)
);
                            

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
