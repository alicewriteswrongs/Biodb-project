#Biological Databases final project

contains the files for our biological databases final project

Currently:

* fastaintodb.py - inserts our data into the appropriate tables
* maketables.sql - SQL commands to make the tables we want in our database
* populatedatasets.py - inserts the records for the 'dataset' table
* droptables.sql - drops the tables in the right order (foreign key constraints)
* proposal
    * proposal.tex
    * proposal.pdf
    * ERdiagram.pdf
    * ERdiagram-crop.pdf
    * ERdiagram.dia

##Using fastaintodb.py:

The script is broken up into several sections. This script should be run (on bioed) after:

* Running maketables.sql and verifying table structure
* Running populatedatasets.py

And that should be it! Note that fastaintodb.py Just gets in the sequence data - it doesn't
insert any of our alignment data. It's not ready to start testing just yet, still needs some
ironing out.

####Definitions:

This holds definitions for all of the functions we need

####MAIN

This has commands and function calls written out to insert the various kinds of data.

Make sure to comment out ones you don't need! 

##Todo:

* get data into tables
* get tables and data onto bioed

