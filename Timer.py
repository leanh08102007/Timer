import pygame
import time
import math
pygame.init()
screen=pygame.display.set_mode((500,600))
pygame.display.set_caption('Timer')
GRAY=(64, 64, 71)
BLUE=(0,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
WHITE=(255,255,255)
font1=pygame.font.SysFont('sans',50)
font2=pygame.font.SysFont('sans',80)
a1=font1.render('+',True,BLACK)
a2=font1.render('-',True,BLACK)
a3=font1.render('Min',True,WHITE)
a4=font1.render('Sec',True,WHITE)
a5=font1.render('Start',True,BLACK)
a6=font1.render('Reset',True,BLACK)
clock=pygame.time.Clock()
mins=0
secs=0
total_secs=0
total=0
start=False
sound1=pygame.mixer.Sound('tick.wav')	#Tạo tiếng đồng hồ khi chạy
sound2=pygame.mixer.Sound('timeout.wav')	#Tạo tiếng khi hết giờ
running=True
while running:
	clock.tick(60)
	screen.fill(GRAY)
	mouse_x, mouse_y=pygame.mouse.get_pos()	#pos là viết tắt của position
	#Vẽ hình chữ nhật
	pygame.draw.rect(screen,BLUE,(100,50,50,50))	
	pygame.draw.rect(screen,BLUE,(100,130,50,50))	
	pygame.draw.rect(screen,BLUE,(350,50,50,50))	
	pygame.draw.rect(screen,BLUE,(350,130,50,50))	
	pygame.draw.rect(screen,BLUE,(50,200,170,50))	
	pygame.draw.rect(screen,BLUE,(280,200,170,50))	
	pygame.draw.rect(screen,BLACK,(45,495,410,60))	
	pygame.draw.rect(screen,WHITE,(50,500,400,50))	
	#Vẽ Min
	screen.blit(a3,(10,45))
	screen.blit(a3,(420,45))
	#Vẽ Sec
	screen.blit(a4,(10,125))
	screen.blit(a4,(420,125))
	#Dấu cộng
	screen.blit(a1,(113,45))
	screen.blit(a1,(113,125))
	#Dấu trừ
	screen.blit(a2,(368,45))
	screen.blit(a2,(368,125))
	#Chữ Start, Reset
	screen.blit(a5,(90,195))
	screen.blit(a6,(310,195))
	#Vẽ đồng hồ
	pygame.draw.circle(screen,BLACK,(250,380),100)
	pygame.draw.circle(screen,WHITE,(250,380),95)
	pygame.draw.circle(screen,BLACK,(250,380),5)

	#Nút start
	if start:
		if total_secs>0:
			total_secs-=1
			pygame.mixer.Sound.play(sound1)	#Chạy file âm thanh
			time.sleep(1)
		else:
			pygame.mixer.Sound.play(sound2)	#Chạy file âm thanh
			start=False
	#Vẽ thời gian
	mins=total_secs//60
	secs=total_secs- mins*60
	text_time=font2.render(str(mins)+':'+str(secs), True, RED)
	screen.blit(text_time,(175,70))
	#Vẽ kim giây chạy
	x_sec=250+90*math.sin(6*secs*math.pi/180)
	y_sec=380-90*math.cos(6*secs*math.pi/180)
	pygame.draw.line(screen, BLACK, (250,380),(int(x_sec),int(y_sec)),3)
	#Vẽ kim phút chạy
	x_min=250+50*math.sin(6*mins*math.pi/180)
	y_min=380-50*math.cos(6*mins*math.pi/180)
	pygame.draw.line(screen, BLACK, (250,380),(int(x_min),int(y_min)),4)
	#Hình chữ nhật đỏ
	if total!=0:
		pygame.draw.rect(screen, RED, (50,500,int(400*(total_secs/total)),50))

	
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
		if event.type==pygame.MOUSEBUTTONDOWN:	#Khi ta nhận chuột xuống
			if event.button==1:	#Khi ta nhấn chuột trái
				if 100<mouse_x<150 and 50<mouse_y<100:
					total_secs+=60
					total=total_secs
				if 100<mouse_x<150 and 130<mouse_y<180:
					total_secs+=1
					total=total_secs
				if 350<mouse_x<400 and 50<mouse_y<100:
					total_secs-=60
					total=total_secs
				if 350<mouse_x<400 and 130<mouse_y<180:
					total_secs-=1
					total=total_secs
				if 50<mouse_x<220 and 200<mouse_y<250:
					start=True
					total=total_secs
				if 280<mouse_x<450 and 200<mouse_y<250:
					total_secs=0

	pygame.display.flip()

pygame.quit()