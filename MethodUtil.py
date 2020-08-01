class MethodUtil:
    @staticmethod
    def method_get():
        """
        description:
            returns a Get value as string
        \nreturn value:
            "GET" as string
        """
        return "GET"

    @staticmethod
    def method_post():
        """
        description:
            returns a Post value as string
        \nreturn value:
            "POST" as string
        """
        return "POST"

    @staticmethod
    def list_ALL():
        """
        description:\n
            returns a list with GET and POST strings
        \nreturn value:\n
            "['GET','POST']"
        """
        methodList = [
            MethodUtil.method_get(),
            MethodUtil.method_post(),
        ]
        return methodList

    @staticmethod
    def list_GETOnly():
        """
        description:\n
            returns a list with GET string
        \nreturn value:\n
            ["GET"]
        """
        methodList = [MethodUtil.method_get()]
        return methodList

    @staticmethod
    def list_POSTOnly():
        """
        description:\n
            returns a list with POST string
        \nreturn value:\n
            "['POST']"
        """
        methodList = [MethodUtil.method_post()]
        return methodList
