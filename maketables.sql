-- this file creates the tables we want in our database

-- I think we want to use VARCHAR for these short ones
CREATE TABLE csb (
    id VARCHAR(25) NOT NULL,
    sequence VARCHAR(500) NOT NULL,
    PRIMARY KEY (id)
)
ENGINE = INNODB;

CREATE TABLE smallrna (
    id VARCHAR(25) NOT NULL,
    sequence TEXT(2000) NOT NULL,
    PRIMARY KEY (id)
)
ENGINE = INNODB;

CREATE TABLE dataset (
    id VARCHAR(25) NOT NULL,
    -- some info here
    PRIMARY KEY (id)
)
ENGINE = INNODB;

CREATE TABLE minicircles (
    id VARCHAR(25) NOT NULL,
    datasetid VARCHAR(25) NOT NULL,
    sequence TEXT(2000) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY datasetid REFERENCES dataset(id)
)
ENGINE = INNODB;

CREATE TABLE csb_maps (
    csbid VARCHAR(25) NOT NULL,
    minicircid VARCHAR(25) NOT NULL,
    startpos INT NOT NULL,
    endpos INT NOT NULL,
    strandinfo VARCHAR(25) NOT NULL,
    quality VARCHAR(25) NOT NULL,
    PRIMARY KEY (csbid,minicircid,startpos),
    FOREIGN KEY (csbid) REFERENCES csb(id),
    FOREIGN KEY (minicircid) REFERENCES minicircles(id)
)
ENGINE = INNODB;

CREATE TABLE smrna_maps (
    smallrnaid VARCHAR(25) NOT NULL,
    minicircid VARCHAR(25) NOT NULL,
    startpos INT NOT NULL,
    endpos INT NOT NULL,
    strandinfo VARCHAR(25) NOT NULL,
    quality VARCHAR(25) NOT NULL,
    PRIMARY KEY (smallrnaid,minicircid,startpos),
    FOREIGN KEY (smallrnaid REFERENCES smallrna(id),
    FOREIGN KEY (minicircid) REFERENCES minicircles(id)
)
ENGINE = INNODB;















