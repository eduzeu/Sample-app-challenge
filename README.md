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