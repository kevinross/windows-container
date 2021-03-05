import glob

# root_dir needs a trailing slash (i.e. /root/dir/)
for filename in glob.iglob('C:/Program Files (x86)/Microsoft Visual Studio 14.0/', recursive=True):
     print(filename)
