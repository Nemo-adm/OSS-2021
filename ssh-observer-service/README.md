# Сервис мониторинга сеансов пользователей

## Тестовое задание

Разработать сервис, который выполняет мониторинг подключённых к системе пользователей по `ssh` каждые `30` секунд. При подключении внешнего пользователя по `ssh`, пользователю должно выводиться на экран уведомление (механизм `notify`) с именем пользователя, который подключился к системе удалённо.


## Демонстрация работы

```
[nikolai@10 ~]$ pstree
systemd─┬─ModemManager───2*[{ModemManager}]
        ├─NetworkManager─┬─dhclient
        │                └─2*[{NetworkManager}]
        ├─3*[VBoxClient───VBoxClient───2*[{VBoxClient}]]
        ├─VBoxClient───VBoxClient───3*[{VBoxClient}]
        ├─VBoxService───8*[{VBoxService}]
        ├─2*[abrt-watch-log]
        ├─abrtd
        ├─accounts-daemon───2*[{accounts-daemon}]
        ├─alsactl
        ├─anacron
        ├─at-spi-bus-laun─┬─dbus-daemon───{dbus-daemon}
        │                 └─3*[{at-spi-bus-laun}]
        ├─at-spi2-registr───2*[{at-spi2-registr}]
        ├─atd
        ├─auditd─┬─audispd─┬─sedispatch
        │        │         └─{audispd}
        │        └─{auditd}
        ├─avahi-daemon───avahi-daemon
        ├─boltd───2*[{boltd}]
        ├─chronyd
        ├─colord───2*[{colord}]
        ├─crond
        ├─cupsd
        ├─2*[dbus-daemon───{dbus-daemon}]
        ├─dbus-launch
        ├─dconf-service───2*[{dconf-service}]
        ├─dnsmasq───dnsmasq
        ├─evolution-addre─┬─evolution-addre───5*[{evolution-addre}]
        │                 └─4*[{evolution-addre}]
        ├─evolution-calen─┬─evolution-calen───8*[{evolution-calen}]
        │                 └─4*[{evolution-calen}]
        ├─evolution-sourc───3*[{evolution-sourc}]
        ├─firewalld───{firewalld}
        ├─fwupd───4*[{fwupd}]
        ├─gdm─┬─X───{X}
        │     ├─gdm-session-wor─┬─gnome-session-b─┬─abrt-applet───2*[{abrt-applet}]
        │     │                 │                 ├─gnome-shell─┬─ibus-daemon─┬─ibus-dconf─+++
        │     │                 │                 │             │             ├─ibus-engine+
        │     │                 │                 │             │             └─2*[{ibus-da+
        │     │                 │                 │             └─9*[{gnome-shell}]
        │     │                 │                 ├─gnome-software───3*[{gnome-software}]
        │     │                 │                 ├─gsd-a11y-settin───3*[{gsd-a11y-settin}]
        │     │                 │                 ├─gsd-account───3*[{gsd-account}]
        │     │                 │                 ├─gsd-clipboard───2*[{gsd-clipboard}]
        │     │                 │                 ├─gsd-color───3*[{gsd-color}]
        │     │                 │                 ├─gsd-datetime───3*[{gsd-datetime}]
        │     │                 │                 ├─gsd-disk-utilit───2*[{gsd-disk-utilit}]
        │     │                 │                 ├─gsd-housekeepin───3*[{gsd-housekeepin}]
        │     │                 │                 ├─gsd-keyboard───3*[{gsd-keyboard}]
        │     │                 │                 ├─gsd-media-keys───3*[{gsd-media-keys}]
        │     │                 │                 ├─gsd-mouse───3*[{gsd-mouse}]
        │     │                 │                 ├─gsd-power───3*[{gsd-power}]
        │     │                 │                 ├─gsd-print-notif───2*[{gsd-print-notif}]
        │     │                 │                 ├─gsd-rfkill───2*[{gsd-rfkill}]
        │     │                 │                 ├─gsd-screensaver───2*[{gsd-screensaver}]
        │     │                 │                 ├─gsd-sharing───3*[{gsd-sharing}]
        │     │                 │                 ├─gsd-smartcard───4*[{gsd-smartcard}]
        │     │                 │                 ├─gsd-sound───3*[{gsd-sound}]
        │     │                 │                 ├─gsd-wacom───2*[{gsd-wacom}]
        │     │                 │                 ├─gsd-xsettings───3*[{gsd-xsettings}]
        │     │                 │                 ├─nautilus-deskto───3*[{nautilus-deskto}]
        │     │                 │                 ├─seapplet
        │     │                 │                 ├─ssh-agent
        │     │                 │                 ├─tracker-extract───14*[{tracker-extract}+
        │     │                 │                 ├─tracker-miner-a───3*[{tracker-miner-a}]
        │     │                 │                 ├─tracker-miner-f───3*[{tracker-miner-f}]
        │     │                 │                 ├─tracker-miner-u───3*[{tracker-miner-u}]
        │     │                 │                 └─3*[{gnome-session-b}]
        │     │                 └─2*[{gdm-session-wor}]
        │     └─3*[{gdm}]
        ├─gedit───3*[{gedit}]
        ├─gnome-keyring-d───3*[{gnome-keyring-d}]
        ├─gnome-shell-cal───5*[{gnome-shell-cal}]
        ├─gnome-terminal-─┬─bash───pstree
        │                 ├─gnome-pty-helpe
        │                 └─3*[{gnome-terminal-}]
        ├─goa-daemon───3*[{goa-daemon}]
        ├─goa-identity-se───3*[{goa-identity-se}]
        ├─gsd-printer───2*[{gsd-printer}]
        ├─gssproxy───5*[{gssproxy}]
        ├─gvfs-afc-volume───3*[{gvfs-afc-volume}]
        ├─gvfs-goa-volume───2*[{gvfs-goa-volume}]
        ├─gvfs-gphoto2-vo───2*[{gvfs-gphoto2-vo}]
        ├─gvfs-mtp-volume───2*[{gvfs-mtp-volume}]
        ├─gvfs-udisks2-vo───2*[{gvfs-udisks2-vo}]
        ├─gvfsd─┬─gvfsd-burn───2*[{gvfsd-burn}]
        │       ├─gvfsd-dnssd───2*[{gvfsd-dnssd}]
        │       ├─gvfsd-network───3*[{gvfsd-network}]
        │       ├─gvfsd-trash───2*[{gvfsd-trash}]
        │       └─2*[{gvfsd}]
        ├─gvfsd-fuse───5*[{gvfsd-fuse}]
        ├─gvfsd-metadata───2*[{gvfsd-metadata}]
        ├─haveged
        ├─httpd───5*[httpd]
        ├─ibus-portal───2*[{ibus-portal}]
        ├─ibus-x11───2*[{ibus-x11}]
        ├─imsettings-daem───3*[{imsettings-daem}]
        ├─ksmtuned───sleep
        ├─libvirtd───16*[{libvirtd}]
        ├─lsmd
        ├─lvmetad
        ├─master─┬─pickup
        │        └─qmgr
        ├─mission-control───3*[{mission-control}]
        ├─packagekitd───2*[{packagekitd}]
        ├─polkitd───6*[{polkitd}]
        ├─pulseaudio───2*[{pulseaudio}]
        ├─rngd
        ├─rpcbind
        ├─rsyslogd───2*[{rsyslogd}]
        ├─rtkit-daemon───2*[{rtkit-daemon}]
        ├─smartd
        ├─sshd
        ├─systemd-hostnam
        ├─systemd-journal
        ├─systemd-logind
        ├─systemd-machine
        ├─systemd-udevd
        ├─tracker-store───7*[{tracker-store}]
        ├─tuned───4*[{tuned}]
        ├─udisksd───4*[{udisksd}]
        ├─upowerd───2*[{upowerd}]
        ├─wpa_supplicant
        └─xdg-permission-───2*[{xdg-permission-}]

[nikolai@10 ~]$ sudo systemctl start sshd
[nikolai@10 ~]$ sudo systemctl status sshd
● sshd.service - OpenSSH server daemon
   Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled; vendor preset: enabled)
   Active: active (running) since Пт 2022-05-27 10:17:59 MSK; 3s ago
     Docs: man:sshd(8)
           man:sshd_config(5)
 Main PID: 4175 (sshd)
    Tasks: 1
   CGroup: /system.slice/sshd.service
           └─4175 /usr/sbin/sshd -D

май 27 10:17:59 10.0.2.15 systemd[1]: Starting OpenSSH server daemon...
май 27 10:17:59 10.0.2.15 sshd[4175]: Server listening on 0.0.0.0 port 22.
май 27 10:17:59 10.0.2.15 sshd[4175]: Server listening on :: port 22.
май 27 10:17:59 10.0.2.15 systemd[1]: Started OpenSSH server daemon.
[nikolai@10 ~]$ journalctl -f -u sshd
-- Logs begin at Пт 2022-05-27 09:47:31 MSK. --
май 27 09:49:10 localhost.localdomain sshd[1083]: Server listening on 0.0.0.0 port 22.
май 27 09:49:10 localhost.localdomain sshd[1083]: Server listening on :: port 22.
май 27 09:49:10 localhost.localdomain systemd[1]: Started OpenSSH server daemon.
май 27 10:17:27 10.0.2.15 sshd[1083]: Received signal 15; terminating.
май 27 10:17:27 10.0.2.15 systemd[1]: Stopping OpenSSH server daemon...
май 27 10:17:27 10.0.2.15 systemd[1]: Stopped OpenSSH server daemon.
май 27 10:17:59 10.0.2.15 systemd[1]: Starting OpenSSH server daemon...
май 27 10:17:59 10.0.2.15 sshd[4175]: Server listening on 0.0.0.0 port 22.
май 27 10:17:59 10.0.2.15 sshd[4175]: Server listening on :: port 22.
май 27 10:17:59 10.0.2.15 systemd[1]: Started OpenSSH server daemon.
[nikolai@10 ~]$ sudo kill -SIGUSR1 4175
[nikolai@10 ~]$ sudo systemctl status sshd
● sshd.service - OpenSSH server daemon
   Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled; vendor preset: enabled)
   Active: activating (auto-restart) (Result: signal) since Пт 2022-05-27 10:19:10 MSK; 4s ago
     Docs: man:sshd(8)
           man:sshd_config(5)
  Process: 4175 ExecStart=/usr/sbin/sshd -D $OPTIONS (code=killed, signal=USR1)
 Main PID: 4175 (code=killed, signal=USR1)

май 27 10:19:10 10.0.2.15 systemd[1]: sshd.service: main process exited, code=kille...SR1

[nikolai@10 ssh-monitoring-1.0]$ sudo ./ssh-monitoring-test
new_user1@127.0.0.1's password:
new_user1@127.0.0.1's password: 
Service works correctly
[nikolai@10 ssh-monitoring-1.0]$ man ssh-monitoring
SESSION-MONITOR(8)        SESSION MONITORING SERVICE        SESSION-MONITOR(8)

NAME
       ssh-monitoring

DESCRIPTION
       ssh-monitoring  -  monitors  users connected to system via ssh every 30
       seconds. When an external user connects  via  ssh,  a  notification  w/
       notify  mechanism  must  be displayed to user with name of the user who
       has connected to the system remotely.

AUTHOR
       Nikolay Izyurov Z

SESSION-MONITOR 1.0               22 MAY 2022               SESSION-MONITOR(8)
```
