import distutils
from setuptools import setup
from version import VERSION

try:
    distutils.dir_util.remove_tree("dist")
except:
    pass

setup(
    name='kervi-device-library',
    version=VERSION,
    author='Tim Wentzlau',
    author_email='tim.wentzlau@gmail.com',
    url='https://github.com/kervi/kervi-components',
    description="""Component library for kervi""",
    packages=[
        "kervi_devices",
        "kervi_devices.sensors"
    ]
)
