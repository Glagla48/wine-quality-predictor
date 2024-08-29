
import setuptools
from distutils.util import convert_path

main_ns = {}
ver_path = convert_path('wqp/__init__.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)


setuptools.setup(
    name='wqp',
    version=main_ns['__version__'],
    author='lissandre.m@gmail.com',
    description='Wine quality predictor - a packaged machine learning algorithm to predict wine quality',
    packages=setuptools.find_packages(),
    install_requires=[
        "scikit-learn>=1",
        "pandas>=2.0.1",
        "click>=1.0"
    ],
    entry_points='''
    [console_scripts]
    wqp=wqp.cli:wqp
    '''
)