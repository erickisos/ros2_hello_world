from setuptools import setup

package_name = 'simple_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            [f'resource/{package_name}'],
        ),
        (f'share/{package_name}', ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='erickisos',
    maintainer_email='erickisos653@gmail.com',
    description='This is just a simple test for ros2 humble',
    license='GPLv3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = simple_test.talker:main',
            'listener = simple_test.listener:main',
        ],
    },
)
