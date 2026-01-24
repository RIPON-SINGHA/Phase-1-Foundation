# Here i am learning about how to install and use third party libraries in python and in a local source code
# Thrid party libraries are those which dos not come with the python itself, we have ti install it first then import it
# in this case i am learning a third party library called "cowsay" by downloading it using pip install and then importing it in to local source code
# this is a fun library with so small usage to it. but it's fun to use and know how third party libraries work

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
    cowsay.trex("I AM TREX, " + sys.argv[1])
    cowsay.tux("Mi gusto!")
    my_fish = r'''
    \
     \  
            /`·.¸
        /¸...¸`:·
    ¸.·´  ¸   `·.¸.·´)
    : © ):´;      ¸  {
    `·.¸ `·  ¸.·´\`·¸)
        `\\´´\¸.·´
    '''
    cowsay.draw("Hello i am under the water.....", my_fish)
    cowsay.daemon("Hand's  UP")
    cowsay.meow("MEOW MEOW, Nigga!")
    cowsay.octopus(".........")
    cowsay.kitty("meowwwww")
    cowsay.stegosaurus("grahhhhhhh")