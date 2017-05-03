from datetime import datetime, timedelta

logger = []

timestamp = datetime.now()
print "-" * 40 + "\nenter 'q' to quit and save" + "\n"
while True:

    entry = raw_input("> ")
    timestamp = datetime.now().replace(microsecond = 0)
    just_time = timestamp.strftime("%H:%M:%S")
    if entry == 'q':
        break

    if len(logger) == 0:
        print str(just_time) + "\n"
        last_print_time = timestamp
    elif (timestamp - logger[-1][0]) > timedelta(0, 60 * 5, 0):
        print str(just_time) + "\n"
        last_print_time = timestamp
    elif (timestamp - last_print_time) > timedelta(0, 60 * 10, 0):
        print str(just_time) + "\n"

    logger.append((timestamp, entry))

logger_name = timestamp.strftime("%Y-%m-%d") + ".log"


with open("C:\\Users\\nick\\Documents\\daytrader\\logger\\logs\\" + logger_name, "a+") as f:
    for e in logger:
        line = '\t'.join([e[0].strftime("%H:%M:%S"), e[1]])
        f.write(line + '\n')
