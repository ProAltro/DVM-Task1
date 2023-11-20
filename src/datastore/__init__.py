"""
The goal of this package is to create a data storage service that can be used by other services.
The main reason this exists is that if we decide to swap out the storage mechanism, we can do so without changing the code of other services.

The package mainly provides a SQLHandler object, which contains all endpoints for any action needed by the API calling service. The Handler in turn consists of multiple sub handlers, each of which is responsible for a particular model. This makes it easy to add new models to the datastore without changing the code of other models. This essentially does the job an ORM would otherwise do.
"""
