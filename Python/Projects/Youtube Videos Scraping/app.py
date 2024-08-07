from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta

driver = webdriver.Chrome()

def convert_upload_list(upload_lst):
    for i in range(len(upload_lst)):
        array = upload_lst[i].split(" ")
        join_word = ' '.join(array[:2])
        upload_lst[i] = join_word
    return upload_lst

def subtract_time(duration, unit):
    """
    Subtracts a specified duration from the current date and time and returns the resulting day, month, and year.

    Parameters:
    duration (int): The amount of time to subtract.
    unit (str): The unit of time ('seconds', 'minutes', 'hours', 'days', 'weeks', 'months', 'years').

    Returns:
    tuple: The resulting day, month, and year after subtraction.
    """

    now = datetime.now()
    print(now)

    unit = unit.lower().rstrip('s')
    
    if unit == 'second':
        result = now - timedelta(seconds=duration)
    elif unit == 'minute':
        result = now - timedelta(minutes=duration)
    elif unit == 'hour':
        result = now - timedelta(hours=duration)
    elif unit == 'day':
        result = now - timedelta(days=duration)
    elif unit == 'week':
        result = now - timedelta(weeks=duration)
    elif unit == 'month':
        result = now - relativedelta(months=duration)
    elif unit == 'year':
        result = now - relativedelta(years=duration)
    else:
        raise ValueError("Invalid unit. Choose from 'second', 'minute', 'hour', 'day', 'week', 'month', 'year'.")
    print(f"{unit} {duration} {result}")
    return result.day, result.month, result.year

def format_date(day, month, year):
    def get_day_suffix(day):
        if 10 <= day % 100 <= 20:
            suffix = 'th'
        else:
            suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
        return suffix

    # Convert month number to month abbreviation
    month_name = time.strftime("%b", time.struct_time((year, month, 1, 0, 0, 0, 0, 0, -1)))

    # Format the date with suffix
    day_with_suffix = f"{day}{get_day_suffix(day)}"
    formatted_date = f"{day_with_suffix} {month_name}, {year}"

    return formatted_date

yt_url = "https://www.youtube.com/@PW-Foundation/videos"
r = driver.get(yt_url)
# driver.implicitly_wait(10)
videos = driver.find_elements(By.TAG_NAME,"ytd-rich-item-renderer")
driver.implicitly_wait(30)
thumbnail_links = []
for video in videos:
    tb = video.find_element(By.TAG_NAME,"ytd-thumbnail")
    anchor_tag = tb.find_element(By.ID,"thumbnail")
    video_link = anchor_tag.get_attribute("href")
    thumbnail_links.append(video_link)

print(thumbnail_links)
print(len(thumbnail_links))

video_links = []

for video in videos:
    content_page = video.find_element(By.ID,"content")
    video_link_page = content_page.find_element(By.TAG_NAME,"ytd-rich-grid-media")
    dismissible_page = video_link_page.find_element(By.ID,"dismissible")
    details_page = dismissible_page.find_element(By.ID,"details")
    meta_page = dismissible_page.find_element(By.ID,"meta")
    head_page = dismissible_page.find_element(By.TAG_NAME,"h3")
    anchor_link = head_page.find_element(By.TAG_NAME,"a").get_attribute("href")
    video_links.append(anchor_link)

print(video_links)

title_list = []
for title in videos:
    content_page = title.find_element(By.ID,"content")
    video_link_page = content_page.find_element(By.TAG_NAME,"ytd-rich-grid-media")
    dismissible_page = video_link_page.find_element(By.ID,"dismissible")
    details_page = dismissible_page.find_element(By.ID,"details")
    meta_page = dismissible_page.find_element(By.ID,"meta")
    head_page = dismissible_page.find_element(By.TAG_NAME,"h3")
    anchor_link = head_page.find_element(By.TAG_NAME,"a")
    title = anchor_link.find_element(By.TAG_NAME,"yt-formatted-string").text
    title_list.append(title)

print(title_list)

view_list = []
upload_list = []
for view in videos:
    content_page = view.find_element(By.ID,"content")
    video_link_page = content_page.find_element(By.TAG_NAME,"ytd-rich-grid-media")
    dismissible_page = video_link_page.find_element(By.ID,"dismissible")
    details_page = dismissible_page.find_element(By.ID,"details")
    meta_page = dismissible_page.find_element(By.ID,"meta")
    view_page = meta_page.find_element(By.TAG_NAME,"ytd-video-meta-block")
    metadata_page = view_page.find_element(By.ID,"metadata")
    metadata_line_page = metadata_page.find_element(By.ID,"metadata-line")
    spans = metadata_line_page.find_elements(By.TAG_NAME,"span")
    view = spans[0].text.split(" ")[0]
    upload = spans[1].text
    view_list.append(view)
    upload_list.append(upload)

print(view_list)
print(len(view_list))


upload_list = convert_upload_list(upload_list)
print(upload_list)
print(len(upload_list))

upload_split = lambda x : x.split(" ")
upload_map = map(upload_split, upload_list)
index = 0
for i in upload_map:
    day,month,year = subtract_time(int(i[0]),i[1])
    upload_list[index] = str(format_date(day,month,year))
    print(upload_list[index])
    index += 1

driver.quit()
