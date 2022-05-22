from typing import Any
from config_access import Config


class Experiment:
    def __init__(self, config: Config) -> None:
        self.config = config

    def load_data(self) -> None:
        data_path = self.config.get("data_path")
        if not data_path:
            raise ValueError("no datapath")
        print(f"loading data from {data_path}")

    def setup_log(self) -> None:
        log_path = self.config.get("log_path")
        if not log_path:
            raise ValueError("no logpath")
        print(f"logging to {log_path}")

    def train_model(self) -> None:
        epoch_count = self.config.get("epoch_count")
        print(f"training {epoch_count} epochs")

    def run(self):
        self.load_data()
        self.setup_log()
        self.train_model()
