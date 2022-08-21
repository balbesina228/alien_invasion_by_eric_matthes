class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 854
        self.screen_height = 480
        self.bg_color = (0, 3, 123)

        # Параметры снаряда
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (94, 251, 17)
        self.bullets_allowed = 3
        self.ship_limit = 3

        # Настройки пришельцев
        self.fleet_drop_speed = 10
        # fleet_direction = 1 means to the right; -1 means to the left
        self.fleet_direction = 1

        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Рост стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_speed = 1.0
        self.alien_points = 50

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)