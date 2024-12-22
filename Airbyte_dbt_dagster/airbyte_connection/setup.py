from setuptools import find_packages, setup

setup(
    name="airbyte_connection",
    packages=find_packages(exclude=["airbyte_connection_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
