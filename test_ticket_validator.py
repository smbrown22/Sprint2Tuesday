import pytest
from unittest.mock import Mock
from ticket_validator import validate_ticket, get_ticket_tier, calculate_total 


def test_validate_ticket_pass(code):
    assert validate_ticket(code) is str and len(code) == 8 and code(0 , 1) is 'TX'

