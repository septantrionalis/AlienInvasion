class DupeCheck():

    def __init__(self):
        pass

    def run(self):
        print("Running...")
        filename = "areas.bbs"
        list = []
        with open(filename, 'r') as handle:
            lineCount = 1
            for line in handle:
                ids = line.split()
                if len(ids) > 0:
                    id = ids[0]
                    print("Processing " + id)
                    if id in list:
                        print("DUPLICATE FOUND: " + id)
                        exit()
                    list.append(id)
                else:
                    print("Invalid line found on line " + str(lineCount))
                lineCount += 1

        print("No Duplicates Found")

dupeCheck = DupeCheck()
dupeCheck.run()
