class FileSystem:
    """File system encapsulation.
    Aspose.3D will use this to read/write dependencies."""

    def __init__(self):
        raise NotImplementedError("FileSystem is an abstract class")

    @staticmethod
    def create_zip_file_system(stream, base_dir: str) -> 'FileSystem':
        raise NotImplementedError("create_zip_file_system is not implemented")

    @staticmethod
    def create_zip_file_system(file_name: str) -> 'FileSystem':
        raise NotImplementedError("create_zip_file_system is not implemented")

    @staticmethod
    def create_local_file_system(directory: str) -> 'FileSystem':
        raise NotImplementedError("create_local_file_system is not implemented")

    @staticmethod
    def create_dummy_file_system() -> 'FileSystem':
        raise NotImplementedError("create_dummy_file_system is not implemented")

    def read_file(self, file_name: str, options) -> 'io.IOBase':
        raise NotImplementedError("read_file is not implemented")

    def write_file(self, file_name: str, options) -> 'io.IOBase':
        raise NotImplementedError("write_file is not implemented")
