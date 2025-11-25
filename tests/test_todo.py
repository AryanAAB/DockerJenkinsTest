import os
import json
from src.todo import add_task, load_data, save_data

def test_add_task():
    # Setup
    test_file = "todo_data.json"
    if os.path.exists(test_file):
        os.remove(test_file)

    add_task("Sample Task")

    data = load_data()
    assert len(data) == 1
    assert data[0]["task"] == "Sample Task"
    assert data[0]["done"] is False
