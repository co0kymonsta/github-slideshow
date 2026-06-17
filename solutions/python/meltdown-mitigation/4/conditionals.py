"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    if (temperature < 800 
    and neutrons_emitted > 500
    and temperature * neutrons_emitted < 500000):
        return True
    return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    percentage_value = int((generated_power/ theoretical_max_power)*100)

    if (percentage_value) >= 80:
        return 'green'
    if (percentage_value) >= 60 and (percentage_value) < 80:
        return 'orange' 
    if (percentage_value) >= 30 and (percentage_value) < 60:
        return 'red'
    if (percentage_value) < 30:
        return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    if temperature * neutrons_produced_per_second < (0.9 * threshold):
        return 'LOW'
    if (0.9 * threshold) <= (temperature * neutrons_produced_per_second) <= (1.10 * threshold):
        return 'NORMAL'
    return 'DANGER'
    