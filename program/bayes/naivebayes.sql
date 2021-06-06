-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 27, 2020 at 05:33 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `naivebayes`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add datas', 7, 'add_datas'),
(26, 'Can change datas', 7, 'change_datas'),
(27, 'Can delete datas', 7, 'delete_datas'),
(28, 'Can view datas', 7, 'view_datas');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$216000$KtUt4OtdEC7g$Ca8e54RChEOu3QN/IuePaNy4YXbEzwr2GbkT9V7LF1Q=', '2020-10-27 16:13:34.259696', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2020-10-21 07:31:31.007990');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2020-10-24 03:16:30.186455', '1', 'perempuan', 1, '[{\"added\": {}}]', 7, 1),
(2, '2020-10-24 03:16:59.659220', '2', 'laki - laki', 1, '[{\"added\": {}}]', 7, 1),
(3, '2020-10-24 03:17:23.352820', '2', 'laki - laki', 3, '', 7, 1),
(4, '2020-10-24 03:17:23.441655', '1', 'perempuan', 3, '', 7, 1),
(5, '2020-10-24 05:03:27.278009', '1', 'l', 1, 'new through import_export', 7, 1),
(6, '2020-10-24 05:03:27.359959', '2', 'p', 1, 'new through import_export', 7, 1),
(7, '2020-10-24 05:03:27.419923', '3', 'l', 1, 'new through import_export', 7, 1),
(8, '2020-10-24 05:03:27.475890', '4', 'l', 1, 'new through import_export', 7, 1),
(9, '2020-10-24 05:03:27.530855', '5', 'p', 1, 'new through import_export', 7, 1),
(10, '2020-10-24 05:03:27.575823', '6', 'p', 1, 'new through import_export', 7, 1),
(11, '2020-10-24 05:03:27.677548', '7', 'p', 1, 'new through import_export', 7, 1),
(12, '2020-10-24 05:03:27.731527', '8', 'l', 1, 'new through import_export', 7, 1),
(13, '2020-10-24 05:03:27.776647', '9', 'l', 1, 'new through import_export', 7, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'myapp', 'datas'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-10-21 07:26:13.570706'),
(2, 'auth', '0001_initial', '2020-10-21 07:26:19.266402'),
(3, 'admin', '0001_initial', '2020-10-21 07:26:31.601893'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-10-21 07:26:35.281657'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-10-21 07:26:35.435354'),
(6, 'contenttypes', '0002_remove_content_type_name', '2020-10-21 07:26:38.181317'),
(7, 'auth', '0002_alter_permission_name_max_length', '2020-10-21 07:26:40.603318'),
(8, 'auth', '0003_alter_user_email_max_length', '2020-10-21 07:26:41.004928'),
(9, 'auth', '0004_alter_user_username_opts', '2020-10-21 07:26:41.097127'),
(10, 'auth', '0005_alter_user_last_login_null', '2020-10-21 07:26:43.165861'),
(11, 'auth', '0006_require_contenttypes_0002', '2020-10-21 07:26:43.214709'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2020-10-21 07:26:43.283658'),
(13, 'auth', '0008_alter_user_username_max_length', '2020-10-21 07:26:43.465753'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2020-10-21 07:26:43.709826'),
(15, 'auth', '0010_alter_group_name_max_length', '2020-10-21 07:26:43.865942'),
(16, 'auth', '0011_update_proxy_permissions', '2020-10-21 07:26:43.954083'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2020-10-21 07:26:44.541469'),
(18, 'myapp', '0001_initial', '2020-10-21 07:26:45.157947'),
(19, 'sessions', '0001_initial', '2020-10-21 07:26:46.521865'),
(20, 'myapp', '0002_datas_prediksi', '2020-10-26 20:53:42.067967');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('5m1jztzjvlslwxj89b3wsq15ssm7gqhp', '.eJxVjDsOwyAQBe9CHSHAfFOm9xnQwi7BSYQlY1dR7h5bcpG0b2bem0XY1hq3TkuckF2ZZJffLUF-UjsAPqDdZ57nti5T4ofCT9r5OCO9bqf7d1Ch171WzpDXqIotBUWwEkFooFy0khiSdQMUL7xJg9kBaZec1yWnIAwoqTT7fAHsyDfP:1kXRbK:1zf-HyKFM85ylloXg8-iiZIe6g-5RT6a5XMcPJ_-dDQ', '2020-11-10 16:13:34.320112'),
('cqfzg7y8t6otx9xb9xsdhcc3ptn5ls9k', '.eJxVjDsOwyAQBe9CHSHAfFOm9xnQwi7BSYQlY1dR7h5bcpG0b2bem0XY1hq3TkuckF2ZZJffLUF-UjsAPqDdZ57nti5T4ofCT9r5OCO9bqf7d1Ch171WzpDXqIotBUWwEkFooFy0khiSdQMUL7xJg9kBaZec1yWnIAwoqTT7fAHsyDfP:1kV8bJ:d6HNrOYwEfn-JVaFd50xRHnNQbJkISZpXKYCHwtFMvs', '2020-11-04 07:32:01.366736'),
('rl4xybl1pmzmnvdl6eqmnhijrd22a0nr', '.eJxVjDsOwyAQBe9CHSHAfFOm9xnQwi7BSYQlY1dR7h5bcpG0b2bem0XY1hq3TkuckF2ZZJffLUF-UjsAPqDdZ57nti5T4ofCT9r5OCO9bqf7d1Ch171WzpDXqIotBUWwEkFooFy0khiSdQMUL7xJg9kBaZec1yWnIAwoqTT7fAHsyDfP:1kWBgv:0loEDevW5NbFBl7FJ_PzlBqcy8d34VSR5NGK0rp5LHU', '2020-11-07 05:02:09.953267'),
('rp2o7kmj7af190rqk5u8xa42w39fp1qi', '.eJxVjDsOwyAQBe9CHSHAfFOm9xnQwi7BSYQlY1dR7h5bcpG0b2bem0XY1hq3TkuckF2ZZJffLUF-UjsAPqDdZ57nti5T4ofCT9r5OCO9bqf7d1Ch171WzpDXqIotBUWwEkFooFy0khiSdQMUL7xJg9kBaZec1yWnIAwoqTT7fAHsyDfP:1kW9uD:zFYnwkKnx9cz-o7gBXJzjK2OHsN29P7Iv0P3GQ-YsxY', '2020-11-07 03:07:45.769088');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_datas`
--

CREATE TABLE `myapp_datas` (
  `id` int(11) NOT NULL,
  `jk` varchar(50) NOT NULL,
  `p_mengulang` varchar(30) NOT NULL,
  `ipk` double NOT NULL,
  `p_cuti` varchar(30) NOT NULL,
  `sam_bekerja` varchar(30) NOT NULL,
  `a_papua` varchar(30) NOT NULL,
  `ipk_sm1` double NOT NULL,
  `prediksi` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_datas`
--

INSERT INTO `myapp_datas` (`id`, `jk`, `p_mengulang`, `ipk`, `p_cuti`, `sam_bekerja`, `a_papua`, `ipk_sm1`, `prediksi`) VALUES
(1, 'l', 'y', 2.4, 'y', 'y', 'y', 2, 't'),
(2, 'p', 'y', 3, 't', 'y', 'y', 2.5, 'tw'),
(3, 'l', 't', 3.2, 'y', 'y', 'y', 3.3, 'tw'),
(4, 'l', 't', 2, 'y', 'y', 'y', 3, 'tw'),
(5, 'p', 't', 2.4, 't', 't', 'y', 3, 'tw'),
(6, 'p', 'y', 2.5, 't', 't', 't', 2.8, 't'),
(7, 'p', 't', 3, 'y', 't', 't', 2.7, 'tw'),
(8, 'l', 't', 2.9, 't', 'y', 't', 3, 't'),
(9, 'l', 'y', 2.7, 't', 'y', 'y', 3, 'tw');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `myapp_datas`
--
ALTER TABLE `myapp_datas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `myapp_datas`
--
ALTER TABLE `myapp_datas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
