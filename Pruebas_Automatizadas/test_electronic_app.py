import pytest
from ElectronicApp import LoginApp, Database
from unittest.mock import MagicMock

@pytest.fixture
def app():
    app = LoginApp()
    return app

@pytest.fixture
def db():
    return Database()

# Prueba de registro de usuario
def test_register_user(db):
    db.add_user = MagicMock(return_value=True)
    assert db.add_user("testuser", "password123") is True

def test_register_existing_user(db):
    db.add_user = MagicMock(return_value=False)
    assert db.add_user("existinguser", "password123") is False

# Prueba de inicio de sesión
def test_login_success(db):
    db.verify_user = MagicMock(return_value=True)
    assert db.verify_user("testuser", "password123") is True

def test_login_failure(db):
    db.verify_user = MagicMock(return_value=False)
    assert db.verify_user("wronguser", "wrongpassword") is False

# Prueba de guardar notas
def test_save_note_success(db):
    db.add_note = MagicMock()
    db.add_note("testuser", "Nota de prueba")
    db.add_note.assert_called_once_with("testuser", "Nota de prueba")

def test_get_notes(db):
    db.get_notes = MagicMock(return_value=[("1", "testuser", "Nota de prueba", "2025-02-16")])
    notes = db.get_notes("testuser")
    assert len(notes) == 1
    assert notes[0][2] == "Nota de prueba"


