# l2x_synthetic

[![build status](https://github.com/dunnkers/l2x_synthetic/actions/workflows/python-app.yml/badge.svg)](https://github.com/dunnkers/l2x_synthetic/actions/workflows/python-app.yml) [![pypi badge](https://img.shields.io/pypi/v/l2x_synthetic.svg?maxAge=3600)](https://pypi.org/project/l2x_synthetic/)


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

**XORGenerator**
```python
from l2x_synthetic import XORGenerator
```

**Orange Skin generator**
```python
from l2x_synthetic import OrangeGenerator
```

**Non-linear additive generator**
```python
from l2x_synthetic import AdditiveGenerator
```

**Switch generator: combines orange labels and non-linear additive**
```python
from l2x_synthetic import SwitchGenerator
```

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
