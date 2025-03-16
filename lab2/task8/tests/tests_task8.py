from lab2.task8.src.main import find_height
import time
import tracemalloc
import unittest

class TestHeightTree(unittest.TestCase):

    def test_height_first(self):
        # given
        expected_result = 4
        data_n = 6
        data_nodes = [(-2, 0, 2),
                      (8, 4, 3),
                      (9, 0, 0),
                      (3, 6, 5),
                      (6, 0, 0),
                      (0, 0, 0)]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = find_height(data_n, data_nodes)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = find_height(data_n, data_nodes)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_height_second(self):
        # given
        expected_result = 6
        data_n = 8
        data_nodes = [(-2, 0, 2),
                      (8, 4, 3),
                      (9, 0, 0),
                      (3, 6, 5),
                      (6, 7, 0),
                      (0, 0, 0),
                      (9, 8, 0),
                      (7, 0, 0)]
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = find_height(data_n, data_nodes)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = find_height(data_n, data_nodes)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()