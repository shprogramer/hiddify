{
  "log": {
    "level": "warn",
    "output": "box.log",
    "timestamp": true
  },
  "dns": {
    "servers": [
      {
        "tag": "dns-remote",
        "address": "udp://1.1.1.1",
        "address_resolver": "dns-direct"
      },
      {
        "tag": "dns-trick-direct",
        "address": "https://sky.rethinkdns.com/",
        "detour": "direct-fragment"
      },
      {
        "tag": "dns-direct",
        "address": "1.1.1.1",
        "address_resolver": "dns-local",
        "detour": "direct"
      },
      {
        "tag": "dns-local",
        "address": "local",
        "detour": "direct"
      },
      {
        "tag": "dns-block",
        "address": "rcode://success"
      }
    ],
    "rules": [
      {
        "domain_suffix": ".ir",
        "geosite": "ir",
        "server": "dns-direct"
      },
      {
        "domain": "cp.cloudflare.com",
        "server": "dns-remote",
        "rewrite_ttl": 3000
      }
    ],
    "final": "dns-remote",
    "static_ips": {
      "sky.rethinkdns.com": [
        "188.114.97.3",
        "188.114.96.3",
        "2a06:98c1:3120::3",
        "2a06:98c1:3121::3",
        "104.17.148.22",
        "104.17.147.22",
        "188.114.96.3",
        "188.114.97.3",
        "2a06:98c1:3120::3",
        "2a06:98c1:3121::3"
      ]
    },
    "independent_cache": true
  },
  "inbounds": [
    {
      "type": "tun",
      "tag": "tun-in",
      "mtu": 9000,
      "inet4_address": "172.19.0.1/28",
      "auto_route": true,
      "strict_route": true,
      "endpoint_independent_nat": true,
      "stack": "mixed",
      "sniff": true,
      "sniff_override_destination": true
    },
    {
      "type": "mixed",
      "tag": "mixed-in",
      "listen": "127.0.0.1",
      "listen_port": 2334,
      "sniff": true,
      "sniff_override_destination": true
    },
    {
      "type": "direct",
      "tag": "dns-in",
      "listen": "127.0.0.1",
      "listen_port": 6450
    }
  ],
  "outbounds": [
    {
      "type": "selector",
      "tag": "select",
      "outbounds": [
        "auto",
        "IP-\u003eIran, Yotube:Geekmeek",
        "IP-\u003eMain, Yotube:Geekmeek"
      ],
      "default": "auto"
    },
    {
      "type": "urltest",
      "tag": "auto",
      "outbounds": [
        "IP-\u003eIran, Yotube:Geekmeek",
        "IP-\u003eMain, Yotube:Geekmeek"
      ],
      "url": "http://cp.cloudflare.com/",
      "interval": "10m0s",
      "idle_timeout": "1h40m0s"
    },
    {
      "type": "wireguard",
      "tag": "IP-\u003eIran, Yotube:Geekmeek",
      "local_address": [
        "172.16.0.2/32",
        "2606:4700:110:8981:4697:3548:ae5e:8d59/128"
      ],
      "private_key": "oHKNewDczj1piAutcVpP+zDvfFXZpqsCR74aqLygInM=",
      "server": "162.159.195.151",
      "server_port": 988,
      "peer_public_key": "bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=",
      "reserved": "GVff",
      "mtu": 1280,
      "fake_packets": "5-10"
    },
    {
      "type": "wireguard",
      "tag": "IP-\u003eMain, Yotube:Geekmeek",
      "detour": "IP-\u003eIran, Yotube:Geekmeek",
      "local_address": [
        "172.16.0.2/32",
        "2606:4700:110:8cf7:b8ce:f07e:240:2153/128"
      ],
      "private_key": "kMO6H2p/EjAdRvSzn7QofLIgzbnQB0qH8TbNDYwXTlM=",
      "server": "162.159.195.151",
      "server_port": 988,
      "peer_public_key": "bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=",
      "reserved": "MgOF",
      "mtu": 1230
    },
    {
      "type": "dns",
      "tag": "dns-out"
    },
    {
      "type": "direct",
      "tag": "direct"
    },
    {
      "type": "direct",
      "tag": "direct-fragment",
      "tls_fragment": {
        "enabled": true,
        "size": "1-500",
        "sleep": "0-500"
      }
    },
    {
      "type": "direct",
      "tag": "bypass"
    },
    {
      "type": "block",
      "tag": "block"
    }
  ],
  "route": {
    "geoip": {
      "path": "geo-assets/sagernet-sing-geoip-geoip.db"
    },
    "geosite": {
      "path": "geo-assets/sagernet-sing-geosite-geosite.db"
    },
    "rules": [
      {
        "inbound": "dns-in",
        "outbound": "dns-out"
      },
      {
        "port": 53,
        "outbound": "dns-out"
      },
      {
        "clash_mode": "Direct",
        "outbound": "direct"
      },
      {
        "clash_mode": "Global",
        "outbound": "select"
      },
      {
        "domain_suffix": ".ir",
        "geosite": "ir",
        "geoip": "ir",
        "outbound": "bypass"
      }
    ],
    "final": "select",
    "auto_detect_interface": true,
    "override_android_vpn": true
  },
  "experimental": {
    "cache_file": {
      "enabled": true,
      "path": "clash.db"
    },
    "clash_api": {
      "external_controller": "127.0.0.1:6756",
      "secret": "mv0qGBpbH3c8xZIT"
    }
  }
}
