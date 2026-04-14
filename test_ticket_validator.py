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
    assert get_ticket_tier(ticket).raises ValueError 

def test_calculate_total_valid():
    pricesList = [100.00, 200.00, 300.00]
    discount = 0 
    assert calculate_total(pricesList) = 600.00

def test_calculate_total_invalid_format():
    pricesList = 300 
    assert calculate_total(pricesList).raises(TypeError)

def test_calculate_total_invalid_format():
    pricesList = [100.00, 200.00, 300.00]
    discount = 1.1  
    assert calculate_total(pricesList, discount).raises(ValueError) 


    
