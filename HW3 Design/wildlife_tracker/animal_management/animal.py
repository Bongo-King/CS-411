from typing import Any, Optional

class Animal:
    def __init__(self,
                species: str,
                animal_id: int,
                age: Optional[int] = None,
                health_status: Optional[str] = None,
    ) -> None:
        self.age = age
        self.animal_id = animal_id
        self.health_status = health_status
        self.species = species

    def get_animal_details(self, animal_id) -> dict[str, Any]:
        pass

    def update_animal_details(self, animal_id: int, **kwargs: Any) -> None:
        pass
