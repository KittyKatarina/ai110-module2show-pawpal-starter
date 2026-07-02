"""PawPal+ system class skeletons, generated from uml-diagram.mmd."""

from typing import List, Optional


class CareTask:
    def __init__(self, task: str, pet: "Pet", covered: bool = False):
        self.task: str = task
        self.pet: "Pet" = pet
        self.covered: bool = covered


class Pet:
    def __init__(self, pet_id: int, name: str):
        self.pet_id: int = pet_id
        self.name: str = name
        self.tasks: List[CareTask] = []


class UserSchedule:
    def __init__(self, owner_user_id: int):
        self.owner_user_id: int = owner_user_id
        self.intervals: List[bool] = [False] * 48
        self.tasks: List[Optional[CareTask]] = [None] * 48

    def set_busy(self, slot: int) -> None:
        pass

    def set_free(self, slot: int) -> None:
        pass

    def is_free(self, slot: int) -> bool:
        pass


class User:
    def __init__(self, user_id: int, name: str, schedule: UserSchedule):
        self.user_id: int = user_id
        self.name: str = name
        self.schedule: UserSchedule = schedule

    def create_profile(self) -> None:
        pass

    def add_task(self, task: CareTask, slot: int) -> None:
        pass


class FamilyAccount:
    def __init__(self, account_id: int, family_name: str):
        self.account_id: int = account_id
        self.family_name: str = family_name
        self.members: List[User] = []
        self.pets: List[Pet] = []

    def add_member(self, user: User) -> None:
        pass

    def add_pet(self, pet: Pet) -> None:
        pass
