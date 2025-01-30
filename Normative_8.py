import logging
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def decorator(func):
    def wrapper(*args):
        try:
            logging.info(f'Funksiya {func.__name__} ishga tushdi argumentlar: - {args}')
            result=func(*args)
            logging.info(f'Funksiya {func.__name__} muvofaqiyatli yakulandi answer - {result}')

            return result

        except Exception as e:

            logging.error(f'Funksiya {func.__name__} da xatolik {e}')
            raise f'Xatolik {e}'
    return wrapper



@decorator
def persent(a):
    return a * 10 // 100



@decorator
def multiplier(b,c):
   return b * c


@decorator
def remainder(d,f):
    return d / f


print(persent(100))
print(multiplier(5, 5))
print(remainder(20, 4))
print(remainder(20, 4))

