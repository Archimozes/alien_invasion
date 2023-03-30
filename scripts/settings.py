class Settings():
    def __init__(self):
        # Настройка окна
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        
        # Настройка скорости корабля
        self.speed_ship_factor = 1

        # Настройка снаряда
        self.bullet_speed_factor = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Настройки пришельцев
        self.alien_speed_factor = .2
        self.fleet_drop_speed = 10

        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
