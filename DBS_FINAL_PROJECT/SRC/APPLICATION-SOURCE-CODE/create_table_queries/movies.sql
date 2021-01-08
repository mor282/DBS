CREATE  TABLE DbMysql08.movies(
  `movie_id` INT NOT NULL ,
  `title` CHAR(209) NOT NULL ,
  `budget` INT UNSIGNED NOT NULL ,
  `revenue` BIGINT UNSIGNED NOT NULL ,
  `runtime` MEDIUMINT NOT NULL ,
  `language` TINYTEXT NOT NULL ,
  `poster_link` TEXT NULL ,
  `release_year` YEAR NOT NULL ,
  `genre` SET('Action','Adventure','Animation','Comedy','Crime',
			'Documentary','Drama','Family','Fantasy','History','Horror',
			'Romance','Science Fiction','TV Movie','Thriller','War',
			'Western')NOT NULL ,
  `overview` MEDIUMTEXT NOT NULL ,
  PRIMARY KEY (`movie_id`) ,
  UNIQUE INDEX `movie_id_UNIQUE` (`movie_id` ASC) ,
  UNIQUE INDEX `title_UNIQUE` (`title` ASC) ,
  INDEX `title_index` (`title` ASC) ,
  INDEX `budget_index` (`budget` ASC) );
