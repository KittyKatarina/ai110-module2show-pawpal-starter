"""Simple tests for the PawPal+ system."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pawpal_system import UserSchedule, Pet, CareTask


def test_task_completion():
    """Assigning a task to a schedule should flip its covered flag to True."""
    pet = Pet(pet_id=1, name="Rex")
    task = CareTask("Walk", pet)
    assert task.covered is False

    schedule = UserSchedule(owner_user_id=1)
    schedule.add_task(task)

    assert task.covered is True


def test_task_addition():
    """Adding a task to a pet should increase that pet's task count."""
    pet = Pet(pet_id=1, name="Rex")
    assert pet.task_count() == 0

    pet.add_task(CareTask("Feed", pet))

    assert pet.task_count() == 1


if __name__ == "__main__":
    test_task_completion()
    test_task_addition()
    print("All tests passed.")
