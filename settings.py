class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 854
        self.screen_height = 480
        self.bg_color = (0, 3, 123)

        self.ship_speed = 1.5

        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (94, 251, 17)
        self.bullets_allowed = 3