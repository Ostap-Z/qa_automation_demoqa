from random import randint

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
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_LARGE_BOX_HANDLE), 300, 200)
        max_size = self.get_width_height(self.get_max_min_size(self.locators.RESIZABLE_LARGE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_LARGE_BOX_HANDLE), -350, -150)
        min_size = self.get_width_height(self.get_max_min_size(self.locators.RESIZABLE_LARGE_BOX))
        return max_size, min_size

    def change_size_small_resizable_box(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_SMALL_BOX_HANDLE), 350, 150)
        max_size = self.get_width_height(self.get_max_min_size(self.locators.RESIZABLE_SMALL_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_SMALL_BOX_HANDLE), -400, -300)
        min_size = self.get_width_height(self.get_max_min_size(self.locators.RESIZABLE_SMALL_BOX))
        return max_size, min_size
