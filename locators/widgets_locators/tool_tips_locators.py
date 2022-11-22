from selenium.webdriver.common.by import By


class ToolTipsLocators:
    HOVER_BUTTON = (
        By.CSS_SELECTOR,
        "button#toolTipButton"
    )
    TOOL_TIP_BUTTON = (
        By.CSS_SELECTOR,
        "button[aria-describedby='buttonToolTip']"
    )

    HOVER_INPUT = (
        By.CSS_SELECTOR,
        "input#toolTipTextField"
    )
    TOOL_TIP_INPUT = (
        By.CSS_SELECTOR,
        "input[aria-describedby='textFieldToolTip']"
    )

    HOVER_CONTRARY_LINK = (
        By.XPATH,
        "//a[text()='Contrary']"
    )
    TOOL_TIP_CONTRARY = (
        By.CSS_SELECTOR,
        "a[aria-describedby='contraryTexToolTip']"
    )

    HOVER_SECTION_LINK = (
        By.XPATH,
        "//a[text()='1.10.32']"
    )
    TOOL_TIP_SECTION = (
        By.CSS_SELECTOR,
        "a[aria-describedby='sectionToolTip']"
    )

    TOOL_TIPS_INNER = (
        By.CSS_SELECTOR,
        "div.tooltip-inner"
    )
