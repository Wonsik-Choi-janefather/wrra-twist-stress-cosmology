from __future__ import annotations

import copy
import json
import math
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
CODE = ROOT / "code"
sys.path.insert(0, str(CODE))

from reproduce_all import reproduce  # noqa: E402
from twist_stress_model import (  # noqa: E402
    cosmic_stress_fraction,
    dbi_sound_speed_squared_from_ratio,
    dbi_state,
    elliptic_stability_eigenvalues,
    inferred_stress_fraction,
    matched_transition_acceleration,
    representative_loop_size_m,
    solve_dbi_r,
    twist_invariants,
)


def load_inputs() -> dict:
    return json.loads((ROOT / "data" / "inputs.json").read_text(encoding="utf-8"))


class CrossScaleTests(unittest.TestCase):
    def test_forward_cross_scale_value(self) -> None:
        calculated = matched_transition_acceleration(67.4, 0.265, 1.0)
        self.assertAlmostEqual(calculated, 1.1918126691055912e-10, places=24)

    def test_inverse_value(self) -> None:
        calculated = inferred_stress_fraction(67.4, 1.2e-10, 1.0)
        self.assertAlmostEqual(calculated, 0.2686534181618261, places=15)

    def test_external_a0_is_not_a_forward_input(self) -> None:
        inputs_a = load_inputs()
        inputs_b = copy.deepcopy(inputs_a)
        inputs_b["galaxy_comparison"]["comparison_a0_m_s2"] *= 3.0
        result_a = reproduce(inputs_a)
        result_b = reproduce(inputs_b)
        self.assertEqual(
            result_a["cross_scale"]["a_T_m_s2"],
            result_b["cross_scale"]["a_T_m_s2"],
        )


class TwistStructureTests(unittest.TestCase):
    def test_twist_invariants(self) -> None:
        total, chirality = twist_invariants(3.0, 4.0)
        self.assertEqual(total, 25.0)
        self.assertAlmostEqual(chirality, -7.0 / 25.0)

    def test_stress_fraction_identity(self) -> None:
        zeta = 2.0
        alpha = math.sqrt(0.795)
        self.assertAlmostEqual(cosmic_stress_fraction(zeta, alpha), 0.265)

    def test_loop_size_requires_extra_structure(self) -> None:
        # Same f_T gives different loop sizes when zeta or holonomy changes.
        first = representative_loop_size_m(1.0, 1.0, 0.265, 67.4)
        second = representative_loop_size_m(2.0, 1.0, 0.265, 67.4)
        self.assertAlmostEqual(second / first, 2.0)

    def test_elliptic_stability(self) -> None:
        transverse, longitudinal = elliptic_stability_eigenvalues(0.4, 0.2, 0.5)
        self.assertGreater(transverse, 0.0)
        self.assertGreater(longitudinal, 0.0)


class DBIReproductionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.r_value = solve_dbi_r(67.4, 0.265, 22.3, 1.0)

    def test_present_density_normalization(self) -> None:
        self.assertAlmostEqual(self.r_value, 9.9913e-6, delta=3.0e-11)

    def test_recombination_row(self) -> None:
        state = dbi_state(1.0 / 1100.0, self.r_value, 1.0)
        self.assertAlmostEqual(state.q, 0.999999997, delta=2.0e-10)
        self.assertAlmostEqual(state.equation_of_state_w, 3.76e-5, delta=1.0e-8)
        self.assertAlmostEqual(
            state.adiabatic_sound_speed_squared, 2.83e-9, delta=1.0e-11
        )

    def test_today_row(self) -> None:
        state = dbi_state(1.0, self.r_value, 1.0)
        self.assertAlmostEqual(state.q, 9.99e-6, delta=3.0e-9)
        self.assertAlmostEqual(state.equation_of_state_w, 5.00e-6, delta=1.0e-8)
        self.assertAlmostEqual(
            state.adiabatic_sound_speed_squared, 9.99e-6, delta=3.0e-9
        )

    def test_a10_row(self) -> None:
        state = dbi_state(10.0, self.r_value, 1.0)
        self.assertAlmostEqual(state.q, 9.99e-9, delta=3.0e-12)
        self.assertAlmostEqual(state.equation_of_state_w, 5.00e-9, delta=1.0e-11)
        self.assertAlmostEqual(
            state.adiabatic_sound_speed_squared, 9.99e-9, delta=3.0e-12
        )

    def test_scale_dependent_sound_speed_is_suppressed(self) -> None:
        c_ad_squared = 1.0e-5
        c_s_squared = dbi_sound_speed_squared_from_ratio(c_ad_squared, 2.0e6)
        self.assertGreaterEqual(c_s_squared, 0.0)
        self.assertLess(c_s_squared, c_ad_squared)


class CommittedResultTests(unittest.TestCase):
    def test_reference_results_match_current_calculation(self) -> None:
        reference = json.loads(
            (ROOT / "results" / "reference_results.json").read_text(encoding="utf-8")
        )
        current = reproduce(load_inputs())
        self.assertEqual(current, reference)


if __name__ == "__main__":
    unittest.main()
