"""
build_meta overwrite of setuptools.build_meta to enforce Zig compiler usage.
"""

# import everything from setuptools.build_meta
from setuptools.build_meta import *  # pyright: ignore[reportWildcardImportFromLibrary] # noqa: F401, F403

# enforce Zig compiler usage
from .enforce import enforce_via_build_ext

enforce_via_build_ext()
del enforce_via_build_ext
