import pygame

class Button:
    def __init__(self, img, x, y, font_obj, text):
        self.img = img
        self.x = x
        self.y = y
        self.text = text
        self.rect = self.img.get_rect(center=(self.x, self.y))    # get_rect will return (topleft_coor, size_of_img_button)
        self.text = font_obj.render(self.text, True, "White")
        self.text_rect = self.text.get_rect(center=(self.x, self.y))

    def drawButton(self, surface):
        # print(self.rect.left, self.rect.right, self.rect.top, self.rect.bottom)
        # surface is the screen where we want to draw the object
        surface.blit(self.img, self.rect)
        surface.blit(self.text, self.text_rect)

    def checkPress(self, pos):
        # self.rect.top/bottom/left/right -> will give corresponding coordinates for the button
        horizontal_range = range(self.rect.left, self.rect.right)    # for checking the horizontal boundaries
        vertical_range = range(self.rect.top, self.rect.bottom)     # for checking the vertical boundaries
        if pos[0] in horizontal_range and pos[1] in vertical_range:
            return True