# Networking (L2 / L3)

> Status: placeholder. Demo project to be added.

Hands-on, open-source demos covering Layer 2 switching and Layer 3 routing concepts, with repeatable labs you can run on a laptop.

## Scope

| Layer | Topics |
|---|---|
| L2 | VLANs, trunking (802.1Q), MAC learning, STP, LACP, ARP |
| L3 | IP addressing and subnetting, static routing, OSPF, BGP basics, VRFs, NAT |

## Planned demo

A small virtual lab that builds, configures and verifies a routed topology, driven from Python.

- Topology: 2 access switches, 2 routers, 2 VLANs with inter-VLAN routing
- Validation: automated ping, traceroute and route-table checks after each change
- Subnet planning helpers (reuses the idea from [`../CI-CD`](../CI-CD/README.md))

## Open-source stack

| Purpose | Tool |
|---|---|
| Lab emulation | [Containerlab](https://containerlab.dev), FRRouting, Linux bridge / Open vSwitch |
| Packet crafting and capture | Scapy, tcpdump, Wireshark |
| Device automation | Netmiko, NAPALM, Nornir |
| Source of truth | NetBox |
| Parsing and testing | TextFSM, pytest |

## Proposed layout

```
Networking-L2-L3/
├── labs/          # containerlab topology files
├── configs/       # device configs / templates (Jinja2)
├── src/           # Python automation and validation code
├── tests/
└── README.md
```

## Learning outcomes

- Explain how frames are forwarded at L2 and packets at L3
- Build and troubleshoot VLANs, inter-VLAN routing and a dynamic routing protocol
- Automate configuration and verify network state with code
