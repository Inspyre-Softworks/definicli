class ElementVisibleError(Exception):
    def __init__(self, element_name=None):
        """
        
        To be raised when the specified element is already visible but a call was made to make it visible again.

        Parameters:

            element_name (str): The name of the element in question. (Optional, though strongly encouraged!)

        """
        if element_name is None:
            en = 'Not Provided'
        else:
            en = element_name.upper()
        self.msg = "The specified element is already visible! Element: {}".format(en)
        self.message = self.msg
