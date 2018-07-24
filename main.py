import core.restapi

data = core.restapi.Api(100)

if __name__ == "__main__":
    data.input = 100
    data.sum(20)
    print(data.output)
