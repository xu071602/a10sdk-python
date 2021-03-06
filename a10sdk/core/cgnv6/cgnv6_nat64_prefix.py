from a10sdk.common.A10BaseClass import A10BaseClass


class Prefix(A10BaseClass):
    
    """Class Description::
    Configure NAT64 Prefix.

    Class prefix supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param vrid: {"description": "VRRP-A vrid (Specify ha VRRP-A vrid)", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": true}
    :param prefix_val: {"optional": false, "type": "string", "description": "NAT64 Prefix", "format": "ipv6-address-plen"}
    :param class_list: {"description": "Class-list to match for NAT64", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat64/prefix/{prefix_val}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "prefix_val"]

        self.b_key = "prefix"
        self.a10_url="/axapi/v3/cgnv6/nat64/prefix/{prefix_val}"
        self.DeviceProxy = ""
        self.vrid = ""
        self.prefix_val = ""
        self.class_list = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


