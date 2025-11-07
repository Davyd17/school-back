CREATE DATABASE IF NOT EXISTS school_db;

USE school_db;

--  ROLES & PERMISSIONS

CREATE TABLE roles (
    id          INT PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(100) UNIQUE NOT NULL,
    description VARCHAR(100) NOT NULL
);

CREATE TABLE permissions (
    id   INT PRIMARY KEY KEY AUTO_INCREMENT,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE roles_permissions (
    role_id       INT NOT NULL,
    permission_id INT NOT NULL,
    PRIMARY KEY (role_id, permission_id),
    CONSTRAINT fk_roles_permissions_role
        FOREIGN KEY (role_id) REFERENCES roles (id) ON DELETE CASCADE,
    CONSTRAINT fk_roles_permissions_permission
        FOREIGN KEY (permission_id) REFERENCES permissions (id) ON DELETE CASCADE
);

--  USERS & RELATED TABLES

CREATE TABLE users (
    id          BIGINT PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(100) NOT NULL,
    last_name   VARCHAR(100) NOT NULL,
    username    VARCHAR(100) UNIQUE NOT NULL,
    email       VARCHAR(200) UNIQUE NOT NULL,
    password    VARCHAR(255) NOT NULL,
    is_active   BOOLEAN NOT NULL DEFAULT TRUE,
    created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP,
    role_id     INT NOT NULL,
    CONSTRAINT fk_users_role
        FOREIGN KEY (role_id) REFERENCES roles (id)
);

CREATE TABLE phone_numbers (
    id         BIGINT PRIMARY KEY AUTO_INCREMENT,
    ext        INT,
    phone      VARCHAR(100) UNIQUE NOT NULL,
    is_active  BOOLEAN NOT NULL DEFAULT TRUE,
    user_id    BIGINT NOT NULL,
    CONSTRAINT fk_phone_numbers_user
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

CREATE TABLE admins (
    id       BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id  BIGINT NOT NULL,
    CONSTRAINT fk_admins_user
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

CREATE TABLE teachers (
    id       BIGINT PRIMARY KEY AUTO_INCREMENT,
    salary   DECIMAL(10,2) NOT NULL,
    user_id  BIGINT NOT NULL,
    CONSTRAINT fk_teachers_user
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

CREATE TABLE students (
    id        BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id   BIGINT NOT NULL,
    group_id  INT NOT NULL, -- referenced later after groups table is created
    CONSTRAINT fk_students_user
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);


--  ACADEMIC STRUCTURE

CREATE TABLE grades (
    id     INT PRIMARY KEY AUTO_INCREMENT,
    level  VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE `groups` (
    id          INT PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(10) UNIQUE NOT NULL
);

CREATE TABLE groups_grades (
    group_id    INT NOT NULL,
    grade_id    INT NOT NULL,
    teacher_id  BIGINT,
    PRIMARY KEY (group_id, grade_id),
    CONSTRAINT fk_groups_grades_group
        FOREIGN KEY (group_id) REFERENCES `groups` (id) ON DELETE CASCADE,
    CONSTRAINT fk_groups_grades_grade
        FOREIGN KEY (grade_id) REFERENCES grades (id) ON DELETE CASCADE,
    CONSTRAINT fk_groups_grades_teacher
        FOREIGN KEY (teacher_id) REFERENCES teachers (id) ON DELETE SET NULL
);

ALTER TABLE students
    ADD CONSTRAINT fk_students_group
    FOREIGN KEY (group_id) REFERENCES `groups` (id);

CREATE TABLE subjects (
    id           INT PRIMARY KEY AUTO_INCREMENT,
    name         VARCHAR(100) UNIQUE NOT NULL,
    description  TEXT NOT NULL,
    created_at   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at   TIMESTAMP,
    teacher_id   BIGINT,
    CONSTRAINT fk_subjects_teacher
        FOREIGN KEY (teacher_id) REFERENCES teachers (id) ON DELETE SET NULL
);

CREATE TABLE subjects_grades (
    subject_id INT NOT NULL,
    grade_id   INT NOT NULL,
    PRIMARY KEY (subject_id, grade_id),
    CONSTRAINT fk_subjects_grades_subject
        FOREIGN KEY (subject_id) REFERENCES subjects (id),
    CONSTRAINT fk_subjects_grades_grade
        FOREIGN KEY (grade_id) REFERENCES grades (id)
);

CREATE TABLE student_subject (
    student_id  BIGINT NOT NULL ,
    subject_id  INT NOT NULL,
    average     DECIMAL(5,2) NOT NULL DEFAULT 0,
    PRIMARY KEY (student_id, subject_id),
    CONSTRAINT fk_student_subject_student
        FOREIGN KEY (student_id) REFERENCES students (id),
    CONSTRAINT fk_student_subject_subject
        FOREIGN KEY (subject_id) REFERENCES subjects (id)
);


