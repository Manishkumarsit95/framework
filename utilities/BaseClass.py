import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getlogger(self):
      loggerName = inspect.stack()[1][3]
      logger = logging.getLogger(loggerName)
      fileHandlar = logging.FileHandler('logfile.log')

      formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

      fileHandlar.setFormatter(formatter)

      logger.addHandler(fileHandlar)
      logger.setLevel(logging.DEBUG)
      return logger

    def verifyLinkPresence(self,text):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))


