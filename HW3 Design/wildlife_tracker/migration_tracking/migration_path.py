from typing import Optional

class MigrationPath:
    def __init__(self,
                 path_id: int,
                 duration: Optional[int] = None,
                 ) -> None:
        self.path_id = path_id
        self.duration = duration

    def update_migration_path_details(self, path_id: int, **kwargs) -> None:
        pass

