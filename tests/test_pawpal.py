"""Simple tests for the PawPal+ system."""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pawpal_system import UserSchedule, Pet, CareTask, FamilyAccount, User


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


def test_tasks_sort_by_time():
    """Tasks should be sorted by time, with untimed tasks placed last."""
    pet = Pet(pet_id=1, name="Rex")
    late_task = CareTask("Walk", pet, time="17:30")
    early_task = CareTask("Feed", pet, time="08:00")
    untimed_task = CareTask("Brush", pet)

    pet.add_task(late_task)
    pet.add_task(early_task)
    pet.add_task(untimed_task)

    sorted_tasks = pet.sorted_tasks()

    assert [task.task for task in sorted_tasks] == ["Feed", "Walk", "Brush"]


def test_assign_tasks_records_explanations():
    """Assigned tasks should include a short explanation for why they were chosen."""
    family = FamilyAccount(account_id=1, family_name="Test")
    family.add_member(User(user_id=1, name="Alex"))
    family.add_member(User(user_id=2, name="Sam"))

    pet = Pet(pet_id=1, name="Rex")
    family.add_pet(pet)
    pet.add_task(CareTask("Feed", pet, time="08:00"))
    pet.add_task(CareTask("Walk", pet, time="17:30"))

    family.assign_tasks()

    assigned_tasks = [task for member in family.members for task in member.schedule.view()]

    assert len(assigned_tasks) == 2
    assert all(task.assignment_reason for task in assigned_tasks)


if __name__ == "__main__":
    test_task_completion()
    test_task_addition()
    test_tasks_sort_by_time()
    test_assign_tasks_records_explanations()
    print("All tests passed.")
