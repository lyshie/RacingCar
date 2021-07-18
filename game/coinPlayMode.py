from games.RacingCar.game.coin import Coin
from .car import *
from .highway import *
from .gameMode import GameMode
from .env import *
import pygame
import random
# TODO something

<<<<<<< HEAD
class CoinMode(GameMode):
    def __init__(self, user_num: int, sound_controller):
        super(CoinMode, self).__init__()
        self.frame = 0
        pygame.font.init()
=======
class CoinPlayingMode(PlayingMode):
    def __init__(self, user_num):
        super(CoinPlayingMode, self).__init__(user_num)
        self.creat_coin_time = pygame.time.get_ticks()
        self.coins = pygame.sprite.Group()
>>>>>>> fa34c7aa43c18c14874846de3b044d39d00db5f2

        '''set groups'''
        self.users = pygame.sprite.Group()
        self.cars = pygame.sprite.Group()
        self.computerCars = pygame.sprite.Group()
        self.lanes = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.camera = Camera()
        '''sound'''
        self.sound_controller = sound_controller

        '''image'''
        self.bg_image = pygame.image.load(path.join(IMAGE_DIR, BACKGROUND_IMAGE[0])).convert()
        self.rank_image = pygame.image.load(path.join(IMAGE_DIR, RANKING_IMAGE[1])).convert_alpha()

        self.cars_info = []
        self.user_distance = []
        self.maxVel = 0
        self._init_lanes()
        # user數量
        for user in range(user_num):
            self._init_user(user)
        self.eliminated_user = []
        self.winner = []
        '''
        status incloud "START"、"RUNNING"、"END"
        '''
        self.status = "START"
        if user_num == 1:
            self.is_single = True
        else:
            self.is_single = False
        self.line = Line()
        self.background_x = 0
        self.bg_x = 0
        self.rel_x = 0
        self.lanes.add(self.line)
        self.end = False
        self.creat_coin_frame = 0
        self.end_frame = 0
        self.coin_lanes = [125, 175, 225, 275, 325, 375, 425, 475, 525]
        self.car_lanes = [110, 160, 210, 260, 310, 360, 410, 460, 510]

    def update_sprite(self, command):
        '''update the model of game,call this fuction per frame'''
        self.frame += 1
        self.handle_event()
        self._revise_speed()

        if self.status == "START" and self.frame > FPS:
            self.status = "RUNNING"
            pass
        if self.status == "RUNNING":
            if self.frame > FPS*4:
                self._creat_computercar()
            if self.is_creat_coin():
                self.creat_coins()
            self.user_distance = []
            self.coin_num = []

            self.cars_info = []
            self.camera.update(self.maxVel)

            '''update sprite'''
            self.line.update()
            self.lanes.update(self.camera.position)
            self.line.rect.left = self.line.distance - self.camera.position +500
            self.coins.update()
            self.computerCars.update(self.cars)
            # self.background.update()

            for car in self.users:
                # self.user_out__screen(car)
                self.user_distance.append(car.distance)
                self.coin_num.append(car.coin_num)
                car.update(command["ml_" + str(car.car_no+1) + "P"])

            for car in self.cars:
                '''偵測車子的狀態'''
                self._detect_car_status(car)
                self.cars_info.append(car.get_info())

                '''更新車子位置'''
                car.rect.left = car.distance - self.camera.position + 500

            self._is_game_end()

        elif self.status == "END" and self.close == False:
            self.rank()
            self._print_result()
            self.close = True
            self.end_frame = self.frame
            pass
        else:
            if self.frame - self.end_frame > FPS:
                self.running = False
            pass

<<<<<<< HEAD
    def detect_collision(self):
        super(CoinMode,self).detect_collision()
        for car in self.cars:
            self.cars.remove(car)
            hits = pygame.sprite.spritecollide(car, self.cars, False)
            for hit in hits:
                if hit.status:
                    self.sound_controller.play_hit_sound()
                hit.status = False
                car.status = False
            self.cars.add(car)
        for car in self.users:
            hits = pygame.sprite.spritecollide(car, self.coins, True)
            for hit in hits:
                self.sound_controller.play_coin_sound()
                car.coin_num += 1
            pass

    # def user_out__screen(self,car):
    #     if car.status:
    #             if car.rect.right < -100 or car.rect.bottom > 550 or car.rect.top < 100:
    #                 self.sound_controller.play_lose_sound()
    #                 car.status = False

    def _print_result(self):
        tem = []
        for user in self.winner:
            tem.append({"Player":str(user.car_no + 1) + "P",
                   "Coin":str(user.coin_num),
                   "Distance":str(round(user.distance))+"m",
                   })
            print({"Player":str(user.car_no + 1) + "P",
                   "Coin":str(user.coin_num),
                   "Distance":str(round(user.distance))+"m",
                   })
        self.winner = tem
=======
        for car in self.user_cars:
            car.update(command[car.car_no])
            self.collide_coins(car)
>>>>>>> fa34c7aa43c18c14874846de3b044d39d00db5f2

    def _init_user(self, user_no: int):
        self.car = UserCar((user_no)*100+160 , 0,user_no)
        self.users.add(self.car)
        self.cars.add(self.car)
        return None

    def _init_lanes(self):
        for i in range(8):
            for j in range(23):
                self.lane = Lane(i * 50+150, j * 50-150)
                self.lanes.add(self.lane)

    def _detect_car_status(self, car):
        if car.status:
            pass
        else:
            car.velocity = 0
            if car in self.users:
                car.image = car.image_list[1]
                if car not in self.eliminated_user:
                    self.eliminated_user.append(car)
            else:
                car.image = car.image_list[1]

                # car.rect = car.image.get_rect()

    def _is_game_end(self):
        if len(self.eliminated_user) == len(self.users):
            self.status = "END"
        if self.frame > FPS*57:
            self.status = "END"
        for car in self.users:
            if car.distance >= finish_line:
                self.status = "END"

    def _revise_speed(self):
        self.user_vel = []
        for car in self.users:
            self.user_vel.append(car.velocity)
        self.maxVel = max(self.user_vel)

    def draw_bg(self):
        '''show the background and imformation on screen,call this fuction per frame'''
        super(CoinMode, self).draw_bg()
        self.rel_x = self.background_x % self.bg_image.get_rect().width
        self.bg_x = self.rel_x - self.bg_image.get_rect().width
        self.bg_img.blit(self.bg_image,(self.bg_x,0))
        if self.rel_x <= WIDTH:
            self.bg_img.blit(self.bg_image, (self.rel_x, 0))
        self.background_x -= self.maxVel

        self.bg_img.blit(self.rank_image,(WIDTH-315, 5))

        '''畫出每台車子的資訊'''
        self._draw_user_imformation()
        '''顯示玩家金幣數'''
        for user in self.users:
            self.draw_information(self.screen,str(user.coin_num), 17, 740+user.car_no*78,45)

        self.all_sprites.draw(self.screen)
        self.users.draw(self.screen)

    def drawAllSprites(self):
        '''show all cars and lanes on screen,call this fuction per frame'''
        super(CoinMode,self).drawAllSprites()
        self.lanes.draw(self.screen)
        self.cars.draw(self.screen)

    def _creat_computercar(self):
        if len(self.cars) < cars_num:
                x = random.choice([650,-700])
                y = random.choice(self.car_lanes)
                self.computerCar = ComputerCar(y,self.camera.position+x,x+500)
                self.computerCars.add(self.computerCar)
                self.cars.add(self.computerCar)
                self.car_lanes.remove(y)
        if len(self.car_lanes) == 0:
            self.car_lanes = [110, 160, 210, 260, 310, 360, 410, 460, 510]

    def _draw_user_imformation(self):
        '''全縮圖'''
        pygame.draw.rect(self.screen,BLACK,pygame.Rect(0,650,1000,50))
        for user in self.users:
            pygame.draw.circle(self.screen,USER_COLOR[user.car_no],
                               (round(user.distance*(1000/finish_line)),650+round(user.rect.top*(50/500))),4)
            if user.status == False:
                if user.car_no > 1:
                    pygame.draw.line(self.screen,RED,(700 + user.car_no*75,20),(700 + user.car_no*75 +20,70),2)
                    pygame.draw.line(self.screen, RED, (720 + user.car_no * 75, 20), (720 + user.car_no * 75 - 20, 70), 2)

                elif user.car_no <= 1:
                    pygame.draw.line(self.screen,RED,(700 + user.car_no*70,20),(700 + user.car_no*70 +20,70),2)
                    pygame.draw.line(self.screen, RED, (720 + user.car_no * 75, 20), (720 + user.car_no * 70 - 20, 70), 2)

<<<<<<< HEAD
    def rank(self):
        user_value = []
        for car in self.users:
            user_value.append(car.coin_num * 100000 + car.distance)
        while len(self.eliminated_user) != 0:
            for car in self.eliminated_user:
                car_value = car.coin_num * 100000 + car.distance
                if car_value == max(user_value):
                    self.winner.append(car)
                    user_value.remove(car_value)
                    self.eliminated_user.remove(car)

    def creat_coins(self):
        if self.frame - self.creat_coin_frame > FPS*2:
            coin = Coin(WIDTH,random.choice(self.coin_lanes))
            self.coin_lanes.remove(coin.rect.centery)
            self.all_sprites.add(coin)
            self.coins.add(coin)
            self.creat_coin_frame = self.frame
        if len(self.coin_lanes) == 0:
            self.coin_lanes = [125, 175, 225, 275, 325, 375, 425, 475, 525]
        else:
            pass

    def is_creat_coin(self):
        if self.maxVel >= 11:
            return True
        else:
            return False
=======
        for car in self.cars:
            '''碰撞偵測'''
            self.collide_with_cars(car)
            '''偵測車子的狀態'''
            self.detect_car_state(car)
            self.cars_info.append(car.get_info())

            '''更新車子位置'''
            car.rect.centery += self.camera_vel - car.velocity

        if len(self.user_cars) == 0:
            self.print_result()
            self.running = False
            self.status = "GAMEOVER"

    def creat_coins(self):
        if pygame.time.get_ticks() - self.creat_coin_time > 5000:
            coin = Coin(random.choice(self.lane_center), 0)
            self.all_sprites.add(coin)
            self.coins.add(coin)
            self.creat_coin_time = pygame.time.get_ticks()
        pass

    def collide_coins(self,car):
        hits = pygame.sprite.spritecollide(car, self.coins, True)
        for hit in hits:
            car.coin_num += 1
        pass

    def is_car_arrive_end(self, car):
        if car.distance > self.end_line:
            user_coins = []
            for user in self.user_cars:
                user_coins.append(user.coin_num)
            for user in self.user_cars:
                if user.coin_num == min(user_coins):
                    user_coins.remove(user.coin_num)
                    user.state = False
                    self.detect_car_state(user)

    def draw_user_imformation(self):
        for car in self.user_cars:
            self.draw_information(self.screen, "Player" + str(car.car_no+1) + "("+user_image[4][car.car_no]+")", 17, 510, (car.car_no) * 120 + 10)
            self.draw_information(self.screen, "vel : " + str(round(car.velocity, 2)), 17, 510,
                                  (car.car_no) * 120 + 40)
            self.draw_information(self.screen, "distance : " + str(abs(round(car.distance, 2))), 17, 510,
                                  (car.car_no) * 120 + 70)
            self.draw_information(self.screen, "coins : " + str(car.coin_num), 17, 510,
                                  (car.car_no) * 120 + 100)
>>>>>>> fa34c7aa43c18c14874846de3b044d39d00db5f2
