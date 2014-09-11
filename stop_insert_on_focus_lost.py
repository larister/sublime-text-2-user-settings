import sublime_plugin


class StopInsertOnFocusLost(sublime_plugin.EventListener):
    def on_deactivated(self, view):
        if view.settings().get('command_mode') is False:
            view.run_command('exit_insert_mode')

    def on_activated(self, view):
        if view.settings().get('is_widget') is True:
            view.run_command('enter_insert_mode')
