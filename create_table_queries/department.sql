CREATE  TABLE DbMysql08.department (
  `role` CHAR(50) NOT NULL ,
  `department` CHAR(20) NOT NULL ,
  PRIMARY KEY (`role`) ,
  UNIQUE INDEX `role_UNIQUE` (`role` ASC) );
