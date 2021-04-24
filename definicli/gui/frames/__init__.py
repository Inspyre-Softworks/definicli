from PySimpleGUI import \
    Frame as PSGFrame, \
    Button as Btn


class DynamicFrame:
    def __init__(self, layout, frame_key, window=None, start_visible=False):
        self.window = window
        self.key = frame_key
        self.element = PSGFrame('',
                                layout,
                                key=frame_key,
                                visible=start_visible)
        self.visible = self.element.visible
        print("{} {}".format(self.key, self.visible))


frame = DynamicFrame('', [[Btn('OK')]], "FRAME_1", True)

frame2 = DynamicFrame('', [[Btn('Close')]], 'FRAME_2')

main_layout = [[frame.element, frame2.element]]
#
