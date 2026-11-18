from setuptools import find_packages, setup

package_name = 'tesseract_ur'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/urdf',
            [   'tesseract_ur/urdf/ur5e_default.urdf', 
                'tesseract_ur/urdf/ur5e_plugins.yaml', 
                'tesseract_ur/urdf/ur5e.srdf']
           ),
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='joris',
    maintainer_email='joris@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'tesseract_ur_node = tesseract_ur.tesseract_ur_node:main'
        ],
    },
)
