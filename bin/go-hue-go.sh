#!/usr/bin/env bash
# /etc/init.d/go-hue-go.sh

case "$1" in
    start)
        echo "Starting Hue Sense - python run.py"
        echo "Setup virtual env"
        cd /home/pi/hue-sense/
        source .env/bin/activate
        python run.py
        ;;
    stop)
        echo "Stopping go-hue-go.sh"
        cd /home/pi/hue-sense/
        deactivate
        killall run.py
        ;;
    *)
        echo "Usage: /etc/init.d/go-hue-go.sh {start|stop}"
        exit 1
        ;;
esac

exit 0