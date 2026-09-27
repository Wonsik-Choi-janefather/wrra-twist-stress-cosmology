"""Deterministic equations used in the WRRA twist-stress reproduction package.

The module intentionally depends only on the Python standard library.  It
separates equations original to the twist-stress interpretation from the
imported AQUAL/MOND and Khronon/DBI calculation scaffolds.  That distinction is
part of the scientific ledger, not an implementation detail.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import math


SPEED_OF_LIGHT_M_S = 299_792_458.0
SPEED_OF_LIGHT_KM_S = SPEED_OF_LIGHT_M_S / 1_000.0
MPC_M = 3.085_677_581_491_367_3e22
GRAVITATIONAL_CONSTANT_SI = 6.67430e-11


def _positive(name: str, value: float) -> None:
    if not math.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be finite and positive; got {value!r}")


def hubble_si(h0_km_s_mpc: float) -> float:
    """Convert H0 from km s^-1 Mpc^-1 to s^-1."""

    _positive("h0_km_s_mpc", h0_km_s_mpc)
    return h0_km_s_mpc * 1_000.0 / MPC_M


def cosmic_acceleration(h0_km_s_mpc: float) -> float:
    """Return c H0 in m s^-2."""

    return SPEED_OF_LIGHT_M_S * hubble_si(h0_km_s_mpc)


def matched_transition_acceleration(
    h0_km_s_mpc: float,
    stress_fraction: float,
    response_constant: float = 1.0,
) -> float:
    r"""Equation 16: a_T = C c H0 sqrt(f_T / 8)."""

    _positive("stress_fraction", stress_fraction)
    _positive("response_constant", response_constant)
    return (
        response_constant
        * cosmic_acceleration(h0_km_s_mpc)
        * math.sqrt(stress_fraction / 8.0)
    )


def inferred_stress_fraction(
    h0_km_s_mpc: float,
    transition_acceleration_m_s2: float,
    response_constant: float = 1.0,
) -> float:
    r"""Invert equation 16: f_T = 8[a_T/(C c H0)]^2."""

    _positive("transition_acceleration_m_s2", transition_acceleration_m_s2)
    _positive("response_constant", response_constant)
    denominator = response_constant * cosmic_acceleration(h0_km_s_mpc)
    return 8.0 * (transition_acceleration_m_s2 / denominator) ** 2


def relative_difference(value: float, reference: float) -> float:
    """Return |value-reference|/|reference|."""

    _positive("reference", abs(reference))
    return abs(value - reference) / abs(reference)


def twist_invariants(kappa_plus: float, kappa_minus: float) -> tuple[float, float]:
    r"""Equation 7: total twist magnitude and chirality.

    Returns (kappa_squared, chi_T), where
    kappa_squared = kappa_plus^2 + kappa_minus^2 and
    chi_T = (kappa_plus^2-kappa_minus^2)/kappa_squared.
    """

    if not math.isfinite(kappa_plus) or not math.isfinite(kappa_minus):
        raise ValueError("twist components must be finite")
    total = kappa_plus**2 + kappa_minus**2
    if total == 0.0:
        raise ValueError("chirality is undefined for zero total twist")
    return total, (kappa_plus**2 - kappa_minus**2) / total


def twist_energy_density_j_m3(zeta: float, kappa_squared_m2: float) -> float:
    r"""Equation 9: u_T = zeta c^4 kappa^2/(16 pi G)."""

    _positive("zeta", zeta)
    if not math.isfinite(kappa_squared_m2) or kappa_squared_m2 < 0.0:
        raise ValueError("kappa_squared_m2 must be finite and non-negative")
    return (
        zeta
        * SPEED_OF_LIGHT_M_S**4
        * kappa_squared_m2
        / (16.0 * math.pi * GRAVITATIONAL_CONSTANT_SI)
    )


def cosmic_stress_fraction(zeta: float, alpha: float) -> float:
    r"""Equation 10: f_T = zeta alpha^2/6."""

    _positive("zeta", zeta)
    if not math.isfinite(alpha):
        raise ValueError("alpha must be finite")
    return zeta * alpha**2 / 6.0


def representative_loop_size_m(
    holonomy: float,
    zeta: float,
    stress_fraction: float,
    h0_km_s_mpc: float,
) -> float:
    r"""Equation 8: L_gamma = |Theta| c/H0 sqrt[zeta/(6 f_T)]."""

    if not math.isfinite(holonomy):
        raise ValueError("holonomy must be finite")
    _positive("zeta", zeta)
    _positive("stress_fraction", stress_fraction)
    return (
        abs(holonomy)
        * SPEED_OF_LIGHT_M_S
        / hubble_si(h0_km_s_mpc)
        * math.sqrt(zeta / (6.0 * stress_fraction))
    )


def deep_low_acceleration_response(
    baryonic_acceleration_m_s2: float,
    transition_acceleration_m_s2: float,
) -> float:
    r"""Equation 14 deep-limit RAR: g = sqrt(a_T g_b)."""

    if baryonic_acceleration_m_s2 < 0.0:
        raise ValueError("baryonic acceleration must be non-negative")
    _positive("transition_acceleration_m_s2", transition_acceleration_m_s2)
    return math.sqrt(
        baryonic_acceleration_m_s2 * transition_acceleration_m_s2
    )


def btfr_velocity_fourth_m4_s4(
    baryonic_mass_kg: float,
    transition_acceleration_m_s2: float,
) -> float:
    r"""Equation 14 BTFR: v_f^4 = G M_b a_T."""

    _positive("baryonic_mass_kg", baryonic_mass_kg)
    _positive("transition_acceleration_m_s2", transition_acceleration_m_s2)
    return (
        GRAVITATIONAL_CONSTANT_SI
        * baryonic_mass_kg
        * transition_acceleration_m_s2
    )


def elliptic_stability_eigenvalues(
    mu: float, x: float, derivative_mu_x: float
) -> tuple[float, float]:
    r"""Equation 15: lambda_perp=mu, lambda_parallel=mu+x mu'."""

    if not all(math.isfinite(v) for v in (mu, x, derivative_mu_x)):
        raise ValueError("stability inputs must be finite")
    return mu, mu + x * derivative_mu_x


def dbi_density_target(
    h0_km_s_mpc: float,
    omega_stress_today: float,
    mu_inverse_mpc: float,
) -> float:
    r"""Dimensionless right side of the exact present-density equation.

    Dividing Eq. 100 of the imported Khronon/DBI scaffold by 2 mu^2
    gives D = (3/2) Omega_K,0 (H0 mu^-1 / c)^2 after restoring c.
    """

    _positive("omega_stress_today", omega_stress_today)
    _positive("mu_inverse_mpc", mu_inverse_mpc)
    scale_ratio = h0_km_s_mpc * mu_inverse_mpc / SPEED_OF_LIGHT_KM_S
    return 1.5 * omega_stress_today * scale_ratio**2


def solve_dbi_r(
    h0_km_s_mpc: float,
    omega_stress_today: float,
    mu_inverse_mpc: float,
    lambda_d: float,
    iterations: int = 100,
) -> float:
    r"""Solve the exact Eq. 100 normalization for r=I0/(2 mu^2).

    The dimensionless equation is
      r + [sqrt(1 + lambda_D r^2)-1]/lambda_D = D.
    It is monotone for r>=0, so bisection is deterministic.
    """

    _positive("lambda_d", lambda_d)
    if iterations < 1:
        raise ValueError("iterations must be positive")
    target = dbi_density_target(
        h0_km_s_mpc, omega_stress_today, mu_inverse_mpc
    )
    low, high = 0.0, target
    for _ in range(iterations):
        midpoint = (low + high) / 2.0
        lhs = midpoint + (
            math.sqrt(1.0 + lambda_d * midpoint**2) - 1.0
        ) / lambda_d
        if lhs < target:
            low = midpoint
        else:
            high = midpoint
    return (low + high) / 2.0


@dataclass(frozen=True)
class DBIState:
    scale_factor: float
    z: float
    q: float
    equation_of_state_w: float
    adiabatic_sound_speed_squared: float

    def to_dict(self) -> dict[str, float]:
        return asdict(self)


def dbi_state(scale_factor: float, r: float, lambda_d: float) -> DBIState:
    r"""Equations 23-24 / imported Khronon Eqs. 101-103.

    The Z form is used for numerical stability:
      Z = r/a^3,
      q = Z/sqrt(1+lambda_D Z^2).
    """

    _positive("scale_factor", scale_factor)
    _positive("r", r)
    _positive("lambda_d", lambda_d)
    z = r / scale_factor**3
    root = math.sqrt(1.0 + lambda_d * z**2)
    q = z / root
    w = z / (1.0 + lambda_d * z**2 + (1.0 + z) * root)
    c_ad_squared = z / ((1.0 + lambda_d * z**2) * (root + z))
    return DBIState(
        scale_factor=scale_factor,
        z=z,
        q=q,
        equation_of_state_w=w,
        adiabatic_sound_speed_squared=c_ad_squared,
    )


def dbi_sound_speed_squared_from_ratio(
    adiabatic_sound_speed_squared: float,
    k2_over_4pi_g_a2_rho_1pw: float,
) -> float:
    r"""Equation 25 using a dimensionless, consistently unitized ratio.

    The second argument denotes k^2/[4 pi G a^2 rho_T (1+w)] in one
    consistent unit convention. Keeping that combination explicit prevents an
    accidental mixture of SI and the c=1 convention used by the source
    equation.
    """

    if adiabatic_sound_speed_squared < 0.0:
        raise ValueError("adiabatic sound speed squared must be non-negative")
    if (
        not math.isfinite(k2_over_4pi_g_a2_rho_1pw)
        or k2_over_4pi_g_a2_rho_1pw < 0.0
    ):
        raise ValueError("the scale ratio must be finite and non-negative")
    return adiabatic_sound_speed_squared / (
        1.0
        + adiabatic_sound_speed_squared * k2_over_4pi_g_a2_rho_1pw
    )
