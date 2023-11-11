import pathlib

EXT = ".pdf"


def verify_file(file_name: str) -> pathlib.Path:
    if EXT not in file_name:
        raise RuntimeError(
            f"Provided file {file_name} does not have PDF extension explicitely specified."
        )
    file = pathlib.Path(file_name)

    if not file.exists():
        raise RuntimeError(f"Provided file {file} does not exist.")

    return file
