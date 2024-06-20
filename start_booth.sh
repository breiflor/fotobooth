#!/bin/sh

export XDG_SESSION_PATH=/org/freedesktop/DisplayManager/Session0
export XDG_MENU_PREFIX=lxde-pi-
export QT_WAYLAND_DISABLE_WINDOWDECORATION=1
export SSH_AUTH_SOCK=/tmp/ssh-XXXXXX9U5EQQ/agent.913
export WLR_XWAYLAND=/usr/bin/xwayland-xauth
export DESKTOP_SESSION=LXDE-pi-wayfire
export SSH_AGENT_PID=983
export NO_AT_BRIDGE=1
export XCURSOR_SIZE=24
export XDG_SEAT=seat0
export PWD=/home/fotobox/fotobooth
export LOGNAME=fotobox
export XDG_SESSION_DESKTOP=LXDE-pi-wayfire
export QT_QPA_PLATFORMTHEME=qt5ct
export XDG_SESSION_TYPE=wayland
export GPG_AGENT_INFO=/run/user/1000/gnupg/S.gpg-agent:0:1
export XAUTHORITY=/home/fotobox/.Xauthority
export XDG_GREETER_DATA_DIR=/var/lib/lightdm/data/fotobox
export HOME=/home/fotobox
export LANG=en_GB.UTF-8
export LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=00:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.avif=01;35:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:*~=00;90:*#=00;90:*.bak=00;90:*.old=00;90:*.orig=00;90:*.part=00;90:*.rej=00;90:*.swp=00;90:*.tmp=00;90:*.dpkg-dist=00;90:*.dpkg-old=00;90:*.ucf-dist=00;90:*.ucf-new=00;90:*.ucf-old=00;90:*.rpmnew=00;90:*.rpmorig=00;90:*.rpmsave=00;90:
export _JAVA_AWT_WM_NONREPARENTING=1
export VTE_VERSION=7006
export WAYLAND_DISPLAY=wayland-1
export XDG_SEAT_PATH=/org/freedesktop/DisplayManager/Seat0
export XDG_SESSION_CLASS=user
export TERM=xterm-256color
export USER=fotobox
export DISPLAY=:0
export SHLVL=1
export XDG_VTNR=7
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XCURSOR_THEME=PiXflat
export XDG_DATA_DIRS=/usr/local/share:/usr/share/raspi-ui-overrides:/usr/share:/usr/share/gdm:/var/lib/menu-xdg
export WLR_DRM_NAME=/dev/dri/card1
export GDMSESSION=LXDE-pi-wayfire
export SAL_USE_VCLPLUGIN=gtk3
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
export WAYFIRE_CONFIG_FILE=/home/fotobox/.config/wayfire.ini


cd /home/fotobox/fotobooth/pythonProject
echo $XDG_RUNTIME_DIR
sudo python main.py
