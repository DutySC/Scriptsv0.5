from PK.page_object.login_page import login
from PK.page_object.doctors_diary_page import doctors_diary
from PK.page_object.schedule_page import schedule
from PK.page_object.hospitalization_page import hospitalization
from PK.page_object.search_patient_page import search_patient
# from conftest import browser_SNILS
import time

class Test_PK:
    """Актуальный номер СНИЛСа"""
    # browser_SNILS() # получаем рандомное значение СНИЛСа
    # print(browser_SNILS()) # вывод полученного значения СНИЛС

    def test_PK_full(self, browser_PK):
        start = time.time()  # начало отсчета
        start_page = login(browser_PK) # тест модуля авторизации
        start_page.auth()
        start_doctors_diary = time.time()
        doctors_diary_test = doctors_diary(browser_PK) # тест модуля "Дневник врача"
        doctors_diary_test.diary()
        doctors_diary_test.diary_provide_service()
        doctors_diary_test.diary_delite()
        end_doctors_diary = time.time()
        full_doctors_diary = end_doctors_diary - start_doctors_diary
        print(' ▶️ Модуль - "Дневник врача", выполнен за: ', round(full_doctors_diary, 2), 'с') # вывод полного времени тестирования
        start_patient_schedule = time.time()
        patient_schedule_test = schedule(browser_PK) # тест модуля "Расписание"
        patient_schedule_test.patient_schedule()
        patient_schedule_test.patient_schedule_delete()
        end_patient_schedule = time.time()
        full_patient_schedule = end_patient_schedule - start_patient_schedule
        print(' ▶️ Модуль - "Расписание", выполнен за: ', round(full_patient_schedule, 2), 'с') # вывод полного времени тестирования
        start_patient_hospitalization = time.time()
        patient_hospitalization_test = hospitalization(browser_PK) # тест модуля "Госпитализация"
        patient_hospitalization_test.register_patient()
        patient_hospitalization_test.patient_hospitalization()
        patient_hospitalization_test.patient_cancel_hospitalization()
        patient_hospitalization_test.patient_delete_hospitalization()
        end_patient_hospitalization = time.time()
        full_patient_hospitalization = end_patient_hospitalization - start_patient_hospitalization
        print(' ▶️ Модуль - "Госпитализация", выполнен за: ', round(full_patient_hospitalization, 2), 'с') # вывод полного времени тестирования
        start_search_patient = time.time()
        search_patient_test = search_patient(browser_PK) # тест модуля "Поиск пациента"
        search_patient_test.create_patient()
        search_patient_test.delete_patient()
        end_search_patient = time.time()
        full_search_patient = end_search_patient - start_search_patient
        print(' ▶️ Модуль - "Поиск пациентов", выполнен за: ', round(full_search_patient, 2), 'с') # вывод полного времени тестирования
        end = time.time()  # конец отсчета
        full_test = end - start  # полное время авторизации
        print(' ▶️ Затраченное время на тестирование: ', round(full_test, 2), 'с')  # вывод полного времени тестирования

    """Тест по модулям"""
    # def test_PK(self, browser_PK):
    #     self.test_PK_login(browser_PK)  # тест модуля авторизации
    #     self.test_PK_doctors_diary(browser_PK) # тест модуля "Дневник врача"
    #     self.test_PK_schedule(browser_PK) # тест модуля "Расписание"
    #     self.test_PK_hospitalization(browser_PK) # тест модуля "Госпитализация"

    # def test_PK_login(self, browser_PK):
    #     start_page = login(browser_PK)
    #     start_page.auth()
    #     print('STAGE_1: COMPLETE')

    # def test_PK_doctors_diary(self, browser_PK):
    #     self.test_PK_login(browser_PK) # тест авторизации
    #     doctors_diary_test = doctors_diary(browser_PK)
    #     doctors_diary_test.diary()
    #     doctors_diary_test.diary_provide_service()
    #     doctors_diary_test.diary_delite()
    #     print('STAGE_2: COMPLETE')
    #
    # def test_PK_schedule(self, browser_PK):
    #     self.test_PK_login(browser_PK) # тест авторизации
    #     patient_schedule_test = schedule(browser_PK)
    #     patient_schedule_test.patient_schedule()
    #     patient_schedule_test.patient_schedule_delete()
    #     print('STAGE_3: COMPLETE')
    #
    # def test_PK_hospitalization(self, browser_PK):
    #     self.test_PK_login(browser_PK) # тест авторизации
    #     patient_hospitalization_test = hospitalization(browser_PK)
    #     patient_hospitalization_test.register_patient()
    #     patient_hospitalization_test.patient_hospitalization()
    #     patient_hospitalization_test.patient_cancel_hospitalization()
    #     patient_hospitalization_test.patient_delete_hospitalization()
    #     print('STAGE_4: COMPLETE')
    #
    # def test_PK_search_patient(self, browser_PK):
    #     self.test_PK_login(browser_PK)  # тест авторизации
    #     search_patient_test = search_patient(browser_PK)
    #     search_patient_test.create_patient()
    #     search_patient_test.delete_patient()
    #     print('STAGE_5: COMPLETE')
