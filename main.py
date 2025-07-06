import schedule
import time
from linkedin.bot import LinkedInBot

def full_engagement_cycle():
    bot = LinkedInBot()
    try:
        bot.process_topics()
        bot.like_recent_posts()
        bot.like_comments_on_own_posts()
        bot.reply_to_own_post_comments()
        bot.comment_on_connection_posts()
    finally:
        bot.driver.quit()

# Schedule the job to run every day at 2:00 AM
schedule.every().day.at("02:00").do(full_engagement_cycle)

print("[INFO] LinkedIn engagement bot is running...")

while True:
    schedule.run_pending()
    time.sleep(60)
