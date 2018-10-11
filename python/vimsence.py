import vim
import rpc
import time
import logging

start_time = int(time.time())
base_activity = {
        'details': 'Nothing',
        'timestamps': {
            "start": start_time
        },
        'assets': {
            'small_text': 'Vim',
            'small_image': 'vim_logo',
            'large_text': 'Vim',
            'large_image': 'vim_logo'
        }
    }

client_id = '425602550470017024'

try:
    rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)
    rpc_obj.set_activity(base_activity)
except Exception as e:
    # Discord is not running
    pass

def update_presence():
    """Update presence in Discord
    :returns: TODO

    """
    activity = base_activity
    activity['details'] = get_filename()
    activity['assets']['large_text'] = 'Editing a {} file'.format(get_extension().upper())
    if get_extension():
        activity['assets']['large_image'] = get_extension()

    try:
        rpc_obj.set_activity(activity)
    except BrokenPipeError as e:
        # Connection to Discord is lost
        pass
    except NameError as e:
        # Discord is not running
        pass

def get_filename():
    """Get current filename that is being edited
    :returns: string
    """
    return vim.eval('expand("%:t")')

def get_extension():
    """Get exension for file that is being edited
    :returns: string
    """
    return vim.eval('expand("%:e")')
