class Players:
    batsmen = {"Rohit Sharma" :{"Age":36,"Runs":4231,"Base-Price":5000000},"Virat Kohli":{"Age":36,"Runs":25000,"Base-Price":6000000},"Yuvraj Singh":{"Age":42,"Runs":8701,"Base-Price":4500000}}
    ballers = {"Yuzi Chahal" :{"Age":34,"Wickets":205,"Base-Price":2500000},"J Bhumbra":{"Age":30,"Wickets":149,"Base-Price":1500000},"R Ashwin":{"Age":38,"Wickets":536,"Base-Price":4000000}}
    all_rounders = {"R Jadeja" :{"Age":35,"Wickets":300,"Runs":3122,"Base-Price":4500000},"H Pandya":{"Age":30,"Wickets":1560,"Runs":73,"Base-Price":3000000},"S Raina":{"Age":38,"Wickets":36,"Runs":5615,"Base-Price":3200000}}


    def __init__(self,team_name):
        self.team_name = team_name
        self.team = []
        self.team_price = []

    def batsmen_details(self):
        for name in Players.batsmen:
            print("-"*72)
            print(f"| {name} : {Players.batsmen[name]}|")
        print("-"*72)

    def baller_details(self):
        for name in Players.ballers:
            print("-"*72)
            print(f"| {name} : {Players.ballers[name]}|")
        print("-"*72)

    def all_rounder_details(self):
        for name in Players.all_rounders:
            print("-"*86)
            print(f"| {name} : {Players.all_rounders[name]}|")
        print("-"*86)

    def Team_details(self):
        print("-"*72)
        print(f"""
              Team name      :  {self.team_name}
              Player in team :  {self.team}
              Total spent    :  ₹ {sum(self.team_price)}

               """)
        print("-"*72)
        

class Auction(Players):
    def __init__(self,team_name):
        super().__init__(team_name)

    def buy_batsmen(self,name,price):
        if(name in Players.batsmen):
            if (price>=Players.batsmen[name]["Base-Price"]):
                if(len(self.team)<3):
                    self.team.append(name)
                    self.team_price.append(price)
                    Players.batsmen.pop(name)
                    print("_"*72)
                    print(f"You Brought {name} at ₹{price}")
                    print("-"*72)
                else:
                    print("-"*72)
                    print("Team already full !!!")
                    print("-"*72)
            else :
                print("-"*72)
                print("Price less than Base-Price")
                print("-"*72)
        else:
            print("-"*72)
            print("Player Already sold !!!")
            print("-"*72)

    def buy_baller(self,name,price):
        if(name in Players.ballers):
            if (price>=Players.ballers[name]["Base-Price"]):
                if(len(self.team)<3):
                    self.team.append(name)
                    self.team_price.append(price)
                    Players.ballers.pop(name)
                    print("-"*72)
                    print(f"You Brought {name} at ₹{price}")
                    print("-"*72)
                else:
                    print("-"*72)
                    print("Team Already Full !!!")
                    print("-"*72)
            else :
                print("-"*72)
                print("Price less than Base-Price")
                print("-"*72)
        else:
            print("-"*72)
            print("Player Already sold !!!")
            print("-"*72)

    def buy_all_rounder(self,name,price):
        if(name in Players.all_rounders):
            if (price>=Players.all_rounders[name]["Base-Price"]):
                if(len(self.team)<3):
                    self.team.append(name)
                    self.team_price.append(price)
                    Players.all_rounders.pop(name)
                    print("-"*72)
                    print(f"You Brought {name} at ₹{price}")
                    print("-"*72)
                else:
                    print("-"*72)
                    print("Team Already Full !!!")
                    print("-"*72)
            else :
                print("-"*72)
                print("Price less than Base-Price")
                print("-"*72)
        else:
            print("-"*72)
            print("Player Already sold !!!")
            print("-"*72)

    



a1 = Auction("Mumbai-Indians")
a1.batsmen_details()
a1.buy_batsmen("Rohit Sharma",5000000)
a1.baller_details()
a1.buy_baller("J Bhumbra",3000000)
a1.all_rounder_details()
a1.buy_all_rounder("H Pandya",3100000)
a1.Team_details()
a1.buy_batsmen("Yuvraj Singh",45000000)

a2 = Auction("CSK")
a2.buy_batsmen("Yuvraj Singh",45000000)
a2.buy_baller("R Ashwin",45000000)
a2.buy_all_rounder("R Jadeja",50000000)
a2.Team_details()

a3 = Auction("Rajastan Royals")
a3.batsmen_details()
a3.baller_details()
a3.all_rounder_details()
a3.buy_batsmen("Virat Kohli",6000000)
a3.buy_baller("Yuzi Chahal",25000000)
a3.buy_all_rounder("S Raina",35000000)
a3.Team_details()


