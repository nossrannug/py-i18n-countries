# py-i18n-countries
Country names and nationalities for ISO-3166-1 alpha-2 codes: [Wiki](https://en.wikipedia.org/wiki/ISO_3166-1#Officially_assigned_code_elements)

## Install
```
pip install py-i18n-countries
```

## Use
```python
from py_i18n_countries import get_country, get_nationality

print(get_nationality(code="us"))
# American

print(get_country(code="us"))
# United States of America
```