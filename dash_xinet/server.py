from jupyter_dash import JupyterDash as Dash
import socket

# Function to display hostname and
# IP address


def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Hostname :  ", host_name)
        print("IP : ", host_ip)
    except:
        print("Unable to get Hostname and IP")
        host_ip = 'localhost'
    return host_ip


# Driver code
host_ip = get_Host_name_IP()  # Function call

# This code is conributed by "Sharad_Bhardwaj".


NAME = __name__

META_TAGS = [
    {
        'name': 'description',
        'content': 'Using AI to develop anything interesting'
    },
    # A tag that tells the browser not to scale
    # desktop widths to fit mobile screens.
    # Sets the width of the viewport (browser)
    # to the width of the device, and the zoom level
    # (initial scale) to 1.
    #
    # Necessary for "true" mobile support.
    {
        'name': 'viewport',
        'content': 'width=device-width, initial-scale=1, shrink-to-fit=no'
    }
]


def create_app(name=NAME, server_url=None, title='Dash', external_stylesheets=None, **kwargs):
    # external_scripts = ['https://www.google-analytics.com/analytics.js']
    external_scripts = [
        "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML"]

    _external_stylesheets = ['https://xinetzone.github.io/Font-Awesome/css/all.css',
                             'https://xinetzone.github.io/w3css/4/w3.css',
                             'https://xinetzone.github.io/xinet-css/tabs.css']
    if external_stylesheets:
        external_stylesheets += _external_stylesheets
    else:
        external_stylesheets = _external_stylesheets
    kw = {
        'meta_tags': META_TAGS,
        'external_stylesheets': external_stylesheets,
        'external_scripts': external_scripts
    }
    kwargs.update(kw)
    app = Dash(name, server_url=server_url, title=title, **kwargs)
    return app


async def run_server(app, layout, host=host_ip, port=80, mode='external', debug=True, **kw):
    # host='0.0.0.0' 、 127.0.0.1
    # app = create_app()
    app.layout = layout
    app.run_server(mode, host=host, port=port,
                   debug=debug, use_reloader=False, **kw)
