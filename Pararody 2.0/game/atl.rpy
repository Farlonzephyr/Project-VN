transform hover_main_menu (yoff, hehe):
    subpixel True
    alpha 0 xoffset 75
    pause hehe
    ease 0.7 alpha 1 xoffset 0

    on idle:
        ease 0.25 yoffset 0 xoffset 0 alpha 1
    on hover:
        yoffset yoff xoffset yoff alpha 1
        pause 0.5
        ease 0.25 yoffset yoff xoffset yoff alpha 0
        repeat

transform hover_quit(cekker):
    subpixel True
    alpha 0
    on idle:
        ease 0.25 alpha cekker yoffset 0 xoffset 0 
    on hover:
        alpha 1 yoffset -3 xoffset -3
        pause 0.5
        ease 0.25 yoffset -3 xoffset-3 alpha 0
        repeat