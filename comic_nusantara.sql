-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2024 at 02:25 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `comic nusantara`
--

-- --------------------------------------------------------

--
-- Table structure for table `buyer information`
--

CREATE TABLE `buyer information` (
  `Buyer_Name` varchar(100) NOT NULL,
  `User_Address` varchar(500) NOT NULL,
  `User_Email` varchar(100) NOT NULL,
  `Comic_Series` varchar(50) NOT NULL,
  `Comic_Volume` int(50) NOT NULL,
  `Comic_Quantity` int(50) NOT NULL,
  `Comic_Bundle` varchar(50) NOT NULL,
  `Bundle_Quantity` int(50) NOT NULL,
  `Total_Price` int(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `buyer information`
--

INSERT INTO `buyer information` (`Buyer_Name`, `User_Address`, `User_Email`, `Comic_Series`, `Comic_Volume`, `Comic_Quantity`, `Comic_Bundle`, `Bundle_Quantity`, `Total_Price`) VALUES
('Jamal', 'Perak', 'Jamal@gmail.com', '0', 1, 2, '0', 2, 26),
('Arumugam', 'Mumbai', 'arumugam123@gmail.com', '0', 2, 2, '0', 2, 26),
('Arumugam', 'Mumbai', 'arumugam123@gmail.com', 'Aku, Engkau, dan Jamal', 2, 2, '0', 2, 26),
('Ah Meng', 'Latvia', 'AHmeng@yahoo.com', 'Atomen', 3, 3, '0', 4, 49),
('Ah Meng', 'Latvia', 'AHmeng@yahoo.com', 'Atomen', 3, 3, 'Aspalela Bundle (1-4)', 4, 49),
('Salim', 'UK', 'Sally@yahoo.com', 'Awang Khenit', 3, 2, 'Avatar Bundle (1-4)', 3, 36),
('', '', '', '', 1, 0, '', 0, 0),
('', '', '', '', 1, 0, '', 0, 0),
('Ahmad', 'Perak', 'Jamal@gmail', 'Awang Khenit', 1, 2, 'Atomen Bundle (1-4)', 1, 16);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
