import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from Constants import MESSAGE_LENGTH_FROM, MESSAGE_TIMING, MESSAGE_LENGTH_TO, MESSAGE_COUNT, ROOMID
from Constants import REF_URL


@pytest.fixture(scope='class')  # Основные настройки Chrome, новое окно для каждого класса кейсов
def global_environment_chrome_class(request):
    options = chrome_options()
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.notifications": 1})
    options.add_argument("use-fake-device-for-media-stream") # Использовать фейковую камеру
    options.add_argument('chrome')
    options.add_argument("--enable-javascript")
    driver = webdriver.Remote(command_executor='http://localhost:4444', desired_capabilities=options.to_capabilities())
    yield driver


@pytest.fixture(scope="class")  # Страница подключения к конференции
def get_call_join_page(request, global_environment_chrome_class):
    driver = global_environment_chrome_class
    request.cls.driver = driver
    yield driver
    # driver.quit()


@pytest.fixture()
def global_environment_chrome(request):
    options = chrome_options()
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.notifications": 1})
    options.add_argument("use-fake-device-for-media-stream")  # Использовать фейковую камеру
    options.add_argument('chrome')
    options.add_argument("--enable-javascript")
    driver = webdriver.Remote(command_executor='http://localhost:4444', desired_capabilities=options.to_capabilities())
    yield driver


@pytest.fixture()
def get_data():
    return MESSAGE_COUNT, MESSAGE_LENGTH_FROM, MESSAGE_LENGTH_TO, MESSAGE_TIMING


@pytest.fixture()
def get_url():
    return f"https://meet.gcorelabs.com/call/?roomId={ROOMID}"


@pytest.fixture()
def get_ref():
    return REF_URL




