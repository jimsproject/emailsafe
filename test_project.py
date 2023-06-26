import pytest
from Imap import Imap
from EmlStorage import EmlStorage
from Email import Email
import email.message
from project import parser_args, fetch_inbox, connection
from unittest.mock import patch

server = "imap.gmail.com"
port = 993
username = "cs50.jimmy@gmail.com"
password = "wgmpbbxeamcrdzvr"


# Test for IMAP connection
def test_imap_connection():
    imap = Imap(server, port, username, password, ssl=True)
    imap.connect()
    assert imap.is_connected() == True


def test_imap_connection_fail():
    imap = Imap("wrong_server", port, username, password, ssl=True)
    with pytest.raises(ConnectionError):
        imap.connect()


# Test for email fetching
def test_fetch_email():
    imap = Imap(server, port, username, password, ssl=True)
    imap.connect()
    email_id = b"1"
    email_obj = imap.fetch_email(email_id)
    assert email_obj is not None


def test_fetch_email_fail():
    imap = Imap(server, port, username, password, ssl=True)
    imap.connect()
    wrong_email_id = b"0"
    with pytest.raises(ConnectionError):
        imap.fetch_email(wrong_email_id)


def create_dummy_email():
    dummy_email = {
        'from': 'dummy@example.com',
        'to': 'recipient@example.com',
        'subject': 'Dummy Email',
        'received': 'Mon, 01 Jan 2023 12:00:00 +0000',
        'attachment': False,
        'cc': '',
        'bcc': '',
        'body': 'This is a dummy email body.'
    }

    # Create the email message object
    msg = email.message.Message()
    msg['From'] = dummy_email['from']
    msg['To'] = dummy_email['to']
    msg['Subject'] = dummy_email['subject']
    msg['Date'] = dummy_email['received']
    msg.set_payload(dummy_email['body'])

    return msg


# Test for EmlStorage
def test_save_email():
    email_obj = Email(create_dummy_email())  # Create a dummy email object
    eml_storage = EmlStorage()
    eml_storage.save_email(email_obj)
    # Assert that the email is successfully saved to eml file
    assert eml_storage.file_exists()


# Test for argument parser
def test_argument_parser():
    args = ["--server", "imap.gmail.com", "--port", "993", "--username", "user", "--password", "pass"]
    server, port, username, password = parser_args(args)
    assert server == "imap.gmail.com"
    assert port == 993
    assert username == "user"
    assert password == "pass"


def test_parser_args_fail():
    with pytest.raises(ValueError):
        parser_args([])  # Empty arguments, should raise ValueError


# Test for fetch_inbox function
@patch('EmlStorage.EmlStorage.save_email')
@patch('Imap.Imap.fetch_emails', return_value=[b'1'])
@patch('Imap.Imap.fetch_email')
def test_fetch_inbox(mock_fetch_email, mock_fetch_emails, mock_save_email):
    imap = Imap(server, port, username, password, ssl=True)
    fetch_inbox(imap)
    assert mock_fetch_emails.called
    assert mock_fetch_email.called
    assert mock_save_email.called
