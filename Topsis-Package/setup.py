import setuptools

def readme():
    with open('README.md') as f:
        README = f.read()
    return README
    
setuptools.setup(
 name='Topsis-Yuvraj-102017081',
 version='1.1.2',
 author="Yuvraj Kalsi",
 description="Topsis Package for solving MCDM Problems",
 long_description=readme(),
 long_description_content_type="text/markdown",
 packages=setuptools.find_packages(),
 classifiers=[
 "Programming Language :: Python :: 3",
 "License :: OSI Approved :: MIT License",
 "Operating System :: OS Independent",
 ],
)
