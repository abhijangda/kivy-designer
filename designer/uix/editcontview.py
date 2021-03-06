from kivy.uix.actionbar import ContextualActionView, ActionButton
from kivy.properties import ObjectProperty

from functools import partial

class EditContView(ContextualActionView):
    '''EditContView is a ContextualActionView, used to display Edit items:
       Copy, Cut, Paste, Undo, Redo, Select All, Add Custom Widget. It has
       events:
       on_undo, emitted when Undo ActionButton is clicked.
       on_redo, emitted when Redo ActionButton is clicked.
       on_cut, emitted when Cut ActionButton is clicked.
       on_copy, emitted when Copy ActionButton is clicked.
       on_paste, emitted when Paste ActionButton is clicked.
       on_delete, emitted when Delete ActionButton is clicked.
       on_selectall, emitted when Select All ActionButton is clicked.
       on_add_custom, emitted when Add Custom ActionButton is clicked.
    '''

    __events__ = ('on_undo', 'on_redo', 'on_cut', 'on_copy',
                  'on_paste', 'on_delete', 'on_selectall',
                  'on_next_screen', 'on_prev_screen')
    
    action_btn_next_screen = ObjectProperty(None, allownone=True)
    action_btn_prev_screen = ObjectProperty(None, allownone=True)

    def show_action_btn_screen(self, show):
        if self.action_btn_next_screen:
            self.remove_widget(self.action_btn_next_screen)
        if self.action_btn_prev_screen:
            self.remove_widget(self.action_btn_prev_screen)

        self.action_btn_next_screen = None
        self.action_btn_prev_screen = None

        if show:
            self.action_btn_next_screen = ActionButton(text="Next Screen")
            self.action_btn_next_screen.bind(on_press=partial(self.dispatch, 'on_next_screen'))
            self.action_btn_prev_screen = ActionButton(text="Previous Screen")
            self.action_btn_prev_screen.bind(on_press=partial(self.dispatch, 'on_prev_screen'))

            self.add_widget(self.action_btn_next_screen)
            self.add_widget(self.action_btn_prev_screen)

    def on_undo(self, *args):
        pass

    def on_redo(self, *args):
        pass

    def on_cut(self, *args):
        pass

    def on_copy(self, *args):
        pass

    def on_paste(self, *args):
        pass

    def on_delete(self, *args):
        pass

    def on_selectall(self, *args):
        pass

    def on_next_screen(self, *args):
        pass

    def on_prev_screen(self, *args):
        pass