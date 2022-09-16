from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_to_basket(self, quiz_solve=True):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()
        time.sleep(1)
        if quiz_solve:
            self.solve_quiz_and_get_code()
        # готовим переменные для того, чтобы потом в тесте проверить, совпадает ли имя и цена помещенного в корзину
        # товара, указанное в выскакивающем алерте, с именем товара, который мы добавляли
        self.addable_item_name = self.browser.find_element(*ProductPageLocators.ADDABLE_ITEM_NAME).text
        self.item_name_in_alert_message = self.browser.find_element(
            *ProductPageLocators.NAME_OF_ITEM_ADDED_TO_BASKET_IN_INNER_ALERT_MESSAGE).text
        self.addable_item_price = self.browser.find_element(*ProductPageLocators.ADDABLE_ITEM_PRICE).text
        self.amount_of_basket_in_alert_message = self.browser.find_element(
            *ProductPageLocators.BASKET_AMOUNT_IN_INNER_ALERT_MESSAGE).text


    # def get_addable_item_name(self):
    #     return self.browser.find_element(*ProductPageLocators.ADDABLE_ITEM_NAME).text
    #
    # def get_item_name_in_alert_message(self):
    #     return self.browser.find_element(*ProductPageLocators.NAME_OF_ITEM_ADDED_TO_BASKET_IN_INNER_ALERT_MESSAGE).text
    #
    # def get_amount_of_basket_in_alert_message(self):
    #     return self.browser.find_element(*ProductPageLocators.BASKET_AMOUNT_IN_INNER_ALERT_MESSAGE).text
