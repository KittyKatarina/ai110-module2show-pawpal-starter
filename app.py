import streamlit as st

from pawpal_system import FamilyAccount, User, Pet, CareTask, UserSchedule

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

# Create the FamilyAccount once and keep it in the session "vault" so it
# survives Streamlit's rerun-on-every-interaction. On later reruns the key
# already exists, so we reuse the same instance instead of rebuilding it.
if "family" not in st.session_state:
    family = FamilyAccount(account_id=1, family_name="My Family")
    family.add_member(User(user_id=1, name="Jordan"))
    st.session_state.family = family

family = st.session_state.family

st.subheader("Add a Pet")
col1, col2 = st.columns([3, 1])
with col1:
    new_pet_name = st.text_input("Pet name", value="Mochi", label_visibility="collapsed")
with col2:
    if st.button("Add pet"):
        if new_pet_name.strip():
            # Derive a unique id from the current pets so it survives reruns.
            next_id = max((p.pet_id for p in family.pets), default=0) + 1
            family.add_pet(Pet(pet_id=next_id, name=new_pet_name.strip()))
        else:
            st.warning("Enter a pet name first.")

if not family.pets:
    st.info("No pets yet. Add one above.")

st.divider()

st.subheader("Schedule a Task")
if family.pets:
    col1, col2, col3 = st.columns([2, 3, 2])
    with col1:
        pet_names = [p.name for p in family.pets]
        selected_pet_name = st.selectbox("For pet", pet_names)
    with col2:
        task_title = st.text_input("Task", value="Morning walk")
    with col3:
        task_time = st.time_input("Time")

    if st.button("Add task"):
        pet = next(p for p in family.pets if p.name == selected_pet_name)
        pet.add_task(CareTask(task_title, pet, time=task_time.strftime("%H:%M")))
else:
    st.caption("Add a pet before scheduling tasks.")

# Show each pet's current tasks.
for pet in family.pets:
    st.markdown(f"**{pet.name}** — {pet.task_count()} task(s)")
    for t in pet.tasks:
        when = f"{t.time} — " if t.time else ""
        st.write(f"- {when}{t.task} {'✅' if t.covered else '—'}")

st.divider()

st.subheader("Build Schedule")
st.caption("Automatically assigns every task to family members (round-robin).")

if st.button("Generate schedule"):
    if not any(pet.tasks for pet in family.pets):
        st.warning("Add at least one task first.")
    else:
        family.assign_tasks()
        st.success("Today's Schedule")
        for member in family.members:
            st.markdown(f"**{member.name}**")
            assigned = member.schedule.view()
            if not assigned:
                st.write("- (no tasks assigned)")
            for t in assigned:
                when = f"{t.time} — " if t.time else ""
                st.write(f"- {when}{t.pet.name}: {t.task}")
