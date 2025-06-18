*Crapibara*

**Intro**


crapibara, a stupendously slow, archaic, useless, language written for fun in python without any caffeine
is a bad choice for a senior, junior, student programmer, if you want to use it _suffer_ if you wanna edit
(or make along me _suffer_ also but most importantly it's a crap as the name suggests)

**how to use**

Download the main.py and run it there you can type:
>crapibara (Filename.cb)

and it will run the file

**syntax**

 1. once()
The once() statement is the start of your whole program it is stating that your program is gonna run all the script inside the **once()** literally **once** you should always remember that it should be ended with a end statement
_example script:_
>once() {

>    printlnv("Bye bye world!")

>    end

>}

 2. repeat()
One of the unique intersting features of our language **repeat()** is a simliar form to the **once()** statement however, it runs the script inside it's scope the _amount of time given_ in the parenthesis, the value inside the () should be a **number** without '  ""  ' inside it. Lastly you should also end this with a end statement
_example script:_
>once() {

>    printv("Script started!")

>    repeat(10) {

>        printlnv("This runs for 10 times!")

>        end

>    }

>    end

>}

3. end
The **end** statement is as simple as it gets, end is to be used in all end parts of the scope whether it's a i**if()** or a **repeat()** or a **once()**, it lets the enterpreuter know where is the end of the code.
_example script_:
>once() {

>    printv("Script started!")

>    end

>    ///

>   script ended

>   ///

>}

4. ///
The **///** is a multiline comment statement, it starts with a **///** and ends with a **///**, whatever you write there the enterpreuter won't care

_example script:_
>once() {

>   ///

>   printv("Nothing happens here!")

>   ///

>   end

>}

5. printv and printlnv
The **prints** are each there for print a value and a new line with it or just to continue the line, the printv can be used for various things, mainly for strinf formatting or user input. These statements can also print math statements between plain numbers or variabels and numbers.

_example script:_
>once() {

>    printv("Script started!")

>    printlnv("New line!")

>    end

>}

6. variables
Like in math variables can contain values you want to store away for use, you can declare a variable name and put value in it in a form of:
> "name" = "value"
here the value if putten "" around the given value is registered as a string, meanwhile without it its either a number or a numeric expression.

_example script:_
>once() {

>    number = 5

>    printv("I made a variable!")

>

>    repeat(5) {

>       number = number + 1

>       printv("I incremented the number by one!")

>       end

>   }

>    end

>}