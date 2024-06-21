CREATE TABLE my_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    value INT NOT NULL
);

INSERT INTO my_table (name, value) VALUES
('example1', 100),
('example2', 200);
