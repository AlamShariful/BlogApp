-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: blogapp
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.16.04.1

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
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(8) NOT NULL,
  `title` varchar(100) NOT NULL,
  `body` varchar(3000) NOT NULL,
  `author` varchar(50) NOT NULL,
  `approved` varchar(8) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES (3,0,'First Post edited','<h2>What is Lorem Ipsum?</h2><strong>Lorem Ipsum</strong> is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.<h2>Why do we use it?</h2>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using \'Content here, content here\', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for \'lorem ipsum\' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).<h2>Where does it come from?</h2>Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32.The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from \"de Finibus Bonorum et Malorum\" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.','SHARIFUL ALAM','waiting','2018-02-06 02:26:16'),(5,0,'Third Post','Thiasda','SHARIFUL ALAM','yes','2018-02-05 07:19:39'),(7,14,'Edited Post again','try new','SHARIFUL ALAM','waiting','2018-02-05 18:41:12'),(8,14,'from test 23rd','<blockquote>hi threr</blockquote>','SHARIFUL ALAM','yes','2018-02-06 02:32:06'),(9,14,'new Post for check','new Post for check','SHARIFUL ALAM','yes','2018-02-05 09:02:09'),(10,13,'Lorem Ipsum Final','<h2>What is Lorem Ipsum?</h2>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.<h2>What is Lorem Ipsum?</h2><strong>Lorem Ipsum</strong> is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.<h2>Why do we use it?</h2>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using \'Content here, content here\', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for \'lorem ipsum\' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).<h2>Where does it come from?</h2>Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32.The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from \"de Finibus Bonorum et Malorum\" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.','SHARIFUL ALAM','yes','2018-02-06 05:20:28');
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) NOT NULL,
  `username` varchar(25) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'gh','nm','kjlkjl','kjl'),(3,'SHARIFUL ALAM','sharifulalam','$5$rounds=535000$Ocs99SSZQZdwMpmC$cps2hya1R7mOG7nTFWKu1dkxSfjU2prCt9sVdGgvvR.','dipto181@gmail.com'),(4,'SHARIFUL ALAM','sharifulalam','$5$rounds=535000$cfXPwHGWj/JqImjG$UhSmfY0ysHKY7kiB63tHxBMYx2gdJAAKW9PQZ1ikRy8','dipto181@gmail.com'),(5,'SHARIFUL ALAM','sharifulalam','$5$rounds=535000$yQZwu0d6tp53kMHT$OuHvGHOXmViueeOteLdX7ljN.TmZ5WFB8a5DpN8VLoB','dipto181@gmail.com'),(6,'SHARIFUL ALAM','sharifulalam','$5$rounds=535000$va9NbF611aeaj6Kz$Yx4TNy9Ri.nxnrFvHKbjju2EFCGWMGBihVE/JiNtGu1','dipto181@gmail.com'),(7,'SHARIFUL ALAM','sharifulalam','$5$rounds=535000$AGVv5LFjKU0tHCbM$O.2bibXHau3KGlS/81OOiQSwsuN80vXpz3KdhKgTeR1','dipto181@gmail.com'),(8,'SHARIFUL ALAM','sourav','$5$rounds=535000$S4YXTCxY8uTfXjHm$pWKg.hKB0g4IhQODhhbfQ/f/oUJqODufJXBwWHJEBFC','dipto181@gmail.com'),(9,'SHARIFUL ALAM','sourav','$5$rounds=535000$oOp1JeWpxRejPcIz$TmkY9WxpoxJO8fm6HiykJPpwkmNcN/W24sLumIr/Sp6','dipto181@gmail.com'),(10,'SHARIFUL ALAM','alam.shariful@hotmail.com','$5$rounds=535000$v5OfFAkHEWHdLrkA$6jAD15W08zhfKjrS8mh9AgpmteQdQiHzDjoyr2VgqkB','dipto181@gmail.com'),(11,'SHARIFUL ALAM','sdsfdgd','$5$rounds=535000$1AVlFpIf8V1M7jFR$xaq.krSP5xz5RW2hcHyYwhVkf7/8s2.jlngJIMY78XA','dipto181@gmail.com'),(12,'SHARIFUL ALAM','salam2','$5$rounds=535000$oBKzTsjOpHk5wQIV$uRXnoemE2hqo6ZxgjO12LQde6cmakQnPomUmhPwGFa2','dipto181@gmail.com'),(13,'SHARIFUL ALAM','admin','$5$rounds=535000$FQJWwFMc6hW.aF9O$S.E2cDb0b5gsi9adgTtUv1Jn5OCQNPaBMJDy/bFzQl0','dipto181@gmail.com'),(14,'SHARIFUL ALAM','test','$5$rounds=535000$AS4w9UQmodLkSvGA$cJJY40H4nm/N2neUmJVsKSQIRBAB2haBiHBS5Y2Fb31','dipto181@gmail.com'),(15,'SHARIFUL ALAM','admin','$5$rounds=535000$FaCnV7JrraYTkar4$ddRBEWjBOXedQDAb/hFreXS9RrMcke5jubLwazhQyY1','dipto181@gmail.com'),(16,'Ashraful Hoque','admin','$5$rounds=535000$4Od6ZBLFrQQ3A.4B$8VQSYg5UYJWZ/YoLOTbUX/GVKQmTs8KVRpBzOd8lIA9','asd@gmail.com');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-02-06  7:10:51
