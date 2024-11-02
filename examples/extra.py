from .. import extra as et

Example = et.Namespace(
    a=1,
    b=2,
    c=3
)

constgroup = et.ConstGroup()
constgroup.NAME = "ConstGroup in extra.py"
constgroup.VERSION = "1.0"

print(Example["a"]+Example["b"]+Example["c"])
