import pygame
import sys # oyun penceresini sorunsuz kapatmak için kullanıyoruz


# OYUN PENCERESİ
pygame.init() # pygame modülünün çalışmasını sağlıyor
clock = pygame.time.Clock() # oyunun bir saniyedeki kare sayısını ayarlıyorua FPS
genislik = 800
yukseklik = 600
pencere = pygame.display.set_mode((genislik,yukseklik)) # oyun penceresinin boyutu
pygame.display.set_caption("Ping Pong Oyunu") # oyunun başlığı


# RENKLER
beyaz = (255,255,255) # hepsi 255 olursa beyaz
siyah = (0,0,0)       # hepsi 0 olursa siyah

# ŞEKİLLER
# yükseklik / 2 ekranın ortasında
raket1 = pygame.Rect(750,yukseklik/2-50,20,100) # iki dikdörtgen çizmnek için x konumu y konumu genizlik ve yükselik veriliyor
raket2 = pygame.Rect(30,yukseklik/2-50,20,100) # iki dikdörtgen çizmnek için x konumu y konumu genizlik ve yükselik veriliyor
top = pygame.Rect(genislik/2-10,yukseklik/2-10,20,20)

raket1_hiz = 0
raket2_hiz = 0
top_hiz_x = 5
top_hiz_y = 5

# SKOR
skor1 = 0
skor2 = 0
font = pygame.font.Font(None,50)

# OYUN DÖNGÜSÜ
# penceremizi sürekli günceleyebilmek için
while True:
    # pencerenin kullanıcıdan aldığı bilgiye göre kapatma islemi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                raket1_hiz += 7
            if event.key == pygame.K_UP:
                raket1_hiz -= 7
            if event.key == pygame.K_s:
                raket2_hiz += 7
            if event.key == pygame.K_w:
                raket2_hiz -= 7
        if event.type == pygame.KEYUP:
            raket1_hiz = 0
            raket2_hiz = 0

    if top.left <= 0:
        top_hiz_x *=-1
        top.center = (genislik/2,yukseklik/2)
        skor2 +=1

    if top.right >= genislik:
        top_hiz_x *=-1
        top.center = (genislik/2,yukseklik/2)
        skor1 +=1

    if top.colliderect(raket1) or top.colliderect(raket2):
        top_hiz_x *= -1

    if top.top <= 0 or top.bottom >= yukseklik:
        top_hiz_y *= -1

    if raket1.top <=0:
        raket1.top=0
    if raket1.bottom >=yukseklik:
        raket1.bottom = yukseklik

    if raket2.top <=0:
        raket2.top=0
    if raket2.bottom >=yukseklik:
        raket2.bottom = yukseklik

    raket1.y += raket1_hiz
    raket2.y += raket2_hiz
    top.x += top_hiz_x
    top.y += top_hiz_y
    pencere.fill(siyah)
    pygame.draw.rect(pencere, beyaz, raket1)
    pygame.draw.rect(pencere, beyaz, raket2)
    pygame.draw.ellipse(pencere,beyaz,top)

    skor_yazisi = font.render(f"1. Oyuncu {skor1} /  2. Oyuncu {skor2}",False,beyaz)
    pencere.blit(skor_yazisi,(167,20))

    clock.tick(60) # saniyede 60 kare gösterilecek FPS
    pygame.display.update() # pencereyi sürekli güncelliyoruz


