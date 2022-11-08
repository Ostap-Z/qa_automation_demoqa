from selenium.webdriver.common.by import By


class SliderLocators:
    SLIDER_INPUT = (By.CSS_SELECTOR, "input.range-slider.range-slider--primary")
    SLIDER_VALUE = (By.CSS_SELECTOR, "input#sliderValue")
