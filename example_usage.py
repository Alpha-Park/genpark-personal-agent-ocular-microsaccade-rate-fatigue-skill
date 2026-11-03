"""
Example Usage: Ocular Microsaccade Rate & Fixational Fatigue.
Demonstrates zero-dependency calculation of fixational microsaccade frequency, main sequence ratio, and vigilance fatigue scoring.
"""

from client import OcularMicrosaccadeRateClient


def main():
    client = OcularMicrosaccadeRateClient()
    print("=== Ocular Microsaccade Rate & Fixational Fatigue Demo ===")

    # Test Case 1: Alert, focused individual during sustained fixation
    res1 = client.evaluate_microsaccade_dynamics(
        fixation_duration_sec=30.0,
        microsaccade_count=54,
        mean_amplitude_deg=0.35,
        mean_peak_velocity_deg_s=15.2,
        mean_drift_velocity_deg_s=0.32
    )
    print("\nTest Case 1: Alert High-Vigilance Fixation")
    print(f"  Fixation Duration: {res1['fixation_duration_sec']} s | Microsaccades: {res1['microsaccade_count']}")
    print(f"  Rate: {res1['microsaccade_rate_hz']} Hz | Main Sequence Ratio: {res1['main_sequence_velocity_ratio']} s^-1")
    print(f"  Drift Velocity: {res1['mean_drift_velocity_deg_s']} deg/s")
    print(f"  Alertness Score: {res1['fixational_alertness_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Physiological Interpretation: {res1['physiological_interpretation']}")
    print(f"  Actionable Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Severe cognitive fatigue / drowsiness suppression
    res2 = client.evaluate_microsaccade_dynamics(
        fixation_duration_sec=30.0,
        microsaccade_count=12,
        mean_amplitude_deg=0.22,
        mean_peak_velocity_deg_s=5.1,
        mean_drift_velocity_deg_s=0.88
    )
    print("\nTest Case 2: Cognitive Fatigue & Drowsiness Pattern")
    print(f"  Rate: {res2['microsaccade_rate_hz']} Hz | Drift Velocity: {res2['mean_drift_velocity_deg_s']} deg/s")
    print(f"  Alertness Score: {res2['fixational_alertness_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Actionable Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
