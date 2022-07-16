def choose_level():
    '''This function return the level of difficulty that the user has chosen for the game'''
    print "Please select a game difficalty by typing in!" 
    level = raw_input("Possible choice include easy, medium, and hard. ")
    print 
    return level



easy_paragraph = """A common first thing to do in a language is display 'Hello ___1___!',
in ___2___ this is particularly easy: all you have to do is type in: ___3___ "Hello  ___1___!"
of course, that isn’t a very useful thing to do. However, it is an example of how
to output to the user using the ___3___ command. and produce a program which does something.
so it is useful in that capacity. it may seem a bit odd to do something in a Turing complete language
that can be done even more easily with an ___4___ file in a browser. but it is
a step in learning ___2___ syntax. and that’s really its purpose."""

medium_paragraph = """A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions."""

hard_paragraph = """___1___es provide a means of bundling ___2___ and functionality together.
Creating a new ___1___ creates a new type of ___3___, allowing new ___4___s of that type to be made. Each ___1___ ___4___ can
have ___5___ attached to it for maintaining its state. ___1___ ___4___ can also have ___6___ (defined by its ___1___)for modifying its state.
Compared with other programming languages, Python’s ___1___ mechanism adds ___1___es with a minimum of new syntax and semantics.
It is a mixture of the ___1___ mechanisms found in C++ and Modula-3. Python ___1___es provide all the standard
features of ___3___ Oriented Programming: the ___1___ inheritance mechanism allows multiple base ___1___es, a derived ___1___
can override any ___6___s of its base ___1___ or ___1___es, and a ___6___ can call the ___6___ of a base ___1___ with the same name.
___3___s can contain arbitrary amounts and kinds of ___2___. As is true for modules,
___1___es partake of the dynamic nature of Python: they are created at runtime, and can be modified further after creation."""

def ask_to_fill(blanks, required, replaced):
    '''
    This function get inputs parameters blanks: the blanks to be filled,
    required: the required words that will replace the blanks, replaced
    is the test_paragraph after filling the blanks in it in order.
    It print correct or game over based on the user answer
    
    '''
    for i in range(0, len(blanks)):
        trial = 1
        while trial <= 5:
            print replaced
            substitution = raw_input("what should be substituted in for" + blanks[i] + "?")
            if substitution != required[i]:
                if trial == 5:
                    print "Game Over!!!"
                    return None
                else:
                    print ("That is not the correct answer! Let us try again: you have " + str(5-trial) + " try(s) left!\n")
                trial += 1
            else:
                print "correct!, fantastic you have got it\n"
                trial = 7
        replaced = replaced.replace(blanks[i], substitution)

def easy_level():
    '''
    This function will be called when the level chosen of the game is the easy
    it will ask the user to specify  words that will appropriately fill blanks in order
    and gives the user 5 trial for to fill each blanks 
    '''
    print "You have chosen easy!\n"
    
    blanks = ["___1___", "___2___", "___3___", "___4___"]
    required = ["World", "python", "print", "html"]
    replaced = easy_paragraph
    
    print "You will get only 5 guesses per problem\n"
    print "The current paragraph reads as such: "
    ask_to_fill(blanks, required, replaced)
    
def medium_level():
    '''
    This function will be called when the level chosen of the game is the medium
    it will ask the user to specify  words that will appropriately fill blanks in order
    and gives the user 5 trial for to fill each blanks 
    '''
    print "You have chosen medium!\n"

    blanks = ["___1___", "___2___", "___3___", "___4___"]
    required = ["function", "parameters", "None", "list"]
    replaced = medium_paragraph
    
    print "You will get only 5 guesses per problem\n"
    print "The current paragraph reads as such: "
    ask_to_fill(blanks, required, replaced)

        
    
def hard_level():
    '''
    This function will be called when the level chosen of the game is the hard
    it will ask the user to specify  words that will appropriately fill blanks in order
    and gives the user 5 trial for to fill each blanks 
    '''
    print "You have chosen hard!\n"

    blanks = ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___"]
    required = ["class", "data", "object", "instance", "attributes", "method"]
    replaced = hard_paragraph
    
    print "You will get only 5 guesses per problem\n"
    print "The current paragraph reads as such: "
    ask_to_fill(blanks, required, replaced)

def fill_in_blanks():
    '''
    This function call the choose_level function and specify which function
    called according to the user choice. it will call the easy_level function
    when the user chooses easy level and will call the medium_level function when
    the user chooses medium level and will call the hard_level function when the user
    chooses hard level and when the user doesn’t choose any one from the three level
    it will ask him replay the game again by calling itself
    
    '''
    
    level = choose_level()
    if level == "easy":
        return easy_level()
        
    elif level == "medium":
        return medium_level()
        
    elif level == "hard":
        return hard_level()
    
    else:
        print "Your choice is not present\n"
        return fill_in_blanks()
    
fill_in_blanks()
        
        

