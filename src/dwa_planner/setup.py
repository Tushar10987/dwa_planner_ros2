from setuptools import setup

package_name = 'dwa_planner'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    py_modules=[],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tushar',
    maintainer_email='tusharkalantre323@gmail.com',
    description='DWA Planner for TurtleBot3',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dwa_planner = dwa_planner.dwa_planner:main',
        ],
    },
)

