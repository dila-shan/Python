# import subprocess
# import os

# xampp_path = r'C:\xampp';
# apache_start_path = os.path.join(xampp_path, 'apache_start.bat');
# mysql_start_path = os.path.join(xampp_path, 'mysql_start.bat');

# # Start XAMPP Apache & Mysql
# subprocess.run([apache_start_path]);
# subprocess.run([mysql_start_path]);
import subprocess
import os

xampp_path = r'C:\xampp'
apache_start_path = os.path.join(xampp_path, 'apache_start.bat')
mysql_start_path = os.path.join(xampp_path, 'mysql_start.bat')

# Start XAMPP Apache & Mysql
apache_process = subprocess.Popen([apache_start_path])
mysql_process = subprocess.Popen([mysql_start_path])

# Wait for both processes to complete
apache_process.wait()
mysql_process.wait()
