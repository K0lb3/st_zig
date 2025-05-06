# st_zig

A setuptools extension for compiling native extensions with Zig.

`st_zig` is a lightweight standalone package that enables `setuptools` to use Zig as a C/C++ compiler. By leveraging the standalone [ziglang](https://pypi.org/project/ziglang/) package, which is available for all PyPI-supported target platforms, this tool allows native extensions to be compiled directly on user devices. 

This approach eliminates the need for users to install additional build tools, simplifying the setup process. Additionally, it removes the complexity of managing platform-specific compiler flags, particularly on Windows.

## Usage

To use this package, simply add it as build requirement to your project.
You can choose between two patch options to configure setuptools to use Zig.

You either import and run ``enforce_via_build_ext`` or ``enforce_via_env``.
``st_zig.enforce_via_build_ext`` patches ``build_ext`` so that it picks ``st_zig.ZigCompiler``.
``st_zig.enforce_via_env`` modifies the sysconfig read by python to make the ``UnixCompiler`` use zig.  
The ``UnixCompiler`` class, while primarily designed for Unix-like systems, works seamlessly on Windows as well. This is because Zig includes a bundled version of Clang, which ensures compatibility with Unix-style compiler flags across all platforms, including Windows.

Mind that the ``UnixCompiler`` class just describes unix focussed compilers like gcc and clang, it also works just fine on Windows.
As Zig basically ships clang, you can use the same clang unix flags on all systems.

## Example

``setup.py``
```py
from setuptools import Extension, setup
# Add the following to your setup.py to enable Zig as the compiler
from st_zig import enforce_via_build_ext
enforce_via_build_ext()


setup(
    name="testc",
    ext_modules=[
        Extension(
            "testc",
            ["test.cpp"],
            language="c++",
            # Adjust the compile arguments based on your project's requirements
            extra_compile_args=["-std=c++23"],
        ),  # Note: The above example uses C++23. Modify the flag as needed for your project.
    ],
)
```

``pyproject.toml``
```toml
[build-system]
requires = ["setuptools", "st_zig"]
build-backend = "setuptools.build_meta"

# Add any additional configuration options below as needed
...
```