import sys
import pygame as pg
import random

WIDTH, HEIGHT = 1600, 900

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    tmr = 0

    # 爆弾の初期位置と速度を設定
    bomb_radius = 10
    bomb_color = (255, 0, 0)
    bomb_x = random.randint(bomb_radius, WIDTH - bomb_radius)
    bomb_y = random.randint(bomb_radius, HEIGHT - bomb_radius)
    bomb_vx = 5
    bomb_vy = 5

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 背景とキャラクターの描画
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])

        # 爆弾の描画
        bomb_surface = pg.Surface((2 * bomb_radius, 2 * bomb_radius), pg.SRCALPHA)
        pg.draw.circle(bomb_surface, bomb_color, (bomb_radius, bomb_radius), bomb_radius)
        screen.blit(bomb_surface, (bomb_x - bomb_radius, bomb_y - bomb_radius))

        # 爆弾の位置を更新
        bomb_x += bomb_vx
        bomb_y += bomb_vy

        # 画面端で反対側に移動させる
        if bomb_x < -bomb_radius:
            bomb_x = WIDTH + bomb_radius
        elif bomb_x > WIDTH + bomb_radius:
            bomb_x = -bomb_radius
        if bomb_y < -bomb_radius:
            bomb_y = HEIGHT + bomb_radius
        elif bomb_y > HEIGHT + bomb_radius:
            bomb_y = -bomb_radius

        pg.display.update()
        tmr += 1
        clock.tick(50)  # FPSを50に設定

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
