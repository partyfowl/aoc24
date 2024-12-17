from common import process_instructions


class TestProcessInstructions:
    def test_case_1(self):
        a, b, c, output = process_instructions(a=0, b=0, c=9, instructions=[2, 6])
        assert b == 1

    def test_case_2(self):
        a, b, c, output = process_instructions(
            a=10, b=0, c=0, instructions=[5, 0, 5, 1, 5, 4]
        )
        assert output == "0,1,2"

    def test_case_3(self):
        a, b, c, output = process_instructions(
            a=2024, b=0, c=0, instructions=[0, 1, 5, 4, 3, 0]
        )
        assert output == "4,2,5,6,7,7,7,7,3,1,0"
        assert a == 0

    def test_case_4(self):
        a, b, c, output = process_instructions(a=0, b=29, c=0, instructions=[1, 7])
        assert b == 26

    def test_case_5(self):
        a, b, c, output = process_instructions(
            a=0, b=2024, c=43690, instructions=[4, 0]
        )
        assert b == 44354

    def test_example_input(self):
        a, b, c, output = process_instructions(
            a=729, b=0, c=0, instructions=[0, 1, 5, 4, 3, 0]
        )
        assert output == "4,6,3,5,6,3,5,2,1,0"
