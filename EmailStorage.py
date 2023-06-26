from abc import ABC, abstractmethod


class EmailStorage(ABC):
    """
    Abstract base class for email storage.

    This class defines a common interface for storing emails. Subclasses are expected to
    implement the `save_email` method to handle the specifics of storing the email object
    in the desired format/location.
    """

    @classmethod
    @abstractmethod
    def save_email(cls, email):
        """
        Abstract class method to save an email.

        This method should be implemented by subclasses to save the provided email object
        to a desired format/location.

        If the saving process fails, the method should handle the failure gracefully,
        for example by logging an error message and/or raising an appropriate exception.

        Args:
            email (Email): The email object to be saved.

        Raises:
            NotImplementedError: If the method is not implemented by a concrete subclass.
        """

        raise NotImplementedError("Method should implement in subclasses")
