from subprocess import check_call, STDOUT
import glob

# root_dir needs a trailing slash (i.e. /root/dir/)
for filename in glob.iglob('C:/Program Files (x86)/Microsoft Visual Studio 14.0/**/*.exe', recursive=True):
     if 'rc.' in filename:
          print(filename)

check_call('pip install wheel', stderr = STDOUT)
check_call('python setup.py bdist_wheel', stderr = STDOUT)
