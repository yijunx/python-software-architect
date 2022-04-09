"""a simple pluging loader"""
import importlib


# plugging register new classes to the factory


class PluginInterface:
    """plugin has a single function called initializer"""

    @staticmethod
    def initialize() -> None:
        """initialize the plugin"""


def import_module(name: str) -> PluginInterface:
    return importlib.import_module(name)


def load_plugins(plugins: list[str]) -> None:
    """load the plugings defined in the plugins list"""
    for plugin_name in plugins:
        plugin = import_module(plugin_name)
        plugin.initialize()
