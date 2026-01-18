from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from setuptools._distutils.unixccompiler import UnixCCompiler

    assert UnixCCompiler.src_extensions is not None, (
        "Compiler.src_extensions should not be None"
    )
else:
    from distutils.unixccompiler import UnixCCompiler


class ZigCompiler(UnixCCompiler):
    src_extensions = [
        *UnixCCompiler.src_extensions,
        ".zig",
    ]
    language_map = {
        **UnixCCompiler.language_map,
        ".zig": "c",
    }
    zig_cmd = ["python", "-m", "ziglang"]
    executables = {
        "preprocessor": None,
        "compiler": [*zig_cmd, "cc", "-O"],
        "compiler_so": [*zig_cmd, "cc", "-O"],
        "compiler_cxx": [*zig_cmd, "c++", "-O"],
        "compiler_so_cxx": [*zig_cmd, "c++", "-O"],
        "linker_so": [*zig_cmd, "cc", "-shared"],
        "linker_so_cxx": [*zig_cmd, "c++", "-shared"],
        "linker_exe": [*zig_cmd, "cc"],
        "linker_exe_cxx": [*zig_cmd, "c++"],
        "archiver": [*zig_cmd, "ar", "-cr"],
        "ranlib": [*zig_cmd, "ranlib"],
    }


__all__ = ["ZigCompiler"]
