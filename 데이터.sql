-- CREATE DATABASE oz_form;

USE oz_form;

-- 유저
INSERT INTO users (name, age, gender, email, created_at, updated_at)
VALUES 
('Alice', 'twenty', 'female', 'alice@example.com', NOW(), NOW()),
('Bob', 'thirty', 'male', 'bob@example.com', NOW(), NOW()),
('Charlie', 'teen', 'male', 'charlie@example.com', NOW(), NOW()),
('David', 'fourty', 'male', 'david@example.com', NOW(), NOW()),
('Eve', 'fifty', 'female', 'eve@example.com', NOW(), NOW()),
('Frank', 'twenty', 'male', 'frank@example.com', NOW(), NOW()),
('Grace', 'thirty', 'female', 'grace@example.com', NOW(), NOW()),
('Hank', 'fourty', 'male', 'hank@example.com', NOW(), NOW()),
('Ivy', 'teen', 'female', 'ivy@example.com', NOW(), NOW()),
('Jack', 'fifty', 'male', 'jack@example.com', NOW(), NOW());

-- 이미지
INSERT INTO images (url, type, created_at, updated_at)
VALUES 
('https://example.com/image1.jpg', 'main', NOW(), NOW()),
('https://example.com/image2.jpg', 'sub', NOW(), NOW()),
('https://example.com/image3.jpg', 'main', NOW(), NOW()),
('https://example.com/image4.jpg', 'sub', NOW(), NOW()),
('https://example.com/image5.jpg', 'main', NOW(), NOW()),
('https://example.com/image6.jpg', 'sub', NOW(), NOW()),
('https://example.com/image7.jpg', 'main', NOW(), NOW()),
('https://example.com/image8.jpg', 'sub', NOW(), NOW()),
('https://example.com/image9.jpg', 'main', NOW(), NOW()),
('https://example.com/image10.jpg', 'sub', NOW(), NOW());

-- 질문
INSERT INTO questions (title, is_active, sqe, image_id, created_at, updated_at)
VALUES 
('What is your favorite color?', TRUE, 1, 1, NOW(), NOW()),
('What is your favorite food?', TRUE, 2, 2, NOW(), NOW()),
('What is your dream job?', TRUE, 3, 3, NOW(), NOW()),
('What is your hobby?', TRUE, 4, 4, NOW(), NOW()),
('Where do you want to travel?', TRUE, 5, 5, NOW(), NOW()),
('What is your favorite animal?', TRUE, 6, 6, NOW(), NOW()),
('Do you like music?', TRUE, 7, 7, NOW(), NOW()),
('What is your favorite book?', TRUE, 8, 8, NOW(), NOW()),
('What is your daily routine?', TRUE, 9, 9, NOW(), NOW()),
('What is your biggest goal?', TRUE, 10, 10, NOW(), NOW());

-- 선택지
INSERT INTO choices (content, is_active, sqe, question_id, created_at, updated_at)
VALUES 
('Red', TRUE, 1, 1, NOW(), NOW()),
('Blue', TRUE, 2, 1, NOW(), NOW()),
('Pizza', TRUE, 1, 2, NOW(), NOW()),
('Pasta', TRUE, 2, 2, NOW(), NOW()),
('Doctor', TRUE, 1, 3, NOW(), NOW()),
('Engineer', TRUE, 2, 3, NOW(), NOW()),
('Reading', TRUE, 1, 4, NOW(), NOW()),
('Sports', TRUE, 2, 4, NOW(), NOW()),
('Japan', TRUE, 1, 5, NOW(), NOW()),
('France', TRUE, 2, 5, NOW(), NOW());

-- 대답
INSERT INTO answers (user_id, choice_id, created_at, updated_at)
VALUES 
(1, 1, NOW(), NOW()),
(2, 2, NOW(), NOW()),
(3, 3, NOW(), NOW()),
(4, 4, NOW(), NOW()),
(5, 5, NOW(), NOW()),
(6, 6, NOW(), NOW()),
(7, 7, NOW(), NOW()),
(8, 8, NOW(), NOW()),
(9, 9, NOW(), NOW()),
(10, 10, NOW(), NOW());
