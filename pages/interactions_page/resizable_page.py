from pages.base_page import BasePage
from locators.interactions_locators.resizable_locators import ResizableLocators


class ResizablePage(BasePage):
    locators = ResizableLocators()

    @staticmethod
    def get_width_height(value_size):
        width = value_size.split(";")[0].split(":")[1].lstrip()
        height = value_size.split(";")[1].split(":")[1].lstrip()
        return width, height

    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute("style")
        return size_value

    def change_size_large_resizable_box(self):
        log = self.get_logger()
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_LARGE_BOX_HANDLE), 300, 200)
        log.info("Dragged large resizable box")
        max_size = self.get_width_height(self.get_max_min_size(self.locators.RESIZABLE_LARGE_BOX))
        log.info(f"Got max size of large resizable box: {max_size}")
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_LARGE_BOX_HANDLE), -350, -150)
        log.info("Dragged large resizable box")
        min_size = self.get_width_height(self.get_max_min_size(self.locators.RESIZABLE_LARGE_BOX))
        log.info(f"Got min size of large resizable box: {min_size}")
        return max_size, min_size

    def change_size_small_resizable_box(self):
        log = self.get_logger()
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_SMALL_BOX_HANDLE), 350, 150)
        log.info("Dragged small resizable box")
        max_size = self.get_width_height(self.get_max_min_size(self.locators.RESIZABLE_SMALL_BOX))
        log.info(f"Got max size of small resizable box: {max_size}")
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_SMALL_BOX_HANDLE), -400, -300)
        log.info("Dragged small resizable box")
        min_size = self.get_width_height(self.get_max_min_size(self.locators.RESIZABLE_SMALL_BOX))
        log.info(f"Got min size of small resizable box: {min_size}")
        return max_size, min_size
