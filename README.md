# Cloud and API Automation Developer Challenge
### Eduardo Hernandez | Incoming M.S. Computer Science Student, NYU Tandon (Class of 2028)

## Overview

This application is a prototype AV Operations Dashboard built in Python using Streamlit. The application demonstrates:

- Integration of two separate spreadsheet data sources
- Data manipulation and visualization
- Role-Based Access Control (RBAC)
- JSON-based device command generation

The system simulates a real-world AV management platform where staff schedules and equipment inventory are managed from a single interface.

---

# Running the Application

### Prerequisites

- Python 3.11 or newer
- Streamlit
- Pandas

### Install Dependencies

```bash
pip install streamlit pandas
```

### Start the Application

## 1. Clone the Repository

```bash
git clone https://github.com/eduzeu/Sample-app-challenge.git
cd Sample-app-challenge
```

Alternatively, you can download the repository as a ZIP file:

1. Open: https://github.com/eduzeu/Sample-app-challenge
2. Click the green **Code** button.
3. Select **Download ZIP**.
4. Extract the folder and open it in your preferred IDE.


```bash
streamlit run app.py
```

If the `streamlit` command is not recognized, run:

```bash
python -m streamlit run app.py
```

# Testing the Roles

## Technician Account

```text
Username: technician
Password: technicianAccess
```

Permissions:

- View AV Equipment Inventory
- View Staff Shift Schedules
- View the Unified Dashboard
- Cannot trigger device commands

Expected behavior:

- The **Device Control** section will display an informational message indicating that technicians cannot trigger commands.

---

## Manager Account

```text
Username: manager
Password: managerAccess
```

Permissions:

- View all dashboard data
- Access the Device Control section
- Trigger simulated device commands
- Generate JSON control payloads

Expected behavior:

- Device selection and command selection controls become available.
- Clicking **Trigger Device Command** generates a JSON payload and displays it on the page.

---

# Triggering a Device Command

1. Login using the **Manager** account.
2. Navigate to the **Device Control** section.
3. Select an AV device.
4. Select a command:

- `power_on`
- `power_off`
- `mute`
- `unmute`

5. Click **Trigger Device Command**.

---

# Viewing the Generated JSON Payload

After triggering a command, the JSON payload can be viewed in two places:

### 1. Inside the Streamlit Dashboard

The payload is displayed directly on the page.

Example:

```json
{
  "command": "power_on",
  "device": "projector_1",
  "triggered_by": "manager",
  "timestamp": "2026-07-02T12:35:20"
}
```

### 2. Local Output File

The latest generated payload is automatically saved to:

```text
last_device_payload.json
```

This file is created in the project's root directory and can be opened with any text editor.