#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A tiny “what‑do‑I‑do‑menu‑app”.

Options:
  1 – start a simple Python HTTP server
  2 – start a TCP echo‑server
  3 – act as a client and listen/receive data from a remote host
  4 – exit
"""

import sys
import threading
import socket
import http.server
import socketserver
from functools import partial

# ------------------------------------------------------------------
# 1️⃣  Helper – pretty menu
# ------------------------------------------------------------------
def show_menu():
    print("\n==== MENU ====")
    print("1 – Start a Python HTTP server (default port 8000)")
    print("2 – Start a TCP echo‑server (default port 9000)")
    print("3 – Connect to a remote host & listen for data")
    print("4 – Exit")
    print("================\n")

# ------------------------------------------------------------------
# 2️⃣  Server 1 – simple HTTP server
# ------------------------------------------------------------------
def http_server(port=8000):
    handler = http.server.SimpleHTTPRequestHandler
    httpd   = socketserver.TCPServer(("0.0.0.0", port), handler)
    print(f"\n[*] HTTP server listening on http://0.0.0.0:{port}/")
    print("[*] Press Ctrl‑C to stop.\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] HTTP server stopped.")
    finally:
        httpd.server_close()

# ------------------------------------------------------------------
# 3️⃣  Server 2 – raw TCP echo‑server
# ------------------------------------------------------------------
def echo_server(port=9000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.bind(("0.0.0.0", port))
        srv.listen()
        print(f"\n[*] Echo‑server listening on 0.0.0.0:{port}")
        print("[*] Press Ctrl‑C to stop.\n")

        try:
            while True:
                client, addr = srv.accept()
                print(f"[+] New connection from {addr}")
                threading.Thread(target=handle_echo_client, args=(client, addr), daemon=True).start()
        except KeyboardInterrupt:
            print("\n[*] Echo‑server stopped.")

def handle_echo_client(conn, addr):
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"[{addr}] {data!r}")
            conn.sendall(data)   # echo back
    print(f"[-] Connection closed by {addr}")

# ------------------------------------------------------------------
# 4️⃣  Client – connect to a remote host & listen
# ------------------------------------------------------------------
def client_listen(host, port):
    print(f"\n[*] Connecting to {host}:{port} ...")
    try:
        with socket.create_connection((host, port)) as sock:
            print("[*] Connected. Receiving data… (Ctrl‑C to quit)")
            while True:
                data = sock.recv(4096)
                if not data:
                    break
                print(data.decode(errors="replace"), end="")
    except Exception as exc:
        print(f"\n[!] Error: {exc}")

# ------------------------------------------------------------------
# 5️⃣  Main loop
# ------------------------------------------------------------------
def main():
    while True:
        show_menu()
        choice = input("Choose an option (1‑4): ").strip()
        if choice == "1":
            port = input("Port [8000]: ").strip()
            try:
                port = int(port) if port else 8000
            except ValueError:
                port = 8000
            http_server(port)
        elif choice == "2":
            port = input("Port [9000]: ").strip()
            try:
                port = int(port) if port else 9000
            except ValueError:
                port = 9000
            echo_server(port)
        elif choice == "3":
            host = input("Remote host (e.g. 127.0.0.1): ").strip()
            port = input("Port [9000]: ").strip()
            try:
                port = int(port) if port else 9000
            except ValueError:
                port = 9000
            client_listen(host, port)
        elif choice == "4":
            print("Good‑bye!")
            break
        else:
            print("[!] Invalid choice – pick 1 to 4.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nInterrupted by user.\n")
