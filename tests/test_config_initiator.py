import sys, os, unittest
sys.path.append(os.path.join(os.path.realpath('.'), 'py_config_initiator'))
from config import ConfigInitor


class Test_ConfigInitor(unittest.TestCase):

    def test_check___new_config_created_exception_raised(self):

        ConfigInitor(os.path.dirname(__file__)).set_template(list=['DEFAULT','test=True']).check()

        file_full_path = os.path.join(os.path.dirname(__file__), 'config.ini')
        file_exists = os.path.exists(file_full_path)
        self.assertEquals(file_exists, True)
        if file_exists:
            os.remove(file_full_path)


if __name__ == '__main__':
    unittest.main()

