# 부모 클래스에서 추상 메소드로 선언한 메소드에 대해서는 반드시 상속받은 자식 클래스에서 해당 기능을구현 해야 함

from abc import *

class NetworkAdaptor(metaclass=ABCMeta) :
    @abstractmethod
    def connect(self) :
        pass

class FiveG(NetworkAdaptor) :
    def __init__(self, company) :
        self.company = company
    def connect(self):
        print(f"{self.company} 5G로 연결.")

class WiFi(NetworkAdaptor) :
    def __init__(self, company) :
        self.company = company
    def connect(self):
        print(f"{self.company} Wi-Fi로 연결.")

class LTE(NetworkAdaptor) :
    def __init__(self, company) :
        self.company = company
    def connect(self):
        print(f"{self.company} LTE로 연결.")

net = input("연결할 네트워크를 선택하세요 [1] 5G  [2] Wi-Fi  [3] LTE : ")
if net == "1" :
    adapter = FiveG("KT MegaPass")
    adapter.connect()
elif net == "2" :
    adapter = WiFi("SK Telecom")
    adapter.connect()
else : 
    adapter = LTE("LG U+")
    adapter.connect()
