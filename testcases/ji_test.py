from pytest import mark

from just_because import ji

@mark.parametrize(
    'input_string, output_string', [
        ('鸡你太美', '只因你太美'),
        ('基因重组', '只因因重组'),
        ('弹鸡鸡弹到死', '弹只因只因弹到死')
    ]
)
def test_ji(input_string, output_string):
    """
    this is the test of function ji.
    """
    assert ji(input_string) == output_string
