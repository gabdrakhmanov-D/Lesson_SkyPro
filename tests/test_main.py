import builtins
from unittest import mock
from unittest.mock import patch, Mock

from main import main

# @patch('read_json_file')
# @patch('builtins.input')
def test_welcome_1_json():
    with mock.patch.object(builtins, 'input', lambda _: (_ for _ in [1, 'executed'])):
    # with mock.patch.object(builtins, 'input', lambda _: [_ for _ in [1, 'executed']]):
    #     with mock.patch.object(builtins, 'input', lambda _: 'executed'):
        assert main() == 1