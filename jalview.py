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
    <option value="mini_reset_cluster98_size_107_cid_2298.fasta">test</option>
    </select>
    <br>
    <input type="submit" name="jalview!" value="submit" />
    </form>
"""

form = cgi.FieldStorage()

if form:
    alignment = form["alignment"].value
    print """
    <script type="text/javascript" src="http://www.jalview.org/examples/javascript/jalview.js">
    </script>


    <applet code="jalview.bin.JalviewLite" width="800" height="400" archive="jalviewApplet.jar, justone.zip">
            <param name="permissions" value="sandbox"/>
            <param name="file" value="%s"/>
            <param name="embedded" value="true"/>
            <param name="APPLICATION_URL" value="http://www.jalview.org/services/launchApp"/>
            <param name="format" value="fasta"/>
            <param name="showFeatureSettings" value="false"/>
            <param name="type" value="file"/>
            <param name="nojmol" value="true"/>
    </applet> """ % (alignment)
#I think in the above we just need to update the 'option value' to point to the right location
#not sure how to get the script (running in /var/www/cgi-bin) to recognize a file in /var/www/html/
#print a tail

print """
</body>

</html>
"""
