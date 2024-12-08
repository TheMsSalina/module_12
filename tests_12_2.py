import unittest
from module_12_2 import Runner, Tournament

TestCase = unittest.TestCase


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)


    @classmethod
    def tearDownClass(cls):
        for key, value in enumerate(cls.all_results):
            print(value)

    def test_fist_tur(self):
        tur = Tournament(90, self.usain, self.nik)
        result = {k: str(v) for k, v in tur.start().items()}
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2], 'Ник')


    def test_second_tur(self):
        tur = Tournament(90, self.andrey, self.nik)
        result = {k: str(v) for k, v in tur.start().items()}
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2], 'Ник')

    def test_third_tur(self):
        tur = Tournament(90, self.usain, self.andrey, self.nik)
        result = {k: str(v) for k, v in tur.start().items()}

        TournamentTest.all_results.append(result)
        self.assertTrue(result[3], 'Ник')


if __name__ == '__main__':
    unittest.main()