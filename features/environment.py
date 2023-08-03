from dotenv import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def environment_load(context):
    load_dotenv()
    config = dotenv_values(find_dotenv())
    for key, value in config.items():
        setattr(context, key, value)


def before_all(context):
    environment_load(context)

#    chrome_options = webdriver.ChromeOptions()
#    #chrome_options.add_argument("--headless")
#    #chrome_options.add_argument("--window-size=1920,1080")
#    chrome_options.add_argument("--start-maximized")
#    context.browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    context.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    print("Se esta ejecutando la prueba con selenium")


def after_all(context):
    context.browser.quit()


def before_tag(context, tag):
    pass


def after_tag(context, tag):
    pass


def before_feature(context, feature):
    pass


def after_feature(context, feature):
    pass


def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    pass


def before_step(context, step):
    pass


def after_step(context, step):
    pass