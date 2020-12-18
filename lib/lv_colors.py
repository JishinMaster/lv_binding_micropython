import lvgl as lv
def LV_COLOR_MAKE(r,g,b):
#    return lv.color_hex(r<<16| g<<8 |b)
    return lv.color_make(r,g,b)

class lv_colors:
    WHITE=LV_COLOR_MAKE(0xFF, 0xFF, 0xFF)
    SILVER=LV_COLOR_MAKE(0xC0, 0xC0, 0xC0)
    GRAY=LV_COLOR_MAKE(0x80, 0x80, 0x80)
    BLACK=LV_COLOR_MAKE(0x00, 0x00, 0x00)
    RED=LV_COLOR_MAKE(0xFF, 0x00, 0x00)
    MAROON=LV_COLOR_MAKE(0x80, 0x00, 0x00)
    YELLOW=LV_COLOR_MAKE(0xFF, 0xFF, 0x00)
    OLIVE=LV_COLOR_MAKE(0x80, 0x80, 0x00)
    LIME=LV_COLOR_MAKE(0x00, 0xFF, 0x00)
    GREEN=LV_COLOR_MAKE(0x00, 0x80, 0x00)
    CYAN=LV_COLOR_MAKE(0x00, 0xFF, 0xFF)
    AQUA=CYAN
    TEAL=LV_COLOR_MAKE(0x00, 0x80, 0x80)
    BLUE=LV_COLOR_MAKE(0x00, 0x00, 0xFF)
    NAVY=LV_COLOR_MAKE(0x00, 0x00, 0x80)
    MAGENTA=LV_COLOR_MAKE(0xFF, 0x00, 0xFF)
    PURPLE=LV_COLOR_MAKE(0x80, 0x00, 0x80)
    ORANGE=LV_COLOR_MAKE(0xFF, 0xA5, 0x00)
