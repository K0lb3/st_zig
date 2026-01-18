from setuptools import Extension, setup

setup(
    name="test",
    version="0.1.0",
    ext_modules=[
        Extension("test", sources=["test.c"]),
    ],
)
