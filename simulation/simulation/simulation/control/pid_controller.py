"""
PID control logic for hoist and lifting systems.

This reflects basic industrial control behaviour
used in automated cranes and PLC systems.
"""

class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0.0
        self.integral = 0.0

    def compute(self, setpoint, measured):
        error = setpoint - measured
        self.integral += error
        derivative = error - self.prev_error
        self.prev_error = error
        return (
            self.kp * error
            + self.ki * self.integral
            + self.kd * derivative
        )
