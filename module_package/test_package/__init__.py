__all__ = ["module_a", "module_b"]

# * Expose submodules so that `from test_package import *` brings them in
from . import module_a, module_b


