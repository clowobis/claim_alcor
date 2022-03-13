import eospy.cleos
import eospy.keys

def r_nodes():
    node_list = open('nodes.txt').read().splitlines()
    cnode = random.choice(node_list)
    return (cnode)

ce = eospy.cleos.Cleos(url=r_nodes())
anchkey = eospy.keys.EOSKey("key")

def claim():
    payload = [
            {
                'args': {
                    "claimer": "#",
                    "drop_id": "#",
                    "claim_amount": '1',
                    "intended_delphi_median": "0",
                    "referrer": "",
                    "country": "",
                },
                "account": "neftyblocksd",
                "name": "claimdrop",
                "authorization": [{
                    "actor": "#",
                    "permission": "active",
                }],
            }
        ]
    data = ce.abi_json_to_bin(payload[0]['account'], payload[0]['name'], payload[0]['args'])
    payload[0]['data'] = data['binargs']
    payload[0].pop('args')
    trx = {"actions": [payload[0]]}
    key = anchkey
    resp = ce.push_transaction(trx, key, broadcast=True)
    print('Success claim...')
    time.sleep(2)

while True:
    claim()
