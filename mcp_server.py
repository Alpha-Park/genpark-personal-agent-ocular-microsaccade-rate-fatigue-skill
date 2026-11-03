"""
MCP Server for Ocular Microsaccade Rate & Fixational Fatigue Skill.
Exposes JSON-RPC Model Context Protocol tools for evaluating microsaccadic frequency, main sequence velocity, and alertness scores.
"""

import sys
import json
from typing import Dict, Any
from client import OcularMicrosaccadeRateClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_microsaccade_dynamics",
                "description": "Calculates ocular microsaccade rate (Hz), main sequence velocity-amplitude ratio, fixational drift, and cognitive alertness score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "fixation_duration_sec": {
                            "type": "number",
                            "description": "Duration of sustained eye tracking / visual fixation in seconds (e.g. 30.0 s)."
                        },
                        "microsaccade_count": {
                            "type": "integer",
                            "description": "Total detected fixational microsaccades during the fixation interval (e.g. 54)."
                        },
                        "mean_amplitude_deg": {
                            "type": "number",
                            "description": "Average amplitude of microsaccades in degrees of visual angle (e.g. 0.35 deg, normative 0.1 - 0.8 deg)."
                        },
                        "mean_peak_velocity_deg_s": {
                            "type": "number",
                            "description": "Average peak angular velocity of microsaccades in degrees per second (e.g. 15.0 deg/s)."
                        },
                        "mean_drift_velocity_deg_s": {
                            "type": "number",
                            "description": "Average slow inter-saccadic fixational drift velocity in degrees per second (default: 0.35 deg/s).",
                            "default": 0.35
                        }
                    },
                    "required": ["fixation_duration_sec", "microsaccade_count", "mean_amplitude_deg", "mean_peak_velocity_deg_s"]
                }
            }
        ]
    }


def handle_request(client: OcularMicrosaccadeRateClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_microsaccade_dynamics":
            res = client.evaluate_microsaccade_dynamics(
                fixation_duration_sec=float(args.get("fixation_duration_sec", 30.0)),
                microsaccade_count=int(args.get("microsaccade_count", 54)),
                mean_amplitude_deg=float(args.get("mean_amplitude_deg", 0.35)),
                mean_peak_velocity_deg_s=float(args.get("mean_peak_velocity_deg_s", 15.0)),
                mean_drift_velocity_deg_s=float(args.get("mean_drift_velocity_deg_s", 0.35))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {name}"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": f"Invalid Request: Unsupported method {method}"
            }
        }


def main():
    client = OcularMicrosaccadeRateClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32700,
                    "message": f"Parse error or exception: {str(e)}"
                }
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
