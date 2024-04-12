import os


"""
This method works only because JPGs always end with hex FFD9,
hence we can write the data after that and read it again.
"""


def write_data(img_path: str, data: bytes) -> int:
    """
    Appends bytes to the end of JPG img.

    Parameters:
    img_path (str): Img path.
    data (bytes): data to hide, represented in bytes.

    Returns:
    int: size of data written to the img.
    """
    if os.path.exists(img_path):
        if isinstance(data, bytes):
            with open(img_path, "ab") as f:
                return f.write(data)


def read_data(img_path: str) -> bytes:
    """

    Read bytes from jpg img end.

    Parameters:
    img_path (str): Img path.

    Returns:
    bytes: hidden bytes if any.
    """
    if os.path.exists(img_path):
        with open(img_path, "rb") as f:
            content = f.read()
            end_offset = content.index(bytes.fromhex("FFD9"))
            data_start = end_offset + 2
            f.seek(data_start)
            return f.read()


def delete_data(img_path: str):
    """
    Delete written bytes after jpg img end.

    Parameters:
    img_path (str): Img path.

    Returns:
    int : Size of deleted data in bytes.
    """

    if os.path.exists(img_path):

        with open(img_path, "rb") as f:
            content = f.read()

        end_index = content.index(bytes.fromhex("FFD9")) + 2
        img_bytes = content[:end_index]
        with open(img_path, "wb") as f:
            f.write(img_bytes)

        return len(img_bytes)
