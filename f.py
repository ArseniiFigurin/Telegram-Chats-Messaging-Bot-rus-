from telethon.sync import TelegramClient, errors
from time import sleep
from telethon.errors.rpcerrorlist import MessageTooLongError, PeerIdInvalidError
import dbm
import python_socks
import socks

def dbm_base():
    file = dbm.open('api11.dbm', 'c')
    try:
        file['api_id11']
    except:
        file['api_id11'] = input('Enter api_id:')
        file['api_hash11'] = input('Enter api_hash:')
    file.close()
    return dbm.open('api11.dbm', 'r')

with open('proxy.txt', encoding='utf-8') as f:
    proxys = f.readlines()
    
file = dbm_base()
api_id = int(file['api_id11'].decode())
api_hash = file['api_hash11'].decode()
client = TelegramClient('client11', api_id, api_hash, proxy = {
    'proxy_type': 'http',
    'addr': f'{proxys[0].split(":")[0]}',
    'port': int(proxys[0].split(":")[1]),
    'username': f'{proxys[0].split(":")[2]}',
    'password': f'{proxys[0].split(":")[3]}'
})

delay = int(input('Znachenie taimera:'))

def dialog_sort(dialog):
    # Sortiruet dialogi po neprochitannie
    return dialog.unread_count


def spammer(client):
    k = 0
    j = 0

    def create_groups_list(groups=[]):
        # Sozdaet spisok grupp, gde neprochitannih soobshenii menshe 1
        for dialog in client.iter_dialogs():
        # Nachinaet begat po dialogam klienta
            if dialog.is_group:
            # True, esli eto gruppa
                if dialog.unread_count >= 1:
                # Skolko msg ne prochitano v danniy moment. Eta peremennaia ne obnovlaetsia pri postuplenii novih soobheniy
                    groups.append(dialog)
        return groups

    with client:
        for m in client.iter_messages('me', 1):
            # History of my chat
            msg = m
        while True:
            groups = create_groups_list()
            groups.sort(key=dialog_sort, reverse=True)
            for g in groups[:10000]:
                try:
                    client.forward_messages(g, msg, 'me')
                    # Otpravliaet msg v gruppu g i otpravil iya
                    k = k + 1
                except errors.ForbiddenError as o:
                    # Obrabotka togo, chto nelza napisat
                    client.delete_dialog(g)
                    if g.entity.username != None:
                        print(f'Error: {o.message} Account pokinul @{g.entity.username}')
                    else:
                        print(f'Error: {o.message} Account pokinul {g.name}')
                except errors.FloodError as e:
                    if e.seconds > 180:
                        continue
                    else:
                        print(f'Error: {e.message} Trebuetsia ozhidanie {e.seconds} secund')
                        sleep(e.seconds)
                except PeerIdInvalidError:
                    # Na obrabotku bota
                    client.delete_dialog(g)
                except MessageTooLongError:
                    print(f'Message was too long ==> {g.name}')
                except errors.BadRequestError as i:
                    print(f'Error: {i.message}')
                except errors.RPCError as a:
                    print(f'Error: {a.message}')
            j = k + j
            k = 0
            print('Otpavleno soobhenii: ', j)
            sleep(delay)
            groups.clear()


if __name__ == '__main__':
    spammer(client)
