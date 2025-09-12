from time import sleep
from typing import List, Tuple
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def extract_data(url: str) -> List[List[str]]:
    """Extract data from Google Doc table."""
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        # Use WebDriverWait instead of sleep
        wait = WebDriverWait(driver, 10)
        table = wait.until(EC.presence_of_element_located((By.XPATH, "//table")))

        # Use list comprehension for data extraction
        rows = table.find_elements(By.TAG_NAME, "tr")
        data = [
            [col.text for col in row.find_elements(By.TAG_NAME, "td")] for row in rows
        ]
        return data
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Error extracting data: {e}")
        return []
    finally:
        driver.quit()


def process_data(raw_data: List[List[str]]) -> List[List[int | str]]:
    """Process the raw data and create grid coordinates."""
    if not raw_data or len(raw_data) <= 1:
        return []

    # Process data excluding header
    try:
        grid_data = []
        for row in raw_data[1:]:
            x, char, y = int(row[0]), row[1], int(row[2])
            grid_data.append([x, char, y])

        # Get grid dimensions
        max_x = max(row[0] for row in grid_data)
        max_y = max(row[2] for row in grid_data)

        # Create complete grid with empty spaces
        final_data = []
        grid_dict = {(row[0], row[2]): row for row in grid_data}

        for x in range(max_x + 1):
            for y in range(max_y + 1):
                final_data.append(grid_dict.get((x, y), [x, " ", y]))

        return final_data
    except (ValueError, IndexError) as e:
        print(f"Error processing data: {e}")
        return []


def print_message(processed_data: List[List[int | str]]) -> None:
    """Print the grid message.

    Coordinate system:
    ^ (y)
    |
    |-------> (x)
    """
    if not processed_data:
        print("No data to display")
        return

    # Get grid dimensions
    max_x = max(row[0] for row in processed_data)
    max_y = max(row[2] for row in processed_data)

    # Create 2D grid
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Fill grid with characters
    for x, char, y in processed_data:
        grid[y][x] = char

    # Print grid from top to bottom
    for row in reversed(grid):
        print("".join(row))


def solution(url: str) -> None:
    """Main solution function."""
    try:
        raw_data = extract_data(url)
        if raw_data:
            processed_data = process_data(raw_data)
            print_message(processed_data)
        else:
            print("Failed to extract data from URL")
    except Exception as e:
        print(f"Error in solution: {e}")


if __name__ == "__main__":
    # url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
    url = "https://docs.google.com/document/d/e/2PACX-1vSZ9d7OCd4QMsjJi2VFQmPYLebG2sGqI879_bSPugwOo_fgRcZLAFyfajPWU91UDiLg-RxRD41lVYRA/pub"
    solution(url)
