from setuptools import find_packages, setup

package_name = 'name_work'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test'], include=[package_name]),
    data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    ('share/' + package_name + '/msg', ['msg/FullNameMessage.msg']),
    ('share/' + package_name + '/srv', ['srv/FullNameSumService.srv']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='belyakovaDep',
    maintainer_email='d.belyakova1@g.nsu.ru',
    description='Simple messages and services',
    license='Apache-2.0 license',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [

        ],
    },
)
