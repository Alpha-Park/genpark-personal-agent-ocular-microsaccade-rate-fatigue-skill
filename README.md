# Ocular Microsaccade Rate & Fixational Fatigue Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for evaluating ocular fixational microsaccade rate (Hz), main sequence velocity kinetics, involuntary ocular drift, and mental vigilance fatigue.

```mermaid
flowchart TD
    GazeFixation["High-Resolution Visual Fixation Stream"] --> DetectMS["Microsaccade Detection (Amp 0.1-0.8 deg)"]
    DetectMS --> RateCalc["Microsaccade Rate (Hz = Count / Sec)"]
    DetectMS --> MainSeq["Main Sequence Ratio (Q = Vmax / Amp)"]
    GazeFixation --> DriftCalc["Involuntary Inter-Saccadic Slow Drift Velocity"]
    RateCalc & MainSeq & DriftCalc --> VigilanceEngine["Cognitive Alertness & Ocular Fatigue Engine"]
    VigilanceEngine --> Agent["OpenClaw / Hermes Personal Agent Intervention"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Ocular Kinematics Standards**: Implements validated equations for fixational microsaccade frequency, main sequence velocity scaling, and ocular drift velocity.
- **Mental Fatigue & Drowsiness Screening**: Sensitive detection of central vigilance drops and microsleep risks during prolonged cognitive effort.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import OcularMicrosaccadeRateClient

client = OcularMicrosaccadeRateClient()
result = client.evaluate_microsaccade_dynamics(
    fixation_duration_sec=30.0,
    microsaccade_count=54,
    mean_amplitude_deg=0.35,
    mean_peak_velocity_deg_s=15.2,
    mean_drift_velocity_deg_s=0.32
)
print("Microsaccade Rate:", result["microsaccade_rate_hz"], "Hz")
print("Alertness Score:", result["fixational_alertness_score"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
