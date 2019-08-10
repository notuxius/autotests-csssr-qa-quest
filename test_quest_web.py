import time


def _sleep_time(sleep_time=1):
    # Fade time from the graph text
    return time.sleep(sleep_time)


def test_click_delve_into_project_details_text_display(driver, chrome_options, connect_to_url):
    graph_link = driver.find_element_by_xpath("/html/body/div[1]/section[1]/section/div[1]/a")
    graph_link.click()
    _sleep_time()

    graph_text = driver.find_element_by_xpath("/html/body/div[1]/section[2]/div[1]/h1")
    assert graph_text.is_displayed()


def test_click_find_imperfections_text_display(driver, chrome_options, connect_to_url):
    graph_link = driver.find_element_by_xpath("/html/body/div[1]/section[1]/section/div[2]/a")
    graph_link.click()
    _sleep_time()
    graph_link.click()
    _sleep_time()

    graph_text = driver.find_element_by_xpath("/html/body/div[1]/section[2]/div[2]/h1")
    assert graph_text.is_displayed()


def test_click_accompany_projects_text_display(driver, chrome_options, connect_to_url):
    graph_link = driver.find_element_by_xpath("/html/body/div[1]/section[1]/section/div[3]/a")
    graph_link.click()
    _sleep_time()
    graph_link.click()
    _sleep_time()

    graph_text = driver.find_element_by_xpath("/html/body/div[1]/section[2]/div[3]/h1")
    assert graph_text.is_displayed()


def test_click_work_with_projects_files_text_display(driver, chrome_options, connect_to_url):
    graph_link = driver.find_element_by_xpath("/html/body/div[1]/section[1]/section/div[4]/a")
    graph_link.click()
    _sleep_time()
    graph_link.click()
    _sleep_time()

    graph_text = driver.find_element_by_xpath("/html/body/div[1]/section[2]/div[4]/h1")
    assert graph_text.is_displayed()
