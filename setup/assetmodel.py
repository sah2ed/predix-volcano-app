
import predix.data.asset


class Volcano(predix.data.asset.AssetCollection):
    def __init__(self, name, description, location, status, *args, **kwargs):
        super(Volcano, self).__init__(*args, **kwargs)

        self.name = name
        self.description = description
        self.location = location
        self.status = status


class Node(predix.data.asset.AssetCollection):
    def __init__(self, name, description, location, status, volcano,
            *args, **kwargs):
        super(Node, self).__init__(*args, **kwargs)

        self.name = name
        self.description = description
        self.location = location
        self.status = status
        self.volcano = volcano


class Sensor(predix.data.asset.AssetCollection):
    def __init__(self, description, status, data_type, data_frequency, node,
            *args, **kwargs):
        super(Sensor, self).__init__(*args, **kwargs)

        self.description = description
        self.status = status
        self.data_type = data_type
        self.data_frequency = data_frequency
        self.node = node


class DataType(predix.data.asset.AssetCollection):
    def __init__(self, data_type, unit, tag, *args, **kwargs):
        super(DataType, self).__init__(*args, **kwargs)

        self.data_type = data_type
        self.unit = unit
        self.tag = tag

