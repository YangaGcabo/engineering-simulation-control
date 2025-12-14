"""
Stress analysis for mechanical components.

This module estimates normal stress on structural
elements under axial loading.
"""

def normal_stress(force, area):
    """
    sigma = F / A
    """
    return force / area
