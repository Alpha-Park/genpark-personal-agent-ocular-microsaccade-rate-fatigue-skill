---
name: genpark-personal-agent-ocular-microsaccade-rate-fatigue-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for evaluating ocular fixational microsaccade rate (Hz), main sequence velocity, involuntary ocular drift, and mental vigilance fatigue.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Ocular Microsaccade Rate & Fixational Fatigue Skill

A sovereign personal agent capability for monitoring fixational eye kinematics, microsaccadic rate dynamics, involuntary inter-saccadic drift, and central nervous system vigilance during sustained desk work and screen interaction.

## Core Capabilities
- **Microsaccade Frequency Analysis**: Calculates real-time microsaccadic rate (Hz) across visual fixation intervals, identifying early central fatigue when rate falls below 0.8 Hz.
- **Main Sequence Velocity Ratio**: Formulates the peak velocity to amplitude relationship ($Q = V_{max} / A$ in $\text{s}^{-1}$) to detect brainstem reticular sluggishness.
- **Fixational Slow Drift Tracking**: Detects breakdown of ocular motor neural integration when slow drift velocity exceeds $0.60^\circ/\text{s}$.
- **Autonomous Ergonomic Pacing**: Triggers micro-recesses, lighting corridor adjustments, and far-distance focal transitions to protect sustained cognitive performance.

## Fast Invocation
```python
from client import OcularMicrosaccadeRateClient

client = OcularMicrosaccadeRateClient()
res = client.evaluate_microsaccade_dynamics(
    fixation_duration_sec=30.0,
    microsaccade_count=54,
    mean_amplitude_deg=0.35,
    mean_peak_velocity_deg_s=15.2,
    mean_drift_velocity_deg_s=0.32
)
print("Microsaccade Rate:", res["microsaccade_rate_hz"], "Hz")
print("Alertness Score:", res["fixational_alertness_score"], "/ 100")
```
