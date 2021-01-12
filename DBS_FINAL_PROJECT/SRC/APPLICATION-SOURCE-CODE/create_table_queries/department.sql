CREATE  TABLE DbMysql08.department (
  `role` CHAR(50) NOT NULL ,
  `department` CHAR(20) NOT NULL ,
  `job_description` TEXT,
  PRIMARY KEY (`role`) ,
  UNIQUE INDEX `role_UNIQUE` (`role` ASC) );
