import setuptools

import sms_reg_api

packages = ["sms_reg_api"] # Название плагина

with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r] # Зависимости



setuptools.setup(
    name=sms_reg_api.name,
    version=sms_reg_api.__version__,
    author=sms_reg_api.__author__,
    packages=packages,
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=requires,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: Russian",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    package_dir={"sms_reg_api": "sms_reg_api"},
    project_urls={"Source": sms_reg_api.__source__},
)
