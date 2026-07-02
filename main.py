"""Demo script for the PawPal+ system."""

from pawpal_system import FamilyAccount, User, Pet, CareTask


def main() -> None:
    # Create a family account with one user and two pets.
    family = FamilyAccount(account_id=1, family_name="Kirby")

    ferrin = User(user_id=1, name="Ferrin")
    family.add_member(ferrin)

    rex = Pet(pet_id=1, name="Rex")
    milo = Pet(pet_id=2, name="Milo")
    family.add_pet(rex)
    family.add_pet(milo)

    # Add at least 3 tasks across the pets, each at a different time.
    rex.add_task(CareTask("Feed (08:00)", rex))
    rex.add_task(CareTask("Walk (17:30)", rex))
    milo.add_task(CareTask("Feed (12:00)", milo))
    milo.add_task(CareTask("Clean litter (20:00)", milo))

    # Automatically assign all tasks to family members.
    family.assign_tasks()

    # Print today's schedule.
    print("=" * 40)
    print(f"Today's Schedule for the {family.family_name} family")
    print("=" * 40)
    for member in family.members:
        print(f"\n{member.name}:")
        tasks = member.schedule.view()
        if not tasks:
            print("  (no tasks assigned)")
        for task in tasks:
            print(f"  - {task.pet.name}: {task.task}")
    print()


if __name__ == "__main__":
    main()
