from setuptools import setup
import os
import glob

package_name = 'ros2_course'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
            (os.path.join('share', package_name, 'launch'), glob.glob('launch/*.launch.py')),
        ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros_user',
    maintainer_email='ros_user@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hello = ros2_course.hello:main',
            'fractal = ros2_course.fractal_turtle:main',
            'turtle = ros2_course.turtle:main',
            'listener = ros2_course.turtle_listener:main'
        ],
    },
)
