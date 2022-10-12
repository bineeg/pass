from discord_webhook import DiscordWebhook
from optparse import OptionParser
import json
import sys

verbose = False
buffer = ""
pipe = False
msg_data = ""
id = ""
app_list = ['discord']


def discord_messenger(hook_url):
    global msg_data
    try:
        webhook = DiscordWebhook(
            url=hook_url, content=msg_data, username='pass',)
        response = webhook.execute()
    except Exception as e:
        print('\n\t'+str(e))


def load_config_file():
    try:
        # provide full path
        with open('pass_config.json', 'r') as file_data:
            config = json.load(file_data)
            return config
    except FileNotFoundError:
        print('[!] Config file missing')
        exit(0)


def data_file_load(file_name):
    global msg_data
    try:
        f = open(file_name, "r")
        msg_data = f.read()
    except Exception as e:
        print("Exception : "+str(e))


def cmd_inline_data():
    global buffer, msg_data
    for cmd_input in sys.stdin:
        buffer += cmd_input
    msg_data = buffer


def parse_options():
    global verbose, id, app_list
    usage = "Usage:  \n\tpython3 pass.py -data <data-file> --id <id-from-config>\n\tcat data | python3 pass.py --pipe --id <id-from-config>"

    parser = OptionParser(
        usage=usage)

    # add options
    parser.add_option('-d', '--data', dest='data', metavar="data",
                      type='string',
                      help='path of data file',)
    parser.add_option('-i', '--id', dest='id', metavar="id",
                      type='string',
                      help='unique id',)
    parser.add_option('-v', "--verbose", action="store_true",
                      dest="verbose", default=False, help="print status")
    parser.add_option('-p', "--pipe", action="store_true",
                      dest="pipe", default=False, help="pipe from another output")

    (options, args) = parser.parse_args()
    if (options.pipe and options.data != None):
        print("\tUse one parameter pipe / data , please check help\n")
    elif options.pipe:
        cmd_inline_data()
    elif (options.data == None):
        print("\t-d / --data parameter is missing , please check help\n")
        exit(0)
    else:
        file_name = options.data
        data_file_load(file_name)
    if options.id == None:
        print("\t-i / --id parameter is missing , please check help\n")
        exit(0)
    else:
        id = options.id
    if options.verbose:
        verbose = True


def parse_config(config):
    global id
    config_list = config
    found = False
    for i in config_list:

        if (i['id'] == id):
            found = True
            if i['app_name'] in app_list:
                if (i['app_name'] == app_list[0]):
                    webhookurl = i['webhookurl']
                    if not (not webhookurl):
                        discord_messenger(webhookurl)
                    else:
                        print('\t\n webhook url missing')
            else:
                print('\tMisconfigured config file\n')
    if found == False:
        print("\n\tProvided id not found, please check config file")
        exit(0)


if __name__ == "__main__":
    banner = """
        PASS
            Tool to pass data to webhook

    """
    config = load_config_file()
    parse_options()
    if verbose:
        print(banner)
    parse_config(config)
