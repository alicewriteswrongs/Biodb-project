-- this file creates the tables we want in our database

-- I think we want to use VARCHAR for these short ones
CREATE TABLE csb (
    csbid VARCHAR(25) NOT NULL,
    sequence VARCHAR(500) NOT NULL,
    PRIMARY KEY (csbid)
)
ENGINE = INNODB;

CREATE TABLE smallrna (
    smid VARCHAR(25) NOT NULL,
    sequence TEXT(100) NOT NULL,
    PRIMARY KEY (smid)
)
ENGINE = INNODB;

CREATE TABLE dataset (
    did VARCHAR(25) NOT NULL,
    PRIMARY KEY (did)
)
ENGINE = INNODB;

CREATE TABLE minicircles (
    mid VARCHAR(25) NOT NULL,
    datasetid VARCHAR(25) NOT NULL,
    sequence TEXT(2000) NOT NULL,
    clusternum INT,
    PRIMARY KEY (mid),
    FOREIGN KEY datasetid REFERENCES dataset(did)
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
    FOREIGN KEY (csbid) REFERENCES csb(csbid),
    FOREIGN KEY (minicircid) REFERENCES minicircles(mid)
)
ENGINE = INNODB;

CREATE TABLE smrna_maps (
    smallrnaid VARCHAR(25) NOT NULL,
    minicircid VARCHAR(25) NOT NULL,
    startpos INT NOT NULL,
    endpos INT NOT NULL,
    strandinfo VARCHAR(25) NOT NULL,
    quality VARCHAR(25) NOT NULL,
    PRIMARY KEY (smallrnaid,minicircid),
    FOREIGN KEY (smallrnaid REFERENCES smallrna(smid),
    FOREIGN KEY (minicircid) REFERENCES minicircles(mid)
)
ENGINE = INNODB;















