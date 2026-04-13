import re

def clean_and_unwrap_paragraph(text):
    # Step 1: Normalize whitespace and remove spaces before punctuation
    text = re.sub(r'\s+', ' ', text)                      # Replace multiple spaces with one
    text = re.sub(r'\s+([.,!?;:])', r'\1', text)          # Remove space before punctuation
    text = text.strip()

    # Step 2: Split into sentences on punctuation followed by space
    sentences = re.split(r'(?<=[.!?])\s+', text)

    # Step 3: Capitalize each sentence properly
    cleaned_sentences = [s.strip().capitalize() for s in sentences if s.strip()]

    # Step 4: Join into a single line paragraph
    paragraph = ' '.join(cleaned_sentences)

    return paragraph

# Example usage
paragraph = """
Jason: In the previous exercise,

you wrote a script that prompted the user

to provide a password for the account

that was being created.

In this lesson, you're going to learn a few different ways

to generate some random data,

including how to automate the process

of generating a random password.

This way you'll be able to improve your script

by requiring less input from the user.

And in my opinion, the more you can automate, the better.

I have a terminal opened up on my local system

and I'm going to move into the class folder.

We're going to continue working on the local user's system,

so I'll just change directory into there.

Now we'll start the virtual machine and log into it.

Now we can connect to it

and move into the vagrant folder into cd/vagrant.

Now I'm going to create a script called luser-demo05.sh.

Of course we always start out our scripts with shebang.

And then we're going to put a header to our file here,

just a short sentence or two about the goal for this script.

And so what this script does

is it generates a list of random passwords.

Now before we do any real coding,

let's look at the bash man page to see if it provides

any way for us to get some random data.

So let me save my changes here and we'll do man bash

and we'll just look for random.

Since random is in all capital letters

and by convention variables are in all capital letters,

I can probably assume that random

is a bash built-in variable, and it is.

And you can confirm that if you were to just go up

the man page here until the header

and you'll see that it is indeed

in the variable section of the man page.

But I'm gonna scroll back down here

and just read what this random variable is about.

It says each time this parameter is referenced,

a random integer between zero and 32,767 is generated.

So let's get back to the command line here by

pressing Q to exit out of the man page

and just echo dollar random and see what happens.

Echo $ RANDOM and there's a random number 4308.

Let's see what happens if we access it again

and we get different numbers each time

we echo the random variable to the screen here.

So that's a pretty simple way to get some random data.

Let's get back into our script here.

So the first password we'll generate

will just be a random number as a password.

So we'll set the PASSWORD variable equal to $ RANDOM

and then we'll just echo that to the screen.

Save my changes and exit.

Of course, this is the first time

I'm going to be executing this script,

so I'm going to set the permissions on it,

chmod 755 luser-demo05.sh,

and then go ahead and execute it.

So if we keep executing it,

you can see we just get a different random number.

Just because I'm lazy,

I'm going to do something here that's a bit of a shortcut.

I'm gonna do !v to execute the most recent command

that started with a v.

And this is called an event designator.

And I go through this in my "Command Line Kung Fu" book,

but it's a quick way to execute a previous command

that starts with a given string.

So instead of me having to retype out the

whole vim space luser-demo05.sh,

and I'm going to be executing this a lot, coming,

executing the script and then going back

and editing and so on and so forth,

I'm just going to use this shortcut.

So if I do !v or bang V and hit Enter,

we'll be back into editing our script.

So just using $ RANDOM might be good enough,

especially if the user is forced to

change their password on login.

And if you're concerned about security,

perhaps you would like a fairly long password.

So let's do something like use two

or three random numbers altogether.

So we'll reassign our password variable to RANDOM

and just do this three times here,

and we'll display that password to the screen.

Okay, I'm gonna execute ./luser-demo05

and I'm gonna use my shortcut here, exclamation mark dot.

When you perform this shortcut,

it actually displays what it executes and then executes it.

I'm just going to hit the up arrow since I'm already here.

So here you can see that we're getting some random data.

The first password is just one random number.

The second password that we're generating here

are three random numbers together,

and as you can see there are varying lengths and whatever.

So this also could be good enough,

but we can do something better.

If you think about it,

something that is always changing is time.

It's never the same time ever again.

It's now and then now was a second ago

and now is also a second ago and so on.

So that is some data that is always changing.

So let's use the current date and time

as the basis for a password to generate.

So let's go ahead and look at the date command

and some of its options.

So obviously the date prints

or sets the system date and time.

The synopsis here is date followed by optional option,

and the ellipses there

says that you can have multiple options.

And then also in brackets, which means it's optional,

is a format plus followed by some sort of format.

So let's check out the different formats

that are available to us

and I'll just do a forward search

with a /FORMAT and press Enter,

hit End to go to the next match,

End to go the next match and so on.

So here it says FORMAT controls the output

and each one of these looks like

they begin with a percent sign.

For example, %a is the abbreviated weekday name,

%A is the full weekday name, and so on and so forth.

I want to point out %s.

Keep going here.

And %s is seconds since 1970-01-01,

January 1st, 1970 at zero hours UTC.

This particular date is called the Epoch,

and some people actually call this Epoch time or Unix time.

This Unix time, and it's also called POSIX time, by the way,

or Epoch time is simply the number of seconds

that have elapsed since January 1st, 1970.

So I'll hit q here to exit out of the man page

and let's just see what that looks like.

We'll do date plus that says,

hey we're going to use a format.

We'll use %s and hit Enter.

And so that is the number of seconds

since January 1st, 1970.

And we do it again and again,

So 14 seconds, 15 seconds, 18, 19, 20,

whoops, 21, and so on.

So this number just continually increments

every single second.

So we could actually use this as a password.

Let's get back to editing our file here.

I'm gonna use my shortcut bang V.

So we'll set the PASSWORD equal to date.

And remember that the dollar sign opening parentheses

and then a command followed by the closing parentheses,

that takes the output of that command within the parentheses

and assigns it to the variable.

So the password variable is going to contain the value

of whatever that date command returns.

And then we'll just echo this to the screen.

Okay, I'm going to execute this script again.

And here we can see that it, you know,

increments by one number each time,

one second each time we run it,

or in this case a couple a seconds,

but because I've been talking for a couple of seconds.

In theory, this password could be guessed.

For example, the more you know

about the password generation technique,

the easier the passwords are to crack.

So if you know what day a password was generated on

and you know that there are only 86,400 seconds in a day,

that means there are only 86,400 possible passwords.

Now you can further infer some more information

and guess that the password was probably generated

during normal business hours,

so that leaves about an eight hour window,

now you're down to about 28, 29,000 possible passwords.

Now I'm getting a little bit off track here,

but you get the idea.

So let's find a way to make this even harder to guess.

Let's get back to the man page for date.

And I know the last command that I executed

that started with an m was man date,

so I can do !m and hit Enter.

So I want to point out this nanoseconds format.

When you use this format,

it prints the nanosecond that the date command was executed.

So there's about nine digits there,

so that leaves us a lot more data to guess.

So it'd be really hard to guess those nanoseconds

because each time you run the date command,

I mean it has to be the exact of the nanosecond,

and that provides us a lot more variation.

So if we actually combine that with the Epoch time,

then we can get a long number.

So let's do this.

Let's run the date command.

We'll say we're going to use a format.

We want the second since the Epoch,

and then we also want the nanoseconds

and we'll hit N here like this and press Enter.

So now when we execute this,

maybe the first portion of the password

that represents %s is only incrementing by one digit,

but the last few digits there pretty much look random

because they're based on the nanoseconds

of when the date command was executed.

So let's go ahead and use this as a possible password.

Assign the date command to the PASSWORD variable

and then echo the PASSWORD.

Okay, let's execute the script a couple of times

and so you can see that it looks fairly random,

so that's a better password

than the just the second since Epoch.

Let's take this one step further by using checksums

or cryptographic hash functions.

A checksum is a numeric value computed for a block of data

that is relatively unique.

Checksums were and are used to verify

the integrity of data such as files.

For example, if you download a file

and you wanna make sure that it's not corrupt in some way,

you find the published checksums for the file

and compare it to the file you downloaded.

Let's take CentOS for example.

They publish sha1sums and sha256sums

for their downloads.

By the way, I didn't include the CentOS ISO

that I'm about to use in the course download

because it's about 700 megabytes

at the time of this recording.

So if you wanna follow along with this specific section,

you're going to have to download the ISO separately

and then look at the checksums published by CentOS

at the time you download the ISO file.

Anyway, here are the contents of the sha1sum text file

published by CentOS.

So for each file that they publish,

they produce a sha1sum that corresponds to that file.

So the first file up there,

the CentOS-7 DVD-1611.iso corresponds to

the c018577 et cetera, sha1sum.

So we can use the sha1sum command on our side

to run the sha1 mathematical algorithm

against this file to return its checksum or sha1sum value.

So I've downloaded the Minimal ISO,

so I'm going to run sha1sum on the CentOS-7 Minimal ISO here

and hit Enter.

So more or less, this number represents all the data

in that single file.

If it matches what is published,

then you're virtually guaranteed

that the data is exactly the same.

So in this case, we have a known good copy of the CentOS ISO

because it's sha1sum matches the published sha1sum.

I'll highlight that here.

Here's the sha1sum of our local file,

and here is the published sha1sum provided by CentOS

that is supposed to correspond to that file.

And so as you can see,

it begins with 71 and ends with 4f

and ours begins with 71 and also ends with 4f,

so we have the same file.

They also publish sha256sum.

So let's use the sha256sum command against that ISO

and hit Enter.

Okay, it generated the sha256sum for that file

and we can compare it to what's published.

So let's look at the sha256sum file

that I downloaded from CentOS.

Okay, this checks out as well.

It should because the other sum checked out,

but we're just experimenting here.

So we have a sha256sum that begins with 27

and ends with 86a.

And sure enough, the Minimal ISO corresponds

begins with 27 and ends with 86a.

Let's change the file just ever so slightly

and see if the sums still match.

So I'm just going to add one character

to the end of the file.

And one way to do that is just simply

do something like echo a 1 to the end of this file

and hit Enter.

So now we've changed the file just a bit.

So I'm gonna back up here

and execute my sha256sum command again and see what happens.

Now it doesn't match.

The sum we received begins with da and ends with a1 here.

And obviously this is a big long string in the middle,

but if we compare that to the known good checksum,

it doesn't match.

So even a very slight change of data

completely changes this checksum that's returned.

By the way, there are other hash functions

in checksum programs.

So we can do a quick ls and usr/bin.

So we'll just do ls dash L usr/bin.

For any programs that end in sum,

we'll use a wild card of asterisk and end in sum

and hit Enter.

So you have cksum, md5sum, sha1sum, sha224, so on.

So all these programs do pretty much the same thing.

They take a big chunk of data

and reduce it down to a single number

or a string that represents that chunk of data

to verify if it's the same or not.

Okay, now let's bring this back to password generation.

As you might have noticed,

the checksums are actually hexadecimals numbers

with zero through nine,

representing, well zero through nine,

and A through F, representing the values from 10 to 16.

If we were to use a sha256sum as a password, for example,

that password would consist of 16 different characters,

that zero through nine and A through F

and be 64 characters in length.

That's a pretty darn good password.

So let's turn the current date and time

into a sha256sum by piping the output of the date command

as the input into the sha256sum command.

So we'll just run the date command by itself

date and we'll use the Epoch here.

And now what I'm going to do is use a pipe symbol,

which takes the output of the proceeding command

and sends it as a standard input

to the following command, sha256sum, and hit Enter.

Okay, so that's the sha256sum of the output

of the date command at the time it was executed.

So obviously when you execute this,

you're going to get a different value

because when you're watching this video,

it's going to be far past when I recorded it,

so obviously you're going to be getting different data here.

So how does this work or why does this work?

So we were running sha256sum against files.

Well, let's look at the man page real quick.

So in the synopsis there we have an optional OPTION

as well as an optional FILE.

And it says with no FILE or when FILE is a dash,

read standard input.

So remember with a pipe,

pipe turns the output of the previous command

as standard input in the command that follows the pipe.

So that is how this works.

And by the way, most commands work like this.

If they take a file as an argument,

you can also not use the file and instead use standard input

via a pipe and it will operate on that input.

So I'll hit q to exit out of the man page here.

Since our goal here is to really generate

a seemingly random set of characters as a password,

we really don't care if the shasum remains intact or not.

We're not gonna be using that check checksum

to check it against another piece of data,

we just want its output.

So if we wanna control the size of this generated password,

you'll need to control

the number of characters returned or displayed.

One way to do this is with the head command.

And just to briefly recap,

how can you tell if head is a program on the system

or if it's a shell built in?

Well, of course you can use the type,

built in type -a head.

Sure enough, head is usr/bin/head, which is a program.

So we can't use help head.

What we have to do is use man head.

Just a quick reminder there.

So what head does is outputs the first part of files

or the head portion of a file.

Without any option,

it just prints the first 10 lines of a file.

You can also see this command,

like the sha256sum command,

it says with no FILE or when FILE is a dash,

read standard input.

So we know we can use this head command

in conjunction with the pipe.

The first option that's listed there is -c,

or --bytes in the long form,

and what that does is prints the first K bytes of each file.

So if we were to do -c1,

then it would just print the first character of the file.

The next option is -n for lines,

and that prints the first number of lines that you specify

instead of the default first 10 lines.

So let's go ahead and try both of these options out.

So let's do head -n1 on /etc/passwd

and what that does is prints the first line of /etc/passwd.

By the way,

you can also do this head -n space 1 /etc/passwd.

So if you see either style,

if you see someone like me

who takes some shortcuts sometimes,

I'll probably squish the value against its options,

so -n1 for example.

But if you see -n space 1, it's the same thing.

So if you see either one, you know it's the same thing.

And by the way, there's an old style

of using this head command.

So let's do this head -1 /etc/passwd.

So instead of using a -n followed by a number,

just use the dash followed by the number.

So here's how to print the first two lines of that file head

-: 2 /etc/passwd and so on.

Obviously that's equivalent of head -n2 /etc/passwd

or head -n space 2 /etc/passwd.

Okay, let's just print the first character

of the password file head -c1 /etc/passwd.

Let's print the first two characters head -c2 /etc/passwd.

So obviously the first line

we can see it starts with the root.

The first character is r, the first two characters are ro.

Now, I'm sure you remember from the man page

how you can use standard input instead of a file

with a head command, so let's try that out.

Let's generate some output from the echo command.

We'll just do echo testing,

and then we will pipe that output

as the standard input into the head command

and let's just print the first two characters, -c2.

So sure enough, it returns te.

Now let's chain the date command,

the sha256sum command and the head command all together.

So you can have multiple pipes, not just one pipe,

but you can keep modifying the output

and keep piping it into different commands.

So we'll execute date, seconds since the Epoch,

we'll get the sha256sum for that,

and we'll print the first eight characters.

So if I hit the up arrow key and do that again,

again, we keep getting a seemingly bit of random data here.

If we wanna make this even better,

we can add those nanoseconds to the mix.

So we can do date+%s%N sha256sum head -c8

and we get even more random data.

Now let's add this method to our script.

So I'll go back and edit the file.

We'll say we'll create a better password.

So we'll use the date command with seconds

and nanosecond sha256sum head -c

and then we'll just say specify

32 character length password here.

And we'll echo this PASSWORD to the screen.

Forgot my opening quote there.

Okay, let's exit to the command line and execute our script.

Okay, so the password at the very bottom here,

the latest thing that we're echoing to the screen

is that 32 character password.

And so each time we execute it,

we get a very different result.

So that looks like a pretty good password to me,

but we can even take this further.

Let's go back and edit our file again.

Let's create an even better password.

One way we can do this

is just add some random numbers to the mix.

So we'll do date plus +%s%N

and we'll follow that by a couple of random numbers here,

and then we'll pipe that into sha256sum.

And then what we're going to do is

let's say we want to make this password

48 characters in length,

so we'll do -c48 and we'll echo that PASSWORD to the screen.

Okay, as you can see, we got a 32 character password

and then a 48 character password here.

So just keep running that,

and we get lots of different passwords

here that we could use.

Now, there are other probably way more secure ways

to generate a password that has nothing to do

with the current date,

but this is really honestly good enough,

especially if you're going to force

a password change on login.

But while we're at it,

let's keep going and add a special character

to the generated password file.

Now let's start out by displaying

the set of special characters that we want to use.

And I'm actually going to store this into a variable

right here in our interactive shell,

so I don't have to keep typing these characters

over and over again.

So I'm just going to use a simple name of capital S.

Now, again, that's not a best practice for shell scripting,

but it's going to work for testing

and we'll use a better,

more descriptive variable name for our script.

But here in the command line

I'm just going to use the variable S

and assign it to the special characters.

Okay, let's echo those characters.

Okay, those are our special characters.

Now we need a way to randomly extract

just one special character from that list.

Now there is a command called shuf, S-H-U-F.

Now let's see if it can do what we want.

So let's look at the man page for this command.

It says write a random permutation of the input lines

to standard output.

So this appears to work on entire lines.

Now of course, if you're unsure what a command does,

well just try it out.

So let's do that here.

Let's run it against the password file, for example,

and see what happens.

Hit q to get outta the man page,

and we'll just do shuf /etc/passwd,

and let's do it a couple of times

to see if we can figure out what it's doing here.

So sure enough, it is definitely printing entire lines.

And if we just look for example,

at the last line here, nfsnobody, rpcuser,

einstein, and so on,

this is definitely displaying random lines

out of the /etc/passwd file.

So we need to break our list of single characters

into individual lines so that we can then use shuf

to do the randomization.

So there happens to be a command called fold

that can do just this.

Let's look at the man page for fold.

So the fold command wraps each input line

to fit in a specified width.

And it looks like there are some different ways

to specify that width.

And by the way,

if we want to change our entire line of special characters

into separate lines,

then we simply need a width of one.

So if we look here, -b says it shows bytes,

-: c counts characters rather than columns,

-: w use width instead of 80.

So it looks like we have a couple of

different options here, -b, -c, or -w that we can use.

It's not really clear here in the man page

what the difference is, so what I like to do is experiment.

So I'm going to use each one of these options

and see if I can spot a difference between them.

So I'll just hit q to get out of the man page

and return to the command line.

So let's echo our string of characters her.

Echo.

Okay, now let's see what fold -b1 does.

Okay, it lists our characters at a width of one.

It looks like our last character here is equal sign,

but it looks like there's an empty line here.

Okay, well let's see what -c1 does.

Same thing.

Let's look at -w1.

Okay, so in my opinion,

it's easier to work with a -w option

because we don't have to account for that blank line

that's being generated.

So now let's pass this output into the shuf command.

So we'll do echo $ S into fold,

and then we will pass that to shuf

and we get a different order of the characters.

Let's keep doing this a couple of times here,

and sure enough, each time we run it,

these characters are displayed in a different order.

Now we're getting a random list of special characters.

If we only want one special character,

we can use the head command with a -c option,

followed by a one.

So let's do that head -c1, and sure enough,

we get a dollar sign that time we executed it.

This time we get a closing parentheses, a pound sign,

a closing parentheses, a carrot symbol, pound sign.

So this appears to be working, doing what we really want,

which is to get a random special character.

Now, I hope you noticed a pattern

in how I worked through this little mini challenge here.

First, I had a goal in mind.

I knew I wanted a random single special character.

Next, I simply displayed what I had.

In this case, I used the echo command

to display the special characters.

Now, if I was working on another problem,

perhaps I would display the contents

of a file or something else.

Next, I changed the output

so that I could work with it easier.

The way you can change the output

is by using that output as the input of another command.

So I pipe the output of the echo command

into the fold command,

and I kept doing this until I reached my goal,

taking the output, piping it in as the input

to another command and keep repeating that.

So it's important to keep in mind the Unix

and Linux philosophy that each program

should only do one thing and that it should do it very well.

So in our case, the echo command only displays output.

It doesn't do any sorting,

it doesn't do any randomization and so on.

It does its one job, and it does it really well.

When you need another job done,

you'll need to use another command.

That's why we use pipe,

so we can string together all these specialized commands

to make the system do exactly what we want.

Some people call this data munging

or string manipulation and so on.

At any rate, I go over a lot of these techniques

in my "Command Line Kung Fu" book,

and it's filled with examples of small specialized commands

all piped together to do something unique and useful.

Anyway, before I get too carried away

about how awesome Linux is and the philosophy and so on,

let's go ahead and add this last way

to generate a password to our script.

We're just going to append a special character

to the password.

So we'll do a SPECIAL_CHARACTER variable name,

which is a lot better than just dollar sign S.

We're going to echo our string of special characters,

pipe that into fold with a width of one column,

shuf to randomize those lines,

and then we're just going to extract

one character from that, the first character.

And now we're going to echo that password

that we generated previously,

and we're going to append this special character to it.

Okay, let's save our changes and execute our script.

Okay, so you can see that this 48 character password

was generated, and then we just displayed that

in addition to a random special character.

So each time we do this,

we'll get a different password

that now includes a special character.

So we have a great password in my opinion,

that you can use,

especially if it's just a one-time password.

So to quickly recap,

in this lesson, you were introduced

to the built-in variable of random,

which generates a random integer

each time that it's referenced.

You also worked with a date command

and used its formatting options to control its output.

From there, we talked about checksums,

and specifically looked at the sha1sum

and sha256sum commands.

You also learned about the head command,

which can display the top or beginning lines

or characters of a file.

Next, you use the fold command to transform

a single line of text into multiple lines.

Finally, you use the shuf command to randomly select a line.







"""

result = clean_and_unwrap_paragraph(paragraph)
print(result)