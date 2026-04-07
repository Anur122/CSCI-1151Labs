"""
Program Name: test_rotation_utils.py
Author: Abdullahi Nur
Purpose: Tests the adjust_rotation function using pytest
Starter Code: rotation_utils.py
Date: April 7, 2026
"""

import pytest
from rotation_utils import adjust_rotation


def test_100():
    assert adjust_rotation(100) == 100


def test_460():
    assert adjust_rotation(460) == 100


def test_820():
    assert adjust_rotation(820) == 100


def test_negative_100():
    assert adjust_rotation(-100) == 260


def test_negative_460():
    assert adjust_rotation(-460) == 260


def test_negative_820():
    assert adjust_rotation(-820) == 260


def test_string_input():
    with pytest.raises(TypeError):
        adjust_rotation("abc")