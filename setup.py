from setuptools import setup

setup(
    name="pdf-cli",
    version="1.0",
    packages=["commands", "functions", "tools"],
    include_package_data=True,
    install_requires=["pypdf==3.4.0",
                      "click==8.1.3",
                      "colorama"],
    py_modules=["main"],
    entry_points="""
        [console_scripts]
        pdf=main:cli
    """,
)
