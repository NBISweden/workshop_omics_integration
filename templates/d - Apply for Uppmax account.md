The below is a template text. Make sure it is modified to your course.

**How to apply for an UPPMAX account - course leader responsibility**

Uppmax guidelines: [<span class="underline">https://www.uppmax.uu.se/support/getting-started/course-projects/</span>](https://www.uppmax.uu.se/support/getting-started/course-projects/)

**WITHOUT COMPLETING THE FOLLOWING AT LEAST 2 WEEKS BEFORE COURSE START, YOU WILL NOT BE ALLOWED TO TAKE PART IN THE COURSE\!**

See more details about each point below, read those before starting as there are a couple of areas where you will be **delayed up to 2 weeks** if you don’t do it properly:

> **1.** **Create an account in SUPR.**
> 
> **2.** **Apply for membership in the course project.**
> 
> **3.** **Accept the SNIC User Agreement in SUPR.**
> 
> **4.** **Apply for an UPPMAX account in SUPR.**
> 
> **5.** **Wait for an email from UPPMAX with your UPPMAX account details.**
> 
> **6.** **Log in with your new UPPMAX account.**
> 
> **7.** **Create a new file with your user name in the designated folder. This way we will know who has completed these steps.**

The reason we are strict on this point is that we have had problems in the past with students not doing these steps before the course. It results in them not being able to do the first day of the course because it takes a couple of hours at best to fix the problem. This only steals time from the teachers and causes the student to fall behind from the start.

> **1.** **Create an account in SUPR.**
> 
> ● If you already have a SUPR account, please continue to step 2.
> 
> ● Go to [<span class="underline">https://supr.snic.se/</span>](https://supr.snic.se/) and click “Register New Person” at the bottom of the first page. Complete the registration process, preferably using SWAMID, and login. If you for some reason can't use SWAMID to login, you will have to send physical (not electronic) copy of your ID to a place in Gothenburg for manual approval. Do this as **soon as possible**, as this process can take **more than 2 weeks.**
> 
> **2.** **Apply for membership in the course project**
> 
> ● Log in using your SUPR account.
> 
> ● Under the “Projects” heading, press the “View and Manage Projects” button.
> 
> ● Search for the project ID: **g2017018**
> 
> ● Press the “Request” button to apply for membership in the project.
> 
> **3.** **Accept the SNIC User Agreement.**
> 
> ● In SUPR, click on the link "Personal Information" in the left sidebar. You will have to accept the SNIC User Agreement to be able to get an UPPMAX account.
> 
> **4.** **Apply for an UPPMAX account**
> 
> ● In SUPR, click on the link "Accounts" in the left sidebar and apply for an UPPMAX account under the heading "Account Requests".
> 
> **5.** **Wait for an email from UPPMAX with your UPPMAX account details.**
> 
> ● Within about 2 working days you should get an email with instructions. *Please, follow these instructions carefully.*
> 
> ● A while later you will get an email with your user name, and another email with a link to your password. **NOTE:** the link is only valid for **1** **VISIT or 7 days**, so if you click the link you better save the password, because you will not be able to use the link again. Do this before 7 days have passed, otherwise the link will no longer be valid.
> 
> **6.** **Log in with your new UPPMAX account**
> 
> ● Open your terminal program (Terminal in OSX and Linux, otherwise download [<span class="underline"> MobaXterm</span>](http://mobaxterm.mobatek.net/download-home-edition.html) (portable edition) if you have Windows).
> 
> ● Type this command in your terminal program:
> 
> **ssh your\_uppmax\_user\_name@milou.uppmax.uu.se**
> 
> (obviously replace *your\_uppmax\_user\_name* with your uppmax user name)
> 
> ● You will be asked for your password now, and you will not see any response in the terminal while typing your password. This is to hide the length of your password, i.e. normal. Just press enter when you have typed it in and you should log in.
> 
> ● If it is the first time you log in, it will ask you to change your LDAP password (the password you just typed). It will directly ask you for your password again, so type it once more. After that it will ask you for your new password, so make up a new one and press enter. After that it will ask you to confirm the new password. When the password change is completed you will be disconnected and you will have to connect again, using your new password to log in this time.
> 
> **7.** **Create a new file with your user name in the designated folder.**
> 
> ● After having received information that your membership is approved, **wait 24 h** before continuing, as it takes 24 h for SUPR to sync with UPPMAX. Else, you will get the message “permission denied” if you try to create the file before this sync has been performed.
> 
> ● Log in to UPPMAX as in step 6
> 
> ● Type the command:
> 
> **touch /proj/** **g2017024/completed/your\_uppmax\_user\_name**
> 
> and of course replace *your\_uppmax\_user\_name* with your uppmax user name.
> 
> ● Unless you got some kind of error message you should now be finished. To make sure the file was created you can type
> 
> **ls /proj/** **g2017024/completed/your\_uppmax\_user\_name**
> 
> (you guessed it, replace it with your user name)
> 
> ● It should write out the name of the file if the file exists. *If you get an error message, please contact the course leader.*
