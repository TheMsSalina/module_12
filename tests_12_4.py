import unittest
import logging
import traceback
from module_12_4 import  Runner, Tournament


logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w',
                    encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner("Вася", -5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner\n{e}")
            logging.warning(traceback.format_exc())

    def test_run(self):
        try:
            runner = Runner(2)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner\n{e}")
            logging.warning(traceback.format_exc())

    def test_challenge(self):
        runner_1 = Runner("Runner1")
        runner_2 = Runner("Runner2")

        for _ in range(10):
            runner_1.run()
            runner_2.walk()

        self.assertNotEqual(runner_1.distance, runner_2.distance)
        logging.info('"test_challenge" выполнен успешно')


if __name__ == '__main__':
    unittest.main()