class Email:
    """
    Represents an email message.

    Attributes:
        sender (str): The sender of the email.
        subject (str): The subject of the email.
        raw_email (str): The raw email content.

    Note:
        The `sender` and `subject` properties are used to get and set the corresponding attributes.
        The `raw_email` property is used to get and set the raw email content as a string.

    Usage:
        email = Email(msg)
        email.sender = "john@example.com"
        email.subject = "Hello, World!"
        email.raw_email = "..."
    """

    def __init__(self, msg):
        """
        Initializes an Email object.

        Args:
            msg (Message): The email message object.

        Note:
            The `msg` parameter should be an instance of the `Message` class from the `email` module.
        """
        self.sender = msg['from']
        self.subject = msg['subject']
        self.raw_email = msg.as_string()

    @property
    def sender(self):
        """
        str: The sender of the email.

        Note:
            This property provides access to the `_sender` attribute.
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """
        Setter for the sender property.

        Args:
            sender (str): The sender email address.

        Note:
            This method sets the `_sender` attribute of the email address.
        """
        # todo: validate email
        self._sender = sender

    @property
    def subject(self):
        """
        str: The subject of the email.

        Note:
            This property provides access to the `_subject` attribute.
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Setter for the subject property.

        Args:
            subject (str): The subject of the email.

        Note:
            This method sets the `_subject` attribute.
        """
        self._subject = subject

    @property
    def raw_email(self):
        """
        str: The raw email content.

        Note:
            This property provides access to the `_raw_email` attribute.
        """
        return self._raw_email

    @raw_email.setter
    def raw_email(self, raw_email):
        """
        Setter for the raw_email property.

        Args:
            raw_email (str): The raw email content.

        Note:
            This method sets the `_raw_email` attribute.
        """
        self._raw_email = raw_email
