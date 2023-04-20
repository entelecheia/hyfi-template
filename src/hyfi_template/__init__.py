import os
import toml
from hyfi import about, global_config

from ._version import __version__

# Read and parse pyproject.toml
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))
pyproject_path = os.path.join(root_dir, "pyproject.toml")

with open(pyproject_path) as f:
    pyproject_data = toml.load(f)

# Extract package information from pyproject.toml
tool_data = pyproject_data.get("tool", {}).get("poetry", {})
about.name = tool_data.get("name", "package name")
about.author = tool_data.get("authors", ["Author name"])[0]
about.description = tool_data.get("description", "package description")
about.homepage = tool_data.get("homepage", "https://package.homepage")
about.version = __version__
global_config.hyfi_package_config_path = "pkg://hyfi_template.conf"


def get_version() -> str:
    """This is the cli function of the package"""
    return __version__
