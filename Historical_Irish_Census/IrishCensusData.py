# You will need to install the third-party module selenium to run this program.
# To do so, run "pip install selenium" from the command line.
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# This is the path to the WebDriver for Google Chrome
# Download it here: https://sites.google.com/a/chromium.org/chromedriver/downloads
# After downloading, replace this variable with the location of the exe file
chrome_driver_path = r'C:\Users\schro333\Downloads\chromedriver_win32\chromedriver.exe'

# Head to the National Archives of Ireland census website
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('http://www.census.nationalarchives.ie/search/')

def get_census_info(year):

    # Store the search form submit button, census year dropdown, and county dropdown in variables
    # Note that the visible county dropdown changes depending on which census year is selected
    # However, 1901 and 1911 use the same county dropdown, so that isn't a problem here
    census_search_submit = driver.find_element_by_css_selector('input[value=Search]')
    census_year_dropdown = Select(driver.find_element_by_id('census_year'))
    census_county_dropdown = Select(driver.find_element_by_id('county19011911'))
    census_ded_field = driver.find_element_by_id('ded')
    
    # Specify an output file for writing the data
    output_file = open(r'H:\Departments\AGSL\GIS\Projects\Ben\irish-census-data-output\\' + year + '.csv', 'w')
    
    # Fill out the search form - select the year in question and County Donegal
    census_year_dropdown.select_by_visible_text(year)
    census_county_dropdown.select_by_visible_text('Donegal')
    census_ded_field.send_keys('Tawnawully')
    census_search_submit.click()

    # Sort results by surname
    sort_by_surname_link = driver.find_element_by_link_text('Surname')
    sort_by_surname_link.click()

    # Show 100 results at a time
    show_100_results_link = driver.find_element_by_link_text('100')
    show_100_results_link.click()

    # Check "Show all information"
    show_all_information = driver.find_element_by_id('show_all')
    show_all_information.click()

    # Add table column headers as the first line in the output CSV
    table_heads = driver.find_elements_by_tag_name('th')
    header_string = ''
    for head in table_heads:
        head_text = head.text
        header_string += head_text
        header_string += ','
    header_string += '\n'
    output_file.write(header_string)
    print(header_string)

    # Iterate through all rows
    while True:
        table_rows = driver.find_elements_by_css_selector('tbody>tr')
        for row in table_rows:
            columns = row.find_elements_by_tag_name('td')
            row_string = ''
            for column in columns:
                column_text = column.text
                if (',' in column_text):
                    column_text = '"' + column_text + '"'
                row_string += column_text
                row_string += ','
            row_string += '\n'
            print(row_string)
            output_file.write(row_string)
        try:
            next_100_link = driver.find_element_by_link_text('Next 100')
            next_100_link.click()
            show_all_information = driver.find_element_by_id('show_all')
            show_all_information.click()
        except:
            driver.get('http://www.census.nationalarchives.ie/search/')
            break

get_census_info('1911')
get_census_info('1901')
driver.close()
