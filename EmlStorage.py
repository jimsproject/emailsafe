from EmailStorage import EmailStorage
import os
from email.header import decode_header


class EmlStorage(EmailStorage):
    """
    Concrete implementation of EmailStorage for saving emails as .eml files.

    Attributes:
        None

    Methods:
        save_email(cls, email):
            Save the email as a .eml file.

        decode_str(encoded_string):
            Decode the encoded string.

        filename(path_backup, email):
            Generate the filename for the email.
    """

    @classmethod
    def save_email(cls, email):
        """
        Save the email as a .eml file.

        The method creates a directory named 'mail' if it does not exist, then writes the raw
        email content to a file with a unique name based on the email sender and subject.

        Args:
            email (Email): The email object to be saved.

        Raises:
            OSError: If there's an error during the directory creation or file writing process.
        """

        path_backup = "mail"
        try:
            os.makedirs(path_backup, exist_ok=True)
            cls.file_name = EmlStorage.filename(path_backup, email)
            if not EmlStorage.file_exists():
                with open(cls.file_name, 'w') as eml_file:
                    eml_file.write(email.raw_email)
        except OSError as e:
            raise OSError()

    @classmethod
    def file_exists(cls):
        """
        Checks if the specified file exists.

        Returns:
           bool: True if the file exists, False otherwise.
        """
        return os.path.isfile(cls.file_name)

    @staticmethod
    def decode_str(encoded_string):
        """
        Decode the encoded string.

        The method takes an encoded string, which may consist of several parts with different encodings,
        decodes each part with the corresponding encoding, and concatenates them into a single string.

        Args:
            encoded_string (str): The encoded string.

        Returns:
            str: The decoded and cleaned string.
        """

        parts = decode_header(encoded_string)
        cleaned_text = ''
        for part in parts:
            if isinstance(part[0], bytes):
                decoded_text = part[0].decode(part[1] or 'utf-8', errors='ignore')
            else:
                decoded_text = part[0]
            cleaned_text += decoded_text
        return cleaned_text

    @staticmethod
    def filename(path_backup, email):
        """
        Generate the filename for the email.

        The method decodes and cleans the sender and subject from the email, then uses these
        to generate a unique filename for the email.

        Args:
            path_backup (str): The backup path directory.
            email (Email): The email object.

        Returns:
            str: The filename for the email, in the format "{cleaned_sender}_{cleaned_subject}.eml".
        """

        cleaned_sender = EmlStorage.decode_str(email.sender)
        cleaned_sender = cleaned_sender.replace("\"", "")
        cleaned_subject = EmlStorage.decode_str(email.subject)
        cleaned_subject = cleaned_subject.replace('\r\n', '')
        cleaned_subject = cleaned_subject.replace("/", "")
        file_name = f"{path_backup}/{cleaned_sender}_{cleaned_subject}.eml"
        return file_name
