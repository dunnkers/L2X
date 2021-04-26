# L2X synthetic datasets

Code to generate synthetic datasets from [L2X](https://arxiv.org/pdf/1802.07814.pdf) available as a **pip** package. To install, run:

```shell
pip install git+https://github.com/dunnkers/L2X.git
```

You can now create the synthetic datasets like:

```python
from l2x_synthetic.make_data import generate_data
X, y, datatypes = generate_data(n=1000, datatype='orange_skin', seed=0)
```

As a `datatype` you can input:
- `orange_skin`
- `nonlinear_additive`
- `XOR`
- `switch`

## Dependencies
Requires:
- `numpy`

## About
See the original repo:

[https://github.com/Jianbo-Lab/L2X/](https://github.com/Jianbo-Lab/L2X/)
