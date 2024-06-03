-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: academease
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `ease_course`
--

DROP TABLE IF EXISTS `ease_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ease_course` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `semester` varchar(255) NOT NULL,
  `course_code` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `hours_lecture` int DEFAULT NULL,
  `hours_tutorial` int DEFAULT NULL,
  `hours_lab` int DEFAULT NULL,
  `pre_requisite` longtext,
  `ects_credit` varchar(255) DEFAULT NULL,
  `total_credits` varchar(255) DEFAULT NULL,
  `grade` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=393 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ease_course`
--

LOCK TABLES `ease_course` WRITE;
/*!40000 ALTER TABLE `ease_course` DISABLE KEYS */;
INSERT INTO `ease_course` VALUES (1,'1','ENGR101','INFORMATION TECHNOLOGY AND APPLICATIONS','FC',2,0,1,'None','2','2','NG'),(2,'1','ENGR103','COMPUTER PROGRAMMING-I','FC',2,0,2,'None','5','3','D'),(3,'1','MATH121','CALCULUS-I','FC',3,2,0,'None','6','4','C'),(4,'1','MATH123','DISCRETE MATHEMATICS','FC',3,1,0,'None','5','3','C-'),(5,'1','PHYS121','PHYSICS-I','FC',3,1,1,'None','5','4','D'),(6,'1','ENGL121','ENGLISH-I','UC',3,0,0,'None','4','3','B+'),(7,'1','TUOG101 / TURK131','TURKISH LANGUAGE-I / TURKISH AS A FOREIGN LANGUAGE-I','UC',2,0,0,'None','3','2','B'),(8,'2','ENGR104','COMPUTER PROGRAMMING-II','FC',2,0,2,'ENGR103','4','3','A'),(9,'2','MATH122','CALCULUS-II','FC',3,2,0,'MATH121','6','4','D'),(10,'2','MATH124','LINEAR ALGEBRA','FC',3,1,0,'None','5','3','None'),(11,'2','PHYS122','PHYSICS-II','FC',3,1,1,'PHYS121','5','4','F'),(12,'2','ENGL122','ENGLISH-II','UC',3,0,0,'ENGL121','4','3','None'),(13,'2','TARH101 / HIST111','ATATURKS PRINCIPLES AND HISTORY OF TURKISH REFORMS-I','UC',2,0,0,'None','3','2','None'),(14,'2','TUOG102 / TURK132','TURKISH LANGUAGE-II / TURKISH AS A FOREIGN LANGUAGE-II','UC',2,0,0,'- / TURK131','3','2','None'),(15,'3','CMPE215','ALGORITHMS AND DATA STRUCTURES','AC',3,0,1,'ENGR104','6','3','None'),(16,'3','ELEE211','DIGITAL LOGIC DESIGN','AC',3,0,2,'None','6','4','None'),(17,'3','ELEE231','CIRCUIT THEORY-I','AC',3,0,2,'MATH124 / PHYS122','6','4','None'),(18,'3','MATH225','DIFFERENTIAL EQUATIONS','FC',4,0,0,'MATH121 / MATH124','5','4','None'),(19,'3','TARH102 / HIST112','ATATURKS PRINCIPLES AND HISTORY OF TURKISH REFORMS-II','UC',2,0,0,'None','3','2','None'),(20,'3','UNIEXX1','UNIVERSITY ELECTIVE','UE',0,0,0,'None','4','3','None'),(21,'4','CMPE216','OBJECT ORIENTED PROGRAMMING','AC',2,0,2,'ENGR104','6','3','None'),(22,'4','CMPE232','OPERATING SYSTEMS','AC',3,0,0,'ENGR104','6','3','None'),(23,'4','CMPE252','ANALYSIS OF ALGORITHMS ','AC',3,0,2,'CMPE215','6','4','None'),(24,'4','ENGR215','RESEARCH METHODS FOR ENGINEERING AND ARCHITECTURE','FC',2,0,0,'None','3','2','None'),(25,'4','OHSA206','OCCUPATIONAL HEALTH AND SAFETY','FC',3,0,0,'None','3','3','None'),(26,'4','STAT226','PROBABILITY AND STATISTICS','FC',3,1,0,'MATH121','6','3','None'),(27,'5','CMPE321','MICROPROCESSORS','AC',3,0,2,'ELEE211','6','4','None'),(28,'5','CMPE341','DATABASE SYSTEMS','AC',3,0,2,'CMPE215','5','4','None'),(29,'5','ELEE341','ELECTRONICS-I','AC',3,0,2,'ELEE231','5','4','None'),(30,'5','SFWE343','SOFTWARE ANALYSIS AND DESIGN','AC',2,0,2,'CMPE216','5','3','None'),(31,'5','ENGRXX1','FACULTY ELECTIVE','FE',0,0,0,'None','5','3','None'),(32,'5','UNIEXX2','UNIVERSITY ELECTIVE','UE',0,0,0,'None','4','3','None'),(33,'6','CMPE322','DATA COMMUNICATION AND COMPUTER NETWORKS','AC',3,0,2,'CMPE215','5','4','None'),(34,'6','CMPE324','COMPUTER ARCHITECTURE','AC',3,0,0,'ELEE211','5','3','None'),(35,'6','MATH328','NUMERICAL ANALYSIS','FC',3,1,0,'MATH124 / MATH225','6','3','None'),(36,'6','ENGRXX2','FACULTY ELECTIVE','FE',0,0,0,'None','5','3','None'),(37,'6','ENGRXX3','FACULTY ELECTIVE','FE',0,0,0,'None','5','3','None'),(38,'6','UNIEXX3','UNIVERSITY ELECTIVE','UE',0,0,0,'None','4','3','None'),(39,'7','CMPE403','SUMMER TRAINING','AC',0,0,0,'None','2','0','None'),(40,'7','CMPE421','PROGRAMMING LANGUAGES','AC',3,0,0,'CMPE216','6','3','None'),(41,'7','ENGR401','ENGINEERING DESIGN-I','FC',1,0,2,'None','6','2','None'),(42,'7','CMPEXX1','AREA ELECTIVE','AE',0,0,0,'None','6','3','None'),(43,'7','CMPEXX2','AREA ELECTIVE','AE',0,0,0,'None','6','3','None'),(44,'7','UNIEXX4','UNIVERSITY ELECTIVE','UE',0,0,0,'None','4','3','None'),(45,'8','ENGR402','ENGINEERING DESIGN-II','FC',1,0,2,'ENGR401','10','2','None'),(46,'8','ENGR404','ENGINEERING ATTRIBUTES AND ETHICS','FC',2,0,0,'None','3','2','None'),(47,'8','CMPEXX3','AREA ELECTIVE','AE',0,0,0,'None','6','3','None'),(48,'8','CMPEXX4','AREA ELECTIVE','AE',0,0,0,'None','6','3','None'),(49,'8','ENGRXX4','FACULTY ELECTIVE','FE',0,0,0,'None','5','3','None'),(50,'1','MATH 101','Calculus 1','FC',4,1,0,'None','6','4','None'),(51,'1','PHYS 101','Physics 1','FC',3,2,0,'None','6','4','None'),(52,'1','MATH 103','Discrete Mathematics','FC',3,0,0,'None','6','3','None'),(53,'1','COMP 100','Fundamentals of Computer Eng.','AC',2,2,0,'None','3','3','None'),(54,'1','COMP 103','Information Technology and Applications','UC',2,1,0,'None','3','2','None'),(55,'1','ENGL101','English I','UC',3,0,0,'None','6','3','None'),(56,'2','MATH 102','Calculus II','FC',4,1,0,'MATH101','6','4','None'),(57,'2','MATH 104','Linear Algebra','FC',3,1,0,'None','5','3','None'),(58,'2','PHYS 102','Physics II','FC',3,2,0,'PHYS101','6','4','None'),(59,'2',' COMP 104',' Computer Programming',' UC',3,2,0,'None','6','4','None'),(60,'2','ENGL102','English II','UC',3,0,0,'ENGL101','6','3','None'),(61,'3','MATH 205','Differential Equations','FC',4,1,0,'MATH101 / MATH104','6','4','None'),(62,'3','COMP 215','Algorithms and Data Structures','AC',3,2,0,'COMP 104','6','4','None'),(63,'3','COMP 225','Digital Logic Design','AC',3,2,0,'MATH103','6','4','None'),(64,'3','ELEC 235','Electrical Circuits','AC',3,2,0,'MATH101','6','4','None'),(65,'3','GEED-01',' General Education Elective-I','UE',3,0,0,'None','4','3','None'),(66,'3','ENGL201','English III','FC',2,0,0,'ENGL102','4','2','None'),(67,'4','MATH 206',' Probability and Statistics','FC',3,1,0,'MATH102','5','3','None'),(68,'4','COMP 216','Object Oriented Programming','AC',3,2,0,' COMP104','6','4','None'),(69,'4',' COMP 232','Operating Systems','AC',3,0,0,'COMP104','6','3','None'),(70,'4','ELEC 240','Electronics','AC',3,1,0,'ELEC 235','5','3','None'),(71,'4','GEED-02','General Education Elective-II',' UE',3,0,0,'None','4','3','None'),(72,'4','HIST100/TURK100','History of Turkish Republic/Turkish as a Second Language',' UC',2,0,0,'None','2','2','None'),(73,'5','MATH 309',' Numerical Analysis','AC',3,1,0,'COMP104/MATH205','6','3','None'),(74,'5','COMP 321 ','Microprocessors','AC',3,2,0,'COMP225','6','4','None'),(75,'5','COMP 333','Systems Programming','AC',3,0,0,'COMP232','6','3','None'),(76,'5','COMP 341','Database Systems',' AC',3,2,0,'COMP215','6','4','None'),(77,'5','COMP 351','Analysis of Algorithms',' AC',3,2,0,'COMP215','6','4','None'),(78,'6','COMP 322','Signals and Systems','AC',3,0,0,'ELEC 240','6','3','None'),(79,'6','COMP 324','Computer Architecture',' AC',3,0,0,'COMP 225','5','3','None'),(80,'6','COMP 332',' Data Communication and Computer Networks','AC',3,2,0,'COMP 215','6','4','None'),(81,'6','COMP 342','Software Engineering','AC',3,2,0,'COMP 215','6','4','None'),(82,'6','COMP 352',' Programming Languages','AC',3,0,0,'COMP 216','6','3','None'),(83,'7','COMP 401','Engineering Design I','FC',1,4,0,'None','6','3','None'),(84,'7','COMP 403','Summer Training','FC',0,0,0,'None','1','0','None'),(85,'7','COMP 471','Computer Simulation',' AC',3,0,0,'COMP 215/MATH206','6','3','None'),(86,'7','TE-01','Technical Elective','AE',3,0,0,'None','7','3','None'),(87,'7','TE-02','Technical Elective','AE',3,0,0,'None','7','3','None'),(88,'7',' GEED-03',' General Education Elective-III',' UE',3,0,0,'None','4','3','None'),(89,'8',' COMP 402','Engineering Design II','FC',0,8,4,'None','8','COMP 401','None'),(90,'8',' COMP 404','Engineering Attributes & Ethics','FC',2,0,0,'None','3','2','None'),(91,'8','COMP 454','Automata Theory',' AC',3,0,0,'MATH103','6','3','None'),(92,'8','TE-03','Technical Elective','AE',3,0,0,'None','7','3','None'),(93,'8','TE-04','Technical Elective','AE',3,0,0,'None','7','3','None');
/*!40000 ALTER TABLE `ease_course` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-02 22:04:27
