-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 16, 2024 at 02:26 AM
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
-- Database: `hall_booking`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking info`
--

CREATE TABLE `booking info` (
  `full_name` text NOT NULL,
  `email` varchar(100) NOT NULL,
  `hall_name` char(100) NOT NULL,
  `time_from` int(50) NOT NULL,
  `time_to` int(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `event_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `booking info`
--

INSERT INTO `booking info` (`full_name`, `email`, `hall_name`, `time_from`, `time_to`, `date`, `event_name`) VALUES
('Jamal', 'jamal@gmail.com', 'Dewan Seri Merbok', 8, 10, '17/01/24', 'Makan2'),
('Luzman', 'luzz@gmail', 'Dewan Seri Merbok', 6, 8, '16/01/24', 'Borak'),
('Luzman', 'luz@gmail.com', 'Dewan Seri Merbok', 2, 5, '19/01/24', 'Borak'),
('Narza', 'deden.encem@gmail.com', 'Dewan Seri Jerai', 1, 4, '16/01/24', 'PDRM');

-- --------------------------------------------------------

--
-- Table structure for table `date/time`
--

CREATE TABLE `date/time` (
  `time_from` int(50) NOT NULL,
  `time_to` int(50) NOT NULL,
  `calendar_date` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `date/time`
--

INSERT INTO `date/time` (`time_from`, `time_to`, `calendar_date`) VALUES
(6, 8, '0'),
(6, 8, '0');

-- --------------------------------------------------------

--
-- Table structure for table `halls`
--

CREATE TABLE `halls` (
  `hall_name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `halls`
--

INSERT INTO `halls` (`hall_name`) VALUES
('Dewan Seri Merbok'),
('Dewan Perdana'),
('Dewan Seri Merbok'),
('Dewan Seri Merbok'),
('Dewan Seri Jerai');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
