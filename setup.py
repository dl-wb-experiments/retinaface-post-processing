
import platform
from pathlib import Path

from pkg_resources import parse_requirements
from setuptools import setup

PACKAGE_DIR = Path(__file__).parent


def load_requirements(requirements_file_name: str) -> list:
    requirements_file_pat = Path(PACKAGE_DIR) / requirements_file_name
    with requirements_file_pat.open() as requirements_file:
        requirements = [
            str(requirement) for requirement in parse_requirements(requirements_file)
        ]
    return requirements


# Collect requirements
REQUIRED_PACKAGES = load_requirements('requirements.txt')

# Read documentation which will be showed on PyPI
with open('README.md', 'r', encoding='utf-8') as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name='retinaface_post_processing',
    author='Tugaryov Artyom',
    author_email='artyom.tugarev@intel.com',
    license='OSI Approved :: Apache Software License',
    description='RetinaFace Post-Processing is a module contains code for post-processing of RetinaFace inference results',
    url='https://github.com/dl-wb-experiments/retinaface-post-processing',
    version='0.0.4',
    install_requires=REQUIRED_PACKAGES,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    packages=['RetinaFacePostProcessing'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)
