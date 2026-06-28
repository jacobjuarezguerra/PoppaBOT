"""
services/leveling.py — Servicio de niveles y experiencia
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Calcula XP, niveles y rankings.
"""

import math
from utils.logger import get_logger

log = get_logger("services.leveling")


class LevelingService:
    """Lógica de niveles — sin dependencias de Discord."""

    XP_PER_MESSAGE = 15
    XP_COOLDOWN_SECONDS = 60
    BASE_XP = 100
    XP_MULTIPLIER = 1.5

    def xp_for_level(self, level: int) -> int:
        """XP total necesaria para alcanzar un nivel."""
        return int(self.BASE_XP * (self.XP_MULTIPLIER ** (level - 1)))

    def calculate_level(self, total_xp: int) -> tuple[int, int, int]:
        """
        Calcula el nivel actual dado el XP total.
        Retorna: (nivel, xp_actual, xp_siguiente_nivel)
        """
        level = 1
        while total_xp >= self.xp_for_level(level + 1):
            total_xp -= self.xp_for_level(level)
            level += 1

        if total_xp < 0:
            total_xp = 0

        return level, total_xp, self.xp_for_level(level + 1)

    def get_progress(self, current_xp: int, needed_xp: int) -> float:
        """Progreso hacia el siguiente nivel (0.0 - 1.0)."""
        if needed_xp <= 0:
            return 1.0
        return min(current_xp / needed_xp, 1.0)


# Singleton
leveling_service = LevelingService()
