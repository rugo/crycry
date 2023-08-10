from setuptools import setup

setup(
    name='crycry',
    version='0.1',
    install_requires=[
        'pycryptodome',
        'ecdsa',
    ],
    scripts=[
        'crycry/encode.py',
        'crycry/count.py',
        'crycry/ecdsareuse.py',
        'crycry/ecdsasign.py',
        'crycry/encode.py',
        'crycry/flip.py',
        'crycry/hash.py',
        'crycry/pad.py',
        'crycry/pkdump.py',
        'crycry/rsaconstruct.py',
        'crycry/xor.py'
    ],
    entry_points={
        'console_scripts': [
            'cc-encode = crycry.encode:main',
            'cc-count = crycry.count:main',
            'cc-ecdsareuse = crycry.ecdsareuse:main',
            'cc-ecdsasign = crycry.ecdsasign:main',
            'cc-flip = crycry.flip:main',
            'cc-hash = crycry.hash:main',
            'cc-pad = crycry.pad:main',
            'cc-pkdump = crycry.pkdump:main',
            'cc-rsaconstruct = crycry.rsaconstruct:main',
            'cc-xor = crycry.xor:main',
        ]
    }
)
