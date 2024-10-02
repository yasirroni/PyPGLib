# PyPGLib

[![PyPI version](https://badge.fury.io/py/pypglib.svg)](https://pypi.org/project/pypglib/)

PyPGLib: A Python Package for Easy Access to Power Grid Lib Benchmark

Latest update: 2 October 2024

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

To loop to all test files:

```python
import glob
import os

from pypglib import PATH_PYPGLIB


opf_dir = os.path.join(PATH_PYPGLIB, "opf")
for file_path in glob.glob(os.path.join(opf_dir, "**", "*.m"), recursive=True):
    print(file_path)
```

To print all the case versions

```python
from pypglib import (
    __VERSION_PYPGLIB_HVDC__,
    __VERSION_PYPGLIB_OPF__,
    __VERSION_PYPGLIB_UC__,
    __version__,
)


print(__VERSION_PYPGLIB_HVDC__)
print(__VERSION_PYPGLIB_OPF__)
print(__VERSION_PYPGLIB_UC__)
print(__version__)
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
