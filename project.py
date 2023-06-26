from Imap import Imap
from sys import exit
from EmlStorage import EmlStorage
import argparse
import sys


def parser_args(args=None):
    # parse args
    parser = argparse.ArgumentParser(description="EmailSafe, the ultimate email backup tool provide a seamless and "
                                                 "efficient solution to safeguard your valuable emails.")
    parser.add_argument("--server", help="IMAP server address")
    parser.add_argument("--port", type=int, help="IMAP server port")
    parser.add_argument("--username", help="Username")
    parser.add_argument("--password", help="Password")

    args = parser.parse_args(args)

    if not all(vars(args).values()):
        parser.print_help()
        raise ValueError("not complete argument")

    server = args.server
    port = args.port
    username = args.username
    password = args.password
    return server, port, username, password


def connection(config):
    print("Connect to server ...")
    imap = Imap(config[0], config[1], config[2], config[3], ssl=True)
    imap.connect()
    if imap.is_connected():
        print("Server Connected")
        return imap
    else:
        raise ConnectionError("Fail connect")


def fetch_inbox(imap):
    animation = '/|\\-'  # Animation characters
    # fetch inbox
    i = 1
    try:
        for email_id in imap.fetch_emails():
            email_obj = imap.fetch_email(email_id)
            EmlStorage.save_email(email_obj)
            sys.stdout.write('\r')
            sys.stdout.write('Processing: [{0}] => {1} Email'.format(animation[i % len(animation)], i))
            sys.stdout.flush()
            i += 1
    except OSError:
        raise
    except ConnectionError:
        raise


def main():
    try:
        config = parser_args()
        imap = connection(config)
        fetch_inbox(imap)
        imap.close()
    except ConnectionError as e:
        exit("error : " + str(e))
    except OSError as e:
        exit("error : " + str(e))
    except ValueError as e:
        exit("error : " + str(e))
    except KeyboardInterrupt:
        print("\nTerminated by user")
        sys.exit(0)


if __name__ == "__main__":
    main()
