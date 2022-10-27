import argparse
import os
import uvicorn

from workshop import __version__ as VERSION
from .manager import create_db_tables


def get_parsed_args():
    """
    Parse command line parameters
    """
    parser = argparse.ArgumentParser('Bookstore', description='Bookstore application service for Intel@PUT workshop')
    parser.add_argument("-v", "--version", action="version", version=f"{VERSION}")
    parser.add_argument("-s", "--server-host", default=os.environ.get('WORKSHOP_APP_HOST', '0.0.0.0'),
                        help='server host (default 0.0.0.0)')
    parser.add_argument("-p", "--server-port", default=int(os.environ.get('WORKSHOP_APP_PORT', 5000)),
                        type=int, help='server port (default 5000)')
    parser.add_argument("-w", "--server-workers", default=int(os.environ.get('WEB_CONCURRENCY', 1)),
                        type=int, help='number of server workers (default 1)')
    return parser.parse_args()


def main():
    """
    Main application entry point
    """
    args = get_parsed_args()
    create_db_tables()
    uvicorn.run("workshop:app",
            host=args.server_host,
            port=args.server_port,
            workers=args.server_workers,
            )

def __main__():
    main()

if __name__=='__main__':
    main()