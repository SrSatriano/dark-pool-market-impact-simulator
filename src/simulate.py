"""Simulação de impacto de mercado com dark pool."""

from __future__ import annotations

import argparse
import numpy as np
from scipy.stats import norm


def expected_slippage(
    volume: float,
    adv: float,
    volatility: float,
    phi_dark: float,
    temporary_gamma: float = 0.1,
) -> float:
    """Slippage esperado (bps) — modelo heurístico calibrável."""
    participation = volume / max(adv, 1.0)
    visible_liquidity = 1.0 - phi_dark
    impact = temporary_gamma * participation / visible_liquidity
    noise = volatility * norm.ppf(0.95) * np.sqrt(participation)
    return (impact + noise) * 1e4  # bps


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--volume", type=float, default=1_000_000)
    p.add_argument("--adv", type=float, default=10_000_000)
    p.add_argument("--mode", choices=["block", "twap", "vwap"], default="block")
    p.add_argument("--dark-pool-phi", type=float, default=0.35)
    args = p.parse_args()

    mult = {"block": 1.0, "twap": 0.55, "vwap": 0.45}[args.mode]
    slip = expected_slippage(args.volume * mult, args.adv, 0.02, args.dark_pool_phi)
    print(f"mode={args.mode} expected_slippage_bps={slip:.2f}")


if __name__ == "__main__":
    main()
