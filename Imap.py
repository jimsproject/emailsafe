import imaplib
import ssl
import email  # python email module
from EmailClient import EmailClient
from Email import Email  # my module


class Imap(EmailClient):
    """
    IMAP email client implementation.

    Inherits from EmailClient.

    Args:
        server (str): The IMAP server address.
        port (int): The server port number.
        username (str): The username for authentication.
        password (str): The password for authentication.
        **opt: Additional optional parameters.

    Keyword Args:
        ssl (bool): Set to True to use SSL/TLS. Default is False.

    Raises:
        ConnectionError: If there's an error connecting to the IMAP server.

    Usage:
        imap = Imap(server, port, username, password, ssl=True)
        imap.connect()
        imap.check_connection()
        email_ids = imap.fetch_emails()
        for email_id in email_ids:
            email_obj = imap.fetch_email(email_id)
            # Process the email object
        imap.close()
    """

    def __init__(self, server, port, username, password, **opt):
        super().__init__(server, port, username, password, **opt)

        if "ssl" in opt:
            self._is_ssl = opt['ssl']
        else:
            self._is_ssl = False

        self._connection = None

    def connect(self, path="INBOX"):
        """
        Connects to the IMAP server.

        Args:
            path (str): The mailbox path to connect to. Default is "INBOX".

        Raises:
            ConnectionError: If there's an error connecting to the IMAP server.
        """

        try:
            if self._is_ssl:
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                self._connection = imaplib.IMAP4_SSL(self._server, self._port, ssl_context=context)
            else:
                self._connection = imaplib.IMAP4(self._server, self._port)

            self._connection.login(self._username, self._password)
            self._connection.select(path)  # Select the desired mailbox after logging in

        except imaplib.IMAP4.error as e:
            raise ConnectionError(str(e))

        except Exception as e:
            raise ConnectionError(str(e))

    def fetch_emails(self):
        """
        Fetches the list of email IDs.

        Returns:
            list: A list of email IDs.

        Raises:
            ConnectionError: If the connection to the IMAP server is not established.
        """
        if self._connection is None:
            raise ConnectionError("Connection not established.")

        status, email_ids = self._connection.search(None, "ALL")

        return email_ids[0].split()

    def fetch_email(self, email_id):
        """
        Fetches the email message with the specified ID.

        Args:
            email_id (bytes): The ID of the email message.

        Returns:
            Email: An Email object representing the fetched email.

        Raises:
            ConnectionError: If the connection to the IMAP server is not established.
        """
        if self._connection is None:
            raise ConnectionError("Connection not established.")
        try:
            status, email_data = self._connection.fetch(email_id, "(RFC822)")
            raw_email = email_data[0][1]  # Use index 1 to access email data
            msg = email.message_from_bytes(raw_email)
            return Email(msg)
        except Exception as e:
            raise ConnectionError(str(e))

    def close(self):
        """
        Closes the connection to the IMAP server.

        Raises:
            ConnectionError: If the connection to the IMAP server is not established.
        """
        if self._connection is None:
            raise ConnectionError("Connection not established.")
        self._connection.logout()

    def is_connected(self):
        """
        Checks the connection status to the IMAP server.

        Returns:
            bool: True if connected, False otherwise.
        """
        return self._connection is not None
