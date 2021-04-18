# coding_exercise

# Running the code localy

## Dependencies
- Python 3
- macOS used.

## Initial Setup

```bash
# Set up Python virtualenv
python3 -m <venv_name> <venv_path>

# Activate Python virtualenv
source <venv_path>/bin/activate

# Download/Update Python dependencies
pip3 install -r requirements.txt


# Inside coding_exercise/.env file, change DB details

## Running the application
```bash
# Switch to project's python virtualenv (if not already active)
. venv/bin/activate

# Update installed dependencies (if changed)
pip3 install -r requirements.txt

# Run the app
cd coding_exercise
python3 manage.py devserver
```