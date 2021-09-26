import site
from os import getenv, makedirs
from os.path import abspath, dirname, join, exists

from plex_trakt_sync.decorators.memoize import memoize


class Path:
    def __init__(self):
        self.app_name = "PlexTraktSync"
        self.module_path = dirname(abspath(__file__))
        self.app_path = dirname(self.module_path)

        self.ensure_dir(self.config_dir)
        self.ensure_dir(self.log_dir)
        self.ensure_dir(self.cache_dir)

        self.default_config_file = join(self.module_path, "config.default.json")
        self.config_file = join(self.config_dir, "config.json")
        self.pytrakt_file = join(self.config_dir, ".pytrakt.json")
        self.env_file = join(self.config_dir, ".env")
        self.log_file = join(self.log_dir, "last_update.log")

    @property
    @memoize
    def config_dir(self):
        if self.installed:
            from appdirs import user_config_dir

            return user_config_dir(self.app_name)

        return getenv("PTS_CONFIG_DIR", self.app_path)

    @property
    @memoize
    def cache_dir(self):
        if self.installed:
            from appdirs import user_cache_dir

            return user_cache_dir(self.app_name)

        return getenv("PTS_CACHE_DIR", self.app_path)

    @property
    @memoize
    def log_dir(self):
        if self.installed:
            from appdirs import user_log_dir

            return user_log_dir(self.app_name)

        return getenv("PTS_LOG_DIR", self.app_path)

    @property
    @memoize
    def installed(self):
        """
        Return true if this package is installed to site-packages
        """
        absdir = dirname(dirname(__file__))
        paths = site.getsitepackages()

        return absdir in paths

    @staticmethod
    def ensure_dir(directory):
        if not exists(directory):
            makedirs(directory)


p = Path()

cache_dir = p.cache_dir
config_dir = p.config_dir
log_dir = p.log_dir

default_config_file = p.default_config_file
config_file = p.config_file
pytrakt_file = p.pytrakt_file
env_file = p.env_file
log_file = p.log_file
