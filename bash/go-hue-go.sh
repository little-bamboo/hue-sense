#!/usr/bin/env bash
# /etc/init.d/go-hue-go.sh

case "$1" in
    start)
        echo "Starting Hue Sense - python soundcapture.py"
        echo "Setup virtual env"

        python /home/pi/hue_pi/soundcapture.py
        ;;
    stop)
        echo "Stopping go-hue-go.sh"
        killall soundcapture.py
        ;;
    *)
        echo "Usage: /etc/init.d/go-hue-go.sh {start|stop}"
        exit 1
        ;;
esac

exit 0