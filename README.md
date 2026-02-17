# BBT.HTI.508 Health Software Development Project
This repository contains the project implementation for a university course Health Software Development Project. 
The project software is a simplified standalone programme that provides an interface for healthcare professionals to get
an overview of the patient's condition relating to blood pressure values. This project will use provided private 
FHIR-based database to simulate blood pressure monitor data. The purpose of this project is to learn about health care 
systems, related standardisations and regulations.

# Project Setup
Requirements:
- Python 3.12 (recommended)

Installation:

1. Clone the repository:
   ```
    git clone <repo-url>
    cd bbt.hti.508-teambloodpressure
    ```
   
2. Create a virtual environment and activate it:
    ```
    python -m venv .venv
    .venv\Scripts\activate.bat
    ```
   
3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Put the local JSON-database file "json_database.json" in the project to location:
    ```
    bbt.hti.508-teambloodpressure\app\database\
    ```

# Remember To

1. ```Git pull``` the latest changes from the repository before starting to work on the project to avoid merge conflicts.
2. ```Git status``` to check which files have been changed and need to be committed.
2. ```Git add <file>```  your changes.
3. ```Git commit -m "message"``` your changes with a descriptive message.
4. ```Git push``` your changes to the repository at the end of the day.

