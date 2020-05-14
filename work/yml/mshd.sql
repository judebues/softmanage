-- MySQL dump 10.13  Distrib 5.7.27, for Win64 (x86_64)
--
-- Host: localhost    Database: mshd
-- ------------------------------------------------------
-- Server version	5.7.27-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `commdisaster`
--
SET character_set_client = utf8;


DROP TABLE IF EXISTS `dataSourceMainCode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dataSourceMainCode` (
  `Code` varchar(1) NOT NULL,
  `info` varchar(100) NOT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `dataSourceMainCode` VALUES ('1','业务报送数据');
INSERT INTO `dataSourceMainCode` VALUES ('2','泛在感知数据');
INSERT INTO `dataSourceMainCode` VALUES ('3','舆情感知数据');
INSERT INTO `dataSourceMainCode` VALUES ('4','承载体基础数据');
INSERT INTO `dataSourceMainCode` VALUES ('5','其他');



DROP TABLE IF EXISTS `dataSourceSubCode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dataSourceSubCode` (
  `Code` varchar(3) NOT NULL,
  `info` varchar(100) NOT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `dataSourceSubCode` VALUES ('101','公网');
INSERT INTO `dataSourceSubCode` VALUES ('102','北斗短报文');
INSERT INTO `dataSourceSubCode` VALUES ('103','卫星通讯');
INSERT INTO `dataSourceSubCode` VALUES ('104','卫星定位');
INSERT INTO `dataSourceSubCode` VALUES ('105','专用救灾');
INSERT INTO `dataSourceSubCode` VALUES ('106','其他');

INSERT INTO `dataSourceSubCode` VALUES ('201','互联网');
INSERT INTO `dataSourceSubCode` VALUES ('202','通信网');
INSERT INTO `dataSourceSubCode` VALUES ('203','电网');
INSERT INTO `dataSourceSubCode` VALUES ('204','其他');

INSERT INTO `dataSourceSubCode` VALUES ('301','微博');
INSERT INTO `dataSourceSubCode` VALUES ('302','博客');
INSERT INTO `dataSourceSubCode` VALUES ('303','论坛');
INSERT INTO `dataSourceSubCode` VALUES ('304','微信');
INSERT INTO `dataSourceSubCode` VALUES ('305','其他');

INSERT INTO `dataSourceSubCode` VALUES ('401','川滇');
INSERT INTO `dataSourceSubCode` VALUES ('402','其他');

INSERT INTO `dataSourceSubCode` VALUES ('501','1-其他');
INSERT INTO `dataSourceSubCode` VALUES ('502','2-其他');
INSERT INTO `dataSourceSubCode` VALUES ('503','3-其他');



DROP TABLE IF EXISTS `province`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `province` (
  `Code` varchar(2) NOT NULL,
  `info` varchar(100) NOT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `province` VALUES ('11','北京市');
INSERT INTO `province` VALUES ('22','上海市');
INSERT INTO `province` VALUES ('33','山东省');
INSERT INTO `province` VALUES ('44','云南省');



DROP TABLE IF EXISTS `city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `city` (
  `Code` varchar(2) NOT NULL,
  `info` varchar(100) NOT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `city` VALUES ('11','青岛市');
INSERT INTO `city` VALUES ('22','昆明市');
INSERT INTO `city` VALUES ('33','泰安市');
INSERT INTO `city` VALUES ('44','曲靖市');

DROP TABLE IF EXISTS `county`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `county` (
  `Code` varchar(2) NOT NULL,
  `info` varchar(100) NOT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `county` VALUES ('11','海淀区');
INSERT INTO `county` VALUES ('22','大兴区');
INSERT INTO `county` VALUES ('33','麒麟区');
INSERT INTO `county` VALUES ('44','浦东新区');

DROP TABLE IF EXISTS `street`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `street` (
  `Code` varchar(3) NOT NULL,
  `info` varchar(100) NOT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `street` VALUES ('111','西土城路');
INSERT INTO `street` VALUES ('222','中关村路');
INSERT INTO `street` VALUES ('333','北太平庄街道');
INSERT INTO `street` VALUES ('444','潇湘街道');


DROP TABLE IF EXISTS `community`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `community` (
  `Code` varchar(3) NOT NULL,
  `info` varchar(100) NOT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `community` VALUES ('111','甲村');
INSERT INTO `community` VALUES ('222','乙村');
INSERT INTO `community` VALUES ('333','丙村');
INSERT INTO `community` VALUES ('444','丁村');



DROP TABLE IF EXISTS `disInfo_mainClass`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;

CREATE TABLE `disInfo_mainClass` (
  `Code` varchar(1) NOT NULL,
  `info` varchar(100) NOT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `disInfo_mainClass` VALUES ('1','人员伤亡及失踪');
INSERT INTO `disInfo_mainClass` VALUES ('2','房屋破坏');
INSERT INTO `disInfo_mainClass` VALUES ('3','生命线工程灾情');
INSERT INTO `disInfo_mainClass` VALUES ('4','次生灾害');
INSERT INTO `disInfo_mainClass` VALUES ('5','震情');


DROP TABLE IF EXISTS `disInfo_subClass`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;

CREATE TABLE `disInfo_subClass` (
  `Code` varchar(2) NOT NULL,
  `info` varchar(100) NOT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `disInfo_subClass` VALUES ('11','死亡');
INSERT INTO `disInfo_subClass` VALUES ('12','受伤');
INSERT INTO `disInfo_subClass` VALUES ('13','失踪');
INSERT INTO `disInfo_subClass` VALUES ('21','土木');
INSERT INTO `disInfo_subClass` VALUES ('22','砖木');
INSERT INTO `disInfo_subClass` VALUES ('23','砖混');
INSERT INTO `disInfo_subClass` VALUES ('24','框架');
INSERT INTO `disInfo_subClass` VALUES ('25','其他');
INSERT INTO `disInfo_subClass` VALUES ('31','交通');
INSERT INTO `disInfo_subClass` VALUES ('32','供水');
INSERT INTO `disInfo_subClass` VALUES ('33','输油');
INSERT INTO `disInfo_subClass` VALUES ('34','燃气');
INSERT INTO `disInfo_subClass` VALUES ('35','电力');
INSERT INTO `disInfo_subClass` VALUES ('36','通信');
INSERT INTO `disInfo_subClass` VALUES ('37','水利');
INSERT INTO `disInfo_subClass` VALUES ('41','崩塌');
INSERT INTO `disInfo_subClass` VALUES ('42','滑坡');
INSERT INTO `disInfo_subClass` VALUES ('43','泥石流');
INSERT INTO `disInfo_subClass` VALUES ('44','岩溶塌陷');
INSERT INTO `disInfo_subClass` VALUES ('45','地裂缝');
INSERT INTO `disInfo_subClass` VALUES ('46','地面沉降');
INSERT INTO `disInfo_subClass` VALUES ('47','其他');
INSERT INTO `disInfo_subClass` VALUES ('51','基本');
INSERT INTO `disInfo_subClass` VALUES ('52','灾情预测');


DROP TABLE IF EXISTS `disInfo_tableName`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;

CREATE TABLE `disInfo_tableName` (
  `Code` varchar(3) NOT NULL,
  `info` varchar(100) NOT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `disInfo_tableName` VALUES ('111','DeathStatistics');
INSERT INTO `disInfo_tableName` VALUES ('221','CivilStructure');
INSERT INTO `disInfo_tableName` VALUES ('336','CommDisaster');
INSERT INTO `disInfo_tableName` VALUES ('441','CollapseRecord');
INSERT INTO `disInfo_tableName` VALUES ('552','DisasterPrediction');
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS `CommDisaster`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CommDisaster` (
  `ID` varchar(19) NOT NULL,
  `date` datetime NOT NULL,
  `location` varchar(100) NOT NULL,
  `type` enum('I','II') NOT NULL,
  `grade` enum('I','II','III','IV','V') NOT NULL,
/*  `picture` mediumblob NOT NULL,*/
  `note` varchar(200) DEFAULT NULL,
  `reportingUnit` varchar(50) NOT NULL,
  PRIMARY KEY (`id`,`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS `DeathStatistics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DeathStatistics` (
  `ID` varchar(19) NOT NULL,
  `date` datetime NOT NULL,
  `location` varchar(100) NOT NULL,
  `number` varchar(5) NOT NULL,
  `reportingUnit` varchar(50) NOT NULL,
  PRIMARY KEY (`id`,`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

DROP TABLE IF EXISTS `CivilStructure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CivilStructure` (
  `ID` varchar(19) NOT NULL,
  `date` datetime NOT NULL,
  `location` varchar(100) NOT NULL,
  `basicallyIntactSquare` varchar(6) NOT NULL,
  `damagedSquare` varchar(6) NOT NULL,
  `distoryedSquare` varchar(6) NOT NULL,
  `note` varchar(200) DEFAULT NULL,
  `reportingUnit` varchar(50) NOT NULL,
  PRIMARY KEY (`id`,`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

DROP TABLE IF EXISTS `CollapseRecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CollapseRecord` (
  `ID` varchar(19) NOT NULL,
  `date` datetime NOT NULL,
  `location` varchar(100) NOT NULL,
  `type` enum('I','II','III','IV') NOT NULL,
  `status` enum('I','II','III','IV') NOT NULL,
  `note` varchar(200) DEFAULT NULL,
  /*  `picture` mediumblob NOT NULL,*/
  `reportingUnit` varchar(50) NOT NULL,
  PRIMARY KEY (`id`,`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

DROP TABLE IF EXISTS `DisasterPrediction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DisasterPrediction` (
  `ID` varchar(19) NOT NULL,
  `date` datetime NOT NULL,
  `location` varchar(100) NOT NULL,
  `longitude` float NOT NULL,
  `latitude` float NOT NULL,
  `depth` float NOT NULL,
  `magnitude` float NOT NULL,
  `intensity` varchar(6) NOT NULL,
  `type` enum('I','II','III','IV') NOT NULL,
  `status` enum('I','II','III','IV') NOT NULL,
  `note` varchar(200) DEFAULT NULL,
  /*  `picture` mediumblob NOT NULL,*/
  `reportingUnit` varchar(50) NOT NULL,
  PRIMARY KEY (`id`,`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS `DisasterRequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DisasterRequest` (
  `ID` varchar(19) NOT NULL,
  `date` datetime NOT NULL,
  `disastertype` varchar(3) NOT NULL,
  `status` varchar(1) NOT NULL,
  `o_URL` varchar(200) DEFAULT NULL,
  /*  `picture` mediumblob NOT NULL,*/
  `reportingUnit` varchar(50) NOT NULL,
  PRIMARY KEY (`id`,`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;



/*!40000 ALTER TABLE `commdisaster` DISABLE KEYS */;
/*
INSERT INTO `commdisaster` VALUES (
			'1100001000001110000',
			'2019-03-05 01:53:55',
			'北京市-海淀区-西土城路10号北京邮电大学',
			'I',
			'I',
			'新冠肺炎疫情',
			'北京邮电大学软件学院');

INSERT INTO `commdisaster` VALUES (
			'1234566543211110000',
			'2019-03-05 01:53:55',
			'北京市-海淀区-西土城路10号北京邮电大学',
			'I',
			'I',
			'新冠肺炎疫情',
			'北京邮电大学软件学院');
			
INSERT INTO `commdisaster` VALUES (
			'1112223334445551000',
			'2019-03-05 01:53:55',
			'北京市-海淀区-西土城路10号北京邮电大学',
			'I',
			'I',
			'新冠肺炎疫情',
			'北京邮电大学软件学院');  */
	
/*!40000 ALTER TABLE `commdisaster` ENABLE KEYS */;



--
-- Dumping events for database 'mshd'
--
--
-- Dumping routines for database 'mshd'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-07 10:01:44
