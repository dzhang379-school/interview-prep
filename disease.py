def find(string, substring):
    if string.length < substring.length:
        return False
    elif string.length == substring.length:
        return string == substring
    else:
        for i in range(len(string) - len(substring)):
            found = True
            for j in range(len(substring)):
                if string[i + j] != substring[j]:
                    found = False
                    continue

            if found:
                return i


class Patient:

    def __init__(self, disease, date, reporter, severity, description = []):
        self.disease = disease
        self.date = date
        self.reporter = reporter
        self.severity = severity
        self.description = description
        self.isAllergy = (disease.find("allergy") >= 0)

    def addDescription(self, description):
        if description not in self.description:
            self.description.append(description)

    def getDescriptions(self):
        if self.isAllergy:
            print("This is an allergy.\n")

        print("Reporter: {}".format(self.reporter))
        print("Severity: {}".format(self.severity))
        print("Time Detected: {}".format(self.date))
        print("Description: \n")

        for i in self.description:
            print("{}".format(i))

        print("---------------------------------")

    def changeSeverity(self, severity):
        self.severity = severity

def main():

    patient1 = Patient("pneumonia", "10/12/2018", "Dr. Cook", "severe")
    patient1.addDescription("coughing")
    patient1.addDescription("stuffy nose");

    patient2 = Patient("peanut allergy", "1/2/2018", "Mother", "mild")
    patient2.changeSeverity("severe")

    patient1.getDescriptions()
    patient2.getDescriptions()

main()
