# PawPal+ UML Class Diagram

```mermaid
classDiagram
    class FamilyAccount {
        +int accountId
        +string familyName
        +List~User~ members
        +List~Pet~ pets
        +addMember(User)
        +addPet(Pet)
        +assignTasks()
    }

    class User {
        +int userId
        +string name
        +UserSchedule schedule
        +createProfile()
    }

    class Pet {
        +int petId
        +string name
        +CareSchedule careSchedule
    }

    class UserSchedule {
        +int ownerUserId
        +bool[48] intervals
        +setBusy(int slot)
        +setFree(int slot)
        +isFree(int slot) bool
    }

    class CareSchedule {
        +int scheduleId
        +int petId
        +bool[48] intervals
        +List~CareTask~ needs
        +addNeed(type, slot)
        +getNeeds() List~CareTask~
    }

    class CareTask {
        +string task
        +int slot
        +bool covered
    }

    class Assign {
        +int assignId
        +int userId
        +int petId
        +CareTask task
        +int slot
        +matchSchedules(UserSchedule, CareSchedule) Assign
    }

    FamilyAccount "1" o-- "many" User : contains
    FamilyAccount "1" o-- "many" Pet : owns
    User "1" --> "1" UserSchedule : has
    Pet "1" --> "1" CareSchedule : has
    CareSchedule "1" *-- "many" CareTask : lists
    Assign ..> User : assigns
    Assign ..> CareTask : covers
    Assign ..> UserSchedule : checks against
```

## Notes
- **FamilyAccount** is the top-level container grouping users and pets.
- **UserSchedule** and **CareSchedule** both use a 48-slot boolean array (30-min intervals over 24h).
- **Assign** holds the matching logic: it pairs a free user slot with a pet care need.
- **CareTask** is broken out so a CareSchedule can list multiple needs (feed, walk) at specific intervals.
