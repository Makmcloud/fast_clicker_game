from dataclasses import dataclass


@dataclass
class Settings:
    scr_width: int = 500
    scr_height: int = 500
    bg_color: tuple = (105, 245, 255)
    game_name: str = 'Fast clicker'
    fps: int = 20
    amount_rects: int = 4
    amount_borders: int = 4
    click_text: str = 'CLICK!'
    right_click_color = 'green'
    bad_click_color = 'red'