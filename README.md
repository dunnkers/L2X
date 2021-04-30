# l2x_synthetic

[![build status](https://github.com/dunnkers/l2x_synthetic/actions/workflows/python-app.yml/badge.svg)](https://github.com/dunnkers/l2x_synthetic/actions/workflows/python-app.yml) [![pypi badge](https://img.shields.io/pypi/v/l2x_synthetic.svg?maxAge=3600)](https://pypi.org/project/l2x_synthetic/)


Exposes synthetic dataset generation code from [L2X](https://arxiv.org/pdf/1802.07814.pdf) as a **pip** package. To install, run:

```shell
pip install l2x_synthetic
```

You can now create the synthetic datasets like:

```python
from l2x_synthetic.make_data import generate_data
X, y = generate_data(n=1000, datatype='orange_skin', seed=0)
```

✨

## API
`generate_data` function:

```python
def generate_data(
    n: int = 100,
    datatype: str = '',
    seed:int = 0,
    as_frame: bool = False
)
```

As a `datatype` you can input:
- `orange_skin`
- `nonlinear_additive`
- `XOR`
- `switch`

## Dependencies
```shell
pip install -r requirements.txt
```

## About
See the original repo:

[https://github.com/Jianbo-Lab/L2X/](https://github.com/Jianbo-Lab/L2X/)
