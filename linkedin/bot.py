import os
import time
import random
import logging
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from linkedin.groq_api import generate_groq_reply
from linkedin.utils import remove_markdown, random_delay

load_dotenv()

class LinkedInBot:
    def __init__(self):
        self.driver = self.setup_driver()
        self.login()

    def setup_driver(self):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        return driver

    def login(self):
        self.driver.get("https://www.linkedin.com/login")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        self.driver.find_element(By.ID, "username").send_keys(os.getenv("LINKEDIN_USERNAME"))
        self.driver.find_element(By.ID, "password").send_keys(os.getenv("LINKEDIN_PASSWORD"), Keys.RETURN)
        time.sleep(5)

    def process_topics(self):
        try:
            with open("Topics.txt", "r") as f:
                topics = f.readlines()
            if not topics:
                return
            topic = topics[0].strip()
            if not topic:
                return
            post_text = generate_groq_reply(topic, context="post")
            post_text = remove_markdown(post_text)
            self.post_to_linkedin(post_text)
            with open("Topics_done.txt", "a") as f:
                f.write(topic + "\n")
            with open("Topics.txt", "w") as f:
                f.writelines(topics[1:])
        except Exception as e:
            logging.error("[ERROR] Posting topic failed:", exc_info=True)

    def post_to_linkedin(self, text):
        try:
            self.driver.get("https://www.linkedin.com/feed/")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Start a post')]"))).click()
            time.sleep(2)
            post_box = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div[role='textbox']")))
            post_box.click()
            post_box.send_keys(text)
            time.sleep(2)
            post_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'share-actions__primary-action')]")))
            post_btn.click()
            logging.info("[INFO] Post published successfully.")
        except Exception as e:
            logging.error("[ERROR] Post to LinkedIn failed:", exc_info=True)

    def like_recent_posts(self):
        self.driver.get("https://www.linkedin.com/feed/")
        time.sleep(3)
        posts = self.driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'Like')]")
        for post in posts[:5]:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView();", post)
                time.sleep(random.uniform(1, 2))
                post.click()
                logging.info("[INFO] Liked a post.")
            except:
                logging.warning("[WARN] Couldn't like a post.")

    def like_comments_on_own_posts(self):
        # Example with dummy post link — customize
        self.driver.get("https://www.linkedin.com/feed/")
        time.sleep(4)
        comment_likes = self.driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'Like this comment')]")
        for btn in comment_likes[:5]:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView();", btn)
                time.sleep(1)
                btn.click()
                logging.info("[INFO] Liked a comment on own post.")
            except:
                logging.warning("[WARN] Failed to like comment.")

    def reply_to_own_post_comments(self):
        # Example with dummy post link — customize
        self.driver.get("https://www.linkedin.com/feed/")
        time.sleep(5)
        comments = self.driver.find_elements(By.XPATH, "//span[contains(@class, 'comments-comment-item__main-content')]")
        for c in comments[:3]:
            try:
                comment_text = c.text
                reply = generate_groq_reply(comment_text, context="reply_comment")
                reply_box = c.find_element(By.XPATH, "..//following-sibling::div//textarea")
                reply_box.send_keys(reply)
                reply_box.send_keys(Keys.RETURN)
                logging.info("[INFO] Replied to a comment.")
                time.sleep(3)
            except:
                logging.warning("[WARN] Failed to reply to comment.")

    def comment_on_connection_posts(self):
        self.driver.get("https://www.linkedin.com/feed/")
        time.sleep(3)
        comment_boxes = self.driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'Comment')]")
        for btn in comment_boxes[:3]:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView();", btn)
                btn.click()
                time.sleep(2)
                parent = btn.find_element(By.XPATH, "../../..")
                post_content = parent.text[:500]
                comment = generate_groq_reply(post_content, context="comment_on_post")
                box = parent.find_element(By.TAG_NAME, "textarea")
                box.send_keys(comment)
                box.send_keys(Keys.RETURN)
                logging.info("[INFO] Commented on a connection's post.")
                time.sleep(3)
            except:
                logging.warning("[WARN] Failed to comment on post.")