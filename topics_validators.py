from abc import ABC
from itertools import product
from pathlib import Path
import re
from attrdict import AttrDict
import pandas as pd
from abc import ABCMeta, abstractmethod
import logging
_log = logging.getLogger(__name__)

class Validator(ABC):
    """
    Validate that the condition logic of an edge (child response) - holds.
    """

    def __init__(self):
        self._processed_input = None

    def validate(self, text: str, **kwargs) -> bool:
        """
        Given the input user, as a single string contains one or more words,
        retrieve boolean indication if the sentence meets the validators logic.

        Parameters
        ----------
        text : str
            The last child's voice transcription
        Returns
        -------
        bool
            True if the edge condition holds, otherwise False
        """
        raise NotImplementedError

    def get_processed_input(self):
        return self._processed_input


if __name__ == "__main__":
    pass
