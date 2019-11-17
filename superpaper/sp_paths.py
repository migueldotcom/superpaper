"""Define paths used by Superpaper."""

import os
import platform
import sys

# Set path to binary / script
if getattr(sys, 'frozen', False):
    PATH = os.path.dirname(os.path.dirname(os.path.realpath(sys.executable)))
else:
    PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def setup_config_path():
    """Sets up config path for settings and profiles.

    On Linux systems use XDG_CONFIG_HOME standard, i.e.
    $HOME/.config/superpaper by default.
    On Windows and Mac use executable portable path for now.
    """
    # from sp_logging import DEBUG, G_LOGGER

    if platform.system() == "Linux":
        config_path = xdg_path_setup("XDG_CONFIG_HOME",
                                     os.path.join(os.path.expanduser("~"),
                                                  ".config")
                                    )
        # if DEBUG: G_LOGGER.info("config path: %s", config_path)
        return config_path
    else:
        # Windows and Mac keep the old portable config behavior for now.
        config_path = PATH
        return config_path


def setup_cache_path():
    """Sets up temp wallpaper path.

    On Linux systems use XDG_CACHE_HOME standard.
    On Windows and Mac use executable portable path (PATH/temp) for now.
    """
    # from sp_logging import DEBUG, G_LOGGER

    if platform.system() == "Linux":
        cache_path = xdg_path_setup("XDG_CACHE_HOME",
                                     os.path.join(os.path.expanduser("~"),
                                                  ".cache")
                                    )
        temp_path = os.path.join(cache_path, "temp")
        # if DEBUG: G_LOGGER.info("temp path: %s", temp_path)
        return temp_path
    else:
        # Windows and Mac keep the old portable config behavior for now.
        temp_path = os.path.join(PATH, "temp")
        return temp_path


def xdg_path_setup(xdg_var, fallback_path):
    """Sets up superpaper folders in the appropriate XDG paths:

    XDG_CONFIG_HOME, or fallback ~/.config/superpaper
    XDG_CACHE_HOME, or fallback ~/.cache/superpaper
    """

    xdg_home = os.environ.get(xdg_var)
    if xdg_home and os.path.isdir(xdg_home):
        xdg_path = os.path.join(xdg_home, "superpaper")
    else:
        xdg_path = os.path.join(fallback_path, "superpaper")
    # Check that the path exists and otherwise make it.
    if os.path.isdir(xdg_path):
        return xdg_path
    else:
        # default path didn't exist
        os.mkdir(xdg_path)
        return xdg_path


# Derivative paths
TEMP_PATH = setup_cache_path()     # Save adjusted wallpapers in here.
if not os.path.isdir(TEMP_PATH):
    os.mkdir(TEMP_PATH)
CONFIG_PATH = setup_config_path()   # Save profiles and settings here.
print(CONFIG_PATH)
PROFILES_PATH = os.path.join(CONFIG_PATH, "profiles")
print(PROFILES_PATH)
if not os.path.isdir(PROFILES_PATH):
    os.mkdir(PROFILES_PATH)
