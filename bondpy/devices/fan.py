from bondpy.devices.base import BondDevice

class BondFanDevice(BondDevice):

    def speed_list(self):
        return list(filter(lambda x: x.name().startswith('Speed'), self.commands))

    def set_speed(self, speed):
        self.api.device_control(self.obj_id, speed.command_id())

    def reverse(self):
        self.api.device_control(self.obj_id, list(filter(lambda x: x.name() == 'Reverse', self.commands))[0])

    def support_reverse(self):
        return len(list(filter(lambda x: x.name() == 'Reverse', self.commands))) > 0



