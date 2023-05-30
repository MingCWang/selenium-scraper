from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import time
import os 

# Specify the download directory
# download_directory = input('Enter the absolute path to the download directory: ') 

download_directory = '/Users/minstonewang/Desktop/lectures/Software-Engineering'

# Get the value of an environment variable
password = os.environ.get('PWD')


# Create Chrome options
options = Options()
options.add_argument('--no-sandbox')  # Optional: If running in a sandboxed environment
options.add_argument('--disable-dev-shm-usage')  # Optional: If running in a Docker container
prefs = {"profile.default_content_settings.popups": 0,    
        "download.default_directory": download_directory, 
        "download.prompt_for_download": False, 
        "download.directory_upgrade": True}
options.add_experimental_option("prefs", prefs)

# Create a new Chrome WebDriver instance with the specified options
driver = webdriver.Chrome(options=options)

# driver = webdriver.Chrome()
driver.get("https://moodle2.brandeis.edu/mod/page/view.php?id=2501641")

# fill out auth form
try:
    form = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'f')))
    username_input = form.find_element(By.NAME, 'j_username')
    password_input = form.find_element(By.NAME, 'j_password')
    username_input.send_keys('mingshihwang')
    password_input.send_keys(password)
    driver.find_element(By.XPATH, '//div[@class="form-element-wrapper form-group form-group pull-right hidden-xs"]//button[@type="submit"]').click()

except Exception as e:
    print(e)


class_names = []

while True:
    # wait for the page to be authenticated by user
    input('After you logged in with your Brandeis account, press enter to continue...... ')
    try:
        link_container = driver.find_element(By.CLASS_NAME, 'no-overflow')
        links = link_container.find_elements(By.TAG_NAME, 'a')
        print(f'\n==========================================\ndownloading {len(links)} files ......\n==========================================')

        count = 1
        for link in links:
            class_name = link.text
            class_names.append(class_name)
            driver.get(link.get_attribute('href'))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'download-btn'))).click()
            print(f'{count}. {class_name}')
            time.sleep(5)
            driver.back()
            count += 1
        
        input('Press enter after all files are downloaded......')
        break
    except Exception as e:
        print('Error: ', e)
        print('Please complete the authentication process to proceed')




files = os.listdir(download_directory)
sorted_files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(download_directory, x)))

# rename all files with the class name
for i in range(len(class_names)):
    file = sorted_files[i]
    print(file)
    class_name = class_names[i]
    # Construct the current file's full path
    current_path = os.path.join(download_directory, file)
    # Modify the file name as desired (e.g., adding a prefix or suffix)
    new_file_name = class_name + ".mp4"
    # Construct the new file's full path
    new_path = os.path.join(download_directory, new_file_name)
    # Rename the file
    os.rename(current_path, new_path)




print(f'\n==========================================\nDOWNLOAD COMPLETED\n==========================================')
