import json
from datetime import datetime

import pandas as pd
import streamlit as st


USERS = {
    "technician": {"password": "technicianAccess", "role": "Technician"},
    "manager": {"password": "managerAccess", "role": "Manager"},
}


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None

if "username" not in st.session_state:
    st.session_state.username = None


def login_page():
    st.markdown(
        "<h1 style='text-align: center;'>Cloud and API Automation Developer Challenge</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align: center;'>Eduardo Hernandez, MSCS '28</h3>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.subheader("Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user = USERS.get(username)

            if user and user["password"] == password:
                st.session_state.logged_in = True
                st.session_state.role = user["role"]
                st.session_state.username = username

                st.success(f"Logged in as {user['role']}")
                st.rerun()
            else:
                st.error("Invalid username or password")


def dashboard():
    st.title("AV Operations Dashboard")

    st.write(f"Logged in as: **{st.session_state.username}**")
    st.write(f"Role: **{st.session_state.role}**")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.role = None
        st.session_state.username = None
        st.rerun()

    inventory = pd.read_csv("data/av_equipment_inventory.csv")
    schedules = pd.read_csv("data/staff_shift_schedules.csv")

    st.subheader("AV Equipment Inventory")
    st.dataframe(inventory)

    st.subheader("Staff Shift Schedules")
    st.dataframe(schedules)

    st.subheader("Unified View")

    unified = schedules.merge(
        inventory,
        left_on="assigned_device_id",
        right_on="device_id",
        how="left",
    )

    st.dataframe(unified)

    st.subheader("Device Control")

    if st.session_state.role == "Manager":
        selected_device = st.selectbox(
            "Select device",
            inventory["device_id"],
        )

        selected_command = st.selectbox(
            "Select command",
            ["power_on", "power_off", "mute", "unmute"],
        )

        if st.button("Trigger Device Command"):
            payload = {
                "command": selected_command,
                "device": selected_device,
                "triggered_by": st.session_state.username,
                "timestamp": datetime.now().isoformat(),
            }

            st.success("Device command triggered")
            st.json(payload)

            with open("last_device_payload.json", "w") as file:
                json.dump(payload, file, indent=4)

    else:
        st.info("Technicians can view data but cannot trigger device commands.")


if not st.session_state.logged_in:
    login_page()
else:
    dashboard()