/*
数据库初始化
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
('1001', '北方车辆厂'),
('1002', '三七机车厂'),
('2001', '天马水泥厂'),
('2002', '江北水泥厂'),
('2003', '江南食品厂'),
('3001', '山陵飞行器材厂'),
('3101', '大叶磨具厂'),
('3102', '江北制造总局'),
('3201', '凤鸣重工'),
('4101', '三阳轻工业公司');

INSERT INTO product VALUES
('01', '轴承', '个'),
('02', '袋装水泥', '吨'),
('03', '电机', '台'),
('04', '钢板', '块'),
('05', '橡胶', '吨'),
('06', '拖车', '辆');

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
