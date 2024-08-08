from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from flask import Flask, request, render_template
import logging

app = Flask(__name__)

logging.basicConfig(filename="yt_scrap_logger.log",level=logging.INFO, format = '%(asctime)s %(levelname)s %(message)s %(lineno)s %(funcName)s')

def extract_video_data(video):
    data = {}
    # logging.info('Extracting thumbnail link')
    data['thumbnail'] = video.find_element(By.TAG_NAME, "ytd-thumbnail").find_element(By.ID, "thumbnail").get_attribute("href")
    content_page = video.find_element(By.ID, "content")
    video_link_page = content_page.find_element(By.TAG_NAME, "ytd-rich-grid-media")
    dismissible_page = video_link_page.find_element(By.ID, "dismissible")
    meta_page = dismissible_page.find_element(By.ID, "meta")
    head_page = dismissible_page.find_element(By.TAG_NAME, "h3")
    anchor_tag = head_page.find_element(By.TAG_NAME, "a")
    # logging.info("Extracting video link")
    data['video_link'] = anchor_tag.get_attribute("href")
    # logging.info("Extracting title of video")
    data['title'] = anchor_tag.find_element(By.TAG_NAME, "yt-formatted-string").text
    view_page = meta_page.find_element(By.TAG_NAME, "ytd-video-meta-block")
    metadata_page = view_page.find_element(By.ID, "metadata")
    metadata_line_page = metadata_page.find_element(By.ID, "metadata-line")
    spans = metadata_line_page.find_elements(By.TAG_NAME, "span")
    # logging.info("Extracting views")
    data['views'] = spans[0].text.split(" ")[0]
    # logging.info("Extracting uploaded time")
    data['upload_time'] = spans[1].text
    return data

@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')

@app.route('/videos', methods=['POST'])
def scrap_page():
    if request.method == 'POST':
        channel_handle = request.form['search'].replace(" ","")
        logging.info(f"User entered channel handle : {channel_handle}")
        yt_url = f"https://www.youtube.com/@{channel_handle}/videos"
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(yt_url)

        logging.info("Entering to container which has entire data")
        videos = driver.find_elements(By.TAG_NAME, "ytd-rich-item-renderer")

        if not videos:
            logging.warning(f"No videos found for channel handle: {channel_handle}")
            driver.quit()
            return render_template('index.html', error="No videos found. Please check the channel handle and try again.")

        video_data = [extract_video_data(video) for video in videos]

        logging.info(f"Complete video data : {video_data}")

        driver.quit()

        return render_template('results.html', results=video_data)

if __name__ == "__main__":
    app.run(debug=True)
