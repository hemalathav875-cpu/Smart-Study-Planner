
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Study Planner", page_icon="📚")

st.title("📚 Smart Study Planner")
st.write("Plan your studies and complete your daily goals!")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.subheader("➕ Add a Study Task")

subject = st.text_input("Subject")
task = st.text_input("Task Name")
deadline = st.date_input("Deadline")

if st.button("Add Task"):
    if subject and task:
        st.session_state.tasks.append({
            "Subject": subject,
            "Task": task,
            "Deadline": str(deadline),
            "Completed": False
        })
        st.success("Task added successfully!")
    else:
        st.warning("Please enter both subject and task.")

st.subheader("📋 Your Study Tasks")

if st.session_state.tasks:
    for i, item in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([4, 1])

        with col1:
            st.write(f"**{item['Subject']}** - {item['Task']}")
            st.caption(f"Deadline: {item['Deadline']}")

        with col2:
            if st.checkbox("Done", key=f"task_{i}"):
                item["Completed"] = True
            else:
                item["Completed"] = False

    completed = sum(t["Completed"] for t in st.session_state.tasks)
    total = len(st.session_state.tasks)

    st.subheader("📊 Study Progress")
    st.progress(completed / total)
    st.write(f"Completed: {completed} / {total}")

    if st.button("Clear All Tasks"):
        st.session_state.tasks = []
        st.rerun()

else:
    st.info("No tasks yet. Add your first study task!")
