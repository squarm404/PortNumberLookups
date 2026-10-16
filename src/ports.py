
class PortFinder:
 
    def port_search():

        PORT_PROTOCOLS = {
        7: "Echo",          19: "CHARGEN",       20: "FTP-data",     21: "FTP",
        22: "SSH/SCP/SFTP", 23: "Telnet",        25: "SMTP",         42: "WINS Replication",
        43: "WHOIS",        49: "TACACS",         53: "DNS",          67: "DHCP/BOOTP",
        68: "DHCP/BOOTP",   69: "TFTP",           70: "Gopher",       79: "Finger",
        80: "HTTP",         88: "Kerberos",       102: "MS Exchange ISO-TSAP",
        110: "POP3",        113: "Ident",         119: "NNTP (Usenet)", 123: "NTP",
        135: "MS RPC EPMAP",137: "NetBIOS-ns",    138: "NetBIOS-dgm", 139: "NetBIOS-ssn",
        143: "IMAP",        161: "SNMP-agents",   162: "SNMP-trap",   177: "XDMCP",
        179: "BGP",         194: "IRC",           201: "AppleTalk",   264: "BGMP",
        318: "TSP",         381: "HP Openview",   383: "HP Openview", 389: "LDAP",
        411: "(Multiple)",  412: "(Multiple)",    427: "SLP",         443: "HTTPS",
        445: "MS DS SMB",   464: "Kerberos",      465: "SMTP/TLS",    497: "Dantz Retrospect",
        500: "IPSec/IKE",   512: "rexec",         513: "rlogin",      514: "syslog",
        515: "LPD/LPR",     520: "RIP",           521: "RIPng",       540: "UUCP",
        546: "DHCPv6",      547: "DHCPv6",        548: "AFP",         554: "RTSP",
        560: "rmonitor",    563: "NNTP/TLS",      587: "SMTP",        591: "FileMaker",
        593: "MS DCOM",     596: "SMSD",          631: "IPP",         636: "LDAP/TLS",
        639: "MSDP (PIM)",  646: "LDP (MPLS)",    691: "MS Exchange", 860: "iSCSI",
        873: "rsync",       902: "VMware Server", 989: "FTPS",        990: "FTPS",
        993: "IMAPS",       995: "POP3S",
    }

        try:
            port_input = int(input("Please Insert Port Number: "))

            if port_input in PORT_PROTOCOLS.keys():
                print(PORT_PROTOCOLS.get(port_input))
        
        except Exception as e:
            print(f"incorrect try dat again. {e}")




#obj

port_lookup = PortFinder.port_search()


if __name__ == "__main__":
    port_lookup 
