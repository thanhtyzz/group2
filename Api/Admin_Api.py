import datetime
import Api.Main_Api as main_api


class Admin_Api(main_api.Api):

    def __init__(self):
        super().__init__()
        self.connector()

    def add_new_item(self, json_data):
        # Get Film_ID from json_data
        film_id = json_data["Film_ID"]
        # Get ticket information from Film_ID in the collection
        ticket = self.warehouse_collection.find_one({'Film_ID': film_id})
        if ticket is None:
            # Check if the information in json_data is complete or not
            S = 0
            for key, value in json_data.items():
                if self.warehouse_collection.find_one({key: value}) is None:
                    S += 1
                else:
                    continue
            if S == 6:  # (Film_ID, Film, Genre, Showtime, Price)
                # If all 6 pieces of information are available, add a new ticket to the database
                self.warehouse_collection.insert_one(json_data)
                return 0  # Success
            else:
                # Error: missing information
                return -1
        else:
            # Update the number of tickets in the database
            current_quantity = ticket["Stock"]
            if current_quantity < 30:
                new_quantity = current_quantity + json_data["Stock"]
                self.warehouse_collection.update_one(
                    {'Film_ID': film_id}, {'$set': {'Stock': new_quantity}})
                return 0  # Success
            else:
                # Error: ticket quantity is full
                return -2

    def update_items(self, json_data, film_id):
        # Get ticket information from json_data
        ticket = self.warehouse_collection.find_one({'Film_ID': film_id})
        _id = ticket['_id']  # Get the ID of the ticket
        if 'Film_ID' in json_data:
            if self.warehouse_collection.find_one({'Film_ID': json_data['Film_ID']}) is not None:
                return -2  # Error: Film_ID already exists in the database
        updated_fields = {}
        if 'Showtime' in json_data:
            try:
                datetime.datetime.strptime(json_data['Showtime'], "%Y/%m/%d")
                updated_fields['Showtime'] = json_data['Showtime']
            except ValueError:
                return -3  # Error: Showtime format is incorrect
        if 'Film' in json_data:
            updated_fields['Film'] = json_data['Film']
        if 'Genre' in json_data:
            updated_fields['Genre'] = json_data['Genre']
        # Update the ticket information in the database
        if updated_fields:
            self.warehouse_collection.update_one({'Film_ID': film_id}, {'$set': updated_fields})
            return 0  # Update successful
        else:
            # No new information was updated
            return -1

    def remove_items(self, film_id):
        # Get ticket information from json_data
        ticket = self.warehouse_collection.find_one({'Film_ID': film_id})
        if ticket is None:
            # Error: ticket not found
            return -2
        elif ticket is not None:
            film_id = ticket['Film_ID']  # get id of ticket
            self.warehouse_collection.delete_one({'Film_ID': film_id})
            return 0  # success
