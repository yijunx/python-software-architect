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


def main() -> None:
    """The main function here is responsible for too many responsibilities

    it is responsible for
    - asking the quality
    - mapping the quality to objects
    - and do the job

    it also has coupling, main needs to know the existence of the class
    now we only have a few classes, if there are more quality choices
    there could be a lot of if else..

    also, we dont have the option of low audio with high video!!!

    we can solve this by separating the where
    - object creation
    - object use

    thus we need factory pattern, factory takes care of the creation.
    """

    # read quality
    export_quality: str
    while True:
        export_quality = input("Enter desired quality (low, high): ")
        if export_quality in {"low", "high"}:
            break
        print(f"Unknown quality: {export_quality}")

    if export_quality == "low":
        video_exp = GarbageVideoExporter()
        audio_exp = GarbageAudioExporter()
    else:
        video_exp = LosslessVideoExporter()
        audio_exp = LosslessAudioExporter()

    # prepare
    video_exp.prepare_export("video_data")
    audio_exp.prepare_export("audio_data")

    # exp
    folder = "/folder"
    video_exp.do_export(folder)
    audio_exp.do_export(folder)


if __name__ == "__main__":
    main()
