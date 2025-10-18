class Engineer:
    def __init__(self, name):
        self.name = name

    def code(self):
        print(self.name,"writes clean code every day.")


class Writer:
    def write(self):
        print(self.name,"writes tech blogs and tutorials.")


class TechBlogger(Engineer,Writer):
    def __init__(self, name, ):
        Engineer.__init__(self, name)

    def introduce(self):
        print(self.name,"i am engineer and a tech writer")

blogger = TechBlogger("John")
blogger.introduce()
blogger.code()
blogger.write()

