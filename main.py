import Buttons
from imports import *

pygame.init()
Xres = 800
Yres = 600
prozor = pygame.display.set_mode((Xres, Yres))
sat = pygame.time.Clock()


def nacrtaj_dugme_bez_centiranja(dugme):
    pygame.draw.rect(prozor, dugme.boja, dugme.rect)
    prozor.blit(dugme.tekst, dugme.rect.topleft)  # lepsi nacin od linije dole, TOPLEFT je pozicija gornje leve tacke
    # prozor.blit(dugme.tekst, (dugme.rect.x, dugme.rect.y) )


def main_menu():
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                sys.exit()
            if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
                if Buttons.main_menu_dugme_quit.rect.collidepoint(dogadjaj.pos):
                    pygame.quit()
                    sys.exit()
                if Buttons.main_menu_dugme_credits.rect.collidepoint(dogadjaj.pos):
                    mycredits()
                if Buttons.main_menu_play_button.rect.collidepoint(dogadjaj.pos):
                    play()

        prozor.fill((pygame.Color("cyan")))
        nacrtaj_dugme_bez_centiranja(Buttons.main_menu_dugme_quit)
        nacrtaj_dugme_bez_centiranja(Buttons.main_menu_dugme_credits)
        nacrtaj_dugme_bez_centiranja(main_menu_play_button)
        pygame.display.flip()
        sat.tick(30)


def mycredits():
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                sys.exit()
            if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
                if Buttons.credits_to_main_menu_button.rect.collidepoint(dogadjaj.pos):
                    main_menu()
        prozor.fill((pygame.Color("cyan")))
        prozor.blit(credits_text_developer, (189, 132))
        prozor.blit(credits_text_teacher, (189, 242))
        prozor.blit(credits_consultant, (189, 359))
        nacrtaj_dugme_bez_centiranja(credits_to_main_menu_button)
        pygame.display.flip()
        sat.tick(30)


def play():
    upaljene_kontrole_misem = False
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                sys.exit()
            if dogadjaj.type == pygame.MOUSEBUTTONUP:
                upaljene_kontrole_misem = True
        dugmici = pygame.key.get_pressed()
        if dugmici[pygame.K_LEFT]:
            igrac.pravac += 7
        if dugmici[pygame.K_RIGHT]:
            igrac.pravac -= 7
        dugmici = pygame.mouse.get_pressed()
        if dugmici[0] and upaljene_kontrole_misem:
            xm, ym = pygame.mouse.get_pos()
            if xm < Xres // 2:
                igrac.pravac += 7
            else:
                igrac.pravac -= 7

        igrac.pozicija = igrac.pozicija + igrac.brzina.rotate(-igrac.pravac)
        prozor.fill((153, 0, 255))
        rotirana_slika = pygame.transform.rotate(igrac.slika, igrac.pravac)
        prozor.blit(rotirana_slika, igrac.pozicija - rotirana_slika.get_rect().center)
        pygame.display.flip()
        sat.tick(30)


main_menu()
pygame.quit()
