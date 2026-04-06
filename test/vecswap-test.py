
import unittest
import random
from tools import (
    generate_full_int, generate_random_int, add_vectors, 
    subtract_vectors, are_equal, normalize, 
    clamp, mirror, reflect_on_axis
)

class TestVecSwap(unittest.TestCase):

    # --- Tests de Generadores ---
    def test_generate_full_int(self):
        result = generate_full_int(5, 10)
        self.assertEqual(result, [10, 10, 10, 10, 10])
        self.assertEqual(len(result), 5)

    def test_generate_random_int(self):
        n, v_min, v_max = 10, 1, 5
        result = generate_random_int(n, v_min, v_max)
        self.assertEqual(len(result), n)
        for x in result:
            self.assertTrue(v_min <= x <= v_max)

    # --- Tests de Operadores ---
    def test_add_vectors(self):
        v1 = [1, 2, 3]
        v2 = [4, 5, 6]
        self.assertEqual(add_vectors(v1, v2), [5, 7, 9])
        
        with self.assertRaises(ValueError):
            add_vectors([1, 2], [1, 2, 3])

    def test_subtract_vectors(self):
        v1 = [10, 10, 10]
        v2 = [1, 2, 3]
        self.assertEqual(subtract_vectors(v1, v2), [9, 8, 7])

    # --- Tests de Transformadores ---
    def test_normalize(self):
        v = [0, 5, 10]
        self.assertEqual(normalize(v), [0.0, 0.5, 1.0])
        # Caso borde: todos iguales
        self.assertEqual(normalize([5, 5, 5]), [0.0, 0.0, 0.0])

    # --- Tests de Reordenamiento ---
    def test_mirror(self):
        self.assertEqual(mirror([1, 2, 3, 4]), [4, 3, 2, 1])

    def test_reflect_on_axis(self):
        v = [1, 2, 3, 4, 5]
        # Eje en el índice 2 (valor '3'), intercambia 2 con 4
        result = reflect_on_axis(v, 2)
        self.assertEqual(result, [1, 4, 3, 2, 5])

    # --- Tests de Limitadores ---
    def test_clamp(self):
        v = [-10, 5, 20]
        # Rango [0, 10]
        self.assertEqual(clamp(v, 0, 10), [0, 5, 10])

    # --- Tests de Comparadores ---
    def test_are_equal(self):
        self.assertTrue(are_equal([1, 2], [1, 2]))
        self.assertFalse(are_equal([1, 2], [2, 1]))

if __name__ == '__main__':
    unittest.main()