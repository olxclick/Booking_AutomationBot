Project Description

Overview

The Booking.com Automation Bot is a Python-based Selenium web scraper and automation tool designed to simplify the process of searching for hotels on Booking.com. It automates hotel searches, applies filters, and sorts results based on user preferences, reducing the time and effort required to manually navigate the website.

Key Features

✅ Automated Hotel Search – Users input their destination and trip dates, and the bot navigates to Booking.com to perform a search.

✅ Dynamic Date Selection – The bot calculates check-in and check-out dates based on user input.

✅ Guest Configuration – It selects the number of guests automatically.

✅ Filters Application – The bot applies filters, such as selecting hotels with specific star ratings (e.g., 3, 4, and 5 stars).

✅ Sorting by Lowest Price – After filtering, it sorts the search results to show the most affordable hotels first.

✅ Cookie Banner Handling – The bot automatically closes cookie pop-ups to ensure smooth execution.

✅ Currency Selection – Allows users to change the currency of displayed prices.

✅ Error Handling & Resilience – Implements exception handling to retry actions in case of stale elements or page reloads.

Project Structure

📂 booking/  (Main project directory)
│-- 📄 main.py           # Entry point; handles user input and starts the bot
│-- 📄 booking.py        # Defines the Booking class, which controls browser interactions
│-- 📄 booking_filters.py # Manages search filters (e.g., star rating, lowest price)
│-- 📄 constants.py      # Contains helper functions for waiting on elements and the base URL
│-- 📄 input.py          # Handles date calculations for check-in and check-out
