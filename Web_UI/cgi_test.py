#!C:\Users\larry\AppData\Local\Programs\Python\Python38\python.exe

import cgi, os
import cgitb; cgitb.enable(display=0, logdir="cgi_logs")

form = cgi.FieldStorage()

#Get filename here.
fileitem = form['filename']

# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open(fn, 'wb').write(fileitem.file.read())

   message = 'The file "' + fn + '" was uploaded successfully'
   
else:
   message = 'No file was uploaded'
   
print("""\
Content-Type: text/html\r\n
<html>
<body>
   <p>%s</p>
</body>
</html>
""" % (fn,))
