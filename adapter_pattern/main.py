import json
from xml_adaptor import XMLConfig
from experiment import Experiment
from bs4 import BeautifulSoup


def main() -> None:
    # what if we want to use some other ways to extract data??
    # adaptor pattern brings interface between xml reader or json reader
    # goal is to adaptor, creating a layer

    # client is experiment, it uses something from an operation

    # operation is to get things from config, operator operates it

    # specific operator is xxx reader, this is the adoptee
    with open("config.xml", encoding="utf8") as file:
        config = file.read()
        # config = json.load(file)
    bs = BeautifulSoup(config, "xml")
    adaptor = XMLConfig(bs=bs)
    experiment = Experiment(adaptor)
    experiment.run()


if __name__ == "__main__":
    main()
