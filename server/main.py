#!/usr/bin/env python3.6

"""
    CS:GO Python Report/Commend Bot
    Author: Capuno
    License: GPL v3

    Usage: script.py [report/commend] [SteamID64]
    Or automatically with the website and the php working from the main GH repo Capuno/BarrongedBot
"""

from multiprocessing import Pool, TimeoutError
from threading import Thread
from steam import SteamClient
from csgo import CSGOClient
import sys, time

def usage():
    print("BarrongedBot by Capuno\n   Usage: {} [report/commend] [SteamID64]\n   Must have a file named bots.txt with valid accounts\n   and with format user:password inside working directory.".format(sys.argv[0]))
    sys.exit()

class bReport(object):
    def __init__(self, bot, target):
        self.returnRequest = "Error"
        self.user = bot[0]
        self.pasw = bot[1]
        self.client = SteamClient()
        self.cs = CSGOClient(self.client)
        self.running = True
        self.timer = 0
    def ripclient(self):
        while 1:
            if not self.running or self.timer > 15:
                self.client.stop()
                break
            time.sleep(1)
            self.timer += 1
    def main(self):
        @self.client.on('logged_on')
        def start_csgo():
            self.cs.launch()
        @self.cs.on('ready')
        def gc_ready():
            self.cs.send(csgo.enums.ECsgoGCMsg.EMsgGCCStrike15_v2_ClientReportPlayer, {
                'account_id': target,
                'match_id': 0,
                'rpt_aimbot': 1,
                'rpt_wallhack': 1,
                'rpt_otherhack': 1,
                'rpt_teamharm': 1,
                'rpt_textabuse': 1,
                'rpt_voiceabuse': 1
             })
            self.returnRequest, = cs.wait_event(ECsgoGCMsg.EMsgGCCStrike15_v2_ClientReportResponse, timeout=10)
        thread = Thread(target = self.ripclient)
        thread.start()
        self.client.login(user, pasw)
        self.client.run_forever()
    def run(self):
        thread = Thread(target = self.main)
        thread.start()

class bCommend(object):
    def __init__(self, bot, target):
        self.returnRequest = "Error"
        self.user = bot[0]
        self.pasw = bot[1]
        self.client = SteamClient()
        self.cs = CSGOClient(self.client)
        self.running = True
        self.timer = 0
    def ripclient(self):
        while 1:
            if not self.running or self.timer > 15:
                self.client.stop()
                break
            time.sleep(1)
            self.timer += 1
    def main(self):
        @self.client.on('logged_on')
        def start_csgo():
            self.cs.launch()
        @self.cs.on('ready')
        def gc_ready():
            self.cs.send(csgo.enums.ECsgoGCMsg.EMsgGCCStrike15_v2_ClientCommendPlayer, {
            'account_id': target,
            'match_id': 0,
            'cmd_friendly': 1,
            'cmd_teaching': 1,
            'cmd_leader': 1
         })
        thread = Thread(target = self.ripclient)
        thread.start()
        self.client.login(user, pasw)
        self.client.run_forever()

def main():
    # SYNTAX
    if len(sys.argv) == 3:
        if sys.argv[1] not in ["commend", "report"]:
            usage()
    else:
        usage()
    # XATNYS
    # BOTS
    bots = []
    try:
        with open("bots.txt", "r") as rBots:
            for bot in rBots.read().splitlines():
                bots.append(tuple(bot.split(":")))
    except FileNotFoundError:
        usage()
    # STOB
    # TARGET
    method = sys.argv[1]
    target = sys.argv[2]
    # TEGRAT
    names = []
    pm = Pool(processes=len(bots))
    ps = []
    for bot in bots:
        ps.append(pm.apply_async( bReport, args = (bot, target) ))
        names.append(bot[0])
    for i, p in enumerate(ps):
        try:
            ok = p.get(timeout=10)
            print(" [>] {}: ".format(names[i]) + str(ok))
        except TimeoutError:
            print(" [>] Error: {} timed out.".format(names[i]))

if __name__ == '__main__':
    main()