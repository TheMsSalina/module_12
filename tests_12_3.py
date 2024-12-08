
import unittest
import inspect
from module_12_2 import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        peshehod = Runner('Пешеход')
        for i in range(10):
            peshehod.walk()
        self.assertEqual(peshehod.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        begun = Runner('Бегун')
        for i in range(10):
            begun.run()
        self.assertEqual(begun.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        walker = Runner('Пешеход')
        runner = Runner('Бегун')
        for i in range(10):
            walker.walk()
            runner.run()
        self.assertNotEqual(walker.distance, runner.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print()
        for test in cls.all_results:
            print()
            print(f'{test}:')
            print({k: str(v) for k, v in cls.all_results[test].items()})

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_fist_tur(self):
        tour = Tournament(90, self.usain, self.nik)
        results = tour.start()
        self.__class__.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_second_tur(self):
        tour = Tournament(90, self.andrey, self.nik)
        results = tour.start()
        self.__class__.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_third_tur(self):
        tour = Tournament(90, self.usain, self.andrey, self.nik)
        results = tour.start()
        self.__class__.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)


if __name__ == '__main__':
    unittest.main()