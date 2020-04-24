#!/usr/bin/env python3


"""

    Author: Hao Yu (yuhao@genomics.cn)
    Date:   2020-04-24
    
"""




import dash




class WebCDCP:
    """"""

    def __init__(self, name, root):
        """"""

        name = __name__ if name == None else name
        root = '/' if root == None else root

        self.app = dash.Dash(name=name, url_base_pathname=root)

    
    def deploy(self, port):
        """"""

        port = 8050 if port == None else port

        self.app.run_server(host='0.0.0.0', port=port)