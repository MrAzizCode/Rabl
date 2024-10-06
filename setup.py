# setup.py
from setuptools import setup, find_packages

setup(
    name="rabl",  # اسم الحزمة
    version="0.1",
    description="A simple Arabic programming language interpreter",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="اسمك",
    author_email="بريدك الإلكتروني",
    url="https://github.com/username/rabl",  # ضع هنا رابط المستودع الخاص بك على GitHub
    packages=find_packages(),
    install_requires=[],  # إذا كانت هناك مكتبات أخرى يعتمد عليها المشروع ضعها هنا
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
