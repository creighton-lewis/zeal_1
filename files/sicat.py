from sicat_2.lib.vuln_exploitdb import ExploitDB
from sicat_2.lib.vuln_packetstormsecurity import PacketStormSecurity
from sicat_2.lib.module_msf import MsfModule
from sicat_2.lib.cve_nvd import NvdDB
from sicat_2.common.out_parse import Output
from sicat_2.common.nmap_parse import NmapParse
import argparse




def main(args, keyword="", keyword_version=""):
    if keyword == None or args.nmap == None:
        pass
    else:
        Output.start(keyword, keyword_version)

    if args.exploitdb:
        if keyword_version != None:
            getnvd = ExploitDB.find(keyword, keyword_version)
        else:
            getnvd = ExploitDB.find(keyword)
        Output.exploitdb(getnvd)

    if args.packetstorm:
        if keyword_version != None:
            getnvd = PacketStormSecurity.find(keyword, keyword_version)
        else:
            getnvd = PacketStormSecurity.find(keyword)
        Output.packetstormsecurity(getnvd)

    if args.msfmodule:
        if keyword_version != None:
            getnvd = MsfModule.find(keyword, keyword_version)
        else:
            getnvd = MsfModule.find(keyword)
        Output.msfmodule(getnvd)

    if args.nvd:
        if keyword_version != None:
            getnvd = NvdDB.find(keyword, keyword_version)
        else:
            getnvd = NvdDB.find(keyword)
        Output.nvddb(getnvd)


    if args.output:
        if args.output_type  == "json":
            Output.outJson(args.output)
        elif args.output_type  == "html":
            Output.outHtml(args.output)
        else:
            Output.outJson(args.output)
            Output.outHtml(args.output)


if __name__ == "__main__":
    #Initialize
    ExploitDB = ExploitDB()
    PacketStormSecurity = PacketStormSecurity()
    MsfModule = MsfModule()
    NvdDB = NvdDB()
    Output = Output()
    NmapParse = NmapParse()


    # print banner
    Output.banner()

    # Initialize the parser
    parser = argparse.ArgumentParser(description='Script to search for vulnerability and exploitation information.')

    # Add arguments
    parser.add_argument('-k','--keyword', type=str, help='File name or path to save the output')
    parser.add_argument('-kv','--keyword_version', type=str, help='File name or path to save the output')
    parser.add_argument('-nm','--nmap', type=str, help='Identify via nmap output')
    parser.add_argument('--nvd', action='store_true', help='Use NVD as a source of information')
    parser.add_argument('--packetstorm', action='store_true', help='Use PacketStorm as a source of information')
    parser.add_argument('--exploitdb', action='store_true', help='Use ExploitDB as a source of information')
    parser.add_argument('--msfmodule', action='store_true', help='Use metasploit module as a source of information')
    parser.add_argument('-o','--output', type=str, help='path to save the output')
    parser.add_argument('-ot','--output_type', type=str, help='output file type json and html')

    args = parser.parse_args()

    if args.nmap:
        nmparse = NmapParse.parse(args.nmap)
        if nmparse:
            for service in nmparse:
                main(args, service['service'], service['version'])
        else:
            print("[!] Only Supported for single host portscan result")
    else:
        keyword = args.keyword
        keyword_version = args.keyword_version
        main(args, keyword , keyword_version)

