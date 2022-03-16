import schedule

from ships_tracker.utils.data_uploader import upload_new_data


def main():
    schedule.every().day.at("00:00").do(upload_new_data)
    while True:
        schedule.run_pending()


if __name__ == "__main__":
    main()
