import time
import sys
import base64


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)


def call(section):
    print(" ")
    delay_print(f"{base64.b64decode(section).decode('utf-8')}\n")
    for item in data[section]:
        print(" ")
        for k, v in item.items():
            if not isinstance(v, list):
                delay_print(f"{base64.b64decode(k).decode('utf-8')} : {base64.b64decode(v).decode('utf-8')}\n")
            else:
                for e in v:
                    delay_print(f"{base64.b64decode(e).decode('utf-8')}\n")


data = {b'RVhQRVJJRU5DRVMgUFJPRkVTU0lPTk5FTExFUw==': [{b'VGl0cmU=': b'QWRtaW5pc3RyYXRldXIgU0lH',
                                          b'RW1wbG95ZXVy': b'VmlsbGUgZGUgTm91bcOpYQ==',
                                          b'QW5uw6ll': b'MjAyMA==',
                                          b'RHVyw6ll': b'NCBhbnM=',
                                          b'TGlldQ==': b'Tm91bcOpYSwgTm91dmVsbGUtQ2Fsw6lkb25pZSAoOTgp',
                                          b'VGFjaGVz': [
                                              b'LSBBZG1pbmlzdHJhdGlvbiBldCBtYWludGllbiBlbiBjb25kaXRpb24gb3DDqXJhdGlvbm5lbGxlIGR1IFNJRy4=',
                                              b'LSBWZWlsbGUgdGVjaG5vbG9naXF1ZSBldCDDqXZvbHV0aW9uIGRlIGwnYXJjaGl0ZWN0dXJlIGR1IFNJRy4=',
                                              b'LSBHZXN0aW9uIGV0IHN1cHBvcnQgZHUgcGFyYyB1dGlsaXNhdGV1ci4=',
                                              b'LSBHZXN0aW9uIGV0IHLDqWFsaXNhdGlvbiBkZSBwcm9qZXRzIFNJRyBtw6l0aWVycyBldCB0cmFuc3ZlcnNhdXgu',
                                              b'LSBEw6l2ZWxvcHBlbnQgZCdvdXRpbCBkJ2FpZGUgw6AgbGEgZ2VzdGlvbiBkdSBTSUcgKHB5dGhvbiwgU1FMKS4=',
                                              b'LSBBbmFseXNlcyBzcGF0aWFsZXMgYXZhbmPDqWVzLg==',
                                              b'LSBJbnTDqXJpbSBkdSBjaGVmIGRlIGTDqXBhcnRlbWVudCBTSUcu']
                                          },
                                         {b'VGl0cmU=': b'SW5nw6luaWV1ciBTSUcgLSBGb3JtYXRldXIgQXJjR0lT',
                                          b'RW1wbG95ZXVy': b'TUFHSVMgU0FSTA==',
                                          b'QW5uw6ll': b'MjAxMg==',
                                          b'RHVyw6ll': b'OCBhbnM=',
                                          b'TGlldQ==': b'Tm91bcOpYSwgTm91dmVsbGUtQ2Fsw6lkb25pZSAoOTgp',
                                          b'VGFjaGVz': [
                                              b'LSBHZXN0aW9uIGV0IHLDqWFsaXNhdGlvbiBkZSBwcm9qZXRzIFNJRy4=',
                                              b'LSBCYXNlcyBkZSBkb25uw6llcyA6IGNvbmNlcHRpb24sIG1vZMOpbGlzYXRpb24sIHN0cnVjdHVyYXRpb24sIGF1dG9tYXRpc2F0aW9uLCBpbnRlcm9ww6lyYWJpbGl0w6ksIHF1YWxpdMOpLCBtw6l0YWRvbm7DqWVzLg==',
                                              b'LSBQdWJsaWNhdGlvbiBkZSBzZXJ2aWNlcyBXZWIgU0lHLCB0cmFpdGVtZW50IFNJRyBhdmFuY8Opcy4=',
                                              b'LSBDb25jZXB0aW9uIGRlIGNhcnRlcyBldCBkZSBzZXJ2aWNlcyBXZWIu',
                                              b'LSBEw6l2ZWxvcHBlbWVudCBQeXRob24gcG91ciBBcmNHSVMsIGF1dG9tYXRpc2F0aW9uIGV0IG91dGlscyBtw6l0aWVyLg==']
                                          },
                                         {b'VGl0cmU=': b'SW5nw6luaWV1ciBTSUc=',
                                          b'RW1wbG95ZXVy': b'Q29uc3VsdGFudCBpbmTDqXBlbmRhbnQ=',
                                          b'QW5uw6ll': b'QW5uw6ll',
                                          b'RHVyw6ll': b'MSBhbg==',
                                          b'TGlldQ==': b'Tm91bcOpYSwgTm91dmVsbGUtQ2Fsw6lkb25pZSAoOTgp',
                                          b'VGFjaGVz': [
                                              b'LSBSw6lhbGlzYXRpb24gZGUgcHJvamV0cyBTSUcu',
                                              b'LSBBdXRvbWF0aXNhdGlvbiwgdHJhaXRlbWVudCBTSUcgYXZhbmPDqXMu',
                                              b'LSBDb25jZXB0aW9uIGRlIGNhcnRlcy4=']
                                          }],
        b'QUdSRU1FTlQgLSBDRVJUSUZJQ0FUSU9O': [{b'QW5uw6ll': b'MjAyMA==',
                                      b'VGl0cmU=': b'QWdyw6ltZW50IGRlIGZvcm1hdGV1ciBk4oCZYWR1bHRlcyBERlBDIE7CsCAyMDIwLzA1MDI='},
                                     {b'QW5uw6ll': b'MjAxNQ==',
                                      b'VGl0cmU=': b'Q2VydGlmaWNhdGlvbiB0ZWNobmlxdWUgRVNSSSDigJMgQXJjR0lTIERlc2t0b3AgQXNzb2NpYXRlIA=='}],
        b'Rk9STUFUSU9OIElOSVRJQUxF': [{b'QW5uw6ll': b'MjAxMQ==',
                                b'VGl0cmU=': b'TWFzdGVyIDIgUHJvZmVzc2lvbm5lbCBHw6lvbWF0aXF1ZSAtIFNJR01B',
                                b'TGlldQ==': b'VW5pdmVyc2l0w6kgVG91bG91c2UgSUkg4oCTIExlIE1pcmFpbCAoMzEp'},
                               {b'QW5uw6ll': b'MjAxMA==',
                                b'VGl0cmU=': b'TWFzdGVyIDEgU0lHIGV0IEFtw6luYWdlbWVudCBkdSBUZXJyaXRvaXJlIC0gU0lHQVQ=',
                                b'TGlldQ==': b'VW5pdmVyc2l0w6kgUmVubmVzIDIgSGF1dGUgQnJldGFnbmUgKDM1KSA='},
                               {b'QW5uw6ll': b'MjAwOQ==',
                                b'VGl0cmU=': b'TGljZW5jZSBQcm9mZXNzaW9ubmVsbGUgU0lHIC0gTFVQU0lH',
                                b'TGlldQ==': b'VW5pdmVyc2l0w6kgZGUgTGEgUm9jaGVsbGUgKDE3KQ=='
                                }],
        b'Q09NUEVURU5DRVM=': [{b'QWRtaW5pc3RyYXRpb24gZHUgU0lH': b'NzUgJQ=='},
                        {b'QmFzZSBkZSBkb25uw6llcw==': b'ODUgJQ=='},
                        {b'QW5hbHlzZXMgc3BhdGlhbGVz': b'ODAgJQ=='},
                        {b'R2VzdGlvbiBkZSBwcm9qZXQ=': b'NzUgJQ=='},
                        {b'RMOpdmVsb3BwZW1lbnQgUHl0aG9u': b'OTAgJQ=='},
                        {b'U3VwcG9ydCB1dGlsaXNhdGV1cg==': b'OTUgJQ=='},
                        {b'Q29uY2VwdGlvbiBncmFwaGlxdWU=': b'NzAgJQ=='},
                        {b'QW5nbGFpcw==': b'NzAgJQ=='}],
        b'Q09OVEFDVA==': [{b'VMOpbMOpcGhvbmU=': b'KzY4NyA4MSA5OSA4Nw=='},
                    {b'RW1haWw=': b'amVyZW1pZS5wZWRvaWFAZ21haWwuY29t'},
                    {b'QWRyZXNzZQ==': b'NCBydWUgSkVOTkVSLCA5ODgwMCBOT1VNRUE='},
                    {b'bGlua2VkaW4=':b'aHR0cHM6Ly93d3cubGlua2VkaW4uY29tL2luL2rDqXLDqW1pZS1wZWRvaWEtYjFhNTNhMjkv'}],
        b'SU5GTyAr': [{b'QWdl': b'MzcgYW5z'},
                   {b'U2l0dWF0aW9uIGZhbWlsaWFsZQ==': b'TWFyacOpLCBkZXV4IGVuZmFudHM='},
                   {b'TW9iaWxpdMOp': b'UGVybWlzIEExLCBBLCBC'}],
        b'TE9JU0lSUw==': [{b'TG9pc2lycw==': [b'RGVzaWduIC0gQ29uY2VwdGlvbiBncmFwaGlxdWU=', b'QmFza2V0IEJhbGw=', b'QmlsbGFyZA==', b'SmV1eCB2aWTDqW8=', b'TXVzaXF1ZQ==',
                                 b'U3BvcnRzIG3DqWNhbmlxdWVz', b'QnJpY29sYWdl', b'UMOqY2hl']}]
        }

sections = [b'RVhQRVJJRU5DRVMgUFJPRkVTU0lPTk5FTExFUw==', b'QUdSRU1FTlQgLSBDRVJUSUZJQ0FUSU9O', b'Rk9STUFUSU9OIElOSVRJQUxF', b'Q09NUEVURU5DRVM=', b'Q09OVEFDVA==',
            b'SU5GTyAr', b'TE9JU0lSUw==']

delay_print(f"{base64.b64decode(b'QmllbnZlbnVlIGRhbnMgbGUgUHl0aHVtIFZpdGFlIGRlIErDqXLDqW1pZSBQRURPSUEsIGluZ8OpbmlldXIgU0lH').decode('utf-8')}\n\n")


delay_print(f"{base64.b64decode(b'LSBDViBjb21wbGV0ICAgICAgICAgICAgICAgICAgIDogdGFwZXogMA==').decode('utf-8')}\n"
            f"{base64.b64decode(b'LSBFeHDDqXJpZW5jZXMgcHJvZmVzc2lvbm5lbGxlcyA6IHRhcGV6IDE=').decode('utf-8')}\n"
            f"{base64.b64decode(b'LSBBZ3LDqW1lbnQgLSBDZXJ0aWZpY2F0aW9uICAgICA6IHRhcGV6IDI=').decode('utf-8')}\n"
            f"{base64.b64decode(b'LSBGb3JtYXRpb24gaW5pdGlhbGUgICAgICAgICAgIDogdGFwZXogMw==').decode('utf-8')}\n"
            f"{base64.b64decode(b'LSBDb21ww6l0ZW5jZXMgICAgICAgICAgICAgICAgICA6IHRhcGV6IDQ=').decode('utf-8')}\n"
            f"{base64.b64decode(b'LSBDb250YWN0ICAgICAgICAgICAgICAgICAgICAgIDogdGFwZXogNQ==').decode('utf-8')}\n"
            f"{base64.b64decode(b'LSBJbmZvICsgICAgICAgICAgICAgICAgICAgICAgIDogdGFwZXogNg==').decode('utf-8')}\n"
            f"{base64.b64decode(b'LSBMb2lzaXJzIGV0IGNlbnRyZSBkJ2ludMOpcsOqdHMgOiB0YXBleiA3').decode('utf-8')}\n"
            f"{base64.b64decode(b'LSBRdWl0dGVyICAgICAgICAgICAgICAgICAgICAgIDogdGFwZXogOQ==').decode('utf-8')}\n"
            )

toPrint = -1

mystery = b'MTI='

while toPrint != 9:
    print(" ")
    toPrint = int(input(f"{base64.b64decode(b'Vm90cmUgY2hvaXggPT4gOg==').decode('utf-8')}"))
    
    if toPrint == 0:
        for i, v in enumerate(sections):
            call(v)
    elif 0 < toPrint < 8:
        s = sections[toPrint - 1]
        call(s)
        
    if base64.b64encode(str.encode(str(toPrint))) == mystery:
        delay_print(f"{base64.b64decode(b'ICAgICAgICAgICAgICAgTyAgbw==').decode('utf-8')}\n")
        delay_print(f"{base64.b64decode(b'ICAgICAgICAgIF9cXyAgIG8=').decode('utf-8')}\n")
        delay_print(f"{base64.b64decode(b'PignPiAgIFxcLyAgb1wgLg==').decode('utf-8')}\n")
        delay_print(f"{base64.b64decode(b'ICAgICAgIC8vXF9fXz0=').decode('utf-8')}\n")
        delay_print(f"{base64.b64decode(b'ICAgICAgICAgICcn').decode('utf-8')}\n")

delay_print(f"{base64.b64decode(b'TWVyY2kgZGUgdm90cmUgYXR0ZW50aW9uICE=').decode('utf-8')}")