import extra as et

FormatCode = et.Namespace()
FormatCode.NORMAL=0
FormatCode.HIGHLIGHT=1
FormatCode.ITALIC=3
FormatCode.UNDERLINE=4
FormatCode.SHINING=5
FormatCode.REVERSE=7
FormatCode.DISABLED=8

FontCode = et.Namespace()
FontCode.BLACK=30
FontCode.RED=31
FontCode.GREEN=32
FontCode.YELLOW=33
FontCode.BLUE=34
FontCode.PURPLE=35
FontCode.CYAN=36
FontCode.GREY=37
FontCode.WHITE=38

BackgroundCode = et.Namespace()
BackgroundCode.BLACK=40
BackgroundCode.RED=41
BackgroundCode.GREEN=42
BackgroundCode.YELLOW=43
BackgroundCode.BLUE=44
BackgroundCode.PURPLE=45
BackgroundCode.CYAN=46
BackgroundCode.GREY=47
BackgroundCode.WHITE=48

def output(text:str, format:int=0, font:int=0, background:int=0):
    return f"\\033[{format};{font};{background}m{text}\033[0m"

def outprint(text:str, format:int=0, font:int=0, background:int=0):
    try:
        print(f"\\033[{format};{font};{background}m{text}\033[0m")
    except Exception as e:
        return e

if __name__ == "__main__":
    print("This is a module of FedpyLib.You should read 'example/colorstring.py' to understand the usage.")
    print(FormatCode)
    print(FontCode)
    print(BackgroundCode)