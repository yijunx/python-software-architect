from math import factorial
import pathlib
from abc import ABC, abstractclassmethod


class VideoExporter(ABC):
    """"""

    @abstractclassmethod
    def prepare_export(self, video_data):
        """prepares video data for exporting"""

    @abstractclassmethod
    def do_export(self, folder: pathlib.Path):
        """export the video data to a folder"""


class LosslessVideoExporter(VideoExporter):
    """well its lossless"""

    def prepare_export(self, video_data):
        print("lossless video preparation")

    def do_export(self, folder: pathlib.Path):
        print(f"exporting lossless video to {folder}")


class GarbageVideoExporter(VideoExporter):
    """well its lossless"""

    def prepare_export(self, video_data):
        print("garbage video preparation")

    def do_export(self, folder: pathlib.Path):
        print(f"exporting garbage video to {folder}")


class AudioExporter(ABC):
    """"""

    @abstractclassmethod
    def prepare_export(self, video_data):
        """prepares audio data for exporting"""

    @abstractclassmethod
    def do_export(self, folder: pathlib.Path):
        """export the audio data to a folder"""


class LosslessAudioExporter(VideoExporter):
    """well its lossless"""

    def prepare_export(self, video_data):
        print("lossless audio preparation")

    def do_export(self, folder: pathlib.Path):
        print(f"exporting lossless audio to {folder}")


class GarbageAudioExporter(VideoExporter):
    """well its lossless"""

    def prepare_export(self, video_data):
        print("garbage audio preparation")

    def do_export(self, folder: pathlib.Path):
        print(f"exporting garbage audio to {folder}")


class ExporterFactory(ABC):
    """the abstract factory
    the factory doesnt maintain any of the instances it creates"""

    @abstractclassmethod
    def get_video_exporter(self) -> VideoExporter:
        ...

    @abstractclassmethod
    def get_audio_exporter(self) -> AudioExporter:
        ...


class FastExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return GarbageVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return GarbageAudioExporter()


class NiceExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return LosslessAudioExporter()


def read_exporter() -> ExporterFactory:
    factories = {
        "low": FastExporter(),
        "high": NiceExporter()
    }
    # read quality
    export_quality: str
    while True:
        export_quality = input("Enter desired quality (low, high): ")
        if export_quality in factories:
            return factories[export_quality]
        print(f"Unknown quality: {export_quality}")


def main(fac: ExporterFactory) -> None:
    """The main function here is responsible for too many responsibilities

    now main does not know about what exporter we have!!
    but factory does not work well for compositions 
    say we have 50 video choices and 50 audio choices
    we cannot create 50*50 concrete factory classes

    in this case, composition will be a better way
    """

    video_exp = fac.get_video_exporter()
    audio_exp = fac.get_audio_exporter()

    # prepare
    video_exp.prepare_export("video_data")
    audio_exp.prepare_export("audio_data")

    # exp
    folder = "/folder"
    video_exp.do_export(folder)
    audio_exp.do_export(folder)


if __name__ == "__main__":
    fac = read_exporter()
    main(fac)
