CREATE DATABASE  IF NOT EXISTS `proyectocerberus` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `proyectocerberus`;
-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: proyectocerberus
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `conversation`
--

DROP TABLE IF EXISTS `conversation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `conversation` (
  `c_id` int NOT NULL AUTO_INCREMENT,
  `user` int NOT NULL,
  `trainer` int NOT NULL,
  `ip` varchar(45) NOT NULL,
  `time` int NOT NULL,
  `status` int NOT NULL,
  PRIMARY KEY (`c_id`),
  UNIQUE KEY `c_id_UNIQUE` (`c_id`),
  KEY `foreng_Key_user_idx` (`user`),
  KEY `fk_conversation_trainer1_idx` (`trainer`),
  CONSTRAINT `fk_conversation_trainer1` FOREIGN KEY (`trainer`) REFERENCES `trainer` (`id`),
  CONSTRAINT `foreng_Key_user` FOREIGN KEY (`user`) REFERENCES `user` (`iduser`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conversation`
--

LOCK TABLES `conversation` WRITE;
/*!40000 ALTER TABLE `conversation` DISABLE KEYS */;
INSERT INTO `conversation` VALUES (2,4,6,'192.168.0.1',0,1);
/*!40000 ALTER TABLE `conversation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conversation_reply`
--

DROP TABLE IF EXISTS `conversation_reply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `conversation_reply` (
  `cr_id` int NOT NULL AUTO_INCREMENT,
  `reply` text NOT NULL,
  `user_trainer_id_fk` int NOT NULL,
  `ip` varchar(45) NOT NULL,
  `time` int NOT NULL,
  `status` int NOT NULL,
  `c_id_fk` int NOT NULL,
  `typeUser` varchar(45) NOT NULL,
  PRIMARY KEY (`cr_id`),
  UNIQUE KEY `cr_id_UNIQUE` (`cr_id`),
  KEY `fk_conversation_reply_conversation1_idx` (`c_id_fk`),
  KEY `fk_conversation_reply_trainer1_idx` (`user_trainer_id_fk`),
  CONSTRAINT `fk_conversation_reply_conversation1` FOREIGN KEY (`c_id_fk`) REFERENCES `conversation` (`c_id`),
  CONSTRAINT `fk_conversation_reply_trainer1` FOREIGN KEY (`user_trainer_id_fk`) REFERENCES `trainer` (`id`),
  CONSTRAINT `fk_conversation_reply_user1` FOREIGN KEY (`user_trainer_id_fk`) REFERENCES `user` (`iduser`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conversation_reply`
--

LOCK TABLES `conversation_reply` WRITE;
/*!40000 ALTER TABLE `conversation_reply` DISABLE KEYS */;
INSERT INTO `conversation_reply` VALUES (8,'Hola mundo',4,'192.168.0.1',15556,1,2,'trainer'),(9,'Hola mundo',4,'192.168.0.1',15556,1,2,'trainer'),(10,'Hola mundo',4,'192.168.0.1',15556,1,2,'trainer'),(11,'Hola mundo',4,'192.168.0.1',15556,1,2,'trainer'),(12,'Hola mundo',4,'192.168.0.1',15556,1,2,'trainer');
/*!40000 ALTER TABLE `conversation_reply` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course` (
  `idcourse` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `description` varchar(500) NOT NULL,
  `duration` varchar(45) NOT NULL,
  `cost` double NOT NULL,
  `iduser` int DEFAULT NULL,
  `idtrainer` int NOT NULL,
  `estado` varchar(45) NOT NULL,
  PRIMARY KEY (`idcourse`),
  UNIQUE KEY `idcourse_UNIQUE` (`idcourse`),
  KEY `fk_course_user1_idx` (`iduser`),
  KEY `fk_course_trainer1_idx` (`idtrainer`),
  CONSTRAINT `fk_course_trainer1` FOREIGN KEY (`idtrainer`) REFERENCES `trainer` (`id`),
  CONSTRAINT `fk_course_user1` FOREIGN KEY (`iduser`) REFERENCES `user` (`iduser`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES (1,'test','test','test',1,3,4,'Finalizado'),(3,'test','test','test',2,3,4,'Finalizado'),(4,'test','test','test',5,3,4,'No finalizado'),(13,'Queso','Queso','Queso',10,4,4,'No finalizado'),(15,'PanFrancesQueso','PanFrancesQueso','PanFrancesQueso',60,NULL,4,'No finalizado'),(20,'Abel','Pan3','tres meses',1,3,4,'No finalizado'),(21,'Sentadillas','Curso de 3 meses con información de dieta incluido','medio año',40,3,4,'No finalizado'),(22,'Flexiones','Curso completo para bajar la dieta con optimización de dieta garantizado!','1 año',100,NULL,9,'No finalizado');
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pays`
--

DROP TABLE IF EXISTS `pays`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pays` (
  `id` int NOT NULL AUTO_INCREMENT,
  `iduser` int NOT NULL,
  `tarjeta` varchar(45) NOT NULL,
  `cvv` varchar(45) NOT NULL,
  `month` int NOT NULL,
  `year` int NOT NULL,
  `ownercard` varchar(45) NOT NULL,
  `date` varchar(45) NOT NULL,
  `amount` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_pays_user1_idx` (`iduser`),
  CONSTRAINT `fk_pays_user1` FOREIGN KEY (`iduser`) REFERENCES `user` (`iduser`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pays`
--

LOCK TABLES `pays` WRITE;
/*!40000 ALTER TABLE `pays` DISABLE KEYS */;
/*!40000 ALTER TABLE `pays` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `routine`
--

DROP TABLE IF EXISTS `routine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `routine` (
  `id` int NOT NULL,
  `idtrainer` int NOT NULL,
  `iduser` int NOT NULL,
  `exercise` varchar(100) NOT NULL,
  `step` int NOT NULL,
  `time` varchar(6) NOT NULL,
  `repetition` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_routine_trainer1_idx` (`idtrainer`),
  KEY `fk_routine_user1_idx` (`iduser`),
  CONSTRAINT `fk_routine_trainer1` FOREIGN KEY (`idtrainer`) REFERENCES `trainer` (`id`),
  CONSTRAINT `fk_routine_user1` FOREIGN KEY (`iduser`) REFERENCES `user` (`iduser`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `routine`
--

LOCK TABLES `routine` WRITE;
/*!40000 ALTER TABLE `routine` DISABLE KEYS */;
INSERT INTO `routine` VALUES (1,4,3,'test1',2,'4','20 set'),(2,4,3,'test1',1,'9','15 set'),(3,4,3,'test2',4,'12','4 set');
/*!40000 ALTER TABLE `routine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trainer`
--

DROP TABLE IF EXISTS `trainer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trainer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `description` varchar(500) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trainer`
--

LOCK TABLES `trainer` WRITE;
/*!40000 ALTER TABLE `trainer` DISABLE KEYS */;
INSERT INTO `trainer` VALUES (4,'prueba','test','test','test','test','test@test'),(6,'Karl','Marx','BestTrainer','123','Soy etc, etc, etc...','karl@email.com'),(8,'Karl','Marx2','BestTrainer2','123','Soy etc, etc, etc...','karl@email.com'),(9,'Karl','Marx3','BestTrainer3','123','Soy etc, etc, etc...','karl@email.com');
/*!40000 ALTER TABLE `trainer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `iduser` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `age` int NOT NULL,
  `weigth` double NOT NULL,
  `size` double NOT NULL,
  `gender` tinyint NOT NULL,
  `wallet` double NOT NULL,
  PRIMARY KEY (`iduser`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (3,'Abel','Cárdenas','Kabel','123','abel_acc@outlook.com',19,180.12,1.82,1,0),(4,'Jhon','Treiner','morex','1234','morex@usa',22,12.3,1.85,1,90);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-26 12:17:54
