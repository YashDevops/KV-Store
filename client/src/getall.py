import os
import argparse
import requests



url="http://localhost:8080/alllist"
def getall():
    result=requests.get(url)


def main():
    usagemsg="usage: getall [-h] requires key | ex getall"
    my_parser = argparse.ArgumentParser(description='A Simple KV (key-value) store web service with a subscription feature. As a user, I should be able to perform set(key, val) and get(key)  operations over HTTP and also subscribe to changes happening to any of the keys.',usage=usagemsg)
    my_parser.add_argument('getall', nargs="*",type=str)
    args = my_parser.parse_args()
    getall()




if __name__ == "__main__":
    main()
