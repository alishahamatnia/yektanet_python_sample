class BaseAdvertising:
    _objects_count = 0

    def __init__(self):
        self._views = 0
        self._clicks = 0
        self._id = type(self)._objects_count
        type(self)._objects_count += 1

    def get_id(self):
        return self._id

    def get_views(self):
        return self._views

    def get_clicks(self):
        return self._clicks

    def get_objects_count(self):
        return type(self)._objects_count

    def inc_clicks(self, count=1):
        self._clicks += count

    def inc_views(self, count=1):
        self._views += count

    def describe_me(self):
        return "this is an object of BaseAdvertising class which has common fields and methods of" \
               " Ad and Advertiser classes, this class could be abstract. this object has id: " + str(self._id)
