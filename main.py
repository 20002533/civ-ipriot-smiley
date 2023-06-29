#William Hampton#
#Program created on 19/06/2023.#

""""Demonstrates the use of the Smiley class and its subclasses.
If you have access to a SenseHAT (either via a Raspberry Pi or a SenseHAT emulator), you can use the real SenseHAT class instead of the mock SenseHAT class.
That is, delete the sense_hat.py file that is included in this bundle."""

import time

from happy import Happy
#Importing Happy class from Happy file.#
if __name__ == '__main__':
    #Anything that runs outside the main file eg if you run another file, the code in it will be treated as main because of the name variable defined here/expressed as main.#
    # This is only needed if you have not deleted sense_hat.py
    # and only in some environments - uncomment only if you have errors
    # from multiprocessing import freeze_support
    # freeze_support()
    ############################################################

    # Create a happy smiley, which is a subclass of Smiley
    smiley = Happy()
#Smiley instance is being created by Happy class.#
    # This is a form of #polymorphism, as the Happy smiley class
    # does not have a method called .show(). This means that
    # the method .show() of the base class {Smiley} will be
    # used in stead. There is no need to specify the base
    # class, like in other, statically typed, languages.
    smiley.show()
#Instance of Smiley calls on show method.#
    # Just a short delay
    time.sleep(1)

    # Another form of polymorphism:
    # The method blink is implemented by the Happy class, but
    # is defined as an interface (i.e., an abstract base class
    # with an abstract method).
    smiley.blink()
