"""Pure network helper functions (stdlib only, easy to unit test)."""

import ipaddress


def subnet_info(cidr: str) -> dict:
    """Return details about a CIDR block. Raises ValueError if invalid."""
    net = ipaddress.ip_network(cidr, strict=False)
    hosts = net.num_addresses - 2 if net.version == 4 and net.prefixlen < 31 else net.num_addresses
    return {
        "cidr": str(net),
        "version": net.version,
        "network_address": str(net.network_address),
        "broadcast_address": str(net.broadcast_address),
        "netmask": str(net.netmask),
        "prefix_length": net.prefixlen,
        "total_addresses": net.num_addresses,
        "usable_hosts": max(hosts, 0),
        "is_private": net.is_private,
    }


def cidrs_overlap(a: str, b: str) -> bool:
    """True if two CIDR blocks overlap. Raises ValueError if either is invalid."""
    na = ipaddress.ip_network(a, strict=False)
    nb = ipaddress.ip_network(b, strict=False)
    return na.version == nb.version and na.overlaps(nb)


def split_subnet(cidr: str, new_prefix: int) -> list[str]:
    """Split a CIDR block into smaller subnets of ``new_prefix`` length."""
    net = ipaddress.ip_network(cidr, strict=False)
    if new_prefix <= net.prefixlen:
        raise ValueError("new_prefix must be longer than the current prefix")
    if new_prefix > net.max_prefixlen:
        raise ValueError("new_prefix exceeds maximum prefix length")
    return [str(s) for s in net.subnets(new_prefix=new_prefix)]
