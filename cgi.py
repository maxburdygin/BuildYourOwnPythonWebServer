from datetime import datetime


s = '''\
<html>
<body>
<p>Generated {0}</p>
</body>
</html>'''.format(datetime.now())

print(s)