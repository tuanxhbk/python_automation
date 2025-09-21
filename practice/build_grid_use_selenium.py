from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def extract_data(url):
    driver = webdriver.Chrome()
    driver.get(url)
    sleep(5)

    # Get table element
    table = driver.find_element(By.XPATH, "//table")

    # Extract data from the table
    data = []
    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        data.append([col.text for col in cols])

    driver.quit()
    return data


def process_data(raw_data):
    list_no_header = raw_data[1:]
    for row in list_no_header:
        row[0] = int(row[0])  # Convert ID to integer
        row[2] = int(row[2])  # Convert Age to integer
    sorted_list = sorted(list_no_header, key=lambda x: (x[0], x[2]))
    set_x_cordinate = set()
    set_y_cordinate = set()
    for row in sorted_list:
        set_x_cordinate.add(row[0])
        set_y_cordinate.add(row[2])
    max_x = max(set_x_cordinate)
    max_y = max(set_y_cordinate)
    print(sorted_list)
    print(f"Max X: {max_x}, Max Y: {max_y}")
    print(f"Length: {len(sorted_list)}")
    final_data = []
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            matched = False
            for row in sorted_list:
                if row[0] == x and row[2] == y:
                    final_data.append(row)
                    matched = True
                    break
            if not matched:
                final_data.append([x, " ", y])
    print(f"Final Data : {final_data}")
    print(f"Length Final Data : {len(final_data)}")
    pass
    # Process raw data as needed


def print_message(processed_data):
    # ^ (y)
    # |
    # |-------> (x)
    pass
    # Print or log the processed data


def solution(url):
    raw_data = extract_data(url)
    processed_data = process_data(raw_data)
    print_message(processed_data)


# url = 'https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub'

url = "https://docs.google.com/document/d/e/2PACX-1vSZ9d7OCd4QMsjJi2VFQmPYLebG2sGqI879_bSPugwOo_fgRcZLAFyfajPWU91UDiLg-RxRD41lVYRA/pub"

raw_data = extract_data(url)
process_data(raw_data)
