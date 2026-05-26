# Simulador de Dark Pools e Impacto de Mercado

Modelo estatístico de liquidez oculta — slippage para ordens institucionais vs TWAP/VWAP.

## Stack

- Python, SciPy, Ray

## Matemática do impacto

Modelo Almgren-Chriss simplificado:

```
S(t) = S₀ + γ · v(t) + η · ∫ v(τ) dτ + σ · W(t)
```

- `γ`: impacto temporário
- `η`: impacto permanente
- Dark pool: fração `φ` da liquidez não visível no book

Calibração: [docs/CALIBRATION.md](docs/CALIBRATION.md)

## Uso

```bash
pip install -r requirements.txt
python -m src.simulate --volume 1e6 --mode twap --dark-pool-phi 0.4
```

## Saídas

- Curva de slippage esperado
- Fronteira eficiente (risco vs custo de execução)
- Gráficos em `output/`

## Estrutura

| Pasta | Função |
|-------|--------|
| `src/model/` | Impacto estocástico |
| `src/execution/` | TWAP, VWAP, block |
| `src/viz/` | Plotly/matplotlib |
