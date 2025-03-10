# l2x_synthetic

[![build status](https://github.com/dunnkers/l2x_synthetic/actions/workflows/python-app.yml/badge.svg)](https://github.com/dunnkers/l2x_synthetic/actions/workflows/python-app.yml) [![pypi badge](https://img.shields.io/pypi/v/l2x_synthetic.svg?maxAge=3600)](https://pypi.org/project/l2x_synthetic/) [![Downloads](https://pepy.tech/badge/l2x-synthetic)](https://pepy.tech/project/l2x-synthetic)


Exposes synthetic dataset generation code from [L2X](https://arxiv.org/pdf/1802.07814.pdf) as a **pip** package. To install, run:

```shell
pip install l2x-synthetic
```

You can now create the synthetic datasets like:

```python
from l2x_synthetic import XORGenerator
generator = XORGenerator(n_samples=100)
X, y = generator.get_data()
```

Which generates new data every time you call `get_data()` ✨. Use `random_state` to create reproducible data generation.

## API
Available generators:

### **XORGenerator**
```python
from l2x_synthetic import XORGenerator
```

Relevant features: `[0, 1]`

### Orange Skin generator
```python
from l2x_synthetic import OrangeGenerator
```

Relevant features: `[0, 1, 2, 3]`

### Non-linear additive generator
```python
from l2x_synthetic import AdditiveGenerator
```

Relevant features: `[0, 1, 2, 3]`

### Switch generator: combines orange labels and non-linear additive
```python
from l2x_synthetic import SwitchGenerator
```

Relevant features for `X[:n//2]` (first 1/2 of dataset): `[0, 1, 2, 3]`

Relevant features for `X[n//2:]` (second 1/2 of dataset): `[4, 5, 6, 7]`

### Generator API

All generators are of the following type:

```python
class l2x_synthetic.DataGenerator:
    name: str = None # contains a human-friendly name for the generator.
    n_samples: int = 100
    random_state: Optional[int] = None

    def get_data(self) -> Tuple[np.ndarray, np.ndarray]:
        ...

    def get_dataframe(self) -> pd.DataFrame:
        ...

```


## Development dependencies
```shell
pip install -r requirements.txt
```

## About
See the original repo:

[https://github.com/Jianbo-Lab/L2X/](https://github.com/Jianbo-Lab/L2X/)
