from setuptools import setup, find_packages
#https://www.freecodecamp.org/news/build-your-first-python-package/
VERSION = '0.0.1' 
DESCRIPTION = 'Python Tools - PhD'
LONG_DESCRIPTION = 'This package contains the python methods that I used to treat the data during my PhD.'

# Setting up
setup(
       
        name="ISOM_tools", 
        version=VERSION,
        author="Malte Schwarz",
        author_email="<malte.d.schwarz@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)