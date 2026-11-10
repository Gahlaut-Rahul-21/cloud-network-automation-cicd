# VPN (S2S / C2S) and IPsec

> Status: placeholder. Demo project to be added.

Open-source demos of site-to-site (S2S) and client-to-site (C2S) VPNs, with IPsec as the core protocol suite.

## Scope

| Area | Topics |
|---|---|
| IPsec fundamentals | IKEv1 vs IKEv2, ESP vs AH, tunnel vs transport mode, SAs, Phase 1 / Phase 2, NAT-T, DPD |
| Site-to-Site (S2S) | Policy-based vs route-based tunnels, VTI / XFRM interfaces, overlapping subnets, BGP over IPsec |
| Client-to-Site (C2S) | Remote access with IKEv2 (EAP / certs), WireGuard and OpenVPN comparison, split vs full tunnel |
| Security | PSK vs certificate auth, cipher suite selection, PFS, rekeying |

## Planned demo

A containerised lab with two "sites" and a roaming client.

1. **S2S:** Site A and Site B gateways form an IKEv2 route-based IPsec tunnel; hosts behind each reach one another
2. **C2S:** a remote client connects to Site A with IKEv2 and reaches internal resources
3. **Validation:** Python checks tunnel state, SA lifetimes and end-to-end ping, plus a packet capture showing ESP traffic
4. **Failure tests:** kill a gateway and confirm DPD detects it and the tunnel recovers

## Open-source stack

| Purpose | Tool |
|---|---|
| IPsec / IKE daemon | [strongSwan](https://www.strongswan.org) (swanctl), Libreswan |
| Alternative VPNs | WireGuard, OpenVPN |
| Lab emulation | Docker Compose or Containerlab, Linux network namespaces |
| Certificates | OpenSSL or step-ca |
| Packet analysis | tcpdump, Wireshark, Scapy |
| Automation and tests | Python, Jinja2 (config templates), pytest |

## Proposed layout

```
VPN-IPsec/
├── labs/          # docker-compose / containerlab topology
├── configs/       # swanctl.conf, WireGuard, OpenVPN templates
├── pki/           # scripts to generate CA and certificates (no keys committed)
├── src/           # Python tunnel status and validation checks
├── tests/
└── README.md
```

## Notes

- Lab-only credentials: never commit private keys or pre-shared keys; generate them at runtime
- Containers need `NET_ADMIN` capability, so a Linux host or Docker Desktop VM is required

## Learning outcomes

- Explain how an IPsec tunnel is negotiated and how traffic is protected
- Build and troubleshoot S2S and C2S VPNs
- Choose between IPsec, WireGuard and OpenVPN for a given use case
