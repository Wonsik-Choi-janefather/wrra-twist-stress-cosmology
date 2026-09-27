#!/usr/bin/env python3
"""Reproduce the declared numerical results and emit an auditable JSON ledger."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from twist_stress_model import (
    cosmic_acceleration,
    dbi_density_target,
    dbi_state,
    deep_low_acceleration_response,
    hubble_si,
    inferred_stress_fraction,
    matched_transition_acceleration,
    relative_difference,
    solve_dbi_r,
)


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def reproduce(inputs: dict[str, Any]) -> dict[str, Any]:
    cosmology = inputs["cosmology"]
    galaxy = inputs["galaxy_comparison"]
    dbi = inputs["dbi_imported_scaffold"]

    h0 = float(cosmology["H0_km_s_Mpc"])
    f_t = float(cosmology["f_T"])
    response_constant = float(cosmology["matched_response_C"])
    a_t = matched_transition_acceleration(h0, f_t, response_constant)
    comparison_a0 = float(galaxy["comparison_a0_m_s2"])
    paper_round_a0 = float(galaxy["paper_rounded_a0_m_s2"])

    r_exact = solve_dbi_r(
        h0_km_s_mpc=h0,
        omega_stress_today=float(dbi["omega_stress_today"]),
        mu_inverse_mpc=float(dbi["mu_inverse_Mpc"]),
        lambda_d=float(dbi["lambda_D"]),
    )

    states: dict[str, Any] = {}
    for label, scale_factor in dbi["scale_factors"].items():
        states[label] = dbi_state(
            scale_factor=float(scale_factor),
            r=r_exact,
            lambda_d=float(dbi["lambda_D"]),
        ).to_dict()

    samples: list[dict[str, float]] = []
    for g_b in inputs["galaxy_deep_limit_demo"]["g_b_m_s2"]:
        g_b_float = float(g_b)
        samples.append(
            {
                "g_b_m_s2": g_b_float,
                "g_predicted_m_s2": deep_low_acceleration_response(g_b_float, a_t),
            }
        )

    return {
        "schema_version": "1.0",
        "deterministic": True,
        "evaluation_chain": {
            "verified_input": [
                "H0, f_T, C=1, exact SI unit conversion",
                "external comparison a0 is withheld from the forward calculation",
                "mu^-1, lambda_D, and the present density fraction for the imported DBI check",
            ],
            "wrra_specific_transformation": [
                "interpret the effective dark component as a twist-stress mass phenotype",
                "apply the matched-response relation a_T=C c H0 sqrt(f_T/8)",
                "apply the same a_T to the low-acceleration renderer",
            ],
            "outputs": [
                "cross-scale transition acceleration and inverse f_T",
                "deep-limit RAR samples",
                "DBI background q, w, and c_ad^2 at declared scale factors",
            ],
            "falsification_conditions": [
                "independent H0, f_T, and galaxy a_T fail the C=1 relation beyond their uncertainties",
                "one shared a_T cannot jointly maintain RAR and BTFR across galaxies",
                "a covariant completion produces unacceptable lensing slip, CMB spectra, growth, or cluster dynamics",
                "the committed calculations cannot be regenerated from the declared inputs",
            ],
        },
        "cross_scale": {
            "H0_s_inverse": hubble_si(h0),
            "cH0_m_s2": cosmic_acceleration(h0),
            "f_T_input": f_t,
            "matched_response_C": response_constant,
            "a_T_m_s2": a_t,
            "external_comparison_a0_m_s2": comparison_a0,
            "external_comparison_relative_difference": relative_difference(
                a_t, comparison_a0
            ),
            "external_comparison_percent_difference": 100.0
            * relative_difference(a_t, comparison_a0),
            "inferred_f_T_from_paper_rounded_a0": inferred_stress_fraction(
                h0, paper_round_a0, response_constant
            ),
            "claim_boundary": (
                "The forward value uses H0 and f_T, not the galaxy comparison value. "
                "It is a conditional WRRA closure under matched response C=1, not a "
                "parameter-free cosmological fit."
            ),
        },
        "galaxy_deep_limit_demo": {
            "equation": "g=sqrt(a_T*g_b)",
            "samples": samples,
            "claim_boundary": (
                "These are transparent equation samples, not a fit to the SPARC catalogue."
            ),
        },
        "dbi_imported_scaffold": {
            "provenance": (
                "Imported covariant Khronon/DBI calculation scaffold; it is not claimed "
                "as an original WRRA field-equation derivation."
            ),
            "density_target_D": dbi_density_target(
                h0,
                float(dbi["omega_stress_today"]),
                float(dbi["mu_inverse_Mpc"]),
            ),
            "r_exact": r_exact,
            "r_reported_rounded": float(dbi["r_reported_rounded"]),
            "lambda_D": float(dbi["lambda_D"]),
            "states": states,
            "claim_boundary": (
                "This reproduces the stated minimal background/sound-speed survival "
                "check; it does not replace a Boltzmann-code CMB likelihood analysis."
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--inputs",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "data" / "inputs.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "reproduced"
        / "reproduction_results.json",
    )
    args = parser.parse_args()
    result = reproduce(load_json(args.inputs))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
