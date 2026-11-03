"""
Ocular Microsaccade Rate & Fixational Fatigue Engine.
Provides deterministic, zero-dependency modeling of fixational microsaccade frequency,
main sequence velocity-amplitude kinetics, involuntary ocular drift, and mental vigilance fatigue.
"""

from typing import Dict, Any, List, Optional


class OcularMicrosaccadeRateClient:
    """
    Deterministic client for calculating ocular microsaccade dynamics and fixational stability.
    Assesses superior colliculus burst neuron activity, paramedian pontine reticular formation (PPRF),
    and central nervous system vigilance during sustained visual fixation.
    """

    def __init__(self):
        pass

    def evaluate_microsaccade_dynamics(
        self,
        fixation_duration_sec: float,
        microsaccade_count: int,
        mean_amplitude_deg: float,
        mean_peak_velocity_deg_s: float,
        mean_drift_velocity_deg_s: float = 0.35
    ) -> Dict[str, Any]:
        """
        Calculates microsaccade rate, main sequence velocity ratio, and cognitive alertness score.
        Normative values for alert visual fixation:
        - Microsaccade Rate: 1.2 - 2.8 Hz (drops to < 0.8 Hz during fatigue or microsleep lapses)
        - Mean Amplitude: 0.10 - 0.80 deg
        - Peak Velocity / Amplitude Main Sequence Ratio: 30.0 - 65.0 s^-1
        - Ocular Drift Velocity: < 0.55 deg/s (elevates to > 0.80 deg/s in severe fatigue)
        """
        if fixation_duration_sec <= 0:
            return {"error": "Fixation duration must be strictly positive"}
        if microsaccade_count < 0:
            return {"error": "Microsaccade count cannot be negative"}
        if mean_amplitude_deg <= 0 or mean_peak_velocity_deg_s <= 0:
            return {"error": "Microsaccade amplitude and velocity must be positive"}

        # 1. Microsaccade Rate (Hz)
        rate_hz = round(microsaccade_count / fixation_duration_sec, 2)

        # 2. Main Sequence Ratio Q = Peak_Vel / Amp (s^-1)
        main_seq_ratio = round(mean_peak_velocity_deg_s / mean_amplitude_deg, 1)

        # 3. Fixational Alertness & Ocular Stability Score (0 - 100)
        score = 80.0
        # Rate evaluation
        if 1.2 <= rate_hz <= 2.6:
            score += 10.0
        elif rate_hz < 0.6:
            score -= 28.0
        elif rate_hz < 0.9:
            score -= 15.0
        elif rate_hz > 3.8:
            score -= 10.0  # Hyperactive fixational instability

        # Main sequence slope
        if 32.0 <= main_seq_ratio <= 60.0:
            score += 5.0
        elif main_seq_ratio < 24.0:
            score -= 15.0

        # Drift velocity
        if mean_drift_velocity_deg_s <= 0.45:
            score += 5.0
        elif mean_drift_velocity_deg_s > 0.80:
            score -= 20.0
        elif mean_drift_velocity_deg_s > 0.60:
            score -= 10.0

        alertness_score = round(min(100.0, max(5.0, score)), 1)

        # Classification
        if alertness_score >= 85.0 and rate_hz >= 1.2 and mean_drift_velocity_deg_s <= 0.50:
            tier = "OPTIMAL_FIXATIONAL_VIGILANCE"
            interp = f"Normal fixational microsaccade frequency ({rate_hz} Hz) and tight ocular drift ({mean_drift_velocity_deg_s} deg/s); intact superior colliculus activation."
            guidance = "Optimal cognitive alertness and steady gaze fixation. High mental endurance ready for precision visual focus."
        elif rate_hz >= 0.9 and mean_drift_velocity_deg_s <= 0.65:
            tier = "MILD_FIXATIONAL_DRIFT_FATIGUE"
            interp = f"Modest drop in microsaccade frequency ({rate_hz} Hz); slight elevation in slow drift ({mean_drift_velocity_deg_s} deg/s)."
            guidance = "Incipient ocular fatigue. Consider 60-second far-distance focal horizon shift (20-20-20 rule) to replenish oculomotor tone."
        elif rate_hz < 0.6 or mean_drift_velocity_deg_s > 0.80:
            tier = "SEVERE_MICROSACCADIC_DEPRESSION_DROWSINESS"
            interp = f"Pronounced suppression of microsaccades ({rate_hz} Hz < 0.6 Hz) and prominent ocular drift ({mean_drift_velocity_deg_s} deg/s > 0.80 deg/s); reflects central parasympathetic shift and impending microsleep."
            guidance = "Critical cognitive fatigue detected. Halt high-consequence precision tasks immediately; schedule a restorative 15-20 min nap or ergonomic recess."
        else:
            tier = "ABNORMAL_FIXATIONAL_SACCADIC_INSTABILITY"
            interp = f"Atypical fixational kinematics (Rate {rate_hz} Hz, Main Sequence {main_seq_ratio} s^-1, Drift {mean_drift_velocity_deg_s} deg/s)."
            guidance = "Oculomotor neural integrator instability. Screen for vestibular-ocular mismatch, screen glare, or pharmacological sedation."

        return {
            "fixation_duration_sec": fixation_duration_sec,
            "microsaccade_count": microsaccade_count,
            "microsaccade_rate_hz": rate_hz,
            "mean_amplitude_deg": mean_amplitude_deg,
            "mean_peak_velocity_deg_s": mean_peak_velocity_deg_s,
            "main_sequence_velocity_ratio": main_seq_ratio,
            "mean_drift_velocity_deg_s": mean_drift_velocity_deg_s,
            "fixational_alertness_score": alertness_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
