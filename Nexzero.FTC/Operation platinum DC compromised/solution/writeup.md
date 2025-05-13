# Operation Platinum DC Compromised - Analysis Report

## Summary

We were supplied a full network capture (PCAP) of the victim environment. By loading it into Wireshark/tshark and related tools, we traced NTLMSSP authentication attempts, extracted and cracked NTLMv2 hashes, decrypted WinRM sessions, reconstructed attacker payloads (including images), and ultimately observed the exfiltration of the domain controller's NTDS.dit database.

## Evidence Provided

- **File:** `chall.pcapng` (network capture of the incident)
- **Tools Used:**
  - Wireshark
  - tshark
  - NetworkMiner
  - Custom scripts
  - hashcat
  - CyberChef
  - Python
  - Shell scripting
  - LLMs (Claude)

## Analysis Steps

### 1. Identifying the Attacker's IP

1. **Loading the PCAP:** 
   - Opened `attack_traffic.pcap` in Wireshark
   - Found approximately 30MB of traffic with hundreds of HTTP POST requests
   - Identified EvilWinRM user agent, commonly used for Active Directory attacks

2. **Traffic Analysis:**
   - Applied display filter `ntlmssp` to isolate authentication traffic
   - Found repeated NTLMSSP failures from **192.168.183.50**, followed by a success

### 2. Pinpointing the First Successful Login

- **NTLMSSP Analysis:** 
  - First successful NTLMv2 authentication:
    - Time: **2024-11-30 10:54:43 UTC**
    - Frame: 3287
    - Source IP: **192.168.183.50**
    - Username: **BRANDO**

### 3. NTLMv2 Hash Extraction & Cracking

1. **Extracting the Hash:**
   - Used NetworkMiner/Apackets to parse PCAP and export NTLMv2 challenge/response pairs
   - Alternative: Used GitHub Python script (`extract_ntlmv2.py`) for exact `LMv2/NTLMv2` fields

2. **Cracking with hashcat:**
   - wordlist : rockyou
   - Recovered password: **Playerskillzpwn14**

![cracked password](https://github.com/n3xusss/Nexzero.FTC/blob/main/forensics/Operation%20platinum%20DC%20compromised/solution/1.png)

### 4. Decrypting WinRM Sessions

For WinRM decryption, an outdated tool from GitHub was used and fixed. The process required:
- Error handling for broken packets
- Continuation logic for failed decryption attempts

**Outcome:** Successfully decrypted hundreds of WinRM packets in XML format.

### 5. NTDS.dit Database Exfiltration

The analysis required understanding WinRM's XML-based data transmission using base64 payloads. The `clean.sh` script facilitated XML object payload extraction.

1. **Detection in PCAP:**
   - Identified commands related to NTDS.dit extraction (shadowcopy, vss)
   - Located multiple large base64 transfers matching NTDS.dit size characteristics

**Impact:** Complete domain credential dump (MITRE ATT&CK ID: T1003.003)

### 6. Image Reconstruction

Windows Remote Management allows file transfers in base64 format across multiple packets:
- Identified PNG header signatures in decrypted WinRM packets
- Used CyberChef to reconstruct image segments
- Found evidence of attacker searching for `cat.png`

![cat](https://github.com/n3xusss/Nexzero.FTC/blob/main/forensics/Operation%20platinum%20DC%20compromised/solution/2.png)

## Flag

```
nexus{192.168.183.50_2024-11-30_10:54:43_brando:Playerskillzpwn14_T1003.003_PWN3D}
```


