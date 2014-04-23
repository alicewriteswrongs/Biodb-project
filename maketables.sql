-- this file creates the tables we want in our database

-- I think we want to use VARCHAR for these short ones
CREATE TABLE csb (
    csbid VARCHAR(45) NOT NULL,
    sequence VARCHAR(500) NOT NULL,
    PRIMARY KEY (csbid)
)
ENGINE = INNODB;


CREATE TABLE smallrna (
    smid VARCHAR(45) NOT NULL,
    sequence TEXT(100) NOT NULL,
    copynum INT,
    PRIMARY KEY (smid)
)
ENGINE = INNODB;



CREATE TABLE dataset (
    did VARCHAR(25) NOT NULL,
    description VARCHAR(100),
    PRIMARY KEY (did)
)
ENGINE = INNODB;

CREATE TABLE minicircles (
    mid INTEGER NOT NULL AUTO_INCREMENT,
    did VARCHAR(25) NOT NULL,
    sequence TEXT(2000) NOT NULL,
    description VARCHAR(100),
    clusternum INT,
    PRIMARY KEY (mid),
    FOREIGN KEY (did) REFERENCES dataset (did)
)
ENGINE = INNODB;

CREATE TABLE csb_maps (
    csbid VARCHAR(25) NOT NULL,
    mid INTEGER NOT NULL,
    startpos INT NOT NULL,
    endpos INT NOT NULL,
    strandinfo VARCHAR(25) NOT NULL,
    quality VARCHAR(25) NOT NULL,
    PRIMARY KEY (csbid,mid,startpos),
    FOREIGN KEY (csbid) REFERENCES csb(csbid),
    FOREIGN KEY (mid) REFERENCES minicircles(mid)
)
ENGINE = INNODB;

CREATE TABLE smrna_maps (
    smid VARCHAR(25) NOT NULL,
    mid INTEGER NOT NULL,
    startpos INT NOT NULL,
    endpos INT NOT NULL,
    strandinfo VARCHAR(25) NOT NULL,
    quality VARCHAR(25) NOT NULL,
    PRIMARY KEY (smid, mid),
    FOREIGN KEY (smid) REFERENCES smallrna(smid),
    FOREIGN KEY (mid) REFERENCES minicircles(mid)
)
ENGINE = INNODB;















