from lab3.task14.src.main import find_min_time
import time
import tracemalloc
import unittest

class TestMinTime(unittest.TestCase):

    def test_height_first(self):
        # given
        expected_result = '5'
        data = (3, 1, 3, 4, [[1, 0, 2, 5], [1, 1, 2, 3], [2, 3, 3, 5], [1, 1, 3, 10]])
        expected_time = 1
        expected_memory = 16

        # when
        time_st = time.perf_counter()
        result = find_min_time(data[0], data[1], data[2], data[3], data[4])
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = find_min_time(data[0], data[1], data[2], data[3], data[4])
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_height_second(self):
        # given
        expected_result = '-1'
        data = (3, 1, 3, 2, [[1, 0, 2, 5], [1, 1, 2, 3]])
        expected_time = 1
        expected_memory = 16

        # when
        time_st = time.perf_counter()
        result = find_min_time(data[0], data[1], data[2], data[3], data[4])
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = find_min_time(data[0], data[1], data[2], data[3], data[4])
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()