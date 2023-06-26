from abc import ABC, abstractmethod


class EmailClient(ABC):
    """
    Abstract base class for email clients.

    Attributes:
        _server (str): The email server address.
        _port (int): The server port number.
        _username (str): The username for authentication.
        _password (str): The password for authentication.
        _timeout (int): The timeout value for the connection in seconds.

    Note:
        The `EmailClient` class is an abstract base class that defines the interface for email clients.
        Subclasses must implement the abstract methods.

    Usage:
        class MyEmailClient(EmailClient):
            def connect(self):
                # implementation

            def is_connected(self):
                # implementation

            def fetch_emails(self, path="INBOX"):
                # implementation

            def fetch_email(self, email_id):
                # implementation

            def close(self):
                # implementation
    """

    def __init__(self, server, port, username, password, **opt):
        """
        Initializes an EmailClient object.

        Args:
            server (str): The email server address.
            port (int): The server port number.
            username (str): The username for authentication.
            password (str): The password for authentication.
            **opt: Additional optional parameters.

        Keyword Args:
            timeout (int): The timeout value for the connection in seconds. Default is 30 seconds.

        Note:
            The `**opt` parameter allows passing additional optional parameters to customize the client behavior.
        """
        self._server = server
        self._port = port
        self._username = username
        self._password = password
        if 'timeout' in opt:
            self._timeout = opt['timeout']
        else:
            # default value for timeout connection in seconds
            self._timeout = 30

    @abstractmethod
    def connect(self, path="INBOX"):
        """
        Connects to the email server.

        Args:
            path (str): The mailbox path to connect to. Default is "INBOX".

        Raises:
            NotImplementedError: This method must be implemented in subclasses.
        """
        raise NotImplementedError("Method should be implemented in subclasses")

    @abstractmethod
    def is_connected(self):
        """
        Checks if the client is connected to the email server.

        Returns:
            bool: True if connected, False otherwise.

        Raises:
            NotImplementedError: This method must be implemented in subclasses.
        """
        raise NotImplementedError("Method should be implemented in subclasses")

    @abstractmethod
    def fetch_emails(self):
        """
        Fetches the list of email IDs from the specified mailbox.

        Returns:
            list: A list of email IDs.

        Raises:
            NotImplementedError: This method must be implemented in subclasses.
        """
        raise NotImplementedError("Method should be implemented in subclasses")

    @abstractmethod
    def fetch_email(self, email_id):
        """
        Fetches the email message with the specified ID.

        Args:
            email_id (str): The ID of the email message.

        Returns:
            Email: An Email object representing the fetched email.

        Raises:
            NotImplementedError: This method must be implemented in subclasses.
        """
        raise NotImplementedError("Method should be implemented in subclasses")

    @abstractmethod
    def close(self):
        """
        Closes the connection to the email server.

        Raises:
            NotImplementedError: This method must be implemented in subclasses.
        """
        raise NotImplementedError("Method should be implemented in subclasses")
