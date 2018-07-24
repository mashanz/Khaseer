import core.restapi

data = core.restapi.Api("http://119.235.255.245/")


def getExample():
    params = dict(
        prodCode='777080',
        pin='e10adc3949ba59abbe56e057f20f883e',
        latitude='-6.8725783',
        phNumber='6281220564514',
        billNumber='6281220564514',
        longitude='107.6179708'
    )
    data.get("derapmw/getDenomFeeComm.php", params)
    print(data.body)


def postExample():
    payloads = dict(
        procCode='38',
        prodCode='070002',
        phNumber='6281324195469',
        billNumber='14022394192',
        pin='1',
        latitude='-6.8725042',
        longitude='107.6180189',
        amount='50000',
        jml_bulan='0',
        bit61='0'
    )
    data.post("derapmw/pembayaran.php", payloads)
    print(data.body)


if __name__ == "__main__":
    getExample()
    postExample()
