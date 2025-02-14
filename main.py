from booking.booking import Booking
from booking.input import add_days_to_current_date

try:
	with Booking() as bot:
		start_date = int(input('In how many days do you want to start your vacation ? '))
		vac_days = int(input('For how many days will you go on vacation ? '))
		end_date = start_date + vac_days
		bot.land_first_page()
		# bot.change_currency('Euro')
		bot.select_place()
		bot.select_date(add_days_to_current_date(start_date), add_days_to_current_date(end_date))
		bot.select_guests(1)
		bot.click_search()
		bot.close_cookie_banner()
		bot.apply_filters()

		input('Press a key to exit...')

except Exception as e:
	if 'in PATH' in str(e):
		print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
	else:
		raise