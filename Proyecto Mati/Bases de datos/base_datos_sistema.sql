-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-08-2024 a las 22:08:55
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `base_datos_sistema`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiantes`
--

CREATE TABLE `estudiantes` (
  `curso` varchar(100) NOT NULL,
  `nombres` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `fecha_ingreso` varchar(10) DEFAULT NULL,
  `dni` int(11) NOT NULL,
  `observaciones` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estudiantes`
--

INSERT INTO `estudiantes` (`curso`, `nombres`, `apellidos`, `fecha_ingreso`, `dni`, `observaciones`) VALUES
('3c', 'Matiass Leonel', 'Gauto Gomez', '11-01-2008', 98777453, 'es un estudiante que estudia si es necesario pero deve de trabajar la conducta'),
('3d', 'Kevin Qui', 'Quiroz Ke', '01-03-2019', 98043357, 'buen estudiante lol\n'),
('4-4', 'thiago', 'hernandez', '06-07-1998', 12345600, 'pruebaza\n'),
('4-5', 'matias', 'gauto', '04-12-2022', 77777777, 'sdfsdf\n'),
('3d', 'Dfgdfgfd', 'Fdgdfg', '11-01-2012', 88888888, 'ñañaña\n');

--
-- Disparadores `estudiantes`
--
DELIMITER $$
CREATE TRIGGER `before_insert_estudiantes` BEFORE INSERT ON `estudiantes` FOR EACH ROW BEGIN
    SET NEW.fecha_ingreso = DATE_FORMAT(STR_TO_DATE(NEW.fecha_ingreso, '%d%m%Y'), '%d-%m-%Y');
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `formato_fecha_before_update` BEFORE UPDATE ON `estudiantes` FOR EACH ROW BEGIN
    SET NEW.fecha_ingreso = CONCAT(
        SUBSTRING(NEW.fecha_ingreso, 1, 2), '-', 
        SUBSTRING(NEW.fecha_ingreso, 3, 2), '-', 
        SUBSTRING(NEW.fecha_ingreso, 5, 4)
    );
END
$$
DELIMITER ;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
