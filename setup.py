import setuptools
import versioneer

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="thinkiq_python_library",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="ThinkIQ",
    author_email="info@thinkiq.com",
    description="ThinkIQ Python Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThinkIQ/thinkiq-python-library",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["psycopg2-binary>=2.8.4", "pytz>=2019.3", "numpy>=1.18.1"],
    classifiers=[
        # Development Status Values
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Datascience",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    keywords="thinkiq datascience manufacturing industrial",
    python_requires=">=3.7",
    project_urls={  # Optional
        "Company Website": "https://thinkiq.com",
        "Source": "https://github.com/ThinkIQ/thinkiq_python_library/",
    },
)
