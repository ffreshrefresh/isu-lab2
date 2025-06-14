#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import subprocess
import datetime
import random
import sys

# ─── Helper: Load JSON Files ──────────────────────────────────────────────
def load_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Load configurations and data
descriptions  = load_json('descriptions.json')
threat_intel  = load_json('threat_intel.json')
try:
    with open('targets.txt','r', encoding='utf-8') as f:
        osint_targets = [l.strip() for l in f if l.strip()]
except FileNotFoundError:
    osint_targets = []

# ─── UI Functions ─────────────────────────────────────────────────────────
def show_welcome():
    print('\n=== NmapEducator ===')
    print('Ağ tarama tekniklerini öğrenmek için bir seçim yapın.\n')

def show_menu():
    print('1)  Ping Taraması (-sn)')
    print('2)  TCP Taraması (-sT)')
    print('3)  SYN Taraması (-sS)')
    print('4)  OS Tespiti (-O)')
    print('5)  Servis Versiyon Tespiti (-sV)')
    print('6)  Script Taraması (vuln)')
    print('7)  Hepsi Bir Arada')
    print('8)  IPv6 Ping Taraması (-6 -sn)')
    print('9)  Zamanlama Şablonları (--T0 .. --T5)')
    print('10) OpenVAS Export (XML)')
    print('11) Evasion Mode (Packet Manipulation)')
    print('12) Cloud Metadata Sorgu')
    print('13) IoT Tarama')
    print('14) Web Enum Tarama')
    print('15) OSINT Hazırlık')
    print('16) Stealth Mode Tarama')
    print('17) XML Görüntüleme')
    print('18) WAF Tespiti')
    print('19) Anomali Tespit Modu')
    print('20) Tehdit İstihbaratı Modu')
    print('0)  Çıkış\n')

# ─── Core Scan Function ───────────────────────────────────────────────────
def run_scan(args, title):
    target = input('Hedef IP/domain girin: ').strip()
    desc   = descriptions.get(args, '')
    print(f"\n[+] {title}")
    if desc:
        print(f"[i] Açıklama: {desc}")
    print(f"[>] nmap {args} {target}\n")
    try:
        result = subprocess.check_output(f"nmap {args} {target}", shell=True, text=True)
        print(result)
        with open('scan_log.txt','a', encoding='utf-8') as log:
            ts = datetime.datetime.now().isoformat()
            log.write(f"\n[{ts}] {title} ({target})\n{result}\n")
    except subprocess.CalledProcessError as e:
        print('[!] Tarama hatası:', e)

# ─── Main Application Loop ─────────────────────────────────────────────────
def main():
    # Standard mappings
    args_map = {
        '1':  '-sn',
        '2':  '-sT',
        '3':  '-sS',
        '4':  '-O',
        '5':  '-sV',
        '6':  '--script vuln',
        '7':  '-sS -sV -O --script vuln',
        '8':  '-6 -sn',
        '9':  '-sn',   # base + timing appended
        '10': '-oX openvas.xml',
        '12': '--script http-fetch',
        '13': '-p 1900,5683',
        '14': '--script http-enum',
        '16': '-sI ::1',
        '17': '-oX scan.xml',
        '18': '--script http-waf-fingerprint'
    }
    titles = {
        '1':  'Ping Taraması',
        '2':  'TCP Taraması',
        '3':  'SYN Taraması',
        '4':  'OS Tespiti',
        '5':  'Servis Versiyon Tespiti',
        '6':  'Script Taraması (vuln)',
        '7':  'Hepsi Bir Arada',
        '8':  'IPv6 Ping Taraması',
        '10': 'OpenVAS Export',
        '12': 'Cloud Metadata Sorgu',
        '13': 'IoT Tarama',
        '14': 'Web Enum Tarama',
        '16': 'Stealth Mode Tarama',
        '17': 'XML Görüntüleme',
        '18': 'WAF Tespiti'
    }

    show_welcome()
    while True:
        show_menu()
        choice = input('Seçiminiz: ').strip()
        if choice == '0':
            print('Çıkılıyor…')
            break

        # 1-8 and 10,12,13,14,16,17,18 basic scans
        if choice in args_map and choice not in ['9', '11', '15', '19', '20']:
            run_scan(args_map[choice], titles.get(choice, 'Nmap Tarama'))

        elif choice == '9':
            # Timing templates
            templates = {
                '0': ('Paranoid', '-T0'),
                '1': ('Sneaky', '-T1'),
                '2': ('Polite',  '-T2'),
                '3': ('Normal',  '-T3'),
                '4': ('Aggressive','-T4'),
                '5': ('Insane',  '-T5')
            }
            print('\nZamanlama Modları:')
            for k,(n,_) in templates.items():
                print(f"{k}) {n}")
            sel = input('Seçiminiz: ').strip()
            if sel in templates:
                name, flag = templates[sel]
                run_scan(f"-sn {flag}", f"Ping Taraması ({name})")
            else:
                print('[!] Geçersiz şablon.')

        elif choice == '11':
            # Evasion / Packet manipulation included by user (skip here)
            print('[!] Bu seçenek zaten Evasion Mode altında mevcut.')

        elif choice == '15':
            # OSINT Tarama
            if not osint_targets:
                print('[!] targets.txt bulunamadı veya boş.')
            else:
                for ip in osint_targets:
                    run_scan('-sn', f"OSINT Tarama ({ip})")

        elif choice == '19':
            # Anomaly detection
            try:
                with open('scan_log.txt','r', encoding='utf-8') as f:
                    logs = f.read().strip().split('\n\n')
                if len(logs) < 2:
                    print('[!] Yeterli tarama geçmişi yok.')
                else:
                    prev_set = set(logs[-2].splitlines())
                    curr_set = set(logs[-1].splitlines())
                    diff = curr_set - prev_set
                    print('\n[!] Anomali Tespit Sonuçları:')
                    for l in diff:
                        print('  ✖', l)
            except FileNotFoundError:
                print('[!] scan_log.txt bulunamadı.')

        elif choice == '20':
            # Threat intelligence
            if not threat_intel:
                print('[!] threat_intel.json bulunamadı.')
            else:
                target = input('Hedef IP/domain girin: ').strip()
                out = subprocess.check_output(f"nmap -sS {target}", shell=True, text=True)
                print('\n[!] Tehdit İstihbaratı Sonuçları:')
                for ln in out.splitlines():
                    if '/tcp' in ln and 'open' in ln:
                        port = ln.split('/')[0]
                        tip  = threat_intel.get(port, 'Bilinmeyen TTP')
                        print(f"[{port}] → {tip}")

        else:
            print('[!] Geçersiz seçim, tekrar deneyin.\n')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n[!] Çıkış yapılıyor…')
        sys.exit(0)
