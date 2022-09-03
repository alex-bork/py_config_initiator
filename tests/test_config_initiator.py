from re import template
import sys, os, unittest
sys.path.append(os.path.realpath('.'))
from py_config_initiator.module import ConfigInitiator


class Test_ConfigInitor(unittest.TestCase):

    def test_check___new_config_created_from_list(self):

        ConfigInitiator.from_list(
            path=os.path.dirname(__file__), 
            template=['DEFAULT','test=True'])

        file_full_path = os.path.join(os.path.dirname(__file__), 'config.ini')
        file_exists = os.path.exists(file_full_path)
        self.assertEquals(file_exists, True)
        if file_exists:
            os.remove(file_full_path)

    def test_check___new_config_created_from_string(self):

        ConfigInitiator(
            path=os.path.dirname(__file__),
            template=
                '''
                DEFAULT
                test=True
                ''')

        file_full_path = os.path.join(os.path.dirname(__file__), 'config.ini')
        file_exists = os.path.exists(file_full_path)
        self.assertEquals(file_exists, True)
        if file_exists:
            os.remove(file_full_path)

    def test_check___new_config_created_from_string_wrong_type_exception_raised(self):

        try:
            ConfigInitiator(
                path=os.path.dirname(__file__),
                template=
                    '''
                    DEFAULT
                    test=True
                    ''')
            self.assertTrue(False)
        except:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

