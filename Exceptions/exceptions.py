class InvalidTextFile(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message
    
class IncorrectData(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message
    
    
def is_text_plain_file(filepath: str) -> bool:
    """
    Check if the file is a text plain file.
    see: https://stackoverflow.com/a/7392391/19043850
    Params:
        filename (str): The path of the file.
    Returns:
        bool: True if the file is a text plain file, False otherwise.
    """

    textchars = bytearray(
        {7, 8, 9, 10, 12, 13, 27} |
        set(range(0x20, 0x100)) - {0x7f}
    )
    def is_binary_string(bytes): return bool(bytes.translate(None, textchars))
    return not is_binary_string(open(filepath, 'rb').read(1024))
