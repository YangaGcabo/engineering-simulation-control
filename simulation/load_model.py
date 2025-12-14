"""
Load modelling for mechanical lifting systems.

This module computes basic lifting forces using
classical mechanics principles. It reflects how
loads act on crane structures during operation.
"""

def lifting_force(mass_kg, gravity=9.81):
    """
    Calculate lifting force using F = m * g
    """
    return mass_kg * gravity
