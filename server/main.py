from multiprocessing import Pool, TimeoutError
from threading import Thread
from steam import SteamClient
from csgo import CSGOClient
import sys

def bReport(bot, target):
    global running
    running = True
    def ripclient(c):
        while 1:
            global running
            if not running:
                c.stop()
                return

    user = bot[0]
    pasw = bot[1]
    client = SteamClient()
    cs = CSGOClient(client)

    print("ok")
    thread = Thread(target = ripclient, args = (client, ) )
    thread.start()

    @client.on('logged_on')
    def start_csgo():
        cs.launch()

    @cs.on('ready')
    def gc_ready():
        global id
        id = str(cs.account_id)
        cs.send(csgo.enums.ECsgoGCMsg.EMsgGCCStrike15_v2_ClientReportPlayer, {
            'account_id': target,
            'match_id': 0,
            'rpt_aimbot': 1,
            'rpt_wallhack': 1,
            'rpt_otherhack': 1,
            'rpt_teamharm': 1,
            'rpt_textabuse': 1,
            'rpt_voiceabuse': 1
         })

    client.login(user, pasw)
    client.run_forever()

def bCommend(bot, target):
    user = bot[0]
    pasw = bot[1]
    client = SteamClient()
    cs = CSGOClient(client)

    @client.on('logged_on')
    def start_csgo():
        cs.launch()

    @cs.on('ready')
    def gc_ready():
        cs.send(csgo.enums.ECsgoGCMsg.EMsgGCCStrike15_v2_ClientCommendPlayer, {
            'account_id': target,
            'match_id': 0,
            'cmd_friendly': 1,
            'cmd_teaching': 1,
            'cmd_leader': 1
         })

    client.login(user, pasw)
    client.run_forever()

def main():
    # BOTS
    bots = []
    with open("bots.txt", "r") as rBots:
        for bot in rBots.read().splitlines():
            bots.append(tuple(bot.split(":")))
    # STOB
    # TARGET
    target = sys.argv[1]
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