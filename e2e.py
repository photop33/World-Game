


def test_scores_service(app_url):
    from selenium import webdriver
    driver = webdriver.Chrome("C:\\Users\\l1313\\.jenkins\\workspace\\Game-World\\chromedriver.exe")
    driver.get(app_url)
    score=driver.find_element_by_xpath("/html/body/h1/div").text
    for i in range(0,1000):
        if i == int(score):
            a=True
            return a
        elif i == 999:
            b=False
            return b
        else:
            continue

app_url = "http://127.0.0.1:8777"
res=test_scores_service(app_url)
def main_function(res):
    print(res)
    if res == True:
        print(0)
        return 0
    else:
        print(1)
        return (1)
main_function(res)
