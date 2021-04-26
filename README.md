# l2x_synthetic

![build status](https://github.com/dunnkers/l2x_synthetic/actions/workflows/python-app.yml/badge.svg)


Exposes synthetic dataset generation code from [L2X](https://arxiv.org/pdf/1802.07814.pdf) as a **pip** package. To install, run:

```shell
pip install -e git+https://github.com/dunnkers/l2x_synthetic.git#egg=l2x_synthetic
```

(in case module cannot be found: try [other methods](https://www.reddit.com/r/Python/comments/2crput/how_to_install_with_pip_directly_from_github/) to install directory from a Github repo.)

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
