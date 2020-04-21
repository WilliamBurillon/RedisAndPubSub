import redis
import time


#monitor server
r = redis.Redis(host='localhost', port=6379, db=3)
#Provider part
alice_r=redis.Redis(host='localhost', port=6379, db=3)

# Customer part
bob_r=redis.Redis(host='localhost', port=6379, db=3)
bob_p= bob_r.pubsub()
bob_p.subscribe("classical_music")
bob_p.subscribe('metalMusic')


def monitoring(r):
    with r.monitor() as m :
        for command in m.listen():
            print(command)

if __name__ == "__main__":
    # monitoring(r)
    alice_r.publish('metal',"test")
    alice_r.publish('metalMusic', "ironamsqddqdiden")
    alice_r.publish('classical_music','Alice music')
    alice_r.publish('classical_music', 'Alice 2nd music')
    alice_r.publish('metalMusic',"ironamiden")
    #
    # #--------------
    # print(bob_p.get_message())
    # music1 = bob_p.get_message()['data']
    # print(music1)
    #
    res = bob_p.get_message()
    while res != None:
        res = bob_p.get_message()
        try:
            print(res)
        except:
            pass


    # print(bob_p.get_message())
    # print(bob_p.get_message())
    # print(bob_p.get_message())
    # print(bob_p.get_message())

    # music2 = bob_p.get_message()
    # print(music2)
    #