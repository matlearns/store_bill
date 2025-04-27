-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 27, 2025 at 02:52 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `store_bill`
--

-- --------------------------------------------------------

--
-- Table structure for table `cost_calculation`
--

CREATE TABLE `cost_calculation` (
  `item_number` int(3) NOT NULL,
  `service_code` char(2) NOT NULL,
  `service` varchar(50) NOT NULL,
  `cost_price` float NOT NULL,
  `maintenance_cost` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cost_calculation`
--

INSERT INTO `cost_calculation` (`item_number`, `service_code`, `service`, `cost_price`, `maintenance_cost`) VALUES
(1, 'AF', 'Application & other in format', 2.95, 1.5),
(2, 'BS', 'Ball pen (safari)', 7.5, 0),
(3, 'BT', 'Ball pen (techno Tip)', 15, 0),
(4, 'BC', 'Ball pen Cheapest', 4.25, 0),
(5, 'BN', 'Binding (tape)', 25, 3),
(6, 'CF', 'Campus Form Online', 3, 3),
(7, 'CB', 'Clear Bag Cheaper', 20, 0),
(8, 'CE', 'Clear Bag Expensive', 28, 0),
(9, 'CP', 'Color/BW print', 5, 5),
(10, 'DR', 'DishHome Recharge', 814, 5),
(11, 'DE', 'Document Edit/IEMIS/Reference/Translation/Design ', 3, 3),
(12, 'ES', 'Extra Sells (Input Every Cell Manually)', 14, 1.25),
(13, 'FR', 'File (Record)', 5, 0),
(14, 'GR', 'Grant/Free/Extra Profit/Extra Works/Loss/Refer Int', 0, 0),
(15, 'IC', 'ID Card (TJMC) with Holder and Cover', 39.6, 15.2),
(16, 'IL', 'Illustration', 15, 15),
(17, 'LA', 'Lamination A4 Size', 14, 6),
(18, 'LC', 'Lamination Admit Card', 9, 6),
(19, 'LD', 'Lamination Driving License', 2, 1),
(20, 'LT', 'Lamination Transcript ', 31, 6),
(21, 'ML', 'Missed to keep record/loss with - sign', 5, 5),
(22, 'NN', 'NCell Sim New (Online)', 30, 0),
(23, 'NE', 'NCell Sim New 2 (Online - Expensive)', 63.5, 0),
(24, 'NO', 'NCell Sim Old', 87.5, 0),
(25, 'NP', 'Nepali Paper', 6, 0),
(26, 'NS', 'NTC SIM', 60, 0),
(27, 'OF', 'Online Form/EDV', 8, 3),
(28, 'OP', 'Online print ', 2.95, 1.75),
(29, 'PC', 'Paper (Certificate)', 5, 0),
(30, 'PH', 'Photo', 43.5, 29),
(31, 'PP', 'Plain Paper', 1.2, 0),
(32, 'PR', 'Print', 2.95, 1.75),
(33, 'RC', 'Recharge', 97.5, 0),
(34, 'RP', 'Result Print', 2.95, 1.75),
(35, 'SC', 'Scan', 3, 3),
(36, 'SE', 'Scan & Email', 3, 3),
(37, 'SF', 'Strip File', 20, 2),
(38, 'TP', 'Thesis Final Print in 80 GSM Paper', 3.15, 1.75),
(39, 'TF', 'Thesis Formatting', 300, 300),
(40, 'TL', 'Tips/loss', 0, 0),
(41, 'TY', 'Typing', 3, 3),
(42, 'XR', 'Xerox', 2.45, 1.25),
(43, 'XA', 'Xerox-A3', 6.62, 3.5),
(44, 'ZB', 'Z(Passive) BSW Proposal Writing Manual', 29.87, 12.75),
(45, 'ZC', 'Z(Passive) Chat GPT Prompt', 5, 5),
(46, 'ZM', 'Z(Passive) M.Ed. Thesis/Proposal Writing Manual (1', 71.36, 5);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cost_calculation`
--
ALTER TABLE `cost_calculation`
  ADD PRIMARY KEY (`item_number`),
  ADD UNIQUE KEY `service_code` (`service_code`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cost_calculation`
--
ALTER TABLE `cost_calculation`
  MODIFY `item_number` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
