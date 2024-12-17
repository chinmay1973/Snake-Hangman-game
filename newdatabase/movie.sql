-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: hangman
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movies` (
  `Id` int DEFAULT NULL,
  `Movie` char(100) DEFAULT NULL,
  `Hint1` char(100) DEFAULT NULL,
  `Hint2` char(100) DEFAULT NULL,
  `Hint3` char(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
INSERT INTO `movies` VALUES (1,'Titanic','Leonardo DiCaprio','Kate Winslet','Iceburg'),(2,'Prestige','Hugh Jackman','Christian Bale','Directed by Christopher Nolan, Magicians'),(3,'The Social Network','Jesse Eisenberg','Andrew Garfield','Story about facebook'),(4,'Grown Ups','Adam Sandler','Kevin James','Story about 5 friends reuniting'),(5,'Doctor Strange','Bennedict Cumberbatch','Rachel Admas','Doctor by day, Magician by night'),(6,'Sherlock Holmes','Robert Downey, Jr.','Rachel Adams','Based on famous crime solving novel'),(7,'The Shining','Jack Nicholson','1980 horror/mystery movie','Stephen King'),(8,'50 first dates','Adam Sandler','Drew Barrymore','Short term memory loss'),(9,'Avatar','Zoe Saldana','Sam Worthington','Directed by James Cameron'),(10,'Furious 7','Vin Diesel','Paul Walker','Robbery of God\'s Eye'),(11,'The Matrix','Keanu Reeves','Laurence Fishburne','War of humanity against comuptrers'),(12,'Marley and me','Owen Wilson','Jennifer Aniston','A couple adopts a puppy named Marley'),(13,'Once upon a time in hollywood','Leonard Dicaprio','Brad Pitt','Academy award nominee and winner in 2020'),(14,'Parasite','Park So-Dam','Korean Movie','Won 4 Academy award'),(15,'Harry potter and the goblet of fire','Daniel Radcliffe','Emma Watson','Tri wizerd tournament'),(16,'The Mummy','Tom Cruise','Sofia Boutella','Dead evil princess is set free by Seargent Nick, who is now after his life.'),(17,'The Dark Knight','Christian bale','Heath Ledger','Directed by Christopher Nolan'),(18,'Jumanji Welcome to the jungle','Karen Gillan','Jack Black','When four students play with a magical video game, where they are trapped as their avatars.'),(19,'Bumblebee','Haliee Steinfeld','John Cena','Voice of the main character given by Dylan O\'Brian,Time during Cybertron Civil war'),(20,'Bohemian Rhapsody','Rami Malek','Queen','Biography of a famous singer'),(21,'Captain Marvel','Brie Larson','Samuel L. jackson','Vers'),(22,'The Jungle Book','Real life remake of an animated movie','Voice of an character given by Scarllet Johnason','a boy brought up in the jungle by a pack of wolves'),(23,'Life of Pi','Suraj Sharma','Irrfan Khan','A boy finds a way to survive in a lifeboat that is adrift in the middle of nowhere. His fight against the odds is heightened by the company of a hyena and a male Bengal tiger.'),(24,'The Hunger Games','Jennifer Lawrence','Liam Hemsworth and Josh Hutcherson','District 12 heros'),(25,'Man of Steel','Henry Cavill','Amy Adams','2013 make of beloved DC character'),(26,'Aladdin','Will Smith','Naomi Scott','Famous arabian nights story'),(27,'Pirates of the Caribbean: The Curse of the Black Pearl','Keira Knightley','Johnny Depp','First part of a very famous movie series on the waters'),(28,'Tomorrowland: A World Beyond','George Clooney','Britt Robertson','Frank, a former inventor, and Casey, a curious teenager, embark on a dangerous mission to unravel the secrets of an unexplored dimension in time and space.'),(29,'Knives Out','Chris Evans','Katherine Langford','Murder mystery of a crime novelist'),(30,'National Treasure','Nicolas Cage','Diane Kruger','Iconic character of the movie-Benjamin Franklin Gates');
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-27 15:52:06
