import pygame, sys

mouse_x, mouse_y = 0, 0
dmouse_x, dmouse_y = 0, 0
mouse_pressed, mouse_changed = False, False

screen = pygame.display.set_mode((600, 500))


def load(n):
    return pygame.image.load(n + ".png").convert_alpha()


t_file = load("file")
t_folder = load("folder")
t_fileinfo = load("filesize")
t_folderinfo1 = load("foldersize1")
t_folderinfo2 = load("foldersize2")
t_gfile = load("grabbed_file")

class FileItem:
    def __init__(self, folderin):
        self.folder = folderin
        self.pos = [50, 50]
        self.grabbed = False
        self.dead = False

    def update(self):
        if self.grabbed:
            self.pos[0] += dmouse_x
            self.pos[1] += dmouse_y
        if mouse_pressed and mouse_changed:
            self.grabbed = True
        elif not mouse_pressed and mouse_changed:
            self.dead = True
            self.folder.state = 1

    def draw(self):
        if not self.dead:
            if self.grabbed:
                screen.blit(t_gfile, self.pos)
            else:
                screen.blit(t_file, self.pos)
                if self.pos[0] + 50 > mouse_x > self.pos[0]:
                    if self.pos[1] + 50 > mouse_y > self.pos[1]:
                        screen.blit(t_fileinfo, (mouse_x, mouse_y))

class FolderItem:
    def __init__(self):
        self.pos = [300, 300]
        self.state = 0

    def draw(self):
        screen.blit(t_folder, self.pos)
        if self.pos[0] + 50 > mouse_x > self.pos[0]:
            if self.pos[1] + 50 > mouse_y > self.pos[1]:
                if self.state == 0:
                    screen.blit(t_folderinfo1, (mouse_x, mouse_y))
                else:
                    screen.blit(t_folderinfo2, (mouse_x, mouse_y))

folder = FolderItem()
file = FileItem(folder)

while True:
    prex, prey = mouse_x, mouse_y
    mouse_x, mouse_y = pygame.mouse.get_pos()
    dmouse_x, dmouse_y = mouse_x - prex, mouse_y - prey
    mouse_changed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True
            mouse_changed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False
            mouse_changed = True

    file.update()
    screen.fill(-1)
    folder.draw()
    file.draw()
    pygame.display.flip()
