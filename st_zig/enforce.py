from typing import Type, TYPE_CHECKING, Optional
from .ZigCompiler import ZigCompiler

if TYPE_CHECKING:
    from setuptools._distutils.command import build_ext
    from setuptools._distutils.compilers.C.unix import Compiler
else:
    from distutils.command import build_ext
    from distutils.compilers.C.unix import Compiler


def enforce_via_build_ext(compiler: Type[Compiler] = ZigCompiler):
    """Forces setuptools to use Zig as the compiler."""

    def new_compiler(
        plat: Optional[str] = None,
        compiler: Optional[str] = None,
        verbose: bool = False,
        dry_run: bool = False,
        force: bool = False,
    ) -> Compiler:
        return ZigCompiler(verbose, dry_run, force)

    build_ext.new_compiler = new_compiler  # type: ignore
    build_ext.customize_compiler = lambda compiler: None  # type: ignore


def enforce_via_env(zig: str = "python -m ziglang"):
    import sys
    import sysconfig

    # patch for the compiler selection
    sys.argv.append("--compiler=unix")

    # patch for the compiler configuration

    CONFIG_VARS = {
        "CC": f"{zig} cc",
        "CCFLAGS": "",
        "CXX": f"{zig} c++",
        "CFLAGS": "",
        "CXXFLAGS": "",
        "CCSHARED": "",
        "LDSHARED": f"{zig} cc -shared",
        "LDCXXSHARED": f"{zig} c++ -shared",
        "AR": f"{zig} ar",
        "ARFLAGS": "-cr",
        "RANLIB": f"{zig} ranlib",
    }

    sysconfig._init_config_vars()  # type: ignore
    SYSCONFIG_VARS: dict = sysconfig._CONFIG_VARS  # type: ignore
    for k, v in CONFIG_VARS.items():
        if k not in SYSCONFIG_VARS:
            SYSCONFIG_VARS[k] = v


__all__ = ["enforce_via_build_ext", "enforce_via_env"]
