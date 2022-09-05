import logging
from fan_controller import server

# switching to debug will break protocol, because printing will increase pulse length
logging.basicConfig(level=logging.INFO)


logger = logging.getLogger(__name__)


def main():
    server.app.run(host='0.0.0.0', port=8081)


if __name__ == '__main__':
    main()
