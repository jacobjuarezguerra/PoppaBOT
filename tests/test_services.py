"""
tests/test_services.py — Tests de los servicios (sin Discord)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Se pueden ejecutar sin un bot:  pytest tests/
"""

from services.greeting import GreetingService
from services.leveling import LevelingService


# ─── Tests: GreetingService ───

def test_greeting_default():
    svc = GreetingService()
    msg = svc.build_greeting("Ana", "Mi Servidor")
    assert "Ana" in msg
    assert "Mi Servidor" in msg


def test_greeting_custom():
    svc = GreetingService()
    msg = svc.build_greeting("Ana", "Mi Servidor", "Bienvenida {member}!")
    assert msg == "Bienvenida Ana!"


def test_farewell():
    svc = GreetingService()
    msg = svc.build_farewell("Ana", "Mi Servidor")
    assert "Ana" in msg


# ─── Tests: LevelingService ───

def test_xp_for_level():
    svc = LevelingService()
    xp = svc.xp_for_level(1)
    assert xp == 100


def test_calculate_level_start():
    svc = LevelingService()
    level, current, needed = svc.calculate_level(0)
    assert level == 1
    assert current == 0


def test_calculate_level_advance():
    svc = LevelingService()
    level, current, needed = svc.calculate_level(250)
    assert level > 1


def test_progress():
    svc = LevelingService()
    progress = svc.get_progress(50, 100)
    assert progress == 0.5
