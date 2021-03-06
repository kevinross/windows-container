from setuptools import setup
from setuptools.extension import Extension
from glob import glob, iglob

# root_dir needs a trailing slash (i.e. /root/dir/)
for filename in iglob('C:/Program Files (x86)/Microsoft Visual Studio 14.0/**/*.exe', recursive=True):
     if 'rc.' in filename:
          print(filename)
def read_readme():
    with open('README.rst', 'r') as f:
        return f.read()

setup(
    name = 'windows-container',
    ext_modules = [
        Extension('winc',
            define_macros = [
                # see https://msdn.microsoft.com/en-us/library/windows/desktop/ms683219(v=vs.85).aspx
                ('PSAPI_VERSION', '1'),
                # FIXME: _HAS_EXCEPTIONS only has effect when /MT
                # But python builds it with /MD
                # ('_HAS_EXCEPTIONS', '0'),
            ],
            include_dirs = [
                'include',
                '.'
            ],
            libraries = [
                'advapi32',
                'ntdll',
                'user32',
                'psapi'
            ],
            sources = glob('core/*.cc') +
                      glob('bindings/binding_python/*.cc')
        )
    ],
    long_description = read_readme()
)
