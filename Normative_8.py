import logging
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

def decorator(func):
    def wrapper(*args):
        try:
            logging.info(f"Funksiya {func.__name__} ishga tushdi argumentlar: {args}")
            result=func(*args)
            logging.info(f"Funfsiya {func.__name__} muvofaqiyatli yakunlandi answer: {result}")
            return result
        except Exception as e:
            logging.error(f"Funksiya {func.__name__} da xatolik {e}")
            raise f"Xatolik: {e}"

    return wrapper


@decorator
def multiplier(b,c):
    return b * c


@decorator
def remainder(d,f):
    return d / f


@decorator
def persent(a,c):
    return a * c // 100


#
# print(persent(100, 10))
# print(remainder(10, 2))
# print(multiplier(5, 5))
#


def generate1(n):
    for i in range(1,n + 1):
        yield i

n=4
print(list(generate1(n)))

