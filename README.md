
# vecswap 📐

[Ver en Español](doc/README-es.md)

**vecswap** is a lightweight Python library designed for the efficient manipulation, transformation, and filtering of vectors (integer lists). It is ideal for projects requiring simple geometric operations, array logic, or data cleaning without relying on heavy external dependencies.

## 🚀 Installation

Currently, you can use **vecswap** by cloning the repository or copying the `tools.py` file into your project directory:

```bash
git clone https://github.com/OliverOnForge/vecswap.git
```

## 🛠️ Modules and Features

### 1\. Generators

Quickly create vectors with predefined or random values.

  * **`generate_full_int(n, value)`**: Creates a vector of size `n` filled with the integer `value`.
  * **`generate_random_int(n, v_min, v_max)`**: Generates a vector with `n` random integers between `v_min` and `v_max`.
  * **`generate_range_int(start, stop, step)`**: Generates a sequence of integers with a defined increment.

### 2\. Operators & Comparators

Tools for comparing and combining vectors.

  * **`add_vectors` / `subtract_vectors`**: Element-wise addition and subtraction (requires vectors of equal length).
  * **`interleave_from`**: Interleaves a second vector into the first one starting from a specific index.
  * **`matched_indices` / `mismatched_indices`**: Returns a list of indices where values match or differ.
  * **`intersection` / `symmetric_difference`**: Logical set operations to find common or unique elements between two lists.

### 3\. Transformers

Modifies vector data while maintaining its original structure and size.

  * **`normalize`**: Scales all vector values to a numerical range between $[0.0, 1.0]$.
  * **`reflect_vertical(vector, center)`**: Reflects each value vertically using a "center" as the axis (formula: $2 \cdot \text{center} - \text{value}$).
  * **`fill_pattern(vector, value, n, m)`**: Overwrites the vector following a pattern: fills `n` elements and skips `m` positions.

### 4\. Reordering & Structure

Changes the physical arrangement of the elements.

  * **`mirror`**: Reverses the entire order of the vector.
  * **`random_swap(vector, changes)`**: Swaps random positions a specified number of times.
  * **`reflect_on_axis(vector, axis_index)`**: Swaps elements around an index acting as a pivot.

### 5\. Limiters

Ensures values stay within specific numerical bounds.

  * **`clamp(vector, min_val, max_val)`**: Restricts all values to the specified range.
  * **`limit_by_range(vector, center, offset)`**: Keeps values within a distance radius relative to a central value.

-----

## 🗺️ Roadmap

> **Have an idea for a new feature?**
> If there is a vector operation you consider essential, feel free to open an issue or contact me via GitHub.

  * **Visualization**: Implementation of dynamic animations to illustrate the behavior of each transformation and reordering function.
  * **Optimization**: Performance improvements for comparison operations in large-scale vectors.

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create\! Any contribution you make is **greatly appreciated**.

To maintain code quality and project consistency, please review our detailed guidelines before submitting a Pull Request:

👉 **[Read Contributing Guidelines](CONTRIBUTING.md)**

## 📃 License

This project is distributed under the **MIT License**. This means you are free to use, modify, and distribute the software as long as the original license and copyright notice are included.

See the [LICENSE](LICENSE) file for more details.

## 📬 Contact

**OliverOnForge** - [GitHub Profile](https://github.com/OliverOnForge)

-----

### 🧪 Testing

To ensure code stability, you can run the unit test suite from the project root:

```bash
python3 -m unittest test/test.py
```