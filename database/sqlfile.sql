
CREATE TABLE MAITE (
    email VARCHAR PRIMARY KEY,
    password VARCHAR(256) NOT NULL,
    fname VARCHAR NOT NULL,
    lname VARCHAR NOT NULL,
    balance DECIMAL(10,2) DEFAULT 0
);

CREATE TABLE ENTRY (
    cr FLOAT DECIMAL(10,2) DEFAULT 0,
    dr FLOAT DECIMAL(10,2) DEFAULT 0,
    description VARCHAR,
    maite_id INT,
    FOREIGN KEY(maite_id) REFERENCES F_MAITE(id)
);

CREATE TABLE EXPENSE (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR,
    type TEXT CHECK (type IN ('Grocery', 'Asset', 'Fun', 'Rent', 'Electricity', 'Water', 'MISC')),
    amount DECIMAL(10,2),
    maite_id INT,
    date DATE NOT NULL,
    FOREIGN KEY (maite_id) REFERENCES F_MAITE(id)
);

INSERT INTO MAITE (email,password,fname,lname,balance) VALUES
('flat','pass','Flat','1',0.0),
('sammy','pass','Sameer','Timsina',0.0),
('thedevil','pass','Janak','Bhandari',0.0);
