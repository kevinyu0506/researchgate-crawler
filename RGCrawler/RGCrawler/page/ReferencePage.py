# from selenium.webdriver.common.by import By
# from RGCrawler.page import Page
#
# from time import sleep
#
#
# class ReferencePage(Page):
#     # Locators
#     LOAD_MORE_BTN = (By.XPATH, "//span[contains(text(), 'Show more')]/..")
#     REF_BTN = (By.XPATH, "//button[contains(@class,'nova-c-nav__item references')]")
#     CITATION_BTN = (By.XPATH, "//div[@class='nova-o-pack__item']//div[contains(text(),'Citations')]")
#     REFERENCE_BTN = (By.XPATH, "//div[@class='nova-o-pack__item']//div[contains(text(),'References')]")
#
#     def __init__(self):
#         super(ReferencePage).__init__()
#
#     def tap_reference_btn(self):
#         ref_btn = self.get_element_locate_by(self.driver, self.REFERENCE_BTN)
#         ref_btn.click()
#
#     def click_load_more(self):
#         while self.get_any_elements_by(self.driver, self.LOAD_MORE_BTN, 10) is not None:
#             self.driver.execute_script("document.getElementsByClassName('nova-c-button nova-c-button--align-center nova-c-button--radius-m nova-c-button--size-xs nova-c-button--color-grey nova-c-button--theme-ghost nova-c-button--width-auto js-lite-click')[0].click();")
#             self.logger.info("Load more btn clicked.")
#             sleep(1)
#
#         self.logger.info("Load all btn, interaction complete.")
#         sleep(3)
