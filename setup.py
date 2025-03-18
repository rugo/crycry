from setuptools import setup

setup(
    name='crycry',
    version='0.2.0',
    install_requires=[
        'pycryptodome',
        'ecdsa',
    ],
    packages = ['crycry'],
    entry_points={
        'console_scripts': [
            'cc-encode = crycry.encode:main',
            'cc-decode = crycry.encode:main',
            'cc-prefix = crycry.prefix:main',
            'cc-suffix = crycry.suffix:main',
            'cc-count = crycry.count:main',
            'cc-ecdsareuse = crycry.ecdsareuse:main',
            'cc-ecdsasign = crycry.ecdsasign:main',
            'cc-flip = crycry.flip:main',
            'cc-hash = crycry.hash:main',
            'cc-pad = crycry.pad:main',
            'cc-pkdump = crycry.pkdump:main',
            'cc-rsaconstruct = crycry.rsaconstruct:main',
            'cc-xor = crycry.xor:main'
        ]
    }
)
