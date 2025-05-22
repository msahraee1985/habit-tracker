# 🧠 Habit Tracker CLI App

A bilingual (English/Persian) command-line application to help users track daily and weekly habits.  
Built with Python — featuring clean code, custom iterators, persistent JSON storage, and PyTest-powered unit tests.

---

## 🚀 Features

- Add, edit, delete habits (daily or weekly)
- Mark habits as completed
- View streaks (current & max)
- English / Persian language support
- JSON-based data persistence
- Custom iterator for habits
- Decorators to log execution time
- Over 85% test coverage

---

## 🧪 Run Tests

Install the dependencies:

```bash
pip install -r requirements.txt

pytest

To check test coverage:
coverage run -m pytest
coverage report
coverage html  # open htmlcov/index.html in your browser

🛠️ Project Structure
habit-tracker/
├── habit_tracker/
│   ├── models/             # Habit and Tracker classes
│   ├── utils/              # Decorators, iterators, validators, etc.
│   ├── tests/              # PyTest-based unit tests
│   ├── data/               # JSON file is saved here
│   ├── main.py             # CLI entry point
├── requirements.txt
├── README.md


▶️ How to Run
Make sure you're in the root of the project and your virtual environment is activated:
python habit_tracker/main.py


👨‍💻 Developer Notes
This project was developed as an educational exercise in best practices:

Clean code with comments and translation

Structured CLI interaction

Test-driven development with PyTest

Use of Iterators and Decorators

Modular design (separate files for models, utils, and tests)

Coverage tracking with coverage.py

🎓 Author
👑 Mehrdad ranjbar (Project Lead)
🤖 Assistant: ChatGPT (coding partner & coffee-powered co-pilot) 😄
