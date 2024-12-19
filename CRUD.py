from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31787
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
    # Complete this create method to implement the C(create) in CRUD
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
            
        # Create method to implement the R(read) in CRUD.
    def read(self, query):
        """
        Reads data from the database based on the provided query.
        If no query is provided, returns all documents in the collection.
        :param query: Dictionary representing the MongoDB query filter.
        :return: Cursor to the documents matching the query.
        """
        if query is not None:
            return self.database.animals.find(query)  # Returns a cursor for all matching documents
        else:
            return self.database.animals.find()  # Returns a cursor for all documents
        
    # Create method to implement the U(update) in CRUD
    def update(self, query, update_data, many=False):
        """
        Updates document(s) in the collection based on the provided query.
        :param query: Dictionary representing the MongoDB query filter.
        :param update_data: Dictionary representing the update to be applied.
        :param many: Boolean indicating whether to update one or many documents.
        :return: The number of documents modified.
        """
        if query is not None and update_data is not None:
            if many:
                result = self.collection.update_many(query, update_data)
            else:
                result = self.collection.update_one(query, update_data)
            return result.modified_count  # Return the number of documents modified
        else:
            raise Exception("Query or update data is empty")
            
    # Create method to implement the D(delete) in CRUD
    def delete(self, query, many=False):
        """
        Deletes document(s) from the collection based on the provided query.
        :param query: Dictionary representing the MongoDB query filter.
        :param many: Boolean indicating whether to delete one or many documents.
        :return: The number of documents deleted.
        """
        if query is not None:
            if many:
                result = self.collection.delete_many(query)
            else:
                result = self.collection.delete_one(query)
            return result.deleted_count  # Return the number of documents deleted
        else:
            raise Exception("Query parameter is empty")
