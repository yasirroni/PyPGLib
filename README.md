# PyPGLib

PyPGLib: A Python Package for Easy Access to Power Grid Lib Benchmark

Current Version: v0.0.2 (1 October 2024)

| Original Repository                                                   | Version in This Package                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| [pglib-opf](https://github.com/power-grid-lib/pglib-opf)              | [v23.07](https://github.com/power-grid-lib/pglib-opf/releases/tag/v23.07)         |
| [pglib-uc](https://github.com/power-grid-lib/pglib-uc)                | [v19.08](https://github.com/power-grid-lib/pglib-uc/releases/tag/v19.08)          |
| [pglib-opf-hvdc](https://github.com/power-grid-lib/pglib-opf-hvdc)    | [v23.09](https://github.com/power-grid-lib/pglib-opf-hvdc/releases/tag/v23.09)    |

## Installation

```shell
pip install pypglib
```

## Usage

Combined with [`matpower-pip`](https://github.com/yasirroni/matpower-pip):

```python
from matpower import start_instance
from pypglib import pglib_opf_case14_ieee


m = start_instance()
m.runpf(pglib_opf_case14_ieee)
```

<!-- Combined with [`PyOPF`](https://github.com/seonho-park/PyOPF):

```python
import opf
from pypglib import pglib_opf_case14_ieee

model = opf.build_model('acopf')
network = opf.parse_file(pglib_opf_case14_ieee)
model.instantiate(network)
result = model.solve(solver_option={'print_level' : 5, 'linear_solver': 'ma27'}, tee=True)
``` -->
