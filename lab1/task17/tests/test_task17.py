from lab1.task17.src.main import count_numbers
import time
import tracemalloc
import unittest

class TestCountNumbers(unittest.TestCase):

    def test_count_first(self):
        # given
        expected_result = 16
        data = 2
        expected_time = 1
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = count_numbers(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = count_numbers(data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_count_second(self):
        # given
        expected_result = 36
        data = 3
        expected_time = 1
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = count_numbers(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = count_numbers(data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_count_third(self):
        # given
        expected_result = 753250816
        data = 1000
        expected_time = 1
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = count_numbers(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = count_numbers(data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()