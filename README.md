# PyPGLib

PyPGLib: A Python Package for Easy Access to Power Grid Lib Benchmark

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
