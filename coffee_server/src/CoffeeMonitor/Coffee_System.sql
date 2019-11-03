/*
Navicat MySQL Data Transfer

Source Server         : vm_mysql
Source Server Version : 50726
Source Host           : 127.0.0.1:3306
Source Database       : Coffee_System

Target Server Type    : MYSQL
Target Server Version : 50726
File Encoding         : 65001

Date: 2019-05-14 11:30:20
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add 设备类型信息', '7', 'add_eqtype');
INSERT INTO `auth_permission` VALUES ('20', 'Can change 设备类型信息', '7', 'change_eqtype');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete 设备类型信息', '7', 'delete_eqtype');
INSERT INTO `auth_permission` VALUES ('22', 'Can add 设备类型信息', '8', 'add_eqtype');
INSERT INTO `auth_permission` VALUES ('23', 'Can change 设备类型信息', '8', 'change_eqtype');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete 设备类型信息', '8', 'delete_eqtype');
INSERT INTO `auth_permission` VALUES ('25', 'Can add 设备信息', '9', 'add_eqinfo');
INSERT INTO `auth_permission` VALUES ('26', 'Can change 设备信息', '9', 'change_eqinfo');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete 设备信息', '9', 'delete_eqinfo');
INSERT INTO `auth_permission` VALUES ('28', 'Can add 设备状态', '10', 'add_eqstate');
INSERT INTO `auth_permission` VALUES ('29', 'Can change 设备状态', '10', 'change_eqstate');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete 设备状态', '10', 'delete_eqstate');
INSERT INTO `auth_permission` VALUES ('31', 'Can add 设备报警', '11', 'add_eqwarning');
INSERT INTO `auth_permission` VALUES ('32', 'Can change 设备报警', '11', 'change_eqwarning');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete 设备报警', '11', 'delete_eqwarning');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$100000$OGULeqIqTPc4$Ggti9o8yu43z5R7NXoZQhgnOmPaTEAfwgTJ+3rQ0D1o=', '2019-05-14 01:58:01.807701', '1', 'admin', '', '', '24830872@qq.com', '1', '1', '2019-04-21 13:20:08.285434');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2019-04-21 13:57:28.647735', '4', '宏达广场1一楼', '1', '[{\"added\": {}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2019-04-21 13:57:58.232237', '4', '宏达广场1一楼', '2', '[{\"changed\": {\"fields\": [\"status\"]}}]', '9', '1');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('7', 'index', 'eqtype');
INSERT INTO `django_content_type` VALUES ('9', 'manage', 'eqinfo');
INSERT INTO `django_content_type` VALUES ('10', 'manage', 'eqstate');
INSERT INTO `django_content_type` VALUES ('8', 'manage', 'eqtype');
INSERT INTO `django_content_type` VALUES ('11', 'manage', 'eqwarning');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2019-04-21 13:17:08.707203');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2019-04-21 13:17:09.540192');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2019-04-21 13:17:09.647101');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2019-04-21 13:17:09.661139');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2019-04-21 13:17:09.729706');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2019-04-21 13:17:09.765806');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2019-04-21 13:17:09.828879');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2019-04-21 13:17:09.839910');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2019-04-21 13:17:09.868987');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2019-04-21 13:17:09.872998');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2019-04-21 13:17:09.884029');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0008_alter_user_username_max_length', '2019-04-21 13:17:09.966850');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0009_alter_user_last_name_max_length', '2019-04-21 13:17:10.009967');
INSERT INTO `django_migrations` VALUES ('14', 'index', '0001_initial', '2019-04-21 13:17:10.028808');
INSERT INTO `django_migrations` VALUES ('15', 'index', '0002_auto_20190419_1044', '2019-04-21 13:17:10.155193');
INSERT INTO `django_migrations` VALUES ('16', 'index', '0003_typedetail', '2019-04-21 13:17:10.210347');
INSERT INTO `django_migrations` VALUES ('17', 'index', '0004_auto_20190421_2113', '2019-04-21 13:17:10.376030');
INSERT INTO `django_migrations` VALUES ('18', 'index', '0005_auto_20190421_2114', '2019-04-21 13:17:10.385055');
INSERT INTO `django_migrations` VALUES ('19', 'sessions', '0001_initial', '2019-04-21 13:17:10.430128');
INSERT INTO `django_migrations` VALUES ('20', 'manage', '0001_initial', '2019-04-21 13:47:03.832475');
INSERT INTO `django_migrations` VALUES ('21', 'manage', '0002_auto_20190419_1044', '2019-04-21 13:47:04.095531');
INSERT INTO `django_migrations` VALUES ('22', 'manage', '0003_typedetail', '2019-04-21 13:47:04.175479');
INSERT INTO `django_migrations` VALUES ('23', 'manage', '0004_auto_20190421_2113', '2019-04-21 13:47:04.306406');
INSERT INTO `django_migrations` VALUES ('24', 'manage', '0005_auto_20190421_2114', '2019-04-21 13:47:04.314424');
INSERT INTO `django_migrations` VALUES ('25', 'manage', '0006_eqinfo', '2019-04-21 13:54:34.623485');
INSERT INTO `django_migrations` VALUES ('26', 'manage', '0007_eqstate', '2019-04-21 14:04:09.872177');
INSERT INTO `django_migrations` VALUES ('27', 'manage', '0008_eqwarning', '2019-04-21 14:09:05.589113');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('4abgg4hzburcl7hvzt8pooadioypqa7e', 'MDFkMjQ2ZmUwYzM5MThjNGQwMWM5ZDYwMTI0MzRiOThhZWY0ZGQ4MDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyZjRiYWYzMzhkMWJmNDY3NGNiMzdjYjhmOTFkOWQzMTAzY2EzYmEzIn0=', '2019-05-25 08:39:04.623398');
INSERT INTO `django_session` VALUES ('9axdn9pth5gc4ev4llgmi8xddrttgv55', 'MDFkMjQ2ZmUwYzM5MThjNGQwMWM5ZDYwMTI0MzRiOThhZWY0ZGQ4MDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyZjRiYWYzMzhkMWJmNDY3NGNiMzdjYjhmOTFkOWQzMTAzY2EzYmEzIn0=', '2019-05-22 03:16:06.894405');
INSERT INTO `django_session` VALUES ('aix0u2ukf8fchkfsqdez5spjas8wmu6x', 'MDFkMjQ2ZmUwYzM5MThjNGQwMWM5ZDYwMTI0MzRiOThhZWY0ZGQ4MDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyZjRiYWYzMzhkMWJmNDY3NGNiMzdjYjhmOTFkOWQzMTAzY2EzYmEzIn0=', '2019-05-05 13:22:34.276707');
INSERT INTO `django_session` VALUES ('x1xh7ppad0y0k0m3nao4ug48fltyzgtr', 'MDFkMjQ2ZmUwYzM5MThjNGQwMWM5ZDYwMTI0MzRiOThhZWY0ZGQ4MDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyZjRiYWYzMzhkMWJmNDY3NGNiMzdjYjhmOTFkOWQzMTAzY2EzYmEzIn0=', '2019-05-28 01:58:01.846796');

-- ----------------------------
-- Table structure for manage_eqinfo
-- ----------------------------
DROP TABLE IF EXISTS `manage_eqinfo`;
CREATE TABLE `manage_eqinfo` (
  `machine_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) NOT NULL,
  `name` varchar(64) NOT NULL,
  `mac_addr` varchar(64) NOT NULL,
  `addr` varchar(128) NOT NULL,
  `position` varchar(64) NOT NULL,
  `install_date` date NOT NULL,
  `install_emp_id` varchar(16) NOT NULL,
  `status` int(11) NOT NULL,
  `mantain_emp_id` varchar(16) NOT NULL,
  PRIMARY KEY (`machine_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of manage_eqinfo
-- ----------------------------
INSERT INTO `manage_eqinfo` VALUES ('1', '1', '华星现代产业园', 'BC-EE-7B-5B-6B-0F', '华星现代产业园', '120.128292,30.281176', '2019-04-10', '梁胜云', '3', '林九峰');
INSERT INTO `manage_eqinfo` VALUES ('2', '1', '黄龙万科中心', 'BC-EE-7B-5B-6B-2F', '黄龙万科中心', '120.132586,30.281694', '2019-04-10', '郭洪山', '3', '林九峰');
INSERT INTO `manage_eqinfo` VALUES ('3', '1', '华星时代广场', 'BC-EE-7B-5B-6B-3F', '华星时代广场', '120.131445,30.283489', '2019-04-10', '张达', '3', '林九峰');
INSERT INTO `manage_eqinfo` VALUES ('4', '1', '莱茵达大厦', 'BC-EE-7B-5B-6B-3F', '莱茵达大厦10楼', '120.130361,30.282419', '2019-04-22', '李一鸣', '3', '李一鸣');
INSERT INTO `manage_eqinfo` VALUES ('5', '1', '东方通信大厦', 'BC-EE-7B-5B-6B-3F', '东方通信大厦1楼', '120.133641,30.283697', '2019-04-22', '李一鸣', '3', '李一鸣');
INSERT INTO `manage_eqinfo` VALUES ('6', '1', '颐高数码大厦', 'BC-EE-7B-5B-6B-3F', '颐高数码大厦', '120.138342,30.282617', '2019-04-22', '李一鸣', '3', '李一鸣');
INSERT INTO `manage_eqinfo` VALUES ('7', '1', '昌地火炬大厦', 'BC-EE-7B-5B-6B-3F', '昌地火炬大厦', '120.140594,30.282918', '2019-04-22', '李一鸣', '3', '李一鸣');
INSERT INTO `manage_eqinfo` VALUES ('8', '1', '浙江科技产业大厦', 'BC-EE-7B-5B-6B-3F', '浙江科技产业大厦', '120.128172,30.28662', '2019-04-22', '李一鸣', '3', '李一鸣');
INSERT INTO `manage_eqinfo` VALUES ('9', '1', '天苑大厦', 'BC-EE-7B-5B-6B-3F', '天苑大厦', '120.12675,30.28313', '2019-04-22', '李一鸣', '3', '李一鸣');
INSERT INTO `manage_eqinfo` VALUES ('10', '1', '西湖国际科技大厦', 'BC-EE-7B-5B-6B-3F', '西湖国际科技大厦', '120.127214,30.287783', '2019-04-22', '李一鸣', '3', '李一鸣');
INSERT INTO `manage_eqinfo` VALUES ('11', '1', '杭州广播电视大学', 'BC-EE-7B-5B-6B-3F', '杭州广播电视大学', '120.123736,30.29235', '2019-04-22', '李一鸣', '3', '李一鸣');
INSERT INTO `manage_eqinfo` VALUES ('12', '1', '支付宝大楼', 'BC-EE-7B-5B-6B-3F', '支付宝大楼', '120.13183,30.279206', '2019-04-22', '李一鸣', '3', '李一鸣');
INSERT INTO `manage_eqinfo` VALUES ('13', '1', '浙大玉泉校区图书馆', 'BC-EE-7B-5B-6B-3F', '浙大玉泉校区图书馆', '120.126728,30.269332', '2019-04-22', '李一鸣', '3', '李一鸣');
INSERT INTO `manage_eqinfo` VALUES ('14', '1', '浙江图书馆', 'BC-EE-7B-5B-6B-3F', '浙江图书馆', '120.143514,30.269521', '2019-04-22', '李一鸣', '3', '李一鸣');
INSERT INTO `manage_eqinfo` VALUES ('15', '1', '浙江电视台', 'BC-EE-7B-5B-6B-3F', '浙江电视台', '120.160271,30.280976', '2019-04-22', '李一鸣', '3', '李一鸣');

-- ----------------------------
-- Table structure for manage_eqstate
-- ----------------------------
DROP TABLE IF EXISTS `manage_eqstate`;
CREATE TABLE `manage_eqstate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `machine_id` int(11) NOT NULL,
  `recv_time` datetime(6) NOT NULL,
  `enviroment_temperature` varchar(16) NOT NULL,
  `boiler_temperature` varchar(16) NOT NULL,
  `boiler_pressue` varchar(16) NOT NULL,
  `material_remainder` varchar(16) NOT NULL,
  `orders_num` int(11) NOT NULL,
  `orders_amt` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24586 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for manage_eqtype
-- ----------------------------
DROP TABLE IF EXISTS `manage_eqtype`;
CREATE TABLE `manage_eqtype` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `size` varchar(64) NOT NULL,
  `weight` decimal(10,2) NOT NULL,
  `power` varchar(32) NOT NULL,
  `dissipation` int(11) NOT NULL,
  `material_buckets` int(11) NOT NULL,
  `water_proofing_grade` varchar(16) NOT NULL,
  `pipe_standard` varchar(16) NOT NULL,
  `inflow_pressue` varchar(16) NOT NULL,
  `work_temperature` varchar(16) NOT NULL,
  `screen_size` decimal(10,2) NOT NULL,
  `comm_interface` varchar(32) NOT NULL,
  `os` varchar(32) NOT NULL,
  `payment_cate` varchar(32) NOT NULL,
  `data_standard` varchar(32) NOT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of manage_eqtype
-- ----------------------------
INSERT INTO `manage_eqtype` VALUES ('1', 'ES4C', '700(H)*420(W)*450(D)mm', '60.00', 'AC220V/50HZ', '2700', '3', 'IPX1', 'G3/8', '0.5-7bar', '75', '14.00', 'USB,WIFI,4G', 'LINUX系统、Android系统', '微信、支付宝', 'EVA-DTS');

-- ----------------------------
-- Table structure for manage_eqwarning
-- ----------------------------
DROP TABLE IF EXISTS `manage_eqwarning`;
CREATE TABLE `manage_eqwarning` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `MACHINE_ID` int(11) DEFAULT NULL,
  `alter_msg` varchar(128) DEFAULT NULL,
  `check_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=114 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of manage_eqwarning
-- ----------------------------
