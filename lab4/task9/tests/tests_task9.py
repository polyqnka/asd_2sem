from lab4.task9.src.main import decompose
import time
import tracemalloc
import unittest

class TestDecompString(unittest.TestCase):

    def test_decomp_first(self):
        # given
        expected_result = "ABC*2+DE*3+F"
        data = "ABCABCDEDEDEF"
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = decompose(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = decompose(data)
        memory = tracemalloc.get_traced_memory()[1]/1024/1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_decomp_second(self):
        # given
        expected_result = "Hello"
        data = "Hello"
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = decompose(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = decompose(data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_decomp_third(self):
        # given
        expected_result = "aabbaa"
        data = "aabbaa"
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = decompose(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = decompose(data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

    def test_decomp_fourth(self):
        # given
        expected_result = "XYZXYZXYZXY*5"
        data = "XYZXYZXYZXYXYZXYZXYZXYXYZXYZXYZXYXYZXYZXYZXYXYZXYZXYZXY"
        expected_time = 2
        expected_memory = 256

        # when
        time_st = time.perf_counter()
        result = decompose(data)
        time_end = time.perf_counter() - time_st

        tracemalloc.start()
        result = decompose(data)
        memory = tracemalloc.get_traced_memory()[1] / 1024 / 1024
        tracemalloc.stop()

        # then
        self.assertEqual(result, expected_result)
        self.assertLessEqual(time_end, expected_time, f"Значение {time_end} превышает порог {expected_time}")
        self.assertLessEqual(memory, expected_memory, f"Значение {memory} превышает порог {expected_memory}")

if __name__ == '__main__':
    unittest.main()