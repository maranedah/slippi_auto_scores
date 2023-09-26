import pathlib
import os

ROOT_FOLDER = pathlib.Path(__file__).parent
SLIPPI_FOLDER = pathlib.Path(
    os.path.join("C:\\", "Users", "mauri", "Documents", "Slippi")
)
scoreinfo_path = (
    ROOT_FOLDER / "Stream Tool" / "Resources" / "Texts" / "ScoreboardInfo.json"
)
spectate_path = SLIPPI_FOLDER / "Spectate" / "duck"
charinfo_path = ROOT_FOLDER / "Stream Tool" / "Resources" / "Texts" / "Character Info"
