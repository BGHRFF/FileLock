# @TheBaghirov - < https://t.me/TheBaghirov >
# Copyright (C) 2022
# Bütün haqları qorunur.
#
# Bu fayl, < https://github.com/bghrff/FileLock > parçasıdır.
# < https://www.github.com/bghrff/FileLock/blob/master/LICENSE/ >
# ================================================================

from setuptools import setup

classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
]

long_description = """
# **🔐 FileLock**
### **🔑 fayl şifrələyici**
- Python fayllarını 15 fərqli kombinasiyada şifrələyə bilər.
<br>

## **🪀 PyPi Kitabxanası:**
<br>

![PyPI](https://img.shields.io/pypi/v/FileLock?color=yellow&logo=python&logoColor=cyan&style=for-the-badge)
<br>

![PyPI - Downloads](https://img.shields.io/pypi/dm/FileLock?label=%C4%B0nd%C4%B0rme&logo=python&style=for-the-badge)
<br>

[![Python](https://img.shields.io/badge/Python-ile%20yap%C4%B1ld%C4%B1-yellow?style=for-the-badge&logo=python&logoColor=cyan)](https://python.org)
<br>

<br><a href="https://t.me/TheBaghirov"><img src="https://github.com/bghrff/FileLock/blob/master/ss.png?raw=true" width="350"></a><br>

### **💻 Qurulum:**

#### **Termux**

```sh
bash <(curl -L https://bit.ly/3IwB8Kw)
```

#### **Terminal**

```sh
pip install FileLock
python3 -m FileLock
```

<br>

📅 ***2022 (c) [GNU Affero General Public License v3.0](https://github.com/bghrff/FileLock/blob/master/LICENSE) ile korunmaktadır.***

<br>

### **📡 Əlaqə :**
[![Github](https://img.shields.io/badge/Github-525252?style=for-the-badge&logo=github)](https://github.com/bghrff) [![Opensource](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/TheBaghirov)
"""


setup(
    name="FileLock",
    version="1.0.0",
    author="bghrff",
    description="Python fayllarını 15 fərqli kombinasiyada şifrələyər.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bghrff/FileLock",
    license="GNU AFFERO GENERAL PUBLIC LICENSE (v3)",
    packages=["FileLock"],
    install_requires="rich",
    classifiers=classifiers,
    python_requires=">3",
)