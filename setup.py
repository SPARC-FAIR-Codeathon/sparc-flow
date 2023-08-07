from setuptools import setup, find_packages
setup(
    name="sparc_flow",
    version="0.1.0",
    description='A Python tool to create tools and workflows for processing SPARC datasets in accordance with FAIR principles.',
    author="Thiranja Prasad Babarenda Gamage, Chinchien Lin, Jiali Xu, Linkun Gao, Matthew French, Michael Hoffman",
    email="psam012@aucklanduni.ac.nz, clin864@aucklanduni.ac.nz",
    license="Apache-2.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['resources./*']},
    install_requires=[
        "scriptcwl>=0.8.1"
    ]
)
