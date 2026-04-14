import pytest
from unittest.mock import Mock
from ticket_validator import validate_ticket, get_ticket_tier, calculate_total 


def test_validate_ticket_pass():
    ticket = "TX123456"
    assert validate_ticket(ticket) is True 

def test_invalid_validate_ticket_pass_numbers():
    ticket = "TFA23456"
    assert validate_ticket(ticket) is False

def test_invalid_validate_ticket_pass_string_length():
    ticket = "TX12345"
    assert validate_ticket(ticket) is False

def test_get_ticket_tier():
    ticket = "TX123456"
    assert get_ticket_tier(ticket) == "General"

def test_get_ticket_tier_invalid():
    ticket = "TX12345"
    assert get_ticket_tier(ticket) raise ValueError


    
