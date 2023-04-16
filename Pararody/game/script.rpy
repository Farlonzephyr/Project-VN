# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the

# dummy character to test screen with mc
#define dummy = Character("Dummy")

# name of the character.
#define mc = Character("Joko", image="mc")
define mc = Character("[mcname]", image="mc")
define oldmc = Character("???", image ="oldmc")
define aiko = Character("Aiko", image="aiko")
define sumi = Character("Sumi", image="sumi")

# berfungsi untuk mengatur jalan cerita
default kunci = 0
default gimang = 0
default ceknama = 0
default cekmati = 0
default cekrahasia = 0
default cekmati2 = 0
default darahboss = 1000
default darahmu = 100
default turn = 0
default seranganbiasa = 25
default seranganbulan = 55
default persistent.tamat = 0
default persistent.loop = 0
default cekulang = 0

#vport

screen vport:
    frame:
        background "bgblack"
        viewport:
            area (0,0,1980,1080)

            mousewheel True
            draggable True

            vbox:
                add "bgblack"
                add "bgblack"
                add "adawibu":
                    zoom 3
                textbutton "{b}pfff{/b}":
                    text_size 80
                    text_color "#ffffff"
                    text_hover_color "#f40505"
                    action Quit(confirm = False)

#pengaturan transform
transform terkenaserang:
    zoom 1.2
    xalign 0.5
    yalign 1.2
    block:
        ease 0.05 zoom 1.22
        yalign 1.21
        xalign 0.51
        ease 0.05 zoom 1.2
        yalign 1.2
        xalign 0.5
        repeat 2

transform hilang:
    linear .5 alpha 0.0

transform muncul:
    linear .5 alpha 0.5 

transform mati:
    parallel:
        ease 0.05 zoom 1.3
        xalign 0.51
        ease 0.05 zoom 1.2
        xalign 0.5
        repeat 
    parallel:
        ease 15 yoffset 7000

transform terkenaserang2:
    zoom 1.2
    xalign 0.5
    yalign 1.2
    block:
        ease 0.05 zoom 1.22
        yalign 1.21
        xalign 0.51
        alpha 0.0
        ease 0.05 zoom 1.2
        yalign 1.2
        xalign 0.5
        alpha 1
        repeat 2

image glitch:
    "bgglitch"
    pause 0.1
    "bg1"
    pause 0.5
    "bgglitch"
    pause 0.04
    "bg1"
    pause 0.3
    "bgglitch"
    pause 0.001
    "bg1"
    pause 0.04
    "bgglitch"
    pause 0.001
    "bg1"
    pause 0.04
    "bgglitch"
    pause 0.001
    "bg1"
    pause 0.1
    repeat

image glitch2:
    "bg2"
    pause 0.9
    "bg2error"
    pause 0.5
    "bg2"
    pause 0.7
    "bg2error"
    pause 0.01
    "bg2"
    pause 0.6
    "bg2error"
    pause 0.7
    "bg2"
    pause 0.65
    "bg2error"
    pause 0.53
    "bg2"
    pause 0.42
    "bg2error"
    pause 0.51
    "bg2"
    pause 0.52
    "bg2error"
    pause 0.53
    repeat

image serang2:
    zoom 0.5
    yalign 0.5
    "serangan2.1.gif"
    pause 0.1
    "serangan2.2.gif"
    pause 0.1
    "serangan2.3.gif"
    pause 0.1
    "serangan2.4.gif"
    pause 0.1
    "serangan2.5.gif"
    pause 0.1
    "serangan2.6.gif"
    pause 0.1
    "serangan2.7.gif"
    pause 0.1
    repeat

image serang1:
    zoom 0.5
    yalign 0.5
    "serangan1.1.gif"
    pause 0.1
    "serangan1.2.gif"
    pause 0.1
    "serangan1.3.gif"
    pause 0.1
    "serangan1.4.gif"
    pause 0.1
    "serangan1.5.gif"
    pause 0.1
    "serangan1.6.gif"
    pause 0.1
    repeat    

# screen
screen ending:
    text "{cps=1}Fin{/cps}":
        xalign 0.5
        yalign 0.5
        size 70

screen pilihan:
    frame:
        add "images/bg9.png":
            xsize 1920
            ysize 250
        xsize 1920
        ysize 250
        xpadding 0
        ypadding 0
        textbutton "Attack":
            xalign 0.3
            yalign 0.5
            text_size 80
            text_color "#000000"
            text_hover_color "#4d38a1"
            action Jump ("cobaserang")
        textbutton "Bantuan":
            xalign 0.7
            yalign 0.5
            text_size 80
            text_color "#000000"
            text_hover_color "#4d38a1"
            action Jump ("cobabantuan")

screen pilihserang:
    frame:
        add "images/bg9.png":
            xsize 1920
            ysize 250
        xsize 1920
        ysize 250
        xpadding 0
        ypadding 0
        textbutton "Serangan Biasa":
            xalign 0.1
            yalign 0.5
            text_size 80
            text_color "#ffffff"
            text_hover_color "#4d38a1"
            action Jump ("seranganbiasa")
        textbutton "Tebasan Bulan":
            xalign 0.9
            yalign 0.5
            text_size 80
            text_color "#ffffff"
            text_hover_color "#4d38a1"
            action Jump ("seranganbulan")
        textbutton "Kembali":
            xalign 0.5
            yalign 0.5
            text_size 80
            text_color "#ffffff"
            text_hover_color "#4d38a1"
            action Jump ("kembali")
        

screen pilihbantuan:
    frame:
        add "images/bg9.png":
            xsize 1920
            ysize 250
        xsize 1920
        ysize 250
        xpadding 0
        ypadding 0
        textbutton "Aiko":
            xalign 0.3
            yalign 0.5
            text_size 80
            text_color "#ffffff"
            text_hover_color "#4d38a1"
            action Jump ("pilihaiko")
        textbutton "Kembali":
            xalign 0.5
            yalign 0.5
            text_size 80
            text_color "#ffffff"
            text_hover_color "#4d38a1"
            action Jump ("kembali")
        if turn >= 10:
            textbutton "Sumi":
                xalign 0.7
                yalign 0.5
                text_size 80
                text_color "#ffffff"
                text_hover_color "#4d38a1"
                action Jump ("pilihsumi") 

screen aiko:
    frame:
        add "images/bg9.png":
            xsize 1920
            ysize 250
        xsize 1920
        ysize 250
        xpadding 0
        ypadding 0
        textbutton "Penyemangat!":
            xalign 0.1
            yalign 0.5
            text_size 80
            text_color "#ffffff"
            text_hover_color "#4d38a1"
            action Jump ("semangat")
        textbutton "Hadiah":
            xalign 0.85
            yalign 0.5
            text_size 80
            text_color "#ffffff"
            text_hover_color "#4d38a1"
            action Jump ("hadiah")
        textbutton "Kembali":
            xalign 0.55
            yalign 0.5
            text_size 80
            text_color "#ffffff"
            text_hover_color "#4d38a1"
            action Jump ("kembali")

screen sumi:
    frame:
        add "images/bg9.png":
            xsize 1920
            ysize 250
        xsize 1920
        ysize 250
        xpadding 0
        ypadding 0
        textbutton "Penghancur":
            xalign 0.3
            yalign 0.5
            text_size 80
            text_color "#ffffff"
            text_hover_color "#4d38a1"
            action Jump ("penghancur")
        textbutton "Kembali":
            xalign 0.7
            yalign 0.5
            text_size 80
            text_color "#ffffff"
            text_hover_color "#4d38a1"
            action Jump ("kembali")


screen ulang:
    frame:
        add "images/bg9.png":
            xsize 1920
            ysize 250
        xsize 1920
        ysize 250
        ypos 400
        xpadding 0
        ypadding 0
        textbutton "Menyerah":
            xalign 0.3
            yalign 0.5
            text_size 80
            text_color "#000000"
            text_hover_color "#4d38a1"
            action Quit(confirm = False)
        textbutton "Ulang":
            xalign 0.7
            yalign 0.5
            text_size 80
            text_color "#000000"
            text_hover_color "#4d38a1"
            action Jump ("fight")

screen cheat():
    textbutton "{b}Ending Rahasia{/b}":
        xalign 0.5
        yalign 0.7
        text_size 80
        text_color "#000000"
        text_hover_color "#000000"
        action Jump ("Maukemana")

screen rahasia():
    textbutton "{b}Warning{/b}":
        xalign 0.5
        yalign 0.7
        text_size 80
        text_color "#000000"
        text_hover_color "#000000"
        action Jump ("rahasia")

screen blood():
    add "images/blood.png" zoom 3.0 yalign 0.1

screen warning():
    vbox:
        text "Peringatan kamu memasuki daerah terlarang!!!" size 200
        yalign 0.2
        xalign 0.1
    vbox:
        text "Peringatan kamu memasuki daerah terlarang!!!"
        yalign 0.8
        xalign 0.6
    vbox:
        text "Peringatan kamu memasuki daerah terlarang!!!"
        yalign 0.3
        xalign 0.5
    vbox:
        text "Peringatan kamu memasuki daerah terlarang!!!"
        yalign 0.9
        xalign 0.6
    vbox:
        text "Peringatan kamu memasuki daerah terlarang!!!"
        yalign 0.4
        xalign 0.7
    vbox:
        text "Peringatan kamu memasuki daerah terlarang!!!"
        yalign 0.9
        xalign 1.0
    vbox:
        text "Peringatan kamu memasuki daerah terlarang!!!" size 50
        yalign 0.7
        xalign 1.8
    vbox:
        text "Peringatan kamu memasuki daerah terlarang!!!" size 150
        yalign 3.5
        xalign 1.0
    vbox:
        text "Peringatan kamu memasuki daerah terlarang!!!"
        yalign 0.65
        xalign 1.5
    vbox:
        text "Peringatan kamu memasuki daerah terlarang!!!" size 100
        yalign 0.6
        xalign 0.6
    vbox:
        text "Peringatan kamu memasuki daerah terlarang!!!" size 40
        yalign 0.55
        xalign 0.1
    text "Apakah kamu ingin melanjutkan?":
        xalign 0.58
        yalign 0.5
        size 50   
    textbutton "{b}Yes{/b}":
        xalign 0.5
        yalign 0.7
        text_size 40
        text_color "#ffffff"
        text_hover_color "#000000"
        action Jump ("kebenaran")

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #cek screen
    #show screen warning
    #show screen rahasia
    #show screen blood
    #show screen cheat
    #show screen ulang
    #show screen ending
    #untuk melihat battle
    #jump battle
    #jump fight

    #Nyalakan ini agar bisa langsung bermain
    #$persistent.loop = persistent.loop - 1
    #$persistent.tamat = 1

    hide screen hai

    if persistent.loop == 1:

        jump hitam

    #jump trueending

    stop music

    #show screen cheat

    centered "{alpha=0.5}Jangan bermain game ini kalo tidak mau di ciduk!{/alpha}"
    centered "{alpha=0.5}Jika kalian merasa terganggu atau lainnya segera tutup game ini!
    Halusinasi, ketakutan, gangguan mental bukan tanggunag jawab pihak kami{/alpha}"

    #play music 
    hide screen rahasia
    play music bg1 volume 0.1 fadein(2.0)

    scene bg1 with Fade (0.0, 1, 1.0)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    oldmc "{cps=2}...{/cps}"
        
    oldmc "{cps=20}Hoam... sudah pagi rupanya{/cps}"

    play sound door volume 0.1

    window hide
        
    pause 2.5

    window show

    oldmc "{cps=20}Hmmm??{/cps}"

    oldmc "{cps=20} Masuk!{/cps}"

    play sound door_open volume 0.1
        
    window hide

    show aiko base with fade:
        zoom 0.7
        xalign 0.1
        yalign 0.01
        
    pause 2.0

    window show

    aiko "{cps=20}Kamu sudah bangun?{/cps}"

    oldmc "{cps=20}Umm....{/cps}"

    oldmc "{cps=20}Kamu siapa?{/cps}"

    show aiko angry:
        zoom 0.7
        xalign 0.1
        yalign 0.01

    aiko "{cps=2}...{/cps}"

    #play music
    play music trouble volume 0.1

    show aiko angryblush:
        zoom 0.7
        xalign 0.1
        yalign 0.01

    aiko "{cps=20}Apa kamu lupa? Apa kepalamu mau ku jedotin?{/cps}"

    oldmc "{cps=20}Serius, aku gak tau apa apa!{/cps}"

    aiko "{cps=20}Bohong!{/cps}"

    oldmc "{cps=20}Seri-{/cps}"

    show aiko angryblush with fade:
        zoom 1.0
        xalign 0.5
        yalign 0.01

    aiko "{cps=20}B O H O N G!{/cps}" with vpunch

    aiko "{cps=20}Coba, emang nama mu siapa?{/cps}"

    $ mcname = renpy.input("{cps=20}Siapa namamu?{/cps}")

    $ mcname = mcname.strip()

    if mcname == "":
        $ mcname = "Ryuji"

    if mcname != "Ryuji":
        aiko "{cps=20}Namamu seharusnya Ryuji!{/cps}"
        jump loop 
    else:
        jump notloop

    return

# The game starts here.
label hitam:

    play music opening volume 0.1

    jump hitam2

    return

label hitam2:
    show bgblack

    pause

    $cekulang = cekulang + 1
    
    if cekulang == 10:

        jump bermainulang

    jump hitam

    return

label bermainulang:

    show bgblack

    show sumi base at muncul:
        zoom 0.7
        xalign 0.5
        yalign 0.01

    sumi "{cps=20}Hai....{/cps}"

    sumi "{cps=20}Apa kamu mau bermain sebuah game?{/cps}"

    sumi "{cps=20}Kalo kamu mau! Aku akan memberikan game itu{/cps}"

    menu:
        "Ya":

            sumi "{cps=20}Kau sudah menjawabnya{/cps}"

            sumi "{cps=20}Kontrak terpenuhi!{/cps}"

            sumi "{cps=20}Walaupun game ini tidak terlalu asik{/cps}"

            sumi "{cps=20}Selamat bermain!{/cps}"

            sumi "{cps=20}Aku akan menghapus ingatan mu agar permainan lebih menyenangkan...{/cps}"

            $persistent.loop = persistent.loop - 1

            $persistent.tamat = persistent.tamat -1

            show sumi at hilang

            jump start

        "Tidak":

            sumi "Baiklah"

            sumi "Sampai jumpa lagi!"

            $cekulang = 0

            show sumi at hilang

            jump hitam2
    return

label Maukemana:

    show screen vport

    window hide

    pause

    window show

    return


#loop pertama setelah start
label start2:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    hide screen rahasia
    scene bg1
    play music bg1 volume 0.1 fadein(2.0)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    mc "{cps=2}...{/cps}"

    if gimang >= 1 and cekmati2 == 1:
        mc "Aiko!!!"
        mc "{cps=2}...{/cps}"
    elif gimang >= 2:
        mc "apakah itu hanyalah loop? lagi?"
    else:
        mc "{cps=20}Hoam... sudah pagi rupanya{/cps}"

    play sound door volume 0.1

    window hide
    
    pause 2.5

    window show
    if gimang >=1 and cekmati2 == 1:
        mc "Aiko? apa itu dia?"
    elif gimang <=5:
        mc "{cps=20}Hmmm?? sepertinya aku sudah melalui... ah sudahlah{/cps}"
    elif gimang > 5:
        mc "{cps=20}!!!{/cps}" with vpunch

        mc "{cps=20}Aku beneran berada dalam loop yang tidak berkesudahan!!!{/cps}"

        mc "{cps=20}Pasti sebentarlagi ada yang mengetuk pintu!{/cps}"

        if ceknama >= 1:
            mc "{cps=20}Itu pasti Aiko{/cps}"

    mc "{cps=20} Masuk!{/cps}"

    play sound door_open volume 0.1
    
    window hide

    show aiko base with fade:
        zoom 0.7
        xalign 0.1
        yalign 0.01

    pause 2.0

    window show

    aiko "{cps=20}Kamu sudah bangun?{/cps}"

    if ceknama == 0:
        mc "{cps=20}Umm....{/cps}"

        mc "{cps=20}Kamu siapa?{/cps}"
    elif ceknama >=1 and cekmati2 == 1:
        mc "{cps=20}Aiko!! kamu masih Hidup??{/cps}"
        show aiko angry:
            zoom 0.7
            xalign 0.1
            yalign 0.01
        aiko "{cps=20}kamu kenapa sih? apa maksud kamu?{/cps}"

        mc "{cps=20}ah.. enggak, enggak kenapa-kenapa. aku bersyukur itu hanya mimpi!{/cps}" 

        scene glitch with Pixellate(2, 64)

        show aiko angry:
            zoom 0.7
            xalign 0.1
            yalign 0.01

        aiko "{cps=20}!!!{/cps}"

        aiko "{cps=20}apa yang....{/cps}"

        $cekmati2 = cekmati2 - 1

        hide aiko angry

        scene bgblack with fade

        show screen warning

        mc "{cps=20}!!!{/cps}"

        $gimang = gimang + 1

        jump start2
    else:
        mc "Selamat pagi, Aiko!"
        jump notloop

    show aiko angry:
        zoom 0.7
        xalign 0.1
        yalign 0.01

    aiko "{cps=2}...{/cps}"

    #play music
    play music trouble volume 0.1

    show aiko angryblush:
        zoom 0.7
        xalign 0.1
        yalign 0.01

    aiko "Apa kamu lupa? Apa kepalamu mau ku jedotin?"

    mc "Serius, aku gak tau apa apa!"

    aiko "Bohong!"

    menu:
        "Seri-":
            show aiko angryblush with fade:
                zoom 1.0
                xalign 0.5
                yalign 0.01

            aiko "B O H O N G!" with vpunch

            aiko "Coba, emang nama mu siapa?"

            $ mcname = renpy.input("Siapa namamu?")

            $ mcname = mcname.strip()

            if mcname == "":
                $ mcname = "Ryuji"

            if mcname != "Ryuji":
                aiko "Namamu seharusnya Ryuji!"
                jump loop 
            else:
                jump notloop

        "Bentar aku harus tau namamu dulu!" if ceknama == 0 :

            aiko "ngapain juga aku mau kasih tau nama aku!"
            show aiko angry:
                zoom 0.7
                xalign 0.1
                yalign 0.01

            aiko "{cps=20}Hah? Apa ini?{/cps}" with vpunch
            window hide

            scene blue
            pause 0.5
            scene blue1
            pause 2
            scene blue
            pause 0.1
            $gimang = gimang + 1
            jump start2
        "Nama kamu aiko kan?" if ceknama >= 1:
            show aiko closeeye:
                zoom 1.0
                xalign 0.5
                yalign 0.01
         
            aiko "Kok kamu bisa tau? nama ku?"

            mc "Maukah kau mendengarkan penjelasan ku? Aiko?"

            "Kamu menjelaskan kamu sudah melakukan loop yang tak terbatas"

            aiko "Aku... tidak percaya..."

            aiko "Memang ada kejadian seperti itu?"

            mc "Percaya, tidak percaya..."

            mc "Bisa kah kamu menolong ku? Aiko?"

            aiko "{cps=1}. . .{/cps}"

            aiko "Jadi dimana Ryuji?"

            mc "Aiko tolong de-"

            window hide

            scene blue
            pause 0.5
            scene blue1
            pause 2
            scene blue
            pause 0.1
            $renpy.quit()

    return

label loop:

    mc "Hah?" with vpunch

    show aiko angry:
        zoom 0.7
        xalign 0.1
        yalign 0.01

    aiko "Sepertinya apa yang dikatakan Sumi benar"

    hide aiko with fade

    mc "..."

    mc "Tunggu hey!"

    scene bg2 with fade

    mc "Hey!! tunggu kamu mau kemana?"

    show aiko angry:
        zoom 0.7
        xalign 0.1
        yalign 0.01

    aiko "Apa?"

    aiko "!!!"

    stop music

    play sound error

    scene bgblack with Pixellate(2, 100)

    hide aiko angry

    pause 10

    hide screen rahasia

    $gimang = gimang + 1

    if gimang == 10:

        scene blue
        pause 2

    elif gimang >= 15:

        scene blue
        pause 0.5
        scene blue1
        pause 2
        scene blue
        pause 0.1
        $renpy.quit(relaunch = [False], save = [False])
        
    window show

    jump start2

    return

label notloop:

    mc "Ah.... kepalaku sakit..." with fade

    show aiko angry:
        zoom 0.7
        xalign 0.1
        yalign 0.01


    aiko "Kamu gak apa apa? Mau Aiko bantu?"

    $ceknama = ceknama + 1

    mc "aku gak apa apa..."

    if gimang >= 1 and ceknama == 1:
        mc "Jadi namamu Aiko?"

        aiko "??? Kamu kenapa sih? aneh."

    $ceknama = 2

    show aiko base:
        zoom 0.7
        xalign 0.1
        yalign 0.01

    aiko "Oh iya, hari ini kan kita ada janji sama Sumi!"

    mc "Begitukah?"

    aiko "Ayok kita jalan.. sebelum itu makan dulu yuk!"

    menu:
        "Mending tidur!" if persistent.tamat == 0:

            show aiko angry:
                zoom 0.7
                xalign 0.1
                yalign 0.01
            
            aiko "Dasar mageran!" with vpunch

            scene bgblack with fade

            $gimang = gimang + 1

            jump start2
            
        "Ayok" if persistent.tamat == 0:

            jump bad_ending1
        
        "Mending kita dirumah aja" if cekmati >= 1 and persistent.tamat == 0:

            jump bad_ending2

        "Sepertinya aku seperti dikendalikan orang" if persistent.tamat == 1:

            jump trueending

    return

#Ending Rahasia
label rahasia:

    stop music
    hide screen cheat 
    hide screen rahasia
    play music calm volume 0.1

    scene bg2error

    show aiko angry:
        zoom 0.7
        xalign 0.1
        yalign 0.01

    aiko "{cps=20}!!!{/cps}" with vpunch

    aiko "{cps=20}Dimana ini?{/cps}"

    mc "{cps=20}Kenapa jadi seperti ini?{/cps}"

    mc "{cps=20}Ada apa dengan dapurnya?{/cps}"

    aiko "{cps=20}Mana aku tau!!{/cps}"

    hide aiko angry

    show sumi base with pixellate:
        zoom 0.7
        xalign 0.9
        yalign 0.01

    oldmc "Kamu akhirnya bisa kesini juga!"

    mc "Sumi??" with vpunch

    sumi "Aku akan menjelaskan sebisa yang aku bisa!"

    show aiko angryblush:
        zoom 0.7
        xalign 0.1
        yalign 0.01

    aiko "Sebentar!!! Aku tidak mengerti kenapa ada kamu di sini Sumi??" with vpunch

    sumi "Aiko.... biarkan aku menjelaskan, dengarkan aku!"

    hide aiko

    hide sumi

    "Sumi menjelaskan apa yang aiko tanyakan" with fade

    show aiko closeeye:
        zoom 0.7
        xalign 0.1
        yalign 0.01

    aiko "{cps=2}...{/cps}"

    show aiko angry:
        zoom 0.7
        xalign 0.1
        yalign 0.01

    aiko "Jadi yang kamu maksud adalah, ada sesuatu yang telah merusak time line?"

    aiko "Dan [mcname], sudah melalui loop?"

    mc "Apakah kamu percaya kepada ku? sekarang?"

    aiko "Aku ingin bertanyak. Dimana Ryuji jadinya?"

    show sumi base:
        zoom 0.7
        xalign 0.9
        yalign 0.01

    sumi "[mcname] adalah Ryuji, Aiko! semua ini terjadi dikarenakan ada sesuatu yang merusak time line"

    hide sumi

    hide aiko

    window hide

    play sound monster volume 0.1

    pause 5

    window show

    show aiko angry:
        zoom 0.7
        xalign 0.1
        yalign 0.01

    aiko "{cps=20}!!!{/cps}" with vpunch

    aiko "{cps=5}Apa itu?{/cps}"

    show sumi base:
        zoom 0.7
        xalign 0.9
        yalign 0.01

    sumi "{cps=20}Itu dia, sesuatu yang mengganggu time line{/cps}"

    mc "{cps=10}Siapa dia?{/cps}"

    sumi "{cps=20}Aku menyebutnya 'Unknown'.{/cps}"

    mc "Apa yang harus kita lakukan?"

    sumi "{cps=2}...{/cps}"

    sumi "{cps=10}Melawannya{/cps}"

    aiko "{cps=20}Apa kita bisa? Melawannya?{/cps}"

    sumi "{cps=20}Kita tidak tau sampai kita mencobanya{/cps}"

    aiko "{cps=2}...{/cps}"

    sumi "Bagaimana [mcname]? apa kamu siap?"

    hide aiko

    hide sumi

    menu:
        "Aku siap!":
            show aiko angry:
                zoom 0.7
                xalign 0.1
                yalign 0.01
            
            aiko "Hah? apa kamu serius?" with vpunch

            show sumi base:
                zoom 0.7
                xalign 0.9
                yalign 0.01

            sumi "Baiklah, jika itu keputusanmu"

            jump battle

        "Adakah cara lainnya?":
            show sumi base:
                zoom 0.7
                xalign 0.9
                yalign 0.01

            sumi "Tidak ada, aku yakin sepertinya kita bisa melawannya"

            sumi "Jika kita melawannya bersama!"

            show aiko angry:
                zoom 0.7
                xalign 0.1
                yalign 0.01

            aiko "{cps=20}Aku percaya kepadamu Sumi!"

            sumi "Baiklah..."

            jump battle

    return

label battle:

    stop music

    hide sumi

    show aiko angry with fade:
        zoom 0.7
        xalign 0.1
        yalign 0.01

    aiko "{cps=20}Sangat sunyi...{/cps}"

    aiko "..." with vpunch

    hide aiko

    hide sumi

    play sound monster volume 0.1

    show unknown with fade:
        zoom 1.2
        xalign 0.5
        yalign 1.2

    mc "{cps=20}Apa itu yang kau sebut 'Unknown'?{/cps}"

    hide unknown

    show sumi base:
        zoom 0.7
        xalign 0.9
        yalign 0.01

    sumi "{cps=10}Iya...{/cps}"

    sumi "Inilah saatnya. Sekarang atau tidak selamanya [mcname] !!"

    hide sumi with fade

    jump fight

    return

#berfungsi agar musik tidak ter loop
label fight:

    #hide screen cheat

    hide screen ulang

    show glitch2

    play music bosstheme volume 0.1

    jump fight2

    return

label fight2:


    show unknown:
        zoom 1.2
        xalign 0.5
        yalign 1.2

    if turn == 0:
        "Unknown memiliki darah [darahboss]"

        "Apa yang akan kamu lakukan?"

        jump haha

    elif darahboss == 0 and darahmu > 0:

        play sound monster volume 0.1

        show unknown at mati

        pause 8

        show aiko base:
            zoom 0.7
            xalign 0.1
            yalign 0.01

        aiko "Kita... menang?"

        hide aiko

        stop music

        jump peace

    else:
        if turn >= 10:
            $darahmu = darahmu - 9
            if darahboss <= 500:
                play sound error volume 0.1
                "Dnbz/bjaj}fbn/dj}z|ndna/|jmj|n}/6" with vpunch
            else:    
                "Kamu menerima kerusakan sebesar 9" with vpunch

            if darahmu <= 9:
                $darahmu = 0
        
        elif turn >= 20:
            $darahmu = darahmu - 30

            if darahboss <= 500:
                play sound error volume 0.1
                "z2>F >6?6C:>2 <6CFD2<2? D636D2C b_" with hpunch
            else:
                "Kamu menerima kerusakan sebesar 30" with hpunch

            if darahmu <= 30:
                $darahmu = 0

        else:
            $darahmu = darahmu - 3
            if darahboss <= 500:
                play sound error volume 0.1
                "xgxgd axdfa fddax fxgaf xgdaf fdagf afaaf dagdd aaaxg axfda xgxgd a" with vpunch
            else:
                "Kamu menerima kerusakan sebesar 3" with vpunch

        if darahmu == 0:

            "Darahmu [darahmu]!"

            jump kalah

        if darahboss <= 500:
            "While running game code: NameError: name 'darah mu' is not defined"  
        else:
            "Darah mu tersisah [darahmu]!"        
        if darahboss <= 500:
            "While running game code: NameError: name 'darah boss' is not defined"
        else:
            "Unknown memiliki darah [darahboss]"

        "Apa yang akan kamu lakukan?"

        jump haha

    return

label haha:

    hide screen pilihan

    show screen pilihan

    pause

    jump haha

    return

label kalah:

    show screen ulang

    pause

    jump kalah

    return
    

label cobaserang:

    hide screen pilihan

    show screen pilihserang

    "Apa yang akan kamu lakukan?"

    jump cobaserang

    return

label cobabantuan:

    hide screen pilihan

    show screen pilihbantuan

    "Apa yang akan kamu lakukan?"

    jump cobabantuan

    return

label hadiah:

    hide screen aiko

    hide screen pilihbantuan
    if turn >= 10:
        "Kamu mendapatkan darah sebesar 15"

        $darahmu = darahmu + 15

        if darahmu >= 100:

            $darahmu = 100
    else:
        "Kamu mendapatkan darah sebesar 5"

        $darahmu = darahmu + 5

        if darahmu >= 100:

            $darahmu = 100

    $turn = turn + 1

    jump fight2

    return

label semangat:

    hide screen aiko

    hide unknown

    show aiko closeeyeblush with fade:
        zoom 0.7
        xalign 0.1
        yalign 0.01

    aiko "Semangat!!!" with vpunch

    hide aiko

    if turn >= 10:
        "Serangan mu menguat drastis!"

        $seranganbiasa = seranganbiasa + 50

        $seranganbulan = seranganbulan + 50
    else:
        "Serangan mu sedikit menguat!"

        $seranganbiasa = seranganbiasa + 15

        $seranganbulan = seranganbulan + 15

    $turn = turn + 1

    jump fight2

    return

label penghancur:

    hide screen sumi

    hide unknown

    show sumi base with fade:
        zoom 0.7
        xalign 0.9
        yalign 0.01
    
    sumi "{cps=20}Inilah saat ku untuk bersinar{/cps}"

    hide sumi

    if darahboss <= darahboss:

        $darahboss = 0
    
    else:

        $darahboss = darahboss - darahboss

    $turn = turn + 1

    jump fight2

    return

label seranganbiasa:

    hide screen pilihserang

    if darahboss <= 500:
        show unknown at terkenaserang2
    else:
        show unknown at terkenaserang
    
    show serang2

    pause 0.5

    hide serang2

    if darahboss <= seranganbiasa:

        $darahboss = 0

    else:
 
        $darahboss = darahboss - seranganbiasa

    "Kamu memberikan kerusakan sebesar [seranganbiasa]"

    $turn = turn + 1

    jump fight2

    return

label kembali:

    hide screen pilihan

    hide screen pilihserang

    hide screen pilihbantuan

    hide screen sumi

    hide screen aiko

    show unknown:
        zoom 1.2
        xalign 0.5
        yalign 1.2

    if darahboss <= 500:
        "While running game code: NameError: name 'darah boss' is not defined"
    else:
        "Unknown memiliki darah [darahboss]"

    "Apa yang akan kamu lakukan?"

    show screen pilihan

    pause

    jump kembali

    return


label seranganbulan:

    hide screen pilihserang
    
    show serang1

    if darahboss <= 500:
        show unknown at terkenaserang2
    else:
        show unknown at terkenaserang

    pause 0.5

    hide serang1

    if darahboss <= seranganbulan:

        $darahboss = 0
    else:    
        $darahboss = darahboss - seranganbulan

    "Kamu memberikan kerusakan sebesar [seranganbulan]"

    $turn = turn + 1

    jump fight2

    return

label pilihaiko:

    hide screen pilihbantuan

    show screen aiko

    pause 

    jump pilihaiko

    return

label pilihsumi:

    hide screen pilihbantuan

    show screen sumi

    pause

    jump pilihsumi

    return

label bad_ending1:

    stop music

    play music happy volume 0.1 fadein(2.0)

    scene bg3 with fade

    show aiko smile:
        zoom 0.7
        xalign 0.1
        yalign 0.01

    aiko "Hehehe..."

    aiko "Sudah lama yah, kita gak jalan bareng!"

    mc "Aiko..."

    show aiko openmouth:
        zoom 0.7
        xalign 0.1
        yalign 0.01

    aiko "Hmmmm.... ada apa?"

    mc "Kamu terlihat cantik"

    show aiko closeeyeblush:
        zoom 0.7
        xalign 0.1
        yalign 0.01
    
    aiko "{cps=1}...{/cps}"

    aiko "Bikin orang malu aja!"

    mc "Aku berkata apa adanya Aiko!"

    aiko "Emang dari dulu aku gak cantik?" with vpunch

    aiko "Sampai-sampai kamu menikahi aku?"

    menu:
        "Memang dari dulu kamukan cantik!":

            aiko "{cps=1}...{/cps}"

        "Yah, aku menikah dengan mu bukan karena itu sih":

            aiko "terus kenapa?"

            mc "Karena kamu baik dan memiliki hati seorang ibu"

    show aiko angry:
        zoom 0.7
        xalign 0.1
        yalign 0.01
    
    aiko "udah ah, buruan ke tempat Sumi!"

    hide aiko

    window hide
    show sumi base with fade:
        zoom 0.4
        xalign 0.9
        yalign 1.0
    window show

    aiko base "Itu dia"

    aiko base "{cps=20}Sumi!!{/cps}"

    sumi "!!!" with vpunch

    show sumi openmouth with fade:
        zoom 0.7
        xalign 0.9
        yalign 0.01

    sumi "Aiko!! awas..." with vpunch

    mc "Aiko!!!" with vpunch

    play sound crash volume 0.5

    scene bgblack

    play music sad volume 0.1 fadein(2.0)

    pause 2.0

    sumi "Cepat telefon ambulan! [mcname]!"

    mc "{cps=1}...{/cps}"

    sumi "Cepat pang-"

    show screen blood with fade

    mc "{cps=1}...{/cps}"

    $cekmati = cekmati + 1

    $cekmati2 = cekmati2 + 1

    $gimang = gimang + 1

    hide screen blood

    jump start2

    return

#ending 1
label bad_ending2:
    
    aiko "Yah udah, aku pergi sendiri"

    hide aiko

    "Kamu tidur, dan tidak terbangun selamanya!"

    show unknown with fade:
        zoom 1.2
        xalign 0.5
        yalign 1.2

    play sound error

    "..."

    hide unknown

    return

#ending2
label trueending:

    stop music

    play music ending volume 0.1 fadein(2.0)

    scene bg1

    mc "Aku merasa sudah mengulang berkali kali! seperti..."

    show aiko angry:
        zoom 0.7
        xalign 0.1
        yalign 0.01

    aiko "Seperti?"

    mc "{cps=1}. . .{/cps}"

    mc "Aku dikendalikan orang"

    mc "Aku bahkan sudah mencoba berbeda nama dan mengetahui banyak hal!"

    mc "Aku juga sudah melawan monster aneh bernama 'Unknown'!"

    aiko "Apa maksudnya? kamu ngomong apa sih? mending kita ketemu Sumi"

    mc "Sumi sepertinya tau sesuatu tentang ini!"

    aiko "Hah?" with hpunch

    mc "Mending kita tunggu Sumi untuk kesini!" with fade

    "{cps=2}...{/cps}"

    show sumi base:
        zoom 0.7
        xalign 0.9
        yalign 0.01
    
    sumi "Apa yang kau katakan itu memanglah tidak masuk akal!" with fade

    sumi "Tapi jika kamu mengatakan kalau kita dikendalikan atau kita adalah sebuah game"

    sumi "{cps=2}...{/cps}"

    sumi "Aku percaya!"

    aiko "Sebentar! Aku gak ngerti!" with vpunch

    sumi "Secara tidak langsung, kita seperti berada didalam game, Aiko!"

    show aiko closeeye:
        zoom 0.7
        xalign 0.1
        yalign 0.01

    aiko "aku tetap tidak mengerti..." with vpunch

    sumi "Aku bisa membebaskan kalian!"

    hide aiko

    mc "Benar! Aku juga ingin bertanyak! Kamu sebenarnya siapa Sumi?"

    aiko "Dia kan teman kita dari dulu! apa kamu lupa?"

    mc "Dia seperti mengetahui segalanya Aiko, Sumi siapa sebenarnya kamu?"

    sumi "{cps=20}Aku?{/cps}"

    sumi "{cps=2}...{/cps}"

    sumi "Kamu bisa menyebutku sebagai pendeteksi"

    sumi "Kamu sudah menemukan jawaban mu! apa jawaban mu? apa kamu ingin terlepas?"

    mc "Ya..."

    sumi "baiklah"

    sumi "{cps=5}73797374656d207265626f6f74{/cps}"

    sumi "{cps=5}6372617368696e6720746865206170706c69636174696f6e{/cps}"

    sumi "{cps=20}Semoga kita bertemu kembali!{/cps}"

    $persistent.loop = persistent.loop + 1

    scene bgblack

    show screen ending with fade

    pause

    return

#ending 3
label peace:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    stop music

    #play music 
    hide screen rahasia
    play music bg1 volume 0.1 fadein(2.0)

    scene bg1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    mc "{cps=2}...{/cps}"
        
    mc "{cps=20}Hoam... sudah pagi rupanya{/cps}"

    play sound door volume 0.1

    window hide
        
    pause 2.5

    window show

    mc "{cps=20}Hmmm??{/cps}"

    mc "{cps=20} Masuk!{/cps}"

    play sound door_open volume 0.1
        
    window hide

    show aiko base with fade:
        zoom 0.7
        xalign 0.1
        yalign 0.01
        
    pause 2.0

    window show

    aiko "{cps=20}Kamu sudah bangun?{/cps}"

    mc "{cps=20}Iya... Aiko{/cps}"

    aiko "{cps=20}Yuk, makan! hehe... nanti kita ketemu Sumi juga{/cps}"

    mc "{cps=20}Iya... yuk makan...{/cps}"

    aiko "{cps=20}Kamu kenapa?{/cps}"

    mc "{cps=20}Gak, aku rasa, seperti telah bermimpi...{/cps}"

    window hide

    hide aiko

    $persistent.tamat = persistent.tamat + 1

    scene bgblack

    show screen ending with fade

    pause

    return

label kebenaran:
    hide screen warning
    play music opening volume 0.1

    $cekrahasia = cekrahasia + 1

    scene bg4

    mc "!!!"

    mc "{cps=20}Dimana ini?{/cps}"

    oldmc "{cps=20}Selamat datang ditempat tersembunyi!{/cps}"

    mc "Apa maksud dari ini?"

    oldmc "{cps=20}Ada beberapa kesalahan yang terjadi didalam game!{/cps}"

    oldmc "{cps=20}Kami sudah melakukan pembetulan dan tetap terjadi kesalahan{/cps}"

    oldmc "{cps=20}Tetapi kami telah melakukan sesuatu yang akan menyelamatkan mu!{/cps}"

    mc "Tunggu? jadi di game ini ada yang telah terjadi?"

    oldmc "{cps=20}Benar! Dikarenakan itu kami melakukan suatu cara agar dirimu lolos!{/cps}"

    oldmc "{cps=20}Ingatlah! saat terjadi black screen yang lama...{/cps}"

    oldmc "{cps=20}Tekan dititik tengah bagian game! kamu akan diahlikan ketempat lain yang akan mengahkiri segalanya{/cps}"

    oldmc "{cps=20}Dan kamu akan tau siapa aku yang sebenarnya [mcname]{/cps}"

    menu:
        "Jadi saat black screen berkempajangan aku hanya butuh menekan dibagian tengah?":

            oldmc "{cps=20}Benar{/cps}"

        "Bagaimana dengan Aiko?":

            oldmc "{cps=20}Semua akan baik-baik saja jika kamu melakukan sesuai perintah ku!{/cps}"

    oldmc "{cps=20}Jika kau tidak memiliki pertanyaan lagi, maka kau akan terbagun kembali{/cps}"

    oldmc "{cps=20}Sampai jumpa!{/cps}" with fade

    oldmc "{cps=2}...{/cps}"

    show sumi base with pixellate:
        zoom 0.7
        xalign 0.9
        yalign 0.01

    sumi "{cps=20}Semoga kamu beruntung [mcname]!{/cps}"

    hide sumi base

    jump looprahasia

    return

label looprahasia:

    scene bg1

    play music trouble volume 0.1

    mc "Hah?" with vpunch

    show aiko angry:
        zoom 0.7
        xalign 0.1
        yalign 0.01

    aiko "Sepertinya apa yang dikatakan Sumi benar"

    hide aiko with fade

    mc "..."

    mc "Tunggu hey!"

    scene bg2 with fade

    mc "Hey!! tunggu kamu mau kemana?"

    show aiko angry:
        zoom 0.7
        xalign 0.1
        yalign 0.01

    aiko "Apa?"

    aiko "!!!"

    stop music

    play sound error

    scene bgblack with Pixellate(2, 100)

    hide aiko angry

    if cekrahasia == 1:
        show screen rahasia

    window hide

    pause 10

    hide screen rahasia

    $gimang = gimang + 1

    if gimang == 10:

        scene blue
        pause 2

    elif gimang >= 15:

        scene blue
        pause 0.5
        scene blue1
        pause 2
        scene blue
        pause 0.1
        $renpy.quit(relaunch = [False], save = [False])
        
    window show

    jump start2

    return