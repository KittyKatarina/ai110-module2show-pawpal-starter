"""PawPal+ system classes, generated from uml-diagram.mmd."""

from typing import List


class CareTask:
    def __init__(self, task: str, pet: "Pet", time: str = "", covered: bool = False):
        self.task: str = task
        self.pet: "Pet" = pet
        self.time: str = time
        self.covered: bool = covered

    def __repr__(self) -> str:
        state = "covered" if self.covered else "uncovered"
        when = f" at {self.time}" if self.time else ""
        return f"CareTask({self.task!r}{when} for {self.pet.name}, {state})"


class Pet:
    def __init__(self, pet_id: int, name: str):
        self.pet_id: int = pet_id
        self.name: str = name
        self.tasks: List[CareTask] = []

    def add_task(self, task: CareTask) -> None:
        """Add a care task to this pet's task list."""
        if task.pet is not self:
            raise ValueError(f"Task {task.task!r} does not belong to {self.name}.")
        if task not in self.tasks:
            self.tasks.append(task)

    def remove_task(self, task: CareTask) -> None:
        """Remove a care task from this pet's task list."""
        if task in self.tasks:
            self.tasks.remove(task)

    def uncovered_tasks(self) -> List[CareTask]:
        """Return this pet's tasks that are not yet covered."""
        return [t for t in self.tasks if not t.covered]

    def task_count(self) -> int:
        """Return the number of tasks this pet has."""
        return len(self.tasks)

    def __repr__(self) -> str:
        return f"Pet(#{self.pet_id} {self.name!r}, {len(self.tasks)} tasks)"


class UserSchedule:
    def __init__(self, owner_user_id: int):
        self.owner_user_id: int = owner_user_id
        self.tasks: List[CareTask] = []

    def add_task(self, task: CareTask) -> None:
        """Assign a task to this schedule and mark it covered."""
        if task not in self.tasks:
            self.tasks.append(task)
            task.covered = True

    def remove_task(self, task: CareTask) -> None:
        """Unassign a task from this schedule and mark it uncovered."""
        if task in self.tasks:
            self.tasks.remove(task)
            task.covered = False

    def view(self) -> List[CareTask]:
        """Return a copy of the tasks assigned to this schedule."""
        return list(self.tasks)

    def __repr__(self) -> str:
        return f"UserSchedule(user #{self.owner_user_id}, {len(self.tasks)} tasks)"


class User:
    def __init__(self, user_id: int, name: str):
        self.user_id: int = user_id
        self.name: str = name
        self.schedule: UserSchedule = UserSchedule(user_id)

    def create_profile(self) -> dict:
        """Return a summary of this user and their assigned tasks."""
        return {
            "userId": self.user_id,
            "name": self.name,
            "tasks": [t.task for t in self.schedule.view()],
        }

    def __repr__(self) -> str:
        return f"User(#{self.user_id} {self.name!r})"


class FamilyAccount:
    def __init__(self, account_id: int, family_name: str):
        self.account_id: int = account_id
        self.family_name: str = family_name
        self.members: List[User] = []
        self.pets: List[Pet] = []

    def add_member(self, user: User) -> None:
        """Add a user to this family account."""
        if user not in self.members:
            self.members.append(user)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this family account."""
        if pet not in self.pets:
            self.pets.append(pet)

    def assign_tasks(self) -> None:
        """Auto-assign every uncovered pet task to members round-robin."""
        if not self.members:
            raise ValueError("No members to assign tasks to.")
        i = 0
        for pet in self.pets:
            for task in pet.uncovered_tasks():
                member = self.members[i % len(self.members)]
                member.schedule.add_task(task)
                i += 1

    def __repr__(self) -> str:
        return (
            f"FamilyAccount(#{self.account_id} {self.family_name!r}, "
            f"{len(self.members)} members, {len(self.pets)} pets)"
        )
