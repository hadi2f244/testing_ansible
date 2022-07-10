#!/usr/bin/python

from ansible.module_utils.basic import *

def main():
    module = AnsibleModule(      
        {
            "url": {"default": True, "type": "str"}
        }
    )
    import urllib.request
    response = urllib.request.urlopen(module.params["url"])
    module.exit_json(changed=False, response_code=response.code)

if __name__ == '__main__':
    main()

