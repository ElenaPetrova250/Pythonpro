'''
Задание №6
Проверить, что выкидываются правильные исключения (файл Exceptions.py) для кода Semin_13Task5
Напишите 3-7 тестов pytest для данного проекта.
Используйте фикстуры (предварительные конкретные данные для теста).
'''

import pytest


from Seminar_14.Semin13_Task5 import UserWorkshop, User
from Seminar_14.Exceptions import AccesErorr, LevelError
from Seminar_14.Semin13_User import User
@pytest.fixture()
def set_up():
    return UserWorkshop()


def test_access_fail_1(set_up):
    with pytest.raises(AccesErorr, match='Access denied'):
        set_up.login('Nesterovs', '1')


def test_access(set_up):
    assert set_up.login('Nesterov', '1') == '5'


def test_access_fail_2(set_up):
    with pytest.raises(LevelError):
        set_up.login('Nesterov', '1')
        set_up.create_user('New_user', '1', '3')



if __name__ == '__main__':
    pytest.main(['-v'])