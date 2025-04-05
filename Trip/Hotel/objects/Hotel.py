#https://www.agoda.com/pt-br/
#   search?
#   &checkIn=2025-03-17
#   &checkOut=2025-03-23
#   &los=6
#   &rooms=1
#   &adults=2
#   &children=0
#   &locale=en-gb
#   &ckuid=f67cf26b-f655-40b3-8524-dca691cf56b9
#   &prid=0
#   &currency=BRL
#   &languageId=1
#   &origin=BR
#   &stateCode=SP
#   &cid=1844104
#   &userId=f67cf26b-f655-40b3-8524-dca691cf56b9
#   &currencyId=7
#   &currencyCode=USD
#   &htmlLanguage=en-gb
#   &cttp=4
#   &isRealUser=False
#   &mode=production
#   &cdnDomain=agoda.net
#   &priceCur=BRL
#   &textToSearch=Pequim
#   &travellerType=1
#   &ds=Y8L4NgAzHw57SDYS&productType=-1
#   city=2002

class Hotel():

    def __init__(self, name, price, url, address, score,source) -> None:
        self.name = name
        self.price = price
        self.url = url
        self.address = address
        self.score = score
        self.source = source
    
    def __str__(self) -> str:
        return 'Name:{}\nPrice:{}\nURL:{}\nScore:{}'.format(
            self.name
            ,self.price
            ,self.url
            ,self.score
        )
    
    def export(self) -> str:
        return {
            'name': self.name,
            'price': self.price,
            'url': self.url,
            'address': self.address,
            'score': self.score
        }