"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages, Extension
# To use a consistent encoding
from codecs import open
from os import path
from datetime import datetime

HERE = path.abspath(path.dirname(__file__))

SQUASHFS_PATH = path.join('squashfs-tools', 'squashfs-tools')

CHANGES_PATH = path.join(HERE, 'squashfs-tools', 'CHANGES')
RELEASE_VERSION, RELEASE_DATE, RELEASE_NEW = list(open(CHANGES_PATH))[2].split('\t')
RELEASE_DATE = datetime.strptime(RELEASE_DATE, '%d %b %Y')

SOURCES = ['swap.c', 'compressor.c', 'date.c']
DEFINE_MACROS = {
    '_FILE_OFFSET_BITS': '64',
    '_LARGEFILE_SOURCE': '1',
    '_GNU_SOURCE': '1',
    'COMP_DEFAULT': '"zstd"',
    'XATTR_SUPPORT': '1',
    'XATTR_DEFAULT': '1',
    'REPRODUCIBLE_DEFAULT': '1',
    'VERSION': f'"{RELEASE_VERSION}"',
    'DATE': f'"{RELEASE_DATE.strftime("%Y/%m/%d")}"',
    'YEAR': f'"{RELEASE_DATE.year}"',
    'main': 'squashfs_main',
    'exit': 'squashfs_exit',
    '__noreturn__': '',
}
EXTRA_COMPILE_ARGS = ['-O0', '-ggdb']
LIBRARIES = ['pthread','m']
EXTRA_LINK_ARGS = ['-ggdb']

DEFINE_MACROS['GZIP_SUPPORT'] = '1'
SOURCES += ['gzip_wrapper.c']
LIBRARIES += ['z']

DEFINE_MACROS['XZ_SUPPORT'] = '1'
SOURCES += ['xz_wrapper.c']
LIBRARIES += ['lzma']

DEFINE_MACROS['LZO_SUPPORT'] = '1'
SOURCES += ['lzo_wrapper.c']
LIBRARIES += ['lzo2']

DEFINE_MACROS['LZ4_SUPPORT'] = '1'
SOURCES += ['lz4_wrapper.c']
LIBRARIES += ['lz4']

DEFINE_MACROS['ZSTD_SUPPORT'] = '1'
SOURCES += ['zstd_wrapper.c']
LIBRARIES += ['zstd']

unsquashfs = Extension(
    'unsquashfs',
    include_dirs = [SQUASHFS_PATH],
    define_macros = list(DEFINE_MACROS.items()),
    extra_compile_args = EXTRA_COMPILE_ARGS,
    libraries = LIBRARIES,
    extra_link_args = EXTRA_LINK_ARGS,
    sources = [
        path.join(SQUASHFS_PATH, x)
        for x in [
            'unsquashfs.c', 'unsquash-1.c', 'unsquash-2.c', 'unsquash-3.c',
        	'unsquash-4.c', 'unsquash-123.c', 'unsquash-34.c', 'unsquash-1234.c',
            'unsquash-12.c', 'unsquashfs_info.c',
            'read_xattrs.c', 'unsquashfs_xattr.c',
            *SOURCES,
        ]
    ] + ['util.c', 'unsquashfs.c'],
)

mksquashfs = Extension(
    'mksquashfs',
    include_dirs = [SQUASHFS_PATH],
    define_macros = list(DEFINE_MACROS.items()),
    extra_compile_args = EXTRA_COMPILE_ARGS,
    libraries = LIBRARIES,
    extra_link_args = EXTRA_LINK_ARGS,
    sources = [
        path.join(SQUASHFS_PATH, x)
        for x in [
            'mksquashfs.c', 'read_fs.c', 'action.c', 'pseudo.c',
        	'sort.c', 'progressbar.c', 'info.c', 'restore.c', 'process_fragments.c',
	        'caches-queues-lists.c', 'reader.c', 'tar.c',
            'xattr.c', 'read_xattrs.c', 'tar_xattr.c', 'pseudo_xattr.c',
            *SOURCES,
        ]
    ] + ['util.c', 'mksquashfs.c'],
)

# Get the long description from the README file
with open(path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    long_description_list = f.readlines()

    long_description = ""

    for line in long_description_list:
        long_description += line
    long_description = long_description.replace("\r", "")

setup(
    name='poorly-done-squashfs-tools',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.1',

    #description='Python C-API Template',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/xloem/poorly-done-squashfs-tools',

    # Author details
    #author='Zuzu_Typ',
    #author_email="zuzu.typ@gmail.com",

    # Choose your license
    license='Public Domain',

##    install_requires=[],

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: Public Domain',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        "Operating System :: MacOS",
        "Operating System :: OS Independent",
        
        'Topic :: Software Development :: Libraries'
        
    ],

    # What does your project relate to?
    #keywords='template example',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    #packages=['squashfs_tools.py'],#{},
    #packages = ['squashfs_tools'],
    py_modules = ['poorly_done_squashfs_tools'],

    platforms = ["Windows", "Linux", "MacOS"],
    
    include_package_data=True,

    ext_modules = [unsquashfs, mksquashfs],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
)
