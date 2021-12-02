
def test():
    return_value = {"message": 1, "url": "ssss"}
    if not (type(return_value) == type(None) or (type(return_value) == dict and all([key in ["file", "url", "filename", "message"] for key in return_value.keys()]))):
        raise Exception("Wrong function return type")
    else:
        print("hola")


if __name__ == "__main__":
    test()
