print(f"Loading {__file__}...")

from pathlib import Path
from nslsii.ophyd_async.providers import NSLS2PathProvider, PathProvider
from ophyd_async.core import init_devices, StaticPathProvider, UUIDFilenameProvider
from isrtools.detectors.eiger import EigerDetector

# pp = NSLS2PathProvider(RE.md)  # noqa: F821

pp = StaticPathProvider(
    directory_path=Path("/nsls2/data/isr/legacy/DATA_Hutch_D/eiger1-test/"),
    filename_provider=UUIDFilenameProvider(),
)


with init_devices():
    eiger = EigerDetector(
        prefix="XF:04IDD-ES{Det:Eig1M}", name="eiger", path_provider=pp
    )