import pytest

from app import netutils


def test_subnet_info_ipv4():
    info = netutils.subnet_info("10.0.0.0/24")
    assert info["netmask"] == "255.255.255.0"
    assert info["usable_hosts"] == 254
    assert info["is_private"] is True


def test_subnet_info_non_strict_host_bits():
    assert netutils.subnet_info("10.0.0.5/24")["cidr"] == "10.0.0.0/24"


def test_subnet_info_invalid():
    with pytest.raises(ValueError):
        netutils.subnet_info("not-a-cidr")


def test_overlap_true_and_false():
    assert netutils.cidrs_overlap("10.0.0.0/16", "10.0.1.0/24") is True
    assert netutils.cidrs_overlap("10.0.0.0/24", "10.0.1.0/24") is False


def test_overlap_mixed_versions():
    assert netutils.cidrs_overlap("10.0.0.0/8", "2001:db8::/32") is False


def test_split_subnet():
    assert netutils.split_subnet("10.0.0.0/24", 26) == [
        "10.0.0.0/26",
        "10.0.0.64/26",
        "10.0.0.128/26",
        "10.0.0.192/26",
    ]


@pytest.mark.parametrize("prefix", [24, 16, 33])
def test_split_subnet_invalid_prefix(prefix):
    with pytest.raises(ValueError):
        netutils.split_subnet("10.0.0.0/24", prefix)
