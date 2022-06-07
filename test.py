#Maria Williams
#6/6/22
#https://click.palletsprojects.com/en/8.1.x/testing/

from click.testing import CliRunner
from clickmodel import hello

def test_run():
    runner = CliRunner()
    result = runner.invoke(hello)
    assert result.output == 'Let me finish your thought! Type "hush" to stop chatting.'