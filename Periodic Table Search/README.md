# Periodic Table Element Lookup

A simple Python utility to look up information about chemical elements. You can search by **element symbol**, **element name**, or **group**. The function returns the element's **name**, **atomic weight**, and **group**.

---

## Features

- Lookup by:
  - Symbol (e.g., `H`, `He`, `Na`)
  - Name (e.g., `Hydrogen`, `Helium`, `Sodium`)
  - Group (e.g., `Alkali metals`, `Noble gases`)
- Covers all **118 elements** of the periodic table.
- Easy to extend with additional properties if needed.

---

## Usage

```python
from element_lookup import element_info

# Lookup by symbol
print(element_info("O"))
# Output:
# Element: Oxygen
# Atomic weight: 16.00
# Group: Nonmetals

# Lookup by name
print(element_info("Sodium"))

# Lookup by group
print(element_info("Noble gases"))
