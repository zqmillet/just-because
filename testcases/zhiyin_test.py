from pytest import mark

from just_because import zhiyin2ji

@mark.parametrize(
    'input_string, output_string', [
        ('只因你太美', '鸡你太美'),
        ('只因因重组', '鸡因重组'),
        ('弹只因只因弹到死', '弹鸡鸡弹到死'),
        ('我喜欢看知音', '我喜欢看鸡'),
        ('他给了我指引', '他给了我鸡'),
    ]
)
def test_zhiyin2ji(input_string, output_string):
    """
    this is the test of function zhiyin.
    """
    assert zhiyin2ji(input_string) == output_string
