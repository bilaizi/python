//ConfigurationSettings_basic.py
class ConfigurationSettings: 
    _instance = None 
    def __new__(cls): 
        if cls._instance is None: 
            cls._instance = super(ConfigurationSettings, cls).__new__(cls) 
        return cls._instance 
    def get_config(self): 
        return self.config 
    def set_config(self, config): 
        self.config = config 
# Usage 
config_settings = ConfigurationSettings() 
config_settings.set_config("Server Settings") 
print(config_settings.get_config())  # Output: Server Settings

//ConfigurationSettings_thread_safe.py
import threading

class ConfigurationSettings:
    _instance = None
    _lock = threading.Lock()
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(ConfigurationSettings, cls).__new__(cls)
        return cls._instance
    def get_config(self):
        return self.config
    def set_config(self, config):
        self.config = config
# Usage
config_settings1 = ConfigurationSettings()
config_settings2 = ConfigurationSettings()
config_settings1.set_config("Server Settings")
print(config_settings1 is config_settings2)  # Output: True 
print(config_settings1.get_config())  # Output: Server Settings
print(config_settings2.get_config())  # Output: Server Settings

//Logging.py
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class Singleton:
    _instance = None
    _config = None
    def __new__(cls):
        if cls._instance is None:
            logging.debug("Creating new Singleton instance.")
            cls._instance = super(Singleton, cls).__new__(cls)
        else:
            logging.debug("Reusing existing Singleton instance.")
        return cls._instance
    def set_config(self, config):
        logging.info(f"Setting configuration to: {config}")
        self._config = config
    def get_config(self):
        logging.info("Fetching current configuration.")
        if self._config is None:
            logging.warning("No configuration has been set!")
        return self._config
    def reset_config(self):
        logging.info("Resetting configuration.")
        self._config = None

# Usage with debugging and logging
if __name__ == "__main__":
    try:
        # Create Singleton instance and set configuration
        singleton = Singleton()
        singleton.set_config({"key": "value"})

        # Fetch configuration
        config = singleton.get_config()
        logging.debug(f"Retrieved configuration: {config}")

        # Reset configuration
        singleton.reset_config()
        config_after_reset = singleton.get_config()
        logging.debug(f"Configuration after reset: {config_after_reset}")

        # Attempt to reuse Singleton
        another_instance = Singleton()
        logging.debug(f"Singleton instances are the same: {singleton is another_instance}")

    except Exception as e:
        logging.error("An error occurred during Singleton operations.", exc_info=True)


