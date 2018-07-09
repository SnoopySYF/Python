/*
���ݿ��ʼ��
*/
USE orders;

CREATE TABLE customer(
    custid CHAR(20) NOT NULL,
    custname CHAR(20),
    PRIMARY KEY(custid)
);

CREATE TABLE product(
    productid CHAR(20) NOT NULL,
    productname CHAR(20),
    unit CHAR(20),
    PRIMARY KEY(productid)
);

CREATE TABLE arrears(
    custid CHAR(20),
    amount FLOAT,
    lastdate CHAR(20),
    PRIMARY KEY(custid)
);

CREATE TABLE orders(
    custid CHAR(20) NOT NULL,
    productid CHAR(20) NOT NULL,
    num INT,
    form CHAR(10),
    PRIMARY KEY(custid, productid)
);

CREATE TABLE inventory(
    productid CHAR(20) NOT NULL,
    qty INT,
    PRIMARY KEY(productid)
);

INSERT INTO customer VALUES
('1001', '����������'),
('1002', '���߻�����'),
('2001', '����ˮ�೧'),
('2002', '����ˮ�೧'),
('2003', '����ʳƷ��'),
('3001', 'ɽ��������ĳ�'),
('3101', '��Ҷĥ�߳�'),
('3102', '���������ܾ�'),
('3201', '�����ع�'),
('4101', '�����Ṥҵ��˾');

INSERT INTO product VALUES
('01', '���', '��'),
('02', '��װˮ��', '��'),
('03', '���', '̨'),
('04', '�ְ�', '��'),
('05', '��', '��'),
('06', '�ϳ�', '��');

INSERT INTO arrears VALUES
('1002', 8700, '2014-1-18'),
('2002', 4560, '2013-12-10'),
('2003', 8000, '2013-12-26'),
('2001', 790, '2014-1-21'),
('4101', 6000, '2014-1-27'),
('3001', 3000, '2014-1-9'),
('3201', 8000, '2014-1-30');

INSERT INTO inventory VALUES
('03', 7),
('05', 70),
('04', 300),
('01', 45),
('02', 56);
