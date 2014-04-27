#!/usr/bin/python

##cgi-script to show Jalview with a user-selected alignment file

import cgi, cgitb


cgitb.enable()

print """Content-type: text/html\n\n
<html>
<title>Jalview test page</title>
"""

#print a little bit of stuff
print """
<body>
<p align="center">
<h1>test page</h1>
</p>
"""


#print form
print """
<form name="jalview_form" method="post" action="jalview.py">
Pick an alignment file:
    <select name="alignment">
    <option value="/var/www/html/msad/genbankexample.fasta">test</option>
    </select>
    <br>
    <input type="submit" name="jalview!" value="submit" />
    </form>
"""

form = cgi.FieldStorage()

if form:
    alignment = form["alignment"].value
    print """
    <applet code="jalview.bin.JalviewLite" width="800" height="400" archive="jalviewApplet.jar">
            <param name="permissions" value="sandbox"/>
            <param name="file" value="%s"/>
            <param name="embedded" value="true"/>
            <param name="APPLICATION_URL" value="http://www.jalview.org/services/launchApp"/>
            <param name="format" value="fasta"/>
            <param name="showFeatureSettings" value="false"/>
            <param name="type" value="file"/>
            <param name="nojmol" value="true"/>
    </applet> """ % (alignment)

#print a tail

print """
</body>

</html>
"""
