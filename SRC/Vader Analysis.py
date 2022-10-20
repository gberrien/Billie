#!/usr/bin/env python
# coding: utf-8

# In[22]:


#pip install vaderSentiment


# In[ ]:


#results = 


# In[7]:


# function to print sentiments
# of the sentence.
def sentiment_scores(sentence):
# Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
# polarity_scores method of SentimentIntensityAnalyzer
# oject gives a sentiment dictionary.
# which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
    #print("Overall sentiment dictionary is : ", sentiment_dict)
    #print("item was rated as ", sentiment_dict['neg']*100, "% Negative")
    #print("item was rated as ", sentiment_dict['neu']*100, "% Neutral")
    #print("item was rated as ", sentiment_dict['pos']*100, "% Positive")
    #print("item Overall Rated As", end = " ")
    # decide sentiment as positive, negative and neutral
    #if sentiment_dict['compound'] >= 0.05 :
        #print("Positive")
    #elif sentiment_dict['compound'] <= - 0.05 :
        #print("Negative")
    #else :
        #print("Neutral")
    return round(((sentiment_dict['pos']*100)-(sentiment_dict['neg']*100)), 2)


# In[54]:


# Driver code
if __name__ == "__main__" :
    print("Text Selected for VADER Sentimental Analysis :")
   # sentence2 = 
    album1 = ('''"White shirt now red, my bloody nose Sleepin', you're on your tippy toes Creepin' around like no one knows Think you're so criminal Bruises on both my knees for you Don't say thank you or please I do what I want when I'm wanting to My soul? So cynical   So you're a tough guy Like it really rough guy Just can't get enough guy Chest always so puffed guy I'm that bad type Make your mama sad type Make your girlfriend mad tight Might seduce your dad type I'm the bad guy Duh [Post-Chorus] I'm the bad guy   I like it when you take control Even if you know that you don't Own me, I'll let you play the role I'll be your animal My mommy likes to sing along with me But she won't sing this song If she reads all the lyrics She'll pity the men I know   So you're a tough guy Like it really rough guy Just can't get enough guy Chest always so puffed guy I'm that bad type Make your mama sad type Make your girlfriend mad tight Might seduce your dad type I'm the bad guy Duh  [Post-Chorus] I'm the bad guy, duh I'm only good at bein' bad, bad You might also like[Bridge] I like when you get mad I guess I'm pretty glad that you're alone You said she's scared of me? I mean, I don't see what she sees But maybe it's 'cause I'm wearing your cologne  [Outro] I'm a bad guy I'm, I'm a bad guy Bad guy, bad guy I'm a bad"
"What is it about them? I must be missing something They just keep doing nothing Too intoxicated to be scared Better off without them They're nothing but unstable Bring ashtrays to the table And that's about the only thing they share   I'm in their secondhand smoke Still just drinking canned Coke I don't need a Xanny to feel better On designated drives home Only one who's not stoned Don't give me a Xanny, now or ever [Interlude] Can you check your Uber rating? Oh my god (And it's like, wait, like, when?)   Wakin' up at sundown (Ooh) They're late to every party (Ooh) Nobody's ever sorry (Ooh) Too inebriated now to dance Morning as they come down (Come down) Their pretty heads are hurting (Hurting) They're awfully bad at learning (Learning) Make the same mistakes, blame circumstance   I'm in their secondhand smoke Still just drinking canned Coke I don't need a Xanny to feel better On designated drives home Only one who's not stoned Don't give me a Xanny, now or ever  [Bridge] Please don't try to kiss me on the sidewalk On your cigarette break I can't afford to love someone Who isn't dying by mistake in Silver Lake You might also like[Outro] What is it about them? I must be missing something They just keep doin' nothing Too intoxicated to be scared Hmm, hmm Hmm, mmm, mmm, mmm, mmm Come down Hurting Learning"
"Bite my tongue, bide my time Wearing a warning sign Wait 'til the world is mine Visions I vandalize Cold in my kingdom size Fell for these ocean eyes   You should see me in a crown I'm gonna run this nothing town Watch me make 'em bow One by one by one One by one by You should see me in a crown Your silence is my favorite sound Watch me make 'em bow One by one by one One by one by one  Count my cards, watch them fall Blood on a marble wall I like the way they all scream Tell me which one is worse Living or dying first Sleeping inside a hearse (I don't dream)  [Bridge] You say, ""Come over, baby I think you're pretty"" I'm okay, I'm not your baby If you think I'm pretty   You should see me in a crown I'm gonna run this nothing town Watch me make 'em bow One by one by one One by one by You should see me in a crown Your silence is my favorite sound Watch me make 'em bow One by one by one One by one by one You might also like[Instrumental Break]   Crown I'm gonna run this nothing town Watch me make 'em bow One by one by one One by one by You should see me in a crown (You should see me, see me) Your silence is my favorite sound (You should see me, see me) Watch me make 'em bow One by one by one One by one by one"
"My Lucifer is lonely   Standing there, killing time Can't commit to anything but a crime Peter's on vacation, an open invitation Animals, evidence Pearly Gates look more like a picket fence Once you get inside 'em Got friends but can't invite them [Pre-Chorus] Hills burn in California My turn to ignore ya Don't say I didn't warn ya   All the good girls go to Hell 'Cause even God herself has enemies And once the water starts to rise And Heaven's out of sight She'll want the Devil on her team  [Post-Chorus] My Lucifer is lonely  Look at you needing me You know I'm not your friend without some greenery Walk in wearin' fetters Peter should know better Your cover up is caving in Man is such a fool, why are we saving him? Poisoning themselves now Begging for our help, wow [Pre-Chorus] Hills burn in California My turn to ignore ya Don't say I didn't warn ya You might also like All the good girls go to Hell (All the good girls go to Hell) 'Cause even God herself (God herself) has enemies And once the water starts to rise (Water starts to rise) And Heaven's out of sight She'll want the Devil on her team  [Post-Chorus] My Lucifer is lonely There's nothing left to save now My god is gonna owe me There's nothing left to save now  [Outro] Haha! I cannot do the snowflake"
"Baby, I don't feel so good,"" six words you never understood ""I'll never let you go,"" five words you'll never say (Aww) I laugh along like nothing's wrong, four days has never felt so long If three's a crowd and two was us, one slipped away (Hahahahahahahaha)   I just wanna make you feel okay But all you do is look the other way I can't tell you how much I wish I didn't wanna stay I just kinda wish you were gay  Is there a reason we're not through? Is there a 12 step just for you? Our conversation's all in blue 11 ""heys"" (Hey, hey, hey, hey) Ten fingers tearin' out my hair Nine times you never made it there I ate alone at 7, you were six minutes away (Yay)   How am I supposed to make you feel okay When all you do is walk the other way? I can't tell you how much I wish I didn't wanna stay I just kinda wish you were gay [Bridge] To spare my pride To give your lack of interest an explanation Don't say I'm not your type Just say that I'm not your preferred sexual orientation I'm so selfish But you make me feel helpless, yeah And I can't stand another day Stand another day You might also like I just wanna make you feel okay But all you do is look the other way, hmm I can't tell you how much I wish I didn't wanna stay I just kinda wish you were gay I just kinda wish you were gay I just kinda wish you were gay"
"Don't you know I'm no good for you? I've learned to lose you, can't afford to Tore my shirt to stop you bleedin' But nothin' ever stops you leavin'   Quiet when I'm coming home and I'm on my own I could lie, say I like it like that, like it like that I could lie, say I like it like that, like it like that  Don't you know too much already? I'll only hurt you if you let me Call me friend, but keep me closer (Call me back) And I'll call you when the party's over   Quiet when I'm coming home and I'm on my own And I could lie, say I like it like that, like it like that Yeah, I could lie, say I like it like that, like it like that  [Bridge] But nothin' is better sometimes Once we've both said our goodbyes Let's just let it go Let me let you go   Quiet when I'm coming home and I'm on my own I could lie, say I like it like that, like it like that I could lie, say I like it like that, like it like that"
"Wait a minute, let me finish I know you don't care But can you listen? I came committed, guess I overdid it Wore my heart out on a chain Around my neck, but now it's missin', hmm   Da-da-da-da-da-da (Hmm) Da-da-da-da-da-da-da (Hmm, hmm, hmm, hmm) Oh, hmm, hmm   So I think I better go I never really know how to please you You're lookin' at me like I'm see-through I guess I'm gonna go I just never know how you feel Do you even feel anything?   Da-da-da-da-da-da-da Da-da-da-da-da-da-da Oh, hmm, hmm You might also like You said, ""Don't treat me badly"" But you said it so sadly So I did the best I could Not thinkin' you would have left me gladly I know you're not sorry Why should you be? 'Cause who am I to be in love When your love never is for me? Me   Da-da-da-da-da-da-da (Hmm) Da-da-da-da-da-da-da (Hmm, hmm, hmm, hmm) Oh, hmm, hmm   So I think I better go I never really know how to please you You're lookin' at me like I'm see-through I guess I'm gonna go I just never know how you feel Do you even feel anything?"
"No, Billy, I haven't done that dance since my wife died There 2019s a whole crowd of people out there who need to learn how to do The Scarn   Don't ask questions you don't wanna know Learned my lesson way too long ago To be talkin 2019 to you, belladonna Shoulda taken a break, not an Oxford comma Take what I want when I wanna And I want ya [Pre-Chorus] Bad, bad news One of us is gonna lose I'm the powder, you're the fuse Just add some friction   You are my strange addiction You are my strange addiction My doctors can't explain My symptoms or my pain But you are my strange addiction  [Interlude] I'm really, really sorry, I think I was just relieved To see that Michael Scarn got his confidence back Yeah, Michael, the movie is amazing It's like, one of the best movies I've ever seen in my life   Deadly fever, please don't ever break Be my reliever  2019cause I don 2019t self medicate And it burns like a gin and I like it Put your lips on my skin and you might ignite it Hurts, but I know how to hide it, kinda like it (Teh) You might also like[Pre-Chorus] Bad, bad news One of us is gonna lose I'm the powder, you 2019re the fuse Just add some friction   You are my strange addiction You are my strange addiction My doctors can't explain My symptoms or my pain But you are my strange addiction  [Bridge] Bite my glass, set myself on fire Can't you tell I'm crass? Can 2019t you tell I'm wired? Tell me nothing lasts, like I don't know You could kiss my 2014 asking about my motto  [Interlude] You should enter it in festivals or carnivals Thoughts? Pretty good reaction Pretty cool... right?   You are my strange addiction You are my strange addiction My doctors can't explain My symptoms or my pain But you are my strange addiction [Outro] Did you like it? Did you like that? Um, which part?"
"What do you want from me? Why don't you run from me? What are you wondering? What do you know? Why aren't you scared of me? Why do you care for me? When we all fall asleep, where do we go?  [Verse 1"", "" Billie Eilish & Mehki Raine] Come here Say it, spit it out, what is it exactly You're payin'? Is the amount cleanin' you out? Am I satisfactory? Today, I'm thinkin' about the things that are deadly The way I'm drinkin' you down Like I wanna drown, like I wanna end me [Refrain"", ' Billie Eilish] Step on the glass, staple your tongue (Ahh) Bury a friend, try to wake up (Ah-ahh) Cannibal class, killing the son (Ahh) Bury a friend, I wanna end me  [Pre-Chorus', ' Billie Eilish] I wanna end me I wanna, I wanna, I wanna 2026 end me I wanna, I wanna, I wanna 2026  [Chorus', "" Billie Eilish] What do you want from me? Why don't you run from me? What are you wondering? What do you know? Why aren't you scared of me? Why do you care for me? When we all fall asleep, where do we go?  [Verse 2"", "" Billie Eilish & Mehki Raine] Listen Keep you in the dark, what had you expected? Me to make you my art and make you a star And get you connected? I'll meet you in the park, I'll be calm and collected But we knew right from the start that you'd fall apart 'Cause I'm too expensive It's probably somethin' that shouldn't be said out loud Honestly, I thought that I would be dead by now (Wow) Calling security, keepin' my head held down Bury the hatchet or bury a friend right now You might also like[Bridge"", "" Billie Eilish & Mehki Raine] The debt I owe, gotta sell my soul 'Cause I can't say no, no, I can't say no Then my limbs all froze and my eyes won't close And I can't say no, I can't say no Careful  [Refrain"", ' Billie Eilish] Step on the glass, staple your tongue (Ahh) Bury a friend, try to wake up (Ah-ahh) Cannibal class, killing the son (Ahh) Bury a friend, I wanna end me [Pre-Chorus', ' Billie Eilish] I wanna end me I wanna, I wanna, I wanna 2026 end me I wanna, I wanna, I wanna 2026  [Chorus', ' Billie Eilish] What do you want from me? Why don't you run from me? What are you wondering? What do you know? Why aren't you scared of me? Why do you care for me? When we all fall asleep, where do we go?"
"Told you not to worry But maybe that's a lie Honey, what's your hurry? Won't you stay inside? Remember not to get too close to stars They're never gonna give you love like ours   Where did you go? I should know, but it's cold And I don't wanna be lonely So show me the way home I can't lose another life  Hurry, I'm worried   The world's a little blurry Or maybe it's my eyes The friends I've had to bury They keep me up at night Said I couldn't love someone 'Cause I might break If you're gonna die, not by mistake   So, where did you go? I should know, but it's cold And I don't wanna be lonely So tell me you'll come home Even if it's just a lie  [Bridge] I tried not to upset you Let you rescue me the day I met you I just wanted to protect you But now I'll never get to   Hurry, I'm worried You might also like[Outro] Where did you go? I should know, but it's cold And I don't wanna be lonely Was hoping you'd come home I don't care if it's a lie"
"Take me to the rooftop I wanna see the world when I stop breathing Turnin' blue Tell me love is endless, don't be so pretentious Leave me like you do (Like you do)  [Pre-Chorus] If you need me, wanna see me Better hurry 'cause I'm leavin' soon  Sorry can't save me now Sorry I don't know how Sorry there's no way out (Sorry) But down Hmm, down   Taste me, the salty tears on my cheek That's what a year-long headache does to you I'm not okay, I feel so scattered Don't say I'm all that matters Leave me, d 00e9j 00e0 vu (Hmm)  [Pre-Chorus] If you need me, wanna see me You better hurry, I'm leavin' soon   Sorry can't save me now (Sorry) Sorry I don't know how (Sorry) Sorry there's no way out (Sorry) But down Hmm, down  [Outro] Call my friends and tell them that I love them And I'll miss them But I'm not sorry Call my friends and tell them that I love them And I'll miss them Sorry"
"It's not true Tell me I 2019ve been lied to Crying isn't like you, ooh What the hell did I do? Never been the type to Let someone see right through, ooh   Maybe won't you take it back? Say you were tryna make me laugh And nothing has to change today You didn 2019t mean to say ""I love you"" I love you and I don't want to, ooh  Up all night on another red-eye I wish we never learned to fly Maybe we should just try To tell ourselves a good lie Didn't mean to make you cry   Maybe won't you take it back? Say you were tryna make me laugh And nothing has to change today You didn't mean to say ""I love you"" I love you and I don't want to, ooh  [Bridge] The smile that you gave me Even when you felt like dying  [Outro] We fall apart as it gets dark I'm in your arms in Central Park There's nothing you could do or say I can 2019t escape the way I love you I don 2019t want to, but I love you, ooh Ooh, ooh Ooh, ooh"
"Please, please Don't leave  me Be   It's not true Take me to the rooftop Told you not to worry What do you want from me? Don't ask questions Wait a minute Don't you know I'm no good for you? Baby, I don't feel so good And all the good girls go  to Hell Bite my tongue, bide my time What is it about them? I'm the bad guy"
''')
    album2 = ('''"I'm gettin' older, I think I'm agin' well I wish someone had told me I'd be doin' this by myself There's reasons that I'm thankful, there's a lot I'm grateful for But it's different when a stranger's always waitin' at your door Which is ironic 'cause the strangers seem to want me more Than anyone before (Anyone before) Too bad they're usually deranged   Last week, I realized I crave pity When I retell a story, I make everything sound worse Can't shake the feeling that I'm just bad at healing And maybe that's the reason every sentence sounds rehearsed Which is ironic because when I wasn't honest I was still bein' ignored (Lyin' for attention just to get neglection) Now we're estranged  Things I once enjoyed Just keep me employed now Things I'm longing for Someday, I'll be bored of It's so weird That we care so much until we don't   I'm gettin' older, I've got more on my shoulders But I'm gettin' better at admitting when I'm wrong I'm happier than ever, at least, that's my endeavor To keep myself together and prioritize my pleasure 'Cause, to be honest, I just wish that what I promise Would depend on what I'm given, mmm (Not on his permission) (Wasn't my decision) To be abused, mmm   Things I once enjoyed Just keep me employed now, mmm Things I'm longing for, mmm Someday, I'll be bored of It's so weird That we care so much until we don't  [Outro] But next week, I hope I'm somewhere laughing For anybody asking, I promise I'll be fine I've had some trauma, did things I didn't wanna Was too afraid to tell ya, but now, I think it's time"
"Okay Mm-mm, I   I didn't change my number I only changed who I reply to Laura said I should be nicer But not to you I love a ""You mad at me?"" text Shoulda guessed That you would think I was upset (Haha) You're obsessed  Don't take it out on me I'm out of sympathy for you Maybe you should leave Before I get too mean   I didn't change my number I only changed who I believe in You were easy on the eyes, eyes, eyes (Eyes, ey 0435s) But looks can be deceivin' I gotta work, I go to work You don't d 0435serve to feel so hurt You got a lot of fuckin' nerve I don't deserve, so   Don't take it out on me I'm out of sympathy for you Maybe you should leave Before I get too mean And take it out on you And your best friend, too I should have left when Drew Said you were bad news You might also like[Outro', ' Billie Eilish & FINNEAS] Mm-mm-mm Mm-mm-mm Mm-mm-mm Mm-mm-mm Mm-mm-mm Mm-mm-mm"
"Mm-mm-mm, mm-mm Da-da-da-da   Love when it comes without a warning 'Cause waiting for it gets so boring A lot can change in twenty seconds A lot can happen in the dark Love when it makes you lose your bearings Some information's not for sharing Use different names at hotel check-ins It's hard to stop it once it starts (It starts)  I'm not sentimental But there's somethin' 'bout the way you look tonight, mm Makes me wanna take a picture Make a movie with you that we'd have to hide   You better lock your phone (Oh) And look at me wh 0435n you're alone Won't take a lot to g 0435t you goin' (Oh) I'm sorry if it's torture though I know, I know   It might be more of an obsession You really make a strong impression (A strong impression) Nobody saw me in the lobby (Saw me in the lobby) Nobody saw me in your arms, mm   I'm not sentimental But there's somethin' 'bout the way you look tonight, mm ('Bout the way you look tonight) Makes me wanna make 'em jealous I'm the only one who does it how you like (Only one who does it how you 2014)   You better lock your phone (Oh) And look at me when you're alone (You're alone, you're alone) Won't take a lot to get you goin' (Get me goin', get me goin') I'm sorry if it's torture though (Torture though) I know, I know You better lock your door (Oh) And look at me a little more We both know I'm worth waitin' for (Waitin' for) That heavy breathin' on the floor (On the floor) I'm yours, I'm yours (I'm yours) You might also like[Outro] I'm not sentimental I'm not sentimental I'm not sentimental"
"I can't seem to focus And you don't seem to notice I'm not here I'm just a mirror You check your complexion To find your reflection's all alone I had to go   Can't you hear me? I'm not comin' home Do you understand? I've 205fchanged 205fmy 205fplans [Chorus] 'Cause I, I'm 205fin love With my 205ffuture Can't wait to meet her And I (I), I'm in love But not with anybody else Just wanna get to know myself   I know supposedly I'm lonely now (Lonely now) Know I'm supposed to be unhappy Without someone (Someone) But aren't I someone? (Aren't I someone? Yeah) I'd (I'd) like to be your answer (Be your answer) 'Cause you're so handsome (You're so handsome)   But I know better Than to drive you home 'Cause you'd invite me in And I'd be yours again  [Chorus] But I (I), I'm in love (Love, love, love, love) With my future And you don't know her (Ooh) And I, I'm in love (Love, love) But not with anybody here I'll see you in a couple years"
"Can't take it back once it's been set in motion You know I love to rub it in like lotion If you only pray on Sunday, could you come my way on Monday? 'Cause I like to do things God doesn't approve of if She saw us   She couldn't look away, look away, look away She'd wanna get involved, involved, involved And what would people say, people say, people say If they listen through the wall, the wall, the wall?  I can see it clear as day You don't really need a break Wanna see what you can take You should really run away  [Post-Chorus] I wanna do bad things to you (To you) I wanna make you yell (Yell) I wanna do bad things to you (To you) Don't wanna treat you well (Well)   Can't take it back once it's been set in motion You know I need you for the oxytocin If you find it hard to swallow, I can loosen up your collar 'Cause as long as you're still breathing Don't you even think of leaving   Not gonna wanna look away, look away, look away You're gonna wanna get involved, involved, involved And what would people say, people say, people say If they listen through the wall, the wall, the wall?   I can see it clear as day You don't really need a break Wanna see what you can take You should really run away Other people wouldn't stay Other people don't obey You and me are both the same You should really run away You might also like[Outro] Bad things To you I wanna do bad things to you I wanna make you yell I wanna do bad things to you Don't wanna treat you well"
"He hath come to the bosom of his beloved Smiling on him, she beareth him to highest heav'n With yearning heart"" ""On thee we gaze, O' gold-wing'd messenger of mighty Gods""     Gold-winged angel Go home, don't tell Anyone what you are You're sacred and they're starved And their art is gettin' dark And there you are to tear apart Tear apart, tear apart, tear apart [Chorus] You better keep your head down-down Da-da-down-down, da-da-down-down Better keep your head down-down Da-da-down-down, da-da-down-down   They're gonna tell you what you wanna hear Then they're gonna disappear Gonna claim you like a souvenir Just to sell you in a year  [Chorus] You better keep your head down-down Da-da-down-down, da-da-down-down Keep your head down-down (Down) Da-da-down-down, da-da-down-down Better keep your head down-down Da-da-down-down, da-da-down-down Keep your head down-down Da-da-down-down, da-da-down-down  [Outro] That's good"
"Something's in the 2014   Something's in the air right now Like I'm losin' track of time (Time, time) Like I don't really care right now But maybe that's fine You weren't even there that day I was waitin' on you (You, you) I wonder if you were aware that day Was the last straw for me and I knew  I sent you flowers Did you even care? You ran the shower And left them by the stairs Ooh-ooh-ooh, a-a-a-ayy Thought you had your shit together, but damn, I was wrong (Wrong)   You ain't nothin' but a lost cause (Cause, cause) And this ain't nothin' like it onc 0435 was (Was, was) I know you think you're such an outlaw But you got no job (Job) You ain't nothin' but a lost cause (Cause) And this ain't nothin' lik 0435 it once was (Was) I know you think you're such an outlaw But you got no job   I used to think you were shy (Shy) But maybe you just had nothing on your mind Maybe you were thinkin' 'bout yourself all the time I used to wish you were mine (Mine) But that was way before I realized Someone like you would always be so easy to find (So) So easy (So, so) Hee, mm-mm-mm, mm You might also like Gave me no flowers Wish I didn't care You'd be gone for hours Could be anywhere Ooh-ooh-ooh Ah-ah-ah-ah-ah Thought you would've grown eventually, but you proved me wrong (Wrong)   You ain't nothing but a lost cause (Cause) And this ain't nothing like it once was (Was) I know you think you're such an outlaw (Yeah) But you got no job (No job) You ain't nothing but a lost cause (Cause) And this ain't nothing like it once was (Was) I know you think you're such an outlaw (Think you're such a lost cause) But you got no job  [Outro] (What did I tell you?) (Don't get complacent) (It's time to face it now, na-na, na-na, na-na) (What did I tell you?) (Don't get complacent) (It's time to face it now, na-na, na-na, na-na)"
"I don't want it And I don't want to want you But in my dreams, I seem to be more honest And I must admit you've been in quite a few   Halley's Comet Comes around more than I do But you're all it takes for me to break a promise Silly me to fall in love with you  I haven't slept since Sunday Midnight for me is 3AM for you But my sleepless nights are better With you than nights could ever be alone, ooh-ooh I was good at feeling nothin', now I'm hopeless What a drag to love you like I do Ooh-ooh-ooh-ooh-ooh   I've been loved before, but right now, in this moment I feel more and more like I was mad 0435 for you For you    [Outro] I'm sitting in my brother's room Haven't slept in a week or two, or two I think I might hav 0435 fallen in love What am I to do?"
"Do you know me? Really know me? You have opinions about my opinions About my music About my clothes About my body Some people hate what I wear Some people praise it Some people use it to shame others Some people use it to shame me But I feel you watching Always And nothing I do goes unseen So while I feel your stares, your disapproval or your sigh of relief If I lived by them, I'd never be able to move Would you like me to be smaller, weaker, softer, taller? Would you like me to be quiet? Do my shoulders provoke you? Does my chest? Am I my stomach? My hips? The body I was born with Is it not what you wanted? If I wear what is comfortable, I am not a woman If I shed the layers, I'm a slut Though you've never seen my body, you still judge it And judge me for it Why? We make assumptions about people based on their size We decide who they are We decide what they're worth If I wear more, if I wear less Who decides what that makes me? What that means? Is my value based only on your perception? Or is your opinion of me not my responsibility?"
"I don't really even know how it happened I started talkin', they started laughin' I don't really even know how it happened I started watchin' them photographin' I don't really (I don't really), how it happened Instead of stoppin', they still were flashin' (I don't really) I started walkin' (I don't really), gave no reaction No reaction   I'm overheated, can't be defeated Can't be deleted, can't un-believ 0435 it I'm overheated, can't b 0435 defeated Can't be deleted, can't be repeated I'm overheated I'm overheated  I don't really wanna know why it went there (Why it went there) I kinda don't care (Kinda don't care) You wanna kill me? (You wanna kill me?) You wanna hurt me? (Mmm) Stop bein' flirty It's kinda workin' Did you really think ""This is the right thing to do""? (Is it news? News to who?) That I really look just like the rest of you   I'm overheated, can't be defeated Can't be deleted, can't un-believe it I'm overheated, can't be defeated Can't be deleted, can't be repeated I'm overheated  [Bridge] And everybody said it was a letdown I was only built like everybody else now But I didn't get a surgery to help out 'Cause I'm not about to redesign myself now, am I? (Am I?) Am I? All these other inanimate bitches, it's none of my business But don't you get sick of posin' for pictures With that plastic body? You might also like Man, I'm overheated, can't be defeated Can't be deleted, can't un-believe it I'm overheated, can't be defeated Can't be deleted, can't be repeated I'm overheated"
"Everybody dies, surprise, surprise We tell each other lies, sometimes, we try To make it feel like we might be right We might not be alone Be alone   ""Everybody dies,"" that's what they say And maybe, in a couple hundred years, they'll find another way I just wonder why you'd wanna stay If everybody goes You'd still be alone [Verse 3] I don't wanna cry, some days I do But not about you It's just a lot to think about the world I'm used to The one I can't get back, at lu0435ast not for a while I sure have a knack for seein' lifu0435 more like a child It's not my fault, it's not so wrong to wonder why Everybody dies And when will I?  [Verse 4] You oughta know That even when it's time, you might not wanna go But it's okay to cry and it's alright to fold But you are not alone You are not unknown"
"Try not to abuse your power I know we didn't choose to change You might not wanna lose your power But havin' it's so strange   She said you were a hero You played the part But you ruined her in a year Don't act like it was hard And you swear you didn't know (Didn't know) No wonder why you didn't ask She was sleepin' in your clothes (In your clothes) But now she's got to get to class  How dare you? And how could you? Will you only feel bad when they find out? If you could take it all back Would you?   Try not to abuse your power I know we didn't choose to change You might not wanna lose your power But havin' it's so strange   I thought that I was special You made me feel Like it was my fault, you were the devil Lost your appeal Does it keep you in control? (In control) For you to keep her in a cage? And you swear you didn't know (Didn't know) You said you thought she was your age   How dare you? And how could you? Will you only feel bad if it turns out That they kill your contract? Would you? You might also like Try not to abuse your power I know we didn't choose to change You might not wanna lose your power But power isn't pain  [Outro] Mmm Ooh La-la-la-la-la, hmm La-la-la-la-la-la, la-la"
"Did you think I'd show up in a limousine? (No) Had to save my money for security Got a stalker walkin' up and down the street Says he's Satan and he'd like to meet I bought a secret house when I was seventeen (Ha) Haven't had a party since I got the keys Had a pretty boy over, but he couldn't stay On his way out, made him sign an NDA, mm Yeah, I made him sign an NDA Once was good enough 'Cause I don't want him havin' shit to say, oh-oh-oh  You couldn't save me, but you can't let me go, oh, no I can crave you, but you don't need to know, oh-oh   Mm, mm-mm, mm 30 Under 30 for another year (Another year) I can barely go outside, I think I hate it her 0435 (I think I hate it here) Mayb 0435 I should think about a new career (Uh) Somewhere in Kauai where I can disappear I've been havin' fun gettin' older now Didn't change my number, made him shut his mouth (Shut his mouth, yeah) At least I gave him somethin' he can cry about I thought about my future, but I want it now, oh-oh-oh Want it now, mm-mm-mm You can't give me up   You couldn't save me, but you can't let me go, oh, no I can crave you, but you don't need to know, oh-oh  [Outro] Did I take it too far? Now I know what you are You hit me so hard I saw stars Think I took it too far When I sold you my heart How'd it get so dark? I saw stars Stars"
"I'm not your friend Or anything, damn You think that you're the man I think, therefore, I am I'm not your friend Or anything, damn You think that you're the man I think, therefore, I am   Stop, what the hell are you talking about? Ha Get my pretty name out of your mouth We are not the same with or without Don't talk 'bout me like how you might know how I feel Top of the world, but your world isn't real Your world's an ideal  So go have fun I really couldn't care less And you can give 'em my best, but just know   I'm not your friend Or anything, damn You think that you're the man I think, therefore, I am I'm not your friend Or anything, damn You think that you're the man I think, therefore, I am   I don't want press to put your name next to mine We're on different lines, so I Wanna be nice enough, they don't call my bluff 'Cause I hate to find Articles, articles, articles Rather you remain unremarkable (Got a lotta) Interviews, interviews, interviews When they say your name, I just act confused   Did you have fun? I really couldn't care less And you can give 'em my best, but just know You might also like I'm not your friend Or anything, damn You think that you're the man I think, therefore, I am I'm not your friend Or anything, damn You think that you're the man I think, therefore, I am  [Bridge] I'm sorry I don't think I caught your name I'm sorry I don't think I caught your name   I'm not your friend (I'm not your friend) Or anything, damn You think that you're the man (They wanna, they can try) I think, therefore, I am I'm not your friend (I'm not your friend) Or anything, damn (They wanna) You think that you're the man I think, therefore, I am"
"When I'm away from you I'm happier than ever Wish I could explain it better I wish it wasn't true   Give me a day or two to think of something clever To write myself a letter To tell me what to do, mm-mm Do you read my interviews? Or do you skip my avenue? When you said you were passin' through Was I even on your way? I knew when I asked you to (When I asked you to) Be cool about what I was tellin' you You'd do the opposite of what you said you'd do (What you said you'd do) And I'd end up more afraid Don't say it isn't fair You clearly wer 0435n't aware that you made me mis 0435rable So if you really wanna know  When I'm away from you (When I'm away from you) I'm happier than ever (Happier than ever) Wish I could explain it better (Wish I could explain it better) I wish it wasn't true, mm-mm   You call me again, drunk in your Benz Drivin' home under the influence You scared me to death, but I'm wastin' my breath 'Cause you only listen to your fuckin' friends I don't relate to you I don't relate to you, no 'Cause I'd never treat me this shitty You made me hate this city   And I don't talk shit about you on the internet Never told anyone anything bad 'Cause that shit's embarrassing, you were my everything And all that you did was make me fuckin' sad So don't waste the time I don't have And don't try to make me feel bad I could talk about every time that you showed up on time But I'd have an empty line 'cause you never did Never paid any mind to my mother or friends, so I Shut 'em all out for you 'cause I was a kid You might also like[Outro] You ruined everything good Always said you were misunderstood Made all my moments your own Just fuckin' leave me alone, yeah (Fuck you) (Ah) (Goddamn) (Ah) (Fuck you) (Fuck you)"''')
    
interview1 = ('''my name is billy eilish billy eilish
i think it's october 18 2017.
it's october 18th 2018.
i'm 15. i'm 16. i have
250 000.
i have 6.3 million
followers 1.13 million
9.6 million when you look at billy
eilish
it's a picture of me and charlie xcx
isn't it the one about me smiling
of course it is the one picture that i
have smiling the most followed person
that follows me is chloe grace moretz
who's the bash has 13 million followers
katy perry maybe
she is 72 million i'd say probably
khalid
which is weird because he's like just a
homie of mine
and like i don't think women's anything
else scissor
i have millie bobby brown sabrina
claudio
oh bad baby lauren herrera osiris
wayleigh
rich the kid little zane gerber miguel
are you kidding me these are just people
that i've texted
it was at the crocodile in seattle and
it was like 500
i think that's what i said
[Music]
oh whoa
that's so cute um
whoo that was oh the best one i've had
was music midtown in atlanta
40 000 people such a dream oh my god
such a dream every time i go anywhere
hands down i might be safe if i go to
trader joe's
but everywhere else is kind of
get recognized which is actually really
cool but you know it's a lot
kind of a lot actually but like not a
ton it's kind of
like maybe like once a week um
i'm kind of jealous of billy a year ago
because i kind of i don't know i'm
really not about to pity myself
for people recognizing who i am which is
because it's like i'm really grateful
for it
but i don't know i i would like to go
to i don't know anywhere and not be
always recognized whoa
don't be so sad it's such a waste of
time
i didn't i didn't live up to that then
and i still haven't lived up to that
so it's good advice though it is a waste
of time dude
ah it's ruined so many things that could
have been amazing
because i was sad dumb but
whatever
[Music]
don't post everything you think
don't just don't if you're watching this
right now
anybody if anybody is watching this
don't
post your feelings don't
do it to yourself um
whoa tyler the creator
no i would love to meet i've not met him
oh my god i would explode if i met him i
met him
i met him and it was great
for me he hits a he hits a part of me
that nobody gets
being apple's up next artist
[Music]
i was such a baby
i did ellen last week jimmy fallon
lollapalooza
um so many festivals i went to tokyo
i met takashi murakami i went to his
studio
dave girl's daughter did a cover of my
song he played guitar for her at a
talent show
i think or something there's been a lot
of that's happened in the last year
my family i'm i'm always talking to my
family always
[Music]
every second of my life fruitville
station
uh fruitvale station
no uh you know what
no this i can't afford a real chain they
are real now they are real but it's all
silver
oh yeah my chains were gifts i did not
buy anything that i'm wearing
at all none of it
[Music]
i bought this though
[Music]
nah yes
yeah uh yep yeah
it's the kind of pressure that's like it
hits me and then i don't care
everybody drop dead right now and i
didn't
i would be left with what i had created
for myself
and what the hell would the point be if
i was just creating something that
somebody else wanted me to create that i
had no say in
and then that person died and everybody
else died and nobody mattered except me
i'm stuck with this i didn't want
in the first place that's trash
no i'm handling the pressure horribly
but i just keep it to myself
all the time except my wall i write
everything i feel on my wall so if you
go in my room look at my wall
just yeah no
i don't like dating at all i don't like
the idea of
oh this is my one person and i only
share time with this person no no
no no thank you
no i don't have a boyfriend i ca i could
not have a boyfriend that would just be
mean to him
uh i don't know i almost had one for
like a little but
it wasn't really exclusive so i don't
know what you'd call that i hate things
that are exclusive
never letting myself be mistreated
for a long long long long time
i had no idea what the was coming
not really uh yeah i was really
mistreated and then i just realized i
was better than that and since then
i just i feel like i've just grown to
know my worth
i think it's taken a minute and i don't
think i'm there yet but i'm
i'm getting there oh billy was so hurt
then
i was so hurt then man
i want to learn that it's all worth it
because it's tiring as heck
and it is worth it and i have to
remember that because
being with like fans and doing shows is
way more important than being tired
is it worth it
[Music]
yes
[Music]
the shows make it worth it the shows and
the supporters
that is something you have to remember
when it it doesn't feel worth it
because a lot of it doesn't feel worth
it but then you get to the points that
do make it worth it and it's like
then it all sort of makes sense and it
kind of clicks in your head no matter
what you do there's
you can never ever ever please anyone
ever
ever ever
facts still true never not true
any picture that is taken of you
if a picture is taken of you somebody
has it and somebody will use it against
you
i wasn't allowed to but i ran away from
security
and i ran into a huge crowd
i like slammed open a door into all of
them through a glass window and
hugged them all i almost caused a
stampede
by sneaking through a crowd at
lollapalooza
i almost died and everyone else almost
died
crazy whoa lil wayne
oh to perform with lil wayne that's a
great answer
wow 15 year old me was ballin i really
want to go to japan again
i went to japan a while ago and it was
the most amazing time
so i feel like brazil might be crazy
literally my first fan account was like
or like second panic it was like billy
island brazil
brockhampton tierra whack is sick
i like bright green a lot
i like black it's been pretty dark
lately so i've just wanted to be dark
with it
the world i mean
[Music]
i don't and then one word no
[Music]
judge me please
that's what i said
i still feel that way totally still feel
that way
but this year i guess i just don't
 know
i don't know what the is going on
i feel this and that i feel like
everything needs to have a certain this
is in this category and this isn't this
like it's like i want to be everything
like shut up
don't tell me what i can't be the hell
[Music]
the music industry man we're all sad as
hell
all these artists we're sad as dude
everybody i know that's an artist
we are sad
that's the way it is my what
what does that even mean what does that
mean everyone is gonna die and no one is
gonna remember you
so it what this said
that's my philosophy
having the approach that no one's had
trying to write something no one's
written
i don't know if that's the best approach
because you might just fail and then
want to die
like i have to write someone right
something no one's ever heard
see that's why i'm i'm still bad at it
because that's what i was trying to do
 you better know how to drive
because i've been putting off driver's
ed because that stuff stinks i hate that
stuff
i do know how to drive shorty well that
is crazy
this is my mom she is sick as a booty
and she has laryngitis as heck i still
love you
[Music]
[Applause]
my name is billy eilish billy eilish
i think it's october 18 2017.
it's october 18th 2018.
i'm 15. i'm 16. i have
250 000.
i have 6.3 million
followers 1.13 million
9.6 million when you look at billy
eilish
it's a picture of me and charlie xcx
isn't it the one about me smiling
of course it is the one picture that i
have smiling the most followed person
that follows me is chloe grace moretz
who's the bash has 13 million followers
katy perry maybe
she is 72 million i'd say probably
khalid
which is weird because he's like just a
homie of mine
and like i don't think women's anything
else scissor
i have millie bobby brown sabrina
claudio
oh bad baby lauren herrera osiris
wayleigh
rich the kid little zane gerber miguel
are you kidding me these are just people
that i've texted
it was at the crocodile in seattle and
it was like 500
i think that's what i said
[Music]
oh whoa
that's so cute um
whoo that was oh the best one i've had
was music midtown in atlanta
40 000 people such a dream oh my god
such a dream every time i go anywhere
hands down i might be safe if i go to
trader joe's
but everywhere else is kind of
get recognized which is actually really
cool but you know it's a lot
kind of a lot actually but like not a
ton it's kind of
like maybe like once a week um
i'm kind of jealous of billy a year ago
because i kind of i don't know i'm
really not about to pity myself
for people recognizing who i am which is
because it's like i'm really grateful
for it
but i don't know i i would like to go
to i don't know anywhere and not be
always recognized whoa
don't be so sad it's such a waste of
time
i didn't i didn't live up to that then
and i still haven't lived up to that
so it's good advice though it is a waste
of time dude
ah it's ruined so many things that could
have been amazing
because i was sad dumb but
whatever
[Music]
don't post everything you think
don't just don't if you're watching this
right now
anybody if anybody is watching this
don't
post your feelings don't
do it to yourself um
whoa tyler the creator
no i would love to meet i've not met him
oh my god i would explode if i met him i
met him
i met him and it was great
for me he hits a he hits a part of me
that nobody gets
being apple's up next artist
[Music]
i was such a baby
i did ellen last week jimmy fallon
lollapalooza
um so many festivals i went to tokyo
i met takashi murakami i went to his
studio
dave girl's daughter did a cover of my
song he played guitar for her at a
talent show
i think or something there's been a lot
of that's happened in the last year
my family i'm i'm always talking to my
family always
[Music]
every second of my life fruitville
station
uh fruitvale station
no uh you know what
no this i can't afford a real chain they
are real now they are real but it's all
silver
oh yeah my chains were gifts i did not
buy anything that i'm wearing
at all none of it
[Music]
i bought this though
[Music]
nah yes
yeah uh yep yeah
it's the kind of pressure that's like it
hits me and then i don't care
everybody drop dead right now and i
didn't
i would be left with what i had created
for myself
and what the hell would the point be if
i was just creating something that
somebody else wanted me to create that i
had no say in
and then that person died and everybody
else died and nobody mattered except me
i'm stuck with this i didn't want
in the first place that's trash
no i'm handling the pressure horribly
but i just keep it to myself
all the time except my wall i write
everything i feel on my wall so if you
go in my room look at my wall
just yeah no
i don't like dating at all i don't like
the idea of
oh this is my one person and i only
share time with this person no no
no no thank you
no i don't have a boyfriend i ca i could
not have a boyfriend that would just be
mean to him
uh i don't know i almost had one for
like a little but
it wasn't really exclusive so i don't
know what you'd call that i hate things
that are exclusive
never letting myself be mistreated
for a long long long long time
i had no idea what the was coming
not really uh yeah i was really
mistreated and then i just realized i
was better than that and since then
i just i feel like i've just grown to
know my worth
i think it's taken a minute and i don't
think i'm there yet but i'm
i'm getting there oh billy was so hurt
then
i was so hurt then man
i want to learn that it's all worth it
because it's tiring as heck
and it is worth it and i have to
remember that because
being with like fans and doing shows is
way more important than being tired
is it worth it
[Music]
yes
[Music]
the shows make it worth it the shows and
the supporters
that is something you have to remember
when it it doesn't feel worth it
because a lot of it doesn't feel worth
it but then you get to the points that
do make it worth it and it's like
then it all sort of makes sense and it
kind of clicks in your head no matter
what you do there's
you can never ever ever please anyone
ever
ever ever
facts still true never not true
any picture that is taken of you
if a picture is taken of you somebody
has it and somebody will use it against
you
i wasn't allowed to but i ran away from
security
and i ran into a huge crowd
i like slammed open a door into all of
them through a glass window and
hugged them all i almost caused a
stampede
by sneaking through a crowd at
lollapalooza
i almost died and everyone else almost
died
crazy whoa lil wayne
oh to perform with lil wayne that's a
great answer
wow 15 year old me was ballin i really
want to go to japan again
i went to japan a while ago and it was
the most amazing time
so i feel like brazil might be crazy
literally my first fan account was like
or like second panic it was like billy
island brazil
brockhampton tierra whack is sick
i like bright green a lot
i like black it's been pretty dark
lately so i've just wanted to be dark
with it
the world i mean
[Music]
i don't and then one word no
[Music]
judge me please
that's what i said
i still feel that way totally still feel
that way
but this year i guess i just don't
 know
i don't know what the is going on
i feel this and that i feel like
everything needs to have a certain this
is in this category and this isn't this
like it's like i want to be everything
like shut up
don't tell me what i can't be the hell
[Music]
the music industry man we're all sad as
hell
all these artists we're sad as dude
everybody i know that's an artist
we are sad
that's the way it is my what
what does that even mean what does that
mean everyone is gonna die and no one is
gonna remember you
so it what this said
that's my philosophy
having the approach that no one's had
trying to write something no one's
written
i don't know if that's the best approach
because you might just fail and then
want to die
like i have to write someone right
something no one's ever heard
see that's why i'm i'm still bad at it
because that's what i was trying to do
 you better know how to drive
because i've been putting off driver's
ed because that stuff stinks i hate that
stuff
i do know how to drive shorty well that
is crazy
this is my mom she is sick as a booty
and she has laryngitis as heck i still
love you
[Music]
[Applause]
my name is billy eilish billy eilish
i think it's october 18 2017.
it's october 18th 2018.
i'm 15. i'm 16. i have
250 000.
i have 6.3 million
followers 1.13 million
9.6 million when you look at billy
eilish
it's a picture of me and charlie xcx
isn't it the one about me smiling
of course it is the one picture that i
have smiling the most followed person
that follows me is chloe grace moretz
who's the bash has 13 million followers
katy perry maybe
she is 72 million i'd say probably
khalid
which is weird because he's like just a
homie of mine
and like i don't think women's anything
else scissor
i have millie bobby brown sabrina
claudio
oh bad baby lauren herrera osiris
wayleigh
rich the kid little zane gerber miguel
are you kidding me these are just people
that i've texted
it was at the crocodile in seattle and
it was like 500
i think that's what i said
[Music]
oh whoa
that's so cute um
whoo that was oh the best one i've had
was music midtown in atlanta
40 000 people such a dream oh my god
such a dream every time i go anywhere
hands down i might be safe if i go to
trader joe's
but everywhere else is kind of
get recognized which is actually really
cool but you know it's a lot
kind of a lot actually but like not a
ton it's kind of
like maybe like once a week um
i'm kind of jealous of billy a year ago
because i kind of i don't know i'm
really not about to pity myself
for people recognizing who i am which is
because it's like i'm really grateful
for it
but i don't know i i would like to go
to i don't know anywhere and not be
always recognized whoa
don't be so sad it's such a waste of
time
i didn't i didn't live up to that then
and i still haven't lived up to that
so it's good advice though it is a waste
of time dude
ah it's ruined so many things that could
have been amazing
because i was sad dumb but
whatever
[Music]
don't post everything you think
don't just don't if you're watching this
right now
anybody if anybody is watching this
don't
post your feelings don't
do it to yourself um
whoa tyler the creator
no i would love to meet i've not met him
oh my god i would explode if i met him i
met him
i met him and it was great
for me he hits a he hits a part of me
that nobody gets
being apple's up next artist
[Music]
i was such a baby
i did ellen last week jimmy fallon
lollapalooza
um so many festivals i went to tokyo
i met takashi murakami i went to his
studio
dave girl's daughter did a cover of my
song he played guitar for her at a
talent show
i think or something there's been a lot
of that's happened in the last year
my family i'm i'm always talking to my
family always
[Music]
every second of my life fruitville
station
uh fruitvale station
no uh you know what
no this i can't afford a real chain they
are real now they are real but it's all
silver
oh yeah my chains were gifts i did not
buy anything that i'm wearing
at all none of it
[Music]
i bought this though
[Music]
nah yes
yeah uh yep yeah
it's the kind of pressure that's like it
hits me and then i don't care
everybody drop dead right now and i
didn't
i would be left with what i had created
for myself
and what the hell would the point be if
i was just creating something that
somebody else wanted me to create that i
had no say in
and then that person died and everybody
else died and nobody mattered except me
i'm stuck with this i didn't want
in the first place that's trash
no i'm handling the pressure horribly
but i just keep it to myself
all the time except my wall i write
everything i feel on my wall so if you
go in my room look at my wall
just yeah no
i don't like dating at all i don't like
the idea of
oh this is my one person and i only
share time with this person no no
no no thank you
no i don't have a boyfriend i ca i could
not have a boyfriend that would just be
mean to him
uh i don't know i almost had one for
like a little but
it wasn't really exclusive so i don't
know what you'd call that i hate things
that are exclusive
never letting myself be mistreated
for a long long long long time
i had no idea what the was coming
not really uh yeah i was really
mistreated and then i just realized i
was better than that and since then
i just i feel like i've just grown to
know my worth
i think it's taken a minute and i don't
think i'm there yet but i'm
i'm getting there oh billy was so hurt
then
i was so hurt then man
i want to learn that it's all worth it
because it's tiring as heck
and it is worth it and i have to
remember that because
being with like fans and doing shows is
way more important than being tired
is it worth it
[Music]
yes
[Music]
the shows make it worth it the shows and
the supporters
that is something you have to remember
when it it doesn't feel worth it
because a lot of it doesn't feel worth
it but then you get to the points that
do make it worth it and it's like
then it all sort of makes sense and it
kind of clicks in your head no matter
what you do there's
you can never ever ever please anyone
ever
ever ever
facts still true never not true
any picture that is taken of you
if a picture is taken of you somebody
has it and somebody will use it against
you
i wasn't allowed to but i ran away from
security
and i ran into a huge crowd
i like slammed open a door into all of
them through a glass window and
hugged them all i almost caused a
stampede
by sneaking through a crowd at
lollapalooza
i almost died and everyone else almost
died
crazy whoa lil wayne
oh to perform with lil wayne that's a
great answer
wow 15 year old me was ballin i really
want to go to japan again
i went to japan a while ago and it was
the most amazing time
so i feel like brazil might be crazy
literally my first fan account was like
or like second panic it was like billy
island brazil
brockhampton tierra whack is sick
i like bright green a lot
i like black it's been pretty dark
lately so i've just wanted to be dark
with it
the world i mean
[Music]
i don't and then one word no
[Music]
judge me please
that's what i said
i still feel that way totally still feel
that way
but this year i guess i just don't
 know
i don't know what the is going on
i feel this and that i feel like
everything needs to have a certain this
is in this category and this isn't this
like it's like i want to be everything
like shut up
don't tell me what i can't be the hell
[Music]
the music industry man we're all sad as
hell
all these artists we're sad as dude
everybody i know that's an artist
we are sad
that's the way it is my what
what does that even mean what does that
mean everyone is gonna die and no one is
gonna remember you
so it what this said
that's my philosophy
having the approach that no one's had
trying to write something no one's
written
i don't know if that's the best approach
because you might just fail and then
want to die
like i have to write someone right
something no one's ever heard
see that's why i'm i'm still bad at it
because that's what i was trying to do
 you better know how to drive
because i've been putting off driver's
ed because that stuff stinks i hate that
stuff
i do know how to drive shorty well that
is crazy
this is my mom she is sick as a booty
and she has laryngitis as heck i still
love you
[Music]
[Applause]''')

interview2 = ('''my name is billy eilish billy eilish my
name is billy eilish my name is billy
eilish
my name is billy eilish
you're five
let's do this
i think it's october 18 2017. october
18th 2018. october 18th 2019 october 18
2020. the date is october 18
2021. i'm 15. i'm 16. i'm 17. i'm 18.
i'm 19.
i have 257
000. i have
6.3 million
40.7 million
67.5 million i have
94.1 million followers
the most followed person that follows me
is chloe grace moretz katy perry maybe
justin bieber ariana grande
kylie jenner
[Music]
million
it's way too many followers girl
but thanks for following me picture of
me and charlie xcx it's a picture of me
smiling when i
first posted a picture of my blonde hair
23 million 54 701
which is
ridiculous
public what is that
well
i
have not been in
at all um since
march
11th
before covet at all like i don't go in
public anyway just because it's a
complete disaster
gosh that girl
was going through an identity crisis oh
my gosh
you can see it in my eyes i mean really
the low bun
please what's going on my attitude used
to be well i can't go out you know i
can't go here i can't go there and i
used to just like not even be able to
like go to a park or like go
get food or get coffee i just it freaked
me out in the last year i have
been opened up
to it i really feel grateful for that
because being able to feel confident in
stepping outside without
a hat and a hood and glasses and a mask
and a jacket and doing this or whatever
it's so much better and you don't have
to live like that and i i realize that
this year that i don't have to live like
that per week if i
am going to stuff it's like anywhere i
go but
if i'm like being cautious and like not
trying to be
in everybody's faces it's like i can
manage
my way around people without them
noticing which is cool i didn't i didn't
used to be able to do that because my
pride was too huge i was like i only
want to be seen if i look like myself
so i would like never wear anything
normal i would wear like
full on like all of the jewelry that i
owned and my hair is blonde now so it's
not like the only person you've ever
seen with green hair walking by and so
who could it be out of the five people
it's gotten a lot easier but if i go out
i mean it's always gonna happen it's
just that i'm first of all fine with it
and i'm i'm very happy about it and also
i just know how to do it now
judge me please
i don't and then one word no
it's my style
billy eilish parody
is my style
i'm so much more open to stuff now so i
guess i would say like
anything
goes any being one word thing being the
second word and then goes
period i did that vogue cover and it was
a genre that we were doing a shoot for
it was a an old kind of hollywood
lingerie
kind of classic
thing
and it was supposed to be like a
specific aesthetic for a photo shoot and
then it was like billy eilish's new
style and then people kept being like
wow her new style like wow it's so much
better than the old style or like wow i
wish that we could have our old style
back i'm so sad that she's
just changed into this and it was so
weird cause i was like it's not a new
style it's
one thing i wore and then i'm gonna wear
this another day and then i'm gonna do
this and literally the thing that i've
been preaching about since i first
started
is
wear what you want
dress how you want act how you want talk
how you want be how you want
that's all i've ever said it's just
being open to new things and not
you know
letting people
ruin it for you i am
for sure a billion times more confident
confident than both of those years
i feel like i'm probably the most
confident i've ever been in my life
that's true
uh yeah no nothing will ever top that
2019
ego
i was feeling myself that is for sure
it's because i had been so miserable for
so long that i finally wasn't and i just
never shut up about it but i've been
i've been good i've been good i mean i'm
starting to have like an adulthood
which is new for me
and
very exciting and i
have had new experiences and new people
and
lots of love
i don't feel
like i do
yes
yeah
uh yep
yeah
but i don't care i really don't
care like it's like
it's the kind of pressure that sounds
like it's me and then i don't care
like i know
and like it's in my brain that people
expect a lot from me and that they
expect this and they want me to do this
and this is just me trying to convince
myself that i didn't care
every single one
every single one i know that i cared and
i was just literally coming up with some
stupid quote that would make me pretend
that i didn't care 80 000 people is way
easier than performing in front of eight
people that's true i used to be just
filled with these like inspirational
quotes just like ready to go all the
time
that i didn't even agree with most of
the time kind of crazy every time i see
an interview from that period when i was
like 16 i'm like
everything i said was so stupid like not
even stupid it just was like not what i
was actually thinking i was thinking
like i'm overwhelmed i hate this
everybody expects something from me i
don't have anything to give them i
 suck
my jewelry is cool
i want tattoos i want a car that's all i
was thinking like i was not thinking
that stuff
i feel a lot of pressure but i also
would say like
back then
i was more loved
i was pretty i was pretty overall like
loved i would say to be honest
and
so i was like scared because i really
wanted to keep that love
and now like tons of people hate me so
i'm not worried anymore i'm like oh okay
well
if you like me like maybe you don't you
don't so
there are things that i regret but i
don't know if i would
change them because everything that
happened that i regret like made me the
way i am and like everybody says that
and it's pretty cliche but it's pretty
true so
i don't know i feel like every situation
that i've been in where
you know maybe i wasn't being the best
that i could i think i learned from it
see
one of those
just another one of those stupid little
oh i'm really smart
and i really know
of course i had regard to regrets dude
don't be so sad it's such a waste of
time
[Music]
don't
post everything you think
this poor kid
oh my god
don't take
anything for granted don't ever come off
stage during this year and think
i didn't really like that show i didn't
really nope
nope
and by the way i'm never doing that
again when shows are allowed i'm
every show is gonna be the best show
i've ever done oh boy you know what's
funny it's so funny how
fast we get used to things it's kind of
scary because you think you know when
you don't have something you think like
oh my god when i have that in front of
me i'm not even gonna get used to it
it's gonna be so exciting and new and
it's exciting for like two seconds and
then it's not and it's super weird i
don't mean shows i just mean everything
in general it takes one second to get
used to stuff
because that's what we're
we're meant to do is adapt i wish that i
could actually tell that year ago billy
because boy was i
suffering not playing shows and not
seeing fans in real life and
you know being able to actually be with
them for real and not through a screen
so it's been amazing but it's so crazy
how fast i just like picked it all right
back up you know i feel like everything
is permanent all the time and it's not
things go in waves and things happen and
things stop and they start and it's like
you you just have no idea what's to come
ever and i think just try to be aware of
the amazing things you have going on
right in the moment instead of
later because even though then you know
i felt like
a year ago now like nothing was good and
and
i had nothing i like to do and there was
nothing that was
and there was so many things that now i
look back and i'm like ah that was cool
and it's just so weird that we don't
realize what's in front of us at all
until it's not it's very weird
my family i'm i'm always talking to my
family always
every second in my life my mom and dad
still come on tour with me finney still
comes on tour with me every day
pretty much every day we're always
together always talking always you know
whatever it's great i love my family i
am so lucky to have my family right now
both of my parents every day for sure i
mean i guess some days go by when i
don't but pretty much every single day
and like phineas pretty much every day
again some days go by right now but
my family is still just as involved as
they have always been in in all the good
ways
i love my family dearly
from fruitvale station
it'll always be up there but i
recently saw a movie called i origins
which was so
so good
i had no idea what it was and i just
finished showed it to me randomly in the
airport and i just it was amazing
five grammys
one two three four
five
six seven
performed at the oscars met like every
celebrity that's ever existed and it was
the most overwhelming insane surreal
thing i've ever experienced i went to
the brits i won a brit it was amazing i
performed
we recorded the bond theme song and
working with hans zimmer and the
orchestra to record it and completely
surreal and amazing
gosh it's been a crazy couple of years
man
i
made an album
i put out an album i did get two more
grammys the documentary came out that
was terrifying went to the bond premiere
in london which was amazing i've never
seen something so crazy i met the royal
family i put out a book i did an amazon
special i put out a movie with disney
which was called a love letter to los
angeles which was amazing
i'm launching a fragrance
which is the most exciting thing to me
no disrespect to all the other things
i've accomplished but
that's very exciting
i was a
host at the met gala
which was
an unbelievable
opportunity
thing i got to do and i wore a big
beautiful dress made by oscar de la
renta
who i
said at the beginning of the
conversation of let's make a miguel
address
you have to stop using fur
because if you don't i'm not working
with you that was also thanks to my mom
for
being with me on that one and and
fighting for it with me so uh
i got oscar de la renta to stop using
fur
completely and that was a really really
big
big thing for me and i i
hope that
more
brands
um follow along with being
environmentally conscious and
try to help the world instead of
make it worse so
yeah
the shows are like the one thing that i
feel like
i've ever been good at i know that
sounds stupid but it's like the only
thing i've ever done that made me feel
like
i belonged
keeping my family safe
and
you know
staying up
cute thing to say
i second that
for sure
i
was really just falling apart not being
able to do shows because
they are the thing that makes me feel
the best that i am
it it feels like the best that i can be
when i'm on stage and getting to do that
again i was like rewound
like i'm a music box that i can be in a
bad mood before a show and then
come off stage and i'm completely
rejuvenated it like winds me up it's
crazy so yeah i agree with that one i've
had some conversations with bieber about
this ariana's been really cool about
stuff even like katy perry told me that
i could reach out to her whenever gaga
has said it to me before it's you know
it's nice to to hear from people that
like have gone through this and know
what it's like
i guess i turned to my mom honestly the
most
in this in this period i feel like
no matter
all the people that have you know
similar things that i've been through or
have similar lifestyles or have
you know advice to give i feel like my
mom still beats them all
even though she's new to this just as i
am
you know meaning fame and
this kind of world but
my mom has a very good way of looking at
the world and she's the main person that
i i go to and
like literally like the almost the only
person
so
my mom
[Music]
face recognition like there's no home
button what the heck they've made
monograms crazy what the hell is a
monogram a hologram is what i meant it's
crazy that you can charge your phone by
like putting it on that little disc
robots doing stuff
the vaccine dude hell yeah i
really
really urge you if you are not already
vaccinated please get vaccinated it's
not just for you you selfish it's
for everyone around you take care of the
people around you man
protect your friends protect your
children protect your grandparents
protect
anyone you walk by
brockhampton tierra whack is sick my
favorite artist is techno i've been
loving some arlo parks
my favorite artist at the moment is
the doe
who like changed my life and perspective
on music
last year it was like one of their
albums i think they only have two albums
one is called
a mouthful and one is called shake shook
shaken shake shake shaken was my
main
source of inspiration
during the making of happier than ever
the album
last year all summer i would just listen
to it to and from phineas house when we
would make the album and then i'd
drive around and i'd go swimming and i'd
play it and it like changed my life that
album and it still does and a mouthful
has also changed my life as of this week
my brother is my best friend my brother
is my best friend my best friend is
phineas
but he is also my brother we got drew we
got zoe we got laura we got shark
we got my family my brother
those is my best friends
i got a lot of good friends
phineas is
definitely one of my best friends
my mom my dad
blank blank blank blank blank blank
blank
are the other best friends
a tattoo maybe
no face tattoos
the only two tattoos i want to get are
the ones that barely anyone could see
i did get a tattoo
but you won't ever see it light again
i have three tattoos now
i have one here
that says eilish
yes i love myself i have one here big
boy here which is a dragon and then i
just got this a few weeks ago which is
some fairies
that are from a book that i had growing
up
a little fairy book called feriapolis
they're like my little
guardian angel fairies i love tattoos my
mom is her hands on her head look at the
way she's sitting rude mom be supportive
my mom hates tattoos no i'm not gonna be
all tatted up but i you know have some
more ideas right now i feel i feel
pretty satisfied
i feel like in a good zone with them i
felt the urge for a while and now i'm
like ah
give me a little more time and then i'll
get another one but i got the dragon
right after last year's all i had at the
last one was this little guy
soda did this one lucy did this one
dragon did this one
amazing people
first thing that came to mind is like
when it's when my feet are close to the
bottom of the bed
that's the scariest part of my day every
day
i jump from like two feet away from my
bed onto the bed and if my feet
are too close to the bottom uh under my
bed i go
like i can't help myself by gag it's
disgusting it creeps me out oh it creeps
me out so much
that's why i like all the furniture at
my house there's nothing underneath i
they all go to the ground i made that
very very clear when i was getting all
my furniture i was like
please don't get anything with space
underneath so all my chairs my couches
my bed frame it all goes all the way to
the ground there's no storage i don't i
would rather lose the storage space
under my bed
than have to step next to the bottom of
my bed
dead ass
i don't really get scared of like
scary things you know like i had a huge
anaconda literally almost choked me to
death
that was so much fun
so much fun i guess that
what is the scariest thing i've ever
done
fallen in love
what
my relationships
bring me a lot of joy babs bring me a
lot of joy like the things that like
just automatically bring me joy are
rain
and clouds and like
mist and fog like these things aren't
they they just i feel happy i have
seasonal affective disorder but the
opposite where i am i am so happy in
gloomy weather and i am pretty miserable
in hot
sunny blue sky weather i
very seriously i i find myself
pretty depressed in the summertime just
because of the weather
and other things but just that's like
the that's initially the thing
yeah
being on stage makes me feel incredibly
powerful there's a part in my show where
i
get on a
lift
that like takes me over the crowd and i
like lean over the edge and look down
and that is a
kind of power that no one should feel
whoosh it makes me feel literally
invincible it's crazy i don't know
clothing
like
clothing makes you feel powerful and it
can also make you feel very very weak
so that's that's a big thing
little things man
oh do i feel grown up for the most part
yeah i feel like i've
felt very grown up this year and i
really like it i like
growing up a lot
i loved being young and i still am young
but i i loved being a teenager and i
kind of have always dreaded growing up
and getting older and it's always been
really scary to me but i've
enjoyed the hell out of it i love it i
love being able to do things on my own
and
have my own freedom and my own choices
and my own
you know right to things it's very
exciting
my mommy come here this is my mom she is
sick as a booty i don't mind i can stay
here that long
i love it
hello baby his grandma
i love you so much i love you so much
come here
join me
i love you billy
my sweet mama
love you dearly we don't have the idiot
dog with us this year i love watching
you do this every year he's at home
farting
stinking up the yard love you too
love you
honey
you're funny
peace
[Music]
you
my name is billy eilish billy eilish my
name is billy eilish my name is billy
eilish
my name is billy eilish
you're five
let's do this
i think it's october 18 2017. october
18th 2018. october 18th 2019 october 18
2020. the date is october 18
2021. i'm 15. i'm 16. i'm 17. i'm 18.
i'm 19.
i have 257
000. i have
6.3 million
40.7 million
67.5 million i have
94.1 million followers
the most followed person that follows me
is chloe grace moretz katy perry maybe
justin bieber ariana grande
kylie jenner
[Music]
million
it's way too many followers girl
but thanks for following me picture of
me and charlie xcx it's a picture of me
smiling when i
first posted a picture of my blonde hair
23 million 54 701
which is
ridiculous
public what is that
well
i
have not been in
at all um since
march
11th
before covet at all like i don't go in
public anyway just because it's a
complete disaster
gosh that girl
was going through an identity crisis oh
my gosh
you can see it in my eyes i mean really
the low bun
please what's going on my attitude used
to be well i can't go out you know i
can't go here i can't go there and i
used to just like not even be able to
like go to a park or like go
get food or get coffee i just it freaked
me out in the last year i have
been opened up
to it i really feel grateful for that
because being able to feel confident in
stepping outside without
a hat and a hood and glasses and a mask
and a jacket and doing this or whatever
it's so much better and you don't have
to live like that and i i realize that
this year that i don't have to live like
that per week if i
am going to stuff it's like anywhere i
go but
if i'm like being cautious and like not
trying to be
in everybody's faces it's like i can
manage
my way around people without them
noticing which is cool i didn't i didn't
used to be able to do that because my
pride was too huge i was like i only
want to be seen if i look like myself
so i would like never wear anything
normal i would wear like
full on like all of the jewelry that i
owned and my hair is blonde now so it's
not like the only person you've ever
seen with green hair walking by and so
who could it be out of the five people
it's gotten a lot easier but if i go out
i mean it's always gonna happen it's
just that i'm first of all fine with it
and i'm i'm very happy about it and also
i just know how to do it now
judge me please
i don't and then one word no
it's my style
billy eilish parody
is my style
i'm so much more open to stuff now so i
guess i would say like
anything
goes any being one word thing being the
second word and then goes
period i did that vogue cover and it was
a genre that we were doing a shoot for
it was a an old kind of hollywood
lingerie
kind of classic
thing
and it was supposed to be like a
specific aesthetic for a photo shoot and
then it was like billy eilish's new
style and then people kept being like
wow her new style like wow it's so much
better than the old style or like wow i
wish that we could have our old style
back i'm so sad that she's
just changed into this and it was so
weird cause i was like it's not a new
style it's
one thing i wore and then i'm gonna wear
this another day and then i'm gonna do
this and literally the thing that i've
been preaching about since i first
started
is
wear what you want
dress how you want act how you want talk
how you want be how you want
that's all i've ever said it's just
being open to new things and not
you know
letting people
ruin it for you i am
for sure a billion times more confident
confident than both of those years
i feel like i'm probably the most
confident i've ever been in my life
that's true
uh yeah no nothing will ever top that
2019
ego
i was feeling myself that is for sure
it's because i had been so miserable for
so long that i finally wasn't and i just
never shut up about it but i've been
i've been good i've been good i mean i'm
starting to have like an adulthood
which is new for me
and
very exciting and i
have had new experiences and new people
and
lots of love
i don't feel
like i do
yes
yeah
uh yep
yeah
but i don't care i really don't
care like it's like
it's the kind of pressure that sounds
like it's me and then i don't care
like i know
and like it's in my brain that people
expect a lot from me and that they
expect this and they want me to do this
and this is just me trying to convince
myself that i didn't care
every single one
every single one i know that i cared and
i was just literally coming up with some
stupid quote that would make me pretend
that i didn't care 80 000 people is way
easier than performing in front of eight
people that's true i used to be just
filled with these like inspirational
quotes just like ready to go all the
time
that i didn't even agree with most of
the time kind of crazy every time i see
an interview from that period when i was
like 16 i'm like
everything i said was so stupid like not
even stupid it just was like not what i
was actually thinking i was thinking
like i'm overwhelmed i hate this
everybody expects something from me i
don't have anything to give them i
 suck
my jewelry is cool
i want tattoos i want a car that's all i
was thinking like i was not thinking
that stuff
i feel a lot of pressure but i also
would say like
back then
i was more loved
i was pretty i was pretty overall like
loved i would say to be honest
and
so i was like scared because i really
wanted to keep that love
and now like tons of people hate me so
i'm not worried anymore i'm like oh okay
well
if you like me like maybe you don't you
don't so
there are things that i regret but i
don't know if i would
change them because everything that
happened that i regret like made me the
way i am and like everybody says that
and it's pretty cliche but it's pretty
true so
i don't know i feel like every situation
that i've been in where
you know maybe i wasn't being the best
that i could i think i learned from it
see
one of those
just another one of those stupid little
oh i'm really smart
and i really know
of course i had regard to regrets dude
don't be so sad it's such a waste of
time
[Music]
don't
post everything you think
this poor kid
oh my god
don't take
anything for granted don't ever come off
stage during this year and think
i didn't really like that show i didn't
really nope
nope
and by the way i'm never doing that
again when shows are allowed i'm
every show is gonna be the best show
i've ever done oh boy you know what's
funny it's so funny how
fast we get used to things it's kind of
scary because you think you know when
you don't have something you think like
oh my god when i have that in front of
me i'm not even gonna get used to it
it's gonna be so exciting and new and
it's exciting for like two seconds and
then it's not and it's super weird i
don't mean shows i just mean everything
in general it takes one second to get
used to stuff
because that's what we're
we're meant to do is adapt i wish that i
could actually tell that year ago billy
because boy was i
suffering not playing shows and not
seeing fans in real life and
you know being able to actually be with
them for real and not through a screen
so it's been amazing but it's so crazy
how fast i just like picked it all right
back up you know i feel like everything
is permanent all the time and it's not
things go in waves and things happen and
things stop and they start and it's like
you you just have no idea what's to come
ever and i think just try to be aware of
the amazing things you have going on
right in the moment instead of
later because even though then you know
i felt like
a year ago now like nothing was good and
and
i had nothing i like to do and there was
nothing that was
and there was so many things that now i
look back and i'm like ah that was cool
and it's just so weird that we don't
realize what's in front of us at all
until it's not it's very weird
my family i'm i'm always talking to my
family always
every second in my life my mom and dad
still come on tour with me finney still
comes on tour with me every day
pretty much every day we're always
together always talking always you know
whatever it's great i love my family i
am so lucky to have my family right now
both of my parents every day for sure i
mean i guess some days go by when i
don't but pretty much every single day
and like phineas pretty much every day
again some days go by right now but
my family is still just as involved as
they have always been in in all the good
ways
i love my family dearly
from fruitvale station
it'll always be up there but i
recently saw a movie called i origins
which was so
so good
i had no idea what it was and i just
finished showed it to me randomly in the
airport and i just it was amazing
five grammys
one two three four
five
six seven
performed at the oscars met like every
celebrity that's ever existed and it was
the most overwhelming insane surreal
thing i've ever experienced i went to
the brits i won a brit it was amazing i
performed
we recorded the bond theme song and
working with hans zimmer and the
orchestra to record it and completely
surreal and amazing
gosh it's been a crazy couple of years
man
i
made an album
i put out an album i did get two more
grammys the documentary came out that
was terrifying went to the bond premiere
in london which was amazing i've never
seen something so crazy i met the royal
family i put out a book i did an amazon
special i put out a movie with disney
which was called a love letter to los
angeles which was amazing
i'm launching a fragrance
which is the most exciting thing to me
no disrespect to all the other things
i've accomplished but
that's very exciting
i was a
host at the met gala
which was
an unbelievable
opportunity
thing i got to do and i wore a big
beautiful dress made by oscar de la
renta
who i
said at the beginning of the
conversation of let's make a miguel
address
you have to stop using fur
because if you don't i'm not working
with you that was also thanks to my mom
for
being with me on that one and and
fighting for it with me so uh
i got oscar de la renta to stop using
fur
completely and that was a really really
big
big thing for me and i i
hope that
more
brands
um follow along with being
environmentally conscious and
try to help the world instead of
make it worse so
yeah
the shows are like the one thing that i
feel like
i've ever been good at i know that
sounds stupid but it's like the only
thing i've ever done that made me feel
like
i belonged
keeping my family safe
and
you know
staying up
cute thing to say
i second that
for sure
i
was really just falling apart not being
able to do shows because
they are the thing that makes me feel
the best that i am
it it feels like the best that i can be
when i'm on stage and getting to do that
again i was like rewound
like i'm a music box that i can be in a
bad mood before a show and then
come off stage and i'm completely
rejuvenated it like winds me up it's
crazy so yeah i agree with that one i've
had some conversations with bieber about
this ariana's been really cool about
stuff even like katy perry told me that
i could reach out to her whenever gaga
has said it to me before it's you know
it's nice to to hear from people that
like have gone through this and know
what it's like
i guess i turned to my mom honestly the
most
in this in this period i feel like
no matter
all the people that have you know
similar things that i've been through or
have similar lifestyles or have
you know advice to give i feel like my
mom still beats them all
even though she's new to this just as i
am
you know meaning fame and
this kind of world but
my mom has a very good way of looking at
the world and she's the main person that
i i go to and
like literally like the almost the only
person
so
my mom
[Music]
face recognition like there's no home
button what the heck they've made
monograms crazy what the hell is a
monogram a hologram is what i meant it's
crazy that you can charge your phone by
like putting it on that little disc
robots doing stuff
the vaccine dude hell yeah i
really
really urge you if you are not already
vaccinated please get vaccinated it's
not just for you you selfish it's
for everyone around you take care of the
people around you man
protect your friends protect your
children protect your grandparents
protect
anyone you walk by
brockhampton tierra whack is sick my
favorite artist is techno i've been
loving some arlo parks
my favorite artist at the moment is
the doe
who like changed my life and perspective
on music
last year it was like one of their
albums i think they only have two albums
one is called
a mouthful and one is called shake shook
shaken shake shake shaken was my
main
source of inspiration
during the making of happier than ever
the album
last year all summer i would just listen
to it to and from phineas house when we
would make the album and then i'd
drive around and i'd go swimming and i'd
play it and it like changed my life that
album and it still does and a mouthful
has also changed my life as of this week
my brother is my best friend my brother
is my best friend my best friend is
phineas
but he is also my brother we got drew we
got zoe we got laura we got shark
we got my family my brother
those is my best friends
i got a lot of good friends
phineas is
definitely one of my best friends
my mom my dad
blank blank blank blank blank blank
blank
are the other best friends
a tattoo maybe
no face tattoos
the only two tattoos i want to get are
the ones that barely anyone could see
i did get a tattoo
but you won't ever see it light again
i have three tattoos now
i have one here
that says eilish
yes i love myself i have one here big
boy here which is a dragon and then i
just got this a few weeks ago which is
some fairies
that are from a book that i had growing
up
a little fairy book called feriapolis
they're like my little
guardian angel fairies i love tattoos my
mom is her hands on her head look at the
way she's sitting rude mom be supportive
my mom hates tattoos no i'm not gonna be
all tatted up but i you know have some
more ideas right now i feel i feel
pretty satisfied
i feel like in a good zone with them i
felt the urge for a while and now i'm
like ah
give me a little more time and then i'll
get another one but i got the dragon
right after last year's all i had at the
last one was this little guy
soda did this one lucy did this one
dragon did this one
amazing people
first thing that came to mind is like
when it's when my feet are close to the
bottom of the bed
that's the scariest part of my day every
day
i jump from like two feet away from my
bed onto the bed and if my feet
are too close to the bottom uh under my
bed i go
like i can't help myself by gag it's
disgusting it creeps me out oh it creeps
me out so much
that's why i like all the furniture at
my house there's nothing underneath i
they all go to the ground i made that
very very clear when i was getting all
my furniture i was like
please don't get anything with space
underneath so all my chairs my couches
my bed frame it all goes all the way to
the ground there's no storage i don't i
would rather lose the storage space
under my bed
than have to step next to the bottom of
my bed
dead ass
i don't really get scared of like
scary things you know like i had a huge
anaconda literally almost choked me to
death
that was so much fun
so much fun i guess that
what is the scariest thing i've ever
done
fallen in love
what
my relationships
bring me a lot of joy babs bring me a
lot of joy like the things that like
just automatically bring me joy are
rain
and clouds and like
mist and fog like these things aren't
they they just i feel happy i have
seasonal affective disorder but the
opposite where i am i am so happy in
gloomy weather and i am pretty miserable
in hot
sunny blue sky weather i
very seriously i i find myself
pretty depressed in the summertime just
because of the weather
and other things but just that's like
the that's initially the thing
yeah
being on stage makes me feel incredibly
powerful there's a part in my show where
i
get on a
lift
that like takes me over the crowd and i
like lean over the edge and look down
and that is a
kind of power that no one should feel
whoosh it makes me feel literally
invincible it's crazy i don't know
clothing
like
clothing makes you feel powerful and it
can also make you feel very very weak
so that's that's a big thing
little things man
oh do i feel grown up for the most part
yeah i feel like i've
felt very grown up this year and i
really like it i like
growing up a lot
i loved being young and i still am young
but i i loved being a teenager and i
kind of have always dreaded growing up
and getting older and it's always been
really scary to me but i've
enjoyed the hell out of it i love it i
love being able to do things on my own
and
have my own freedom and my own choices
and my own
you know right to things it's very
exciting
my mommy come here this is my mom she is
sick as a booty i don't mind i can stay
here that long
i love it
hello baby his grandma
i love you so much i love you so much
come here
join me
i love you billy
my sweet mama
love you dearly we don't have the idiot
dog with us this year i love watching
you do this every year he's at home
farting
stinking up the yard love you too
love you
honey
you're funny
peace
[Music]
you
my name is billy eilish billy eilish my
name is billy eilish my name is billy
eilish
my name is billy eilish
you're five
let's do this
i think it's october 18 2017. october
18th 2018. october 18th 2019 october 18
2020. the date is october 18
2021. i'm 15. i'm 16. i'm 17. i'm 18.
i'm 19.
i have 257
000. i have
6.3 million
40.7 million
67.5 million i have
94.1 million followers
the most followed person that follows me
is chloe grace moretz katy perry maybe
justin bieber ariana grande
kylie jenner
[Music]
million
it's way too many followers girl
but thanks for following me picture of
me and charlie xcx it's a picture of me
smiling when i
first posted a picture of my blonde hair
23 million 54 701
which is
ridiculous
public what is that
well
i
have not been in
at all um since
march
11th
before covet at all like i don't go in
public anyway just because it's a
complete disaster
gosh that girl
was going through an identity crisis oh
my gosh
you can see it in my eyes i mean really
the low bun
please what's going on my attitude used
to be well i can't go out you know i
can't go here i can't go there and i
used to just like not even be able to
like go to a park or like go
get food or get coffee i just it freaked
me out in the last year i have
been opened up
to it i really feel grateful for that
because being able to feel confident in
stepping outside without
a hat and a hood and glasses and a mask
and a jacket and doing this or whatever
it's so much better and you don't have
to live like that and i i realize that
this year that i don't have to live like
that per week if i
am going to stuff it's like anywhere i
go but
if i'm like being cautious and like not
trying to be
in everybody's faces it's like i can
manage
my way around people without them
noticing which is cool i didn't i didn't
used to be able to do that because my
pride was too huge i was like i only
want to be seen if i look like myself
so i would like never wear anything
normal i would wear like
full on like all of the jewelry that i
owned and my hair is blonde now so it's
not like the only person you've ever
seen with green hair walking by and so
who could it be out of the five people
it's gotten a lot easier but if i go out
i mean it's always gonna happen it's
just that i'm first of all fine with it
and i'm i'm very happy about it and also
i just know how to do it now
judge me please
i don't and then one word no
it's my style
billy eilish parody
is my style
i'm so much more open to stuff now so i
guess i would say like
anything
goes any being one word thing being the
second word and then goes
period i did that vogue cover and it was
a genre that we were doing a shoot for
it was a an old kind of hollywood
lingerie
kind of classic
thing
and it was supposed to be like a
specific aesthetic for a photo shoot and
then it was like billy eilish's new
style and then people kept being like
wow her new style like wow it's so much
better than the old style or like wow i
wish that we could have our old style
back i'm so sad that she's
just changed into this and it was so
weird cause i was like it's not a new
style it's
one thing i wore and then i'm gonna wear
this another day and then i'm gonna do
this and literally the thing that i've
been preaching about since i first
started
is
wear what you want
dress how you want act how you want talk
how you want be how you want
that's all i've ever said it's just
being open to new things and not
you know
letting people
ruin it for you i am
for sure a billion times more confident
confident than both of those years
i feel like i'm probably the most
confident i've ever been in my life
that's true
uh yeah no nothing will ever top that
2019
ego
i was feeling myself that is for sure
it's because i had been so miserable for
so long that i finally wasn't and i just
never shut up about it but i've been
i've been good i've been good i mean i'm
starting to have like an adulthood
which is new for me
and
very exciting and i
have had new experiences and new people
and
lots of love
i don't feel
like i do
yes
yeah
uh yep
yeah
but i don't care i really don't
care like it's like
it's the kind of pressure that sounds
like it's me and then i don't care
like i know
and like it's in my brain that people
expect a lot from me and that they
expect this and they want me to do this
and this is just me trying to convince
myself that i didn't care
every single one
every single one i know that i cared and
i was just literally coming up with some
stupid quote that would make me pretend
that i didn't care 80 000 people is way
easier than performing in front of eight
people that's true i used to be just
filled with these like inspirational
quotes just like ready to go all the
time
that i didn't even agree with most of
the time kind of crazy every time i see
an interview from that period when i was
like 16 i'm like
everything i said was so stupid like not
even stupid it just was like not what i
was actually thinking i was thinking
like i'm overwhelmed i hate this
everybody expects something from me i
don't have anything to give them i
 suck
my jewelry is cool
i want tattoos i want a car that's all i
was thinking like i was not thinking
that stuff
i feel a lot of pressure but i also
would say like
back then
i was more loved
i was pretty i was pretty overall like
loved i would say to be honest
and
so i was like scared because i really
wanted to keep that love
and now like tons of people hate me so
i'm not worried anymore i'm like oh okay
well
if you like me like maybe you don't you
don't so
there are things that i regret but i
don't know if i would
change them because everything that
happened that i regret like made me the
way i am and like everybody says that
and it's pretty cliche but it's pretty
true so
i don't know i feel like every situation
that i've been in where
you know maybe i wasn't being the best
that i could i think i learned from it
see
one of those
just another one of those stupid little
oh i'm really smart
and i really know
of course i had regard to regrets dude
don't be so sad it's such a waste of
time
[Music]
don't
post everything you think
this poor kid
oh my god
don't take
anything for granted don't ever come off
stage during this year and think
i didn't really like that show i didn't
really nope
nope
and by the way i'm never doing that
again when shows are allowed i'm
every show is gonna be the best show
i've ever done oh boy you know what's
funny it's so funny how
fast we get used to things it's kind of
scary because you think you know when
you don't have something you think like
oh my god when i have that in front of
me i'm not even gonna get used to it
it's gonna be so exciting and new and
it's exciting for like two seconds and
then it's not and it's super weird i
don't mean shows i just mean everything
in general it takes one second to get
used to stuff
because that's what we're
we're meant to do is adapt i wish that i
could actually tell that year ago billy
because boy was i
suffering not playing shows and not
seeing fans in real life and
you know being able to actually be with
them for real and not through a screen
so it's been amazing but it's so crazy
how fast i just like picked it all right
back up you know i feel like everything
is permanent all the time and it's not
things go in waves and things happen and
things stop and they start and it's like
you you just have no idea what's to come
ever and i think just try to be aware of
the amazing things you have going on
right in the moment instead of
later because even though then you know
i felt like
a year ago now like nothing was good and
and
i had nothing i like to do and there was
nothing that was
and there was so many things that now i
look back and i'm like ah that was cool
and it's just so weird that we don't
realize what's in front of us at all
until it's not it's very weird
my family i'm i'm always talking to my
family always
every second in my life my mom and dad
still come on tour with me finney still
comes on tour with me every day
pretty much every day we're always
together always talking always you know
whatever it's great i love my family i
am so lucky to have my family right now
both of my parents every day for sure i
mean i guess some days go by when i
don't but pretty much every single day
and like phineas pretty much every day
again some days go by right now but
my family is still just as involved as
they have always been in in all the good
ways
i love my family dearly
from fruitvale station
it'll always be up there but i
recently saw a movie called i origins
which was so
so good
i had no idea what it was and i just
finished showed it to me randomly in the
airport and i just it was amazing
five grammys
one two three four
five
six seven
performed at the oscars met like every
celebrity that's ever existed and it was
the most overwhelming insane surreal
thing i've ever experienced i went to
the brits i won a brit it was amazing i
performed
we recorded the bond theme song and
working with hans zimmer and the
orchestra to record it and completely
surreal and amazing
gosh it's been a crazy couple of years
man
i
made an album
i put out an album i did get two more
grammys the documentary came out that
was terrifying went to the bond premiere
in london which was amazing i've never
seen something so crazy i met the royal
family i put out a book i did an amazon
special i put out a movie with disney
which was called a love letter to los
angeles which was amazing
i'm launching a fragrance
which is the most exciting thing to me
no disrespect to all the other things
i've accomplished but
that's very exciting
i was a
host at the met gala
which was
an unbelievable
opportunity
thing i got to do and i wore a big
beautiful dress made by oscar de la
renta
who i
said at the beginning of the
conversation of let's make a miguel
address
you have to stop using fur
because if you don't i'm not working
with you that was also thanks to my mom
for
being with me on that one and and
fighting for it with me so uh
i got oscar de la renta to stop using
fur
completely and that was a really really
big
big thing for me and i i
hope that
more
brands
um follow along with being
environmentally conscious and
try to help the world instead of
make it worse so
yeah
the shows are like the one thing that i
feel like
i've ever been good at i know that
sounds stupid but it's like the only
thing i've ever done that made me feel
like
i belonged
keeping my family safe
and
you know
staying up
cute thing to say
i second that
for sure
i
was really just falling apart not being
able to do shows because
they are the thing that makes me feel
the best that i am
it it feels like the best that i can be
when i'm on stage and getting to do that
again i was like rewound
like i'm a music box that i can be in a
bad mood before a show and then
come off stage and i'm completely
rejuvenated it like winds me up it's
crazy so yeah i agree with that one i've
had some conversations with bieber about
this ariana's been really cool about
stuff even like katy perry told me that
i could reach out to her whenever gaga
has said it to me before it's you know
it's nice to to hear from people that
like have gone through this and know
what it's like
i guess i turned to my mom honestly the
most
in this in this period i feel like
no matter
all the people that have you know
similar things that i've been through or
have similar lifestyles or have
you know advice to give i feel like my
mom still beats them all
even though she's new to this just as i
am
you know meaning fame and
this kind of world but
my mom has a very good way of looking at
the world and she's the main person that
i i go to and
like literally like the almost the only
person
so
my mom
[Music]
face recognition like there's no home
button what the heck they've made
monograms crazy what the hell is a
monogram a hologram is what i meant it's
crazy that you can charge your phone by
like putting it on that little disc
robots doing stuff
the vaccine dude hell yeah i
really
really urge you if you are not already
vaccinated please get vaccinated it's
not just for you you selfish it's
for everyone around you take care of the
people around you man
protect your friends protect your
children protect your grandparents
protect
anyone you walk by
brockhampton tierra whack is sick my
favorite artist is techno i've been
loving some arlo parks
my favorite artist at the moment is
the doe
who like changed my life and perspective
on music
last year it was like one of their
albums i think they only have two albums
one is called
a mouthful and one is called shake shook
shaken shake shake shaken was my
main
source of inspiration
during the making of happier than ever
the album
last year all summer i would just listen
to it to and from phineas house when we
would make the album and then i'd
drive around and i'd go swimming and i'd
play it and it like changed my life that
album and it still does and a mouthful
has also changed my life as of this week
my brother is my best friend my brother
is my best friend my best friend is
phineas
but he is also my brother we got drew we
got zoe we got laura we got shark
we got my family my brother
those is my best friends
i got a lot of good friends
phineas is
definitely one of my best friends
my mom my dad
blank blank blank blank blank blank
blank
are the other best friends
a tattoo maybe
no face tattoos
the only two tattoos i want to get are
the ones that barely anyone could see
i did get a tattoo
but you won't ever see it light again
i have three tattoos now
i have one here
that says eilish
yes i love myself i have one here big
boy here which is a dragon and then i
just got this a few weeks ago which is
some fairies
that are from a book that i had growing
up
a little fairy book called feriapolis
they're like my little
guardian angel fairies i love tattoos my
mom is her hands on her head look at the
way she's sitting rude mom be supportive
my mom hates tattoos no i'm not gonna be
all tatted up but i you know have some
more ideas right now i feel i feel
pretty satisfied
i feel like in a good zone with them i
felt the urge for a while and now i'm
like ah
give me a little more time and then i'll
get another one but i got the dragon
right after last year's all i had at the
last one was this little guy
soda did this one lucy did this one
dragon did this one
amazing people
first thing that came to mind is like
when it's when my feet are close to the
bottom of the bed
that's the scariest part of my day every
day
i jump from like two feet away from my
bed onto the bed and if my feet
are too close to the bottom uh under my
bed i go
like i can't help myself by gag it's
disgusting it creeps me out oh it creeps
me out so much
that's why i like all the furniture at
my house there's nothing underneath i
they all go to the ground i made that
very very clear when i was getting all
my furniture i was like
please don't get anything with space
underneath so all my chairs my couches
my bed frame it all goes all the way to
the ground there's no storage i don't i
would rather lose the storage space
under my bed
than have to step next to the bottom of
my bed
dead ass
i don't really get scared of like
scary things you know like i had a huge
anaconda literally almost choked me to
death
that was so much fun
so much fun i guess that
what is the scariest thing i've ever
done
fallen in love
what
my relationships
bring me a lot of joy babs bring me a
lot of joy like the things that like
just automatically bring me joy are
rain
and clouds and like
mist and fog like these things aren't
they they just i feel happy i have
seasonal affective disorder but the
opposite where i am i am so happy in
gloomy weather and i am pretty miserable
in hot
sunny blue sky weather i
very seriously i i find myself
pretty depressed in the summertime just
because of the weather
and other things but just that's like
the that's initially the thing
yeah
being on stage makes me feel incredibly
powerful there's a part in my show where
i
get on a
lift
that like takes me over the crowd and i
like lean over the edge and look down
and that is a
kind of power that no one should feel
whoosh it makes me feel literally
invincible it's crazy i don't know
clothing
like
clothing makes you feel powerful and it
can also make you feel very very weak
so that's that's a big thing
little things man
oh do i feel grown up for the most part
yeah i feel like i've
felt very grown up this year and i
really like it i like
growing up a lot
i loved being young and i still am young
but i i loved being a teenager and i
kind of have always dreaded growing up
and getting older and it's always been
really scary to me but i've
enjoyed the hell out of it i love it i
love being able to do things on my own
and
have my own freedom and my own choices
and my own
you know right to things it's very
exciting
my mommy come here this is my mom she is
sick as a booty i don't mind i can stay
here that long
i love it
hello baby his grandma
i love you so much i love you so much
come here
join me
i love you billy
my sweet mama
love you dearly we don't have the idiot
dog with us this year i love watching
you do this every year he's at home
farting
stinking up the yard love you too
love you
honey
you're funny
peace
[Music]
you''')

song1A1 =  ('''"White shirt now red, my bloody nose Sleepin', you're on your tippy toes Creepin' around like no one knows Think you're so criminal Bruises on both my knees for you Don't say thank you or please I do what I want when I'm wanting to My soul? So cynical   So you're a tough guy Like it really rough guy Just can't get enough guy Chest always so puffed guy I'm that bad type Make your mama sad type Make your girlfriend mad tight Might seduce your dad type I'm the bad guy Duh [Post-Chorus] I'm the bad guy   I like it when you take control Even if you know that you don't Own me, I'll let you play the role I'll be your animal My mommy likes to sing along with me But she won't sing this song If she reads all the lyrics She'll pity the men I know   So you're a tough guy Like it really rough guy Just can't get enough guy Chest always so puffed guy I'm that bad type Make your mama sad type Make your girlfriend mad tight Might seduce your dad type I'm the bad guy Duh  [Post-Chorus] I'm the bad guy, duh I'm only good at bein' bad, bad You might also like[Bridge] I like when you get mad I guess I'm pretty glad that you're alone You said she's scared of me? I mean, I don't see what she sees But maybe it's 'cause I'm wearing your cologne  [Outro] I'm a bad guy I'm, I'm a bad guy Bad guy, bad guy I'm a bad"''')
song2A1 =  ('''"What is it about them? I must be missing something They just keep doing nothing Too intoxicated to be scared Better off without them They're nothing but unstable Bring ashtrays to the table And that's about the only thing they share   I'm in their secondhand smoke Still just drinking canned Coke I don't need a Xanny to feel better On designated drives home Only one who's not stoned Don't give me a Xanny, now or ever [Interlude] Can you check your Uber rating? Oh my god (And it's like, wait, like, when?)   Wakin' up at sundown (Ooh) They're late to every party (Ooh) Nobody's ever sorry (Ooh) Too inebriated now to dance Morning as they come down (Come down) Their pretty heads are hurting (Hurting) They're awfully bad at learning (Learning) Make the same mistakes, blame circumstance   I'm in their secondhand smoke Still just drinking canned Coke I don't need a Xanny to feel better On designated drives home Only one who's not stoned Don't give me a Xanny, now or ever  [Bridge] Please don't try to kiss me on the sidewalk On your cigarette break I can't afford to love someone Who isn't dying by mistake in Silver Lake You might also like[Outro] What is it about them? I must be missing something They just keep doin' nothing Too intoxicated to be scared Hmm, hmm Hmm, mmm, mmm, mmm, mmm Come down Hurting Learning"''')
song3A1 =  ('''"Bite my tongue, bide my time Wearing a warning sign Wait 'til the world is mine Visions I vandalize Cold in my kingdom size Fell for these ocean eyes   You should see me in a crown I'm gonna run this nothing town Watch me make 'em bow One by one by one One by one by You should see me in a crown Your silence is my favorite sound Watch me make 'em bow One by one by one One by one by one  Count my cards, watch them fall Blood on a marble wall I like the way they all scream Tell me which one is worse Living or dying first Sleeping inside a hearse (I don't dream)  [Bridge] You say, ""Come over, baby I think you're pretty"" I'm okay, I'm not your baby If you think I'm pretty   You should see me in a crown I'm gonna run this nothing town Watch me make 'em bow One by one by one One by one by You should see me in a crown Your silence is my favorite sound Watch me make 'em bow One by one by one One by one by one You might also like[Instrumental Break]   Crown I'm gonna run this nothing town Watch me make 'em bow One by one by one One by one by You should see me in a crown (You should see me, see me) Your silence is my favorite sound (You should see me, see me) Watch me make 'em bow One by one by one One by one by one"''')
song4A1 =  ('''"My Lucifer is lonely   Standing there, killing time Can't commit to anything but a crime Peter's on vacation, an open invitation Animals, evidence Pearly Gates look more like a picket fence Once you get inside 'em Got friends but can't invite them [Pre-Chorus] Hills burn in California My turn to ignore ya Don't say I didn't warn ya   All the good girls go to Hell 'Cause even God herself has enemies And once the water starts to rise And Heaven's out of sight She'll want the Devil on her team  [Post-Chorus] My Lucifer is lonely  Look at you needing me You know I'm not your friend without some greenery Walk in wearin' fetters Peter should know better Your cover up is caving in Man is such a fool, why are we saving him? Poisoning themselves now Begging for our help, wow [Pre-Chorus] Hills burn in California My turn to ignore ya Don't say I didn't warn ya You might also like All the good girls go to Hell (All the good girls go to Hell) 'Cause even God herself (God herself) has enemies And once the water starts to rise (Water starts to rise) And Heaven's out of sight She'll want the Devil on her team  [Post-Chorus] My Lucifer is lonely There's nothing left to save now My god is gonna owe me There's nothing left to save now  [Outro] Haha! I cannot do the snowflake"''')
song5A1 =  ('''"Baby, I don't feel so good,"" six words you never understood ""I'll never let you go,"" five words you'll never say (Aww) I laugh along like nothing's wrong, four days has never felt so long If three's a crowd and two was us, one slipped away (Hahahahahahahaha)   I just wanna make you feel okay But all you do is look the other way I can't tell you how much I wish I didn't wanna stay I just kinda wish you were gay  Is there a reason we're not through? Is there a 12 step just for you? Our conversation's all in blue 11 ""heys"" (Hey, hey, hey, hey) Ten fingers tearin' out my hair Nine times you never made it there I ate alone at 7, you were six minutes away (Yay)   How am I supposed to make you feel okay When all you do is walk the other way? I can't tell you how much I wish I didn't wanna stay I just kinda wish you were gay [Bridge] To spare my pride To give your lack of interest an explanation Don't say I'm not your type Just say that I'm not your preferred sexual orientation I'm so selfish But you make me feel helpless, yeah And I can't stand another day Stand another day You might also like I just wanna make you feel okay But all you do is look the other way, hmm I can't tell you how much I wish I didn't wanna stay I just kinda wish you were gay I just kinda wish you were gay I just kinda wish you were gay"''')
song6A1 =  ('''"Don't you know I'm no good for you? I've learned to lose you, can't afford to Tore my shirt to stop you bleedin' But nothin' ever stops you leavin'   Quiet when I'm coming home and I'm on my own I could lie, say I like it like that, like it like that I could lie, say I like it like that, like it like that  Don't you know too much already? I'll only hurt you if you let me Call me friend, but keep me closer (Call me back) And I'll call you when the party's over   Quiet when I'm coming home and I'm on my own And I could lie, say I like it like that, like it like that Yeah, I could lie, say I like it like that, like it like that  [Bridge] But nothin' is better sometimes Once we've both said our goodbyes Let's just let it go Let me let you go   Quiet when I'm coming home and I'm on my own I could lie, say I like it like that, like it like that I could lie, say I like it like that, like it like that"''')
song7A1 =  ('''"Wait a minute, let me finish I know you don't care But can you listen? I came committed, guess I overdid it Wore my heart out on a chain Around my neck, but now it's missin', hmm   Da-da-da-da-da-da (Hmm) Da-da-da-da-da-da-da (Hmm, hmm, hmm, hmm) Oh, hmm, hmm   So I think I better go I never really know how to please you You're lookin' at me like I'm see-through I guess I'm gonna go I just never know how you feel Do you even feel anything?   Da-da-da-da-da-da-da Da-da-da-da-da-da-da Oh, hmm, hmm You might also like You said, ""Don't treat me badly"" But you said it so sadly So I did the best I could Not thinkin' you would have left me gladly I know you're not sorry Why should you be? 'Cause who am I to be in love When your love never is for me? Me   Da-da-da-da-da-da-da (Hmm) Da-da-da-da-da-da-da (Hmm, hmm, hmm, hmm) Oh, hmm, hmm   So I think I better go I never really know how to please you You're lookin' at me like I'm see-through I guess I'm gonna go I just never know how you feel Do you even feel anything?"''')
song8A1 =  ('''"No, Billy, I haven't done that dance since my wife died There 2019s a whole crowd of people out there who need to learn how to do The Scarn   Don't ask questions you don't wanna know Learned my lesson way too long ago To be talkin 2019 to you, belladonna Shoulda taken a break, not an Oxford comma Take what I want when I wanna And I want ya [Pre-Chorus] Bad, bad news One of us is gonna lose I'm the powder, you're the fuse Just add some friction   You are my strange addiction You are my strange addiction My doctors can't explain My symptoms or my pain But you are my strange addiction  [Interlude] I'm really, really sorry, I think I was just relieved To see that Michael Scarn got his confidence back Yeah, Michael, the movie is amazing It's like, one of the best movies I've ever seen in my life   Deadly fever, please don't ever break Be my reliever  2019cause I don 2019t self medicate And it burns like a gin and I like it Put your lips on my skin and you might ignite it Hurts, but I know how to hide it, kinda like it (Teh) You might also like[Pre-Chorus] Bad, bad news One of us is gonna lose I'm the powder, you 2019re the fuse Just add some friction   You are my strange addiction You are my strange addiction My doctors can't explain My symptoms or my pain But you are my strange addiction  [Bridge] Bite my glass, set myself on fire Can't you tell I'm crass? Can 2019t you tell I'm wired? Tell me nothing lasts, like I don't know You could kiss my 2014 asking about my motto  [Interlude] You should enter it in festivals or carnivals Thoughts? Pretty good reaction Pretty cool... right?   You are my strange addiction You are my strange addiction My doctors can't explain My symptoms or my pain But you are my strange addiction [Outro] Did you like it? Did you like that? Um, which part?"''')
song9A1 =  ('''"What do you want from me? Why don't you run from me? What are you wondering? What do you know? Why aren't you scared of me? Why do you care for me? When we all fall asleep, where do we go?  [Verse 1"", "" Billie Eilish & Mehki Raine] Come here Say it, spit it out, what is it exactly You're payin'? Is the amount cleanin' you out? Am I satisfactory? Today, I'm thinkin' about the things that are deadly The way I'm drinkin' you down Like I wanna drown, like I wanna end me [Refrain"", ' Billie Eilish] Step on the glass, staple your tongue (Ahh) Bury a friend, try to wake up (Ah-ahh) Cannibal class, killing the son (Ahh) Bury a friend, I wanna end me  [Pre-Chorus', ' Billie Eilish] I wanna end me I wanna, I wanna, I wanna 2026 end me I wanna, I wanna, I wanna 2026  [Chorus', "" Billie Eilish] What do you want from me? Why don't you run from me? What are you wondering? What do you know? Why aren't you scared of me? Why do you care for me? When we all fall asleep, where do we go?  [Verse 2"", "" Billie Eilish & Mehki Raine] Listen Keep you in the dark, what had you expected? Me to make you my art and make you a star And get you connected? I'll meet you in the park, I'll be calm and collected But we knew right from the start that you'd fall apart 'Cause I'm too expensive It's probably somethin' that shouldn't be said out loud Honestly, I thought that I would be dead by now (Wow) Calling security, keepin' my head held down Bury the hatchet or bury a friend right now You might also like[Bridge"", "" Billie Eilish & Mehki Raine] The debt I owe, gotta sell my soul 'Cause I can't say no, no, I can't say no Then my limbs all froze and my eyes won't close And I can't say no, I can't say no Careful  [Refrain"", ' Billie Eilish] Step on the glass, staple your tongue (Ahh) Bury a friend, try to wake up (Ah-ahh) Cannibal class, killing the son (Ahh) Bury a friend, I wanna end me [Pre-Chorus', ' Billie Eilish] I wanna end me I wanna, I wanna, I wanna 2026 end me I wanna, I wanna, I wanna 2026  [Chorus', ' Billie Eilish] What do you want from me? Why don't you run from me? What are you wondering? What do you know? Why aren't you scared of me? Why do you care for me? When we all fall asleep, where do we go?"''')
song10A1 =  ('''"Told you not to worry But maybe that's a lie Honey, what's your hurry? Won't you stay inside? Remember not to get too close to stars They're never gonna give you love like ours   Where did you go? I should know, but it's cold And I don't wanna be lonely So show me the way home I can't lose another life  Hurry, I'm worried   The world's a little blurry Or maybe it's my eyes The friends I've had to bury They keep me up at night Said I couldn't love someone 'Cause I might break If you're gonna die, not by mistake   So, where did you go? I should know, but it's cold And I don't wanna be lonely So tell me you'll come home Even if it's just a lie  [Bridge] I tried not to upset you Let you rescue me the day I met you I just wanted to protect you But now I'll never get to   Hurry, I'm worried You might also like[Outro] Where did you go? I should know, but it's cold And I don't wanna be lonely Was hoping you'd come home I don't care if it's a lie"''')
song11A1 =  ('''"Take me to the rooftop I wanna see the world when I stop breathing Turnin' blue Tell me love is endless, don't be so pretentious Leave me like you do (Like you do)  [Pre-Chorus] If you need me, wanna see me Better hurry 'cause I'm leavin' soon  Sorry can't save me now Sorry I don't know how Sorry there's no way out (Sorry) But down Hmm, down   Taste me, the salty tears on my cheek That's what a year-long headache does to you I'm not okay, I feel so scattered Don't say I'm all that matters Leave me, d 00e9j 00e0 vu (Hmm)  [Pre-Chorus] If you need me, wanna see me You better hurry, I'm leavin' soon   Sorry can't save me now (Sorry) Sorry I don't know how (Sorry) Sorry there's no way out (Sorry) But down Hmm, down  [Outro] Call my friends and tell them that I love them And I'll miss them But I'm not sorry Call my friends and tell them that I love them And I'll miss them Sorry"''')
song12A1 =  ('''"It's not true Tell me I 2019ve been lied to Crying isn't like you, ooh What the hell did I do? Never been the type to Let someone see right through, ooh   Maybe won't you take it back? Say you were tryna make me laugh And nothing has to change today You didn 2019t mean to say ""I love you"" I love you and I don't want to, ooh  Up all night on another red-eye I wish we never learned to fly Maybe we should just try To tell ourselves a good lie Didn't mean to make you cry   Maybe won't you take it back? Say you were tryna make me laugh And nothing has to change today You didn't mean to say ""I love you"" I love you and I don't want to, ooh  [Bridge] The smile that you gave me Even when you felt like dying  [Outro] We fall apart as it gets dark I'm in your arms in Central Park There's nothing you could do or say I can 2019t escape the way I love you I don 2019t want to, but I love you, ooh Ooh, ooh Ooh, ooh"''')
song13A1 =  ('''"Please, please Don't leave  me Be   It's not true Take me to the rooftop Told you not to worry What do you want from me? Don't ask questions Wait a minute Don't you know I'm no good for you? Baby, I don't feel so good And all the good girls go  to Hell Bite my tongue, bide my time What is it about them? I'm the bad guy"''')

song1A2 =  ('''"I'm gettin' older, I think I'm agin' well I wish someone had told me I'd be doin' this by myself There's reasons that I'm thankful, there's a lot I'm grateful for But it's different when a stranger's always waitin' at your door Which is ironic 'cause the strangers seem to want me more Than anyone before (Anyone before) Too bad they're usually deranged   Last week, I realized I crave pity When I retell a story, I make everything sound worse Can't shake the feeling that I'm just bad at healing And maybe that's the reason every sentence sounds rehearsed Which is ironic because when I wasn't honest I was still bein' ignored (Lyin' for attention just to get neglection) Now we're estranged  Things I once enjoyed Just keep me employed now Things I'm longing for Someday, I'll be bored of It's so weird That we care so much until we don't   I'm gettin' older, I've got more on my shoulders But I'm gettin' better at admitting when I'm wrong I'm happier than ever, at least, that's my endeavor To keep myself together and prioritize my pleasure 'Cause, to be honest, I just wish that what I promise Would depend on what I'm given, mmm (Not on his permission) (Wasn't my decision) To be abused, mmm   Things I once enjoyed Just keep me employed now, mmm Things I'm longing for, mmm Someday, I'll be bored of It's so weird That we care so much until we don't  [Outro] But next week, I hope I'm somewhere laughing For anybody asking, I promise I'll be fine I've had some trauma, did things I didn't wanna Was too afraid to tell ya, but now, I think it's time"''')
song2A2 =  ('''"Okay Mm-mm, I   I didn't change my number I only changed who I reply to Laura said I should be nicer But not to you I love a ""You mad at me?"" text Shoulda guessed That you would think I was upset (Haha) You're obsessed  Don't take it out on me I'm out of sympathy for you Maybe you should leave Before I get too mean   I didn't change my number I only changed who I believe in You were easy on the eyes, eyes, eyes (Eyes, ey 0435s) But looks can be deceivin' I gotta work, I go to work You don't d 0435serve to feel so hurt You got a lot of fuckin' nerve I don't deserve, so   Don't take it out on me I'm out of sympathy for you Maybe you should leave Before I get too mean And take it out on you And your best friend, too I should have left when Drew Said you were bad news You might also like[Outro', ' Billie Eilish & FINNEAS] Mm-mm-mm Mm-mm-mm Mm-mm-mm Mm-mm-mm Mm-mm-mm Mm-mm-mm"''')
song3A2 =  ('''"Mm-mm-mm, mm-mm Da-da-da-da   Love when it comes without a warning 'Cause waiting for it gets so boring A lot can change in twenty seconds A lot can happen in the dark Love when it makes you lose your bearings Some information's not for sharing Use different names at hotel check-ins It's hard to stop it once it starts (It starts)  I'm not sentimental But there's somethin' 'bout the way you look tonight, mm Makes me wanna take a picture Make a movie with you that we'd have to hide   You better lock your phone (Oh) And look at me wh 0435n you're alone Won't take a lot to g 0435t you goin' (Oh) I'm sorry if it's torture though I know, I know   It might be more of an obsession You really make a strong impression (A strong impression) Nobody saw me in the lobby (Saw me in the lobby) Nobody saw me in your arms, mm   I'm not sentimental But there's somethin' 'bout the way you look tonight, mm ('Bout the way you look tonight) Makes me wanna make 'em jealous I'm the only one who does it how you like (Only one who does it how you 2014)   You better lock your phone (Oh) And look at me when you're alone (You're alone, you're alone) Won't take a lot to get you goin' (Get me goin', get me goin') I'm sorry if it's torture though (Torture though) I know, I know You better lock your door (Oh) And look at me a little more We both know I'm worth waitin' for (Waitin' for) That heavy breathin' on the floor (On the floor) I'm yours, I'm yours (I'm yours) You might also like[Outro] I'm not sentimental I'm not sentimental I'm not sentimental"''')
song4A2 =  ('''"I can't seem to focus And you don't seem to notice I'm not here I'm just a mirror You check your complexion To find your reflection's all alone I had to go   Can't you hear me? I'm not comin' home Do you understand? I've 205fchanged 205fmy 205fplans [Chorus] 'Cause I, I'm 205fin love With my 205ffuture Can't wait to meet her And I (I), I'm in love But not with anybody else Just wanna get to know myself   I know supposedly I'm lonely now (Lonely now) Know I'm supposed to be unhappy Without someone (Someone) But aren't I someone? (Aren't I someone? Yeah) I'd (I'd) like to be your answer (Be your answer) 'Cause you're so handsome (You're so handsome)   But I know better Than to drive you home 'Cause you'd invite me in And I'd be yours again  [Chorus] But I (I), I'm in love (Love, love, love, love) With my future And you don't know her (Ooh) And I, I'm in love (Love, love) But not with anybody here I'll see you in a couple years"''')
song5A2 =  ('''"Can't take it back once it's been set in motion You know I love to rub it in like lotion If you only pray on Sunday, could you come my way on Monday? 'Cause I like to do things God doesn't approve of if She saw us   She couldn't look away, look away, look away She'd wanna get involved, involved, involved And what would people say, people say, people say If they listen through the wall, the wall, the wall?  I can see it clear as day You don't really need a break Wanna see what you can take You should really run away  [Post-Chorus] I wanna do bad things to you (To you) I wanna make you yell (Yell) I wanna do bad things to you (To you) Don't wanna treat you well (Well)   Can't take it back once it's been set in motion You know I need you for the oxytocin If you find it hard to swallow, I can loosen up your collar 'Cause as long as you're still breathing Don't you even think of leaving   Not gonna wanna look away, look away, look away You're gonna wanna get involved, involved, involved And what would people say, people say, people say If they listen through the wall, the wall, the wall?   I can see it clear as day You don't really need a break Wanna see what you can take You should really run away Other people wouldn't stay Other people don't obey You and me are both the same You should really run away You might also like[Outro] Bad things To you I wanna do bad things to you I wanna make you yell I wanna do bad things to you Don't wanna treat you well"''')
song6A2 =  ('''"He hath come to the bosom of his beloved Smiling on him, she beareth him to highest heav'n With yearning heart"" ""On thee we gaze, O' gold-wing'd messenger of mighty Gods""     Gold-winged angel Go home, don't tell Anyone what you are You're sacred and they're starved And their art is gettin' dark And there you are to tear apart Tear apart, tear apart, tear apart [Chorus] You better keep your head down-down Da-da-down-down, da-da-down-down Better keep your head down-down Da-da-down-down, da-da-down-down   They're gonna tell you what you wanna hear Then they're gonna disappear Gonna claim you like a souvenir Just to sell you in a year  [Chorus] You better keep your head down-down Da-da-down-down, da-da-down-down Keep your head down-down (Down) Da-da-down-down, da-da-down-down Better keep your head down-down Da-da-down-down, da-da-down-down Keep your head down-down Da-da-down-down, da-da-down-down  [Outro] That's good"''')
song7A2 =  ('''"Something's in the 2014   Something's in the air right now Like I'm losin' track of time (Time, time) Like I don't really care right now But maybe that's fine You weren't even there that day I was waitin' on you (You, you) I wonder if you were aware that day Was the last straw for me and I knew  I sent you flowers Did you even care? You ran the shower And left them by the stairs Ooh-ooh-ooh, a-a-a-ayy Thought you had your shit together, but damn, I was wrong (Wrong)   You ain't nothin' but a lost cause (Cause, cause) And this ain't nothin' like it onc 0435 was (Was, was) I know you think you're such an outlaw But you got no job (Job) You ain't nothin' but a lost cause (Cause) And this ain't nothin' lik 0435 it once was (Was) I know you think you're such an outlaw But you got no job   I used to think you were shy (Shy) But maybe you just had nothing on your mind Maybe you were thinkin' 'bout yourself all the time I used to wish you were mine (Mine) But that was way before I realized Someone like you would always be so easy to find (So) So easy (So, so) Hee, mm-mm-mm, mm You might also like Gave me no flowers Wish I didn't care You'd be gone for hours Could be anywhere Ooh-ooh-ooh Ah-ah-ah-ah-ah Thought you would've grown eventually, but you proved me wrong (Wrong)   You ain't nothing but a lost cause (Cause) And this ain't nothing like it once was (Was) I know you think you're such an outlaw (Yeah) But you got no job (No job) You ain't nothing but a lost cause (Cause) And this ain't nothing like it once was (Was) I know you think you're such an outlaw (Think you're such a lost cause) But you got no job  [Outro] (What did I tell you?) (Don't get complacent) (It's time to face it now, na-na, na-na, na-na) (What did I tell you?) (Don't get complacent) (It's time to face it now, na-na, na-na, na-na)"''')
song8A2 =  ('''"I don't want it And I don't want to want you But in my dreams, I seem to be more honest And I must admit you've been in quite a few   Halley's Comet Comes around more than I do But you're all it takes for me to break a promise Silly me to fall in love with you  I haven't slept since Sunday Midnight for me is 3AM for you But my sleepless nights are better With you than nights could ever be alone, ooh-ooh I was good at feeling nothin', now I'm hopeless What a drag to love you like I do Ooh-ooh-ooh-ooh-ooh   I've been loved before, but right now, in this moment I feel more and more like I was mad 0435 for you For you    [Outro] I'm sitting in my brother's room Haven't slept in a week or two, or two I think I might hav 0435 fallen in love What am I to do?"''')
song9A2 =  ('''"Do you know me? Really know me? You have opinions about my opinions About my music About my clothes About my body Some people hate what I wear Some people praise it Some people use it to shame others Some people use it to shame me But I feel you watching Always And nothing I do goes unseen So while I feel your stares, your disapproval or your sigh of relief If I lived by them, I'd never be able to move Would you like me to be smaller, weaker, softer, taller? Would you like me to be quiet? Do my shoulders provoke you? Does my chest? Am I my stomach? My hips? The body I was born with Is it not what you wanted? If I wear what is comfortable, I am not a woman If I shed the layers, I'm a slut Though you've never seen my body, you still judge it And judge me for it Why? We make assumptions about people based on their size We decide who they are We decide what they're worth If I wear more, if I wear less Who decides what that makes me? What that means? Is my value based only on your perception? Or is your opinion of me not my responsibility?"''')
song10A2 =  ('''"I don't really even know how it happened I started talkin', they started laughin' I don't really even know how it happened I started watchin' them photographin' I don't really (I don't really), how it happened Instead of stoppin', they still were flashin' (I don't really) I started walkin' (I don't really), gave no reaction No reaction   I'm overheated, can't be defeated Can't be deleted, can't un-believ 0435 it I'm overheated, can't b 0435 defeated Can't be deleted, can't be repeated I'm overheated I'm overheated  I don't really wanna know why it went there (Why it went there) I kinda don't care (Kinda don't care) You wanna kill me? (You wanna kill me?) You wanna hurt me? (Mmm) Stop bein' flirty It's kinda workin' Did you really think ""This is the right thing to do""? (Is it news? News to who?) That I really look just like the rest of you   I'm overheated, can't be defeated Can't be deleted, can't un-believe it I'm overheated, can't be defeated Can't be deleted, can't be repeated I'm overheated  [Bridge] And everybody said it was a letdown I was only built like everybody else now But I didn't get a surgery to help out 'Cause I'm not about to redesign myself now, am I? (Am I?) Am I? All these other inanimate bitches, it's none of my business But don't you get sick of posin' for pictures With that plastic body? You might also like Man, I'm overheated, can't be defeated Can't be deleted, can't un-believe it I'm overheated, can't be defeated Can't be deleted, can't be repeated I'm overheated"''')
song11A2 =  ('''"Everybody dies, surprise, surprise We tell each other lies, sometimes, we try To make it feel like we might be right We might not be alone Be alone   ""Everybody dies,"" that's what they say And maybe, in a couple hundred years, they'll find another way I just wonder why you'd wanna stay If everybody goes You'd still be alone [Verse 3] I don't wanna cry, some days I do But not about you It's just a lot to think about the world I'm used to The one I can't get back, at lu0435ast not for a while I sure have a knack for seein' lifu0435 more like a child It's not my fault, it's not so wrong to wonder why Everybody dies And when will I?  [Verse 4] You oughta know That even when it's time, you might not wanna go But it's okay to cry and it's alright to fold But you are not alone You are not unknown"''')
song12A2 =  ('''"Try not to abuse your power I know we didn't choose to change You might not wanna lose your power But havin' it's so strange   She said you were a hero You played the part But you ruined her in a year Don't act like it was hard And you swear you didn't know (Didn't know) No wonder why you didn't ask She was sleepin' in your clothes (In your clothes) But now she's got to get to class  How dare you? And how could you? Will you only feel bad when they find out? If you could take it all back Would you?   Try not to abuse your power I know we didn't choose to change You might not wanna lose your power But havin' it's so strange   I thought that I was special You made me feel Like it was my fault, you were the devil Lost your appeal Does it keep you in control? (In control) For you to keep her in a cage? And you swear you didn't know (Didn't know) You said you thought she was your age   How dare you? And how could you? Will you only feel bad if it turns out That they kill your contract? Would you? You might also like Try not to abuse your power I know we didn't choose to change You might not wanna lose your power But power isn't pain  [Outro] Mmm Ooh La-la-la-la-la, hmm La-la-la-la-la-la, la-la"''')
song13A2 =  ('''"Did you think I'd show up in a limousine? (No) Had to save my money for security Got a stalker walkin' up and down the street Says he's Satan and he'd like to meet I bought a secret house when I was seventeen (Ha) Haven't had a party since I got the keys Had a pretty boy over, but he couldn't stay On his way out, made him sign an NDA, mm Yeah, I made him sign an NDA Once was good enough 'Cause I don't want him havin' shit to say, oh-oh-oh  You couldn't save me, but you can't let me go, oh, no I can crave you, but you don't need to know, oh-oh   Mm, mm-mm, mm 30 Under 30 for another year (Another year) I can barely go outside, I think I hate it her 0435 (I think I hate it here) Mayb 0435 I should think about a new career (Uh) Somewhere in Kauai where I can disappear I've been havin' fun gettin' older now Didn't change my number, made him shut his mouth (Shut his mouth, yeah) At least I gave him somethin' he can cry about I thought about my future, but I want it now, oh-oh-oh Want it now, mm-mm-mm You can't give me up   You couldn't save me, but you can't let me go, oh, no I can crave you, but you don't need to know, oh-oh  [Outro] Did I take it too far? Now I know what you are You hit me so hard I saw stars Think I took it too far When I sold you my heart How'd it get so dark? I saw stars Stars"''')
song14A2 =  ('''"I'm not your friend Or anything, damn You think that you're the man I think, therefore, I am I'm not your friend Or anything, damn You think that you're the man I think, therefore, I am   Stop, what the hell are you talking about? Ha Get my pretty name out of your mouth We are not the same with or without Don't talk 'bout me like how you might know how I feel Top of the world, but your world isn't real Your world's an ideal  So go have fun I really couldn't care less And you can give 'em my best, but just know   I'm not your friend Or anything, damn You think that you're the man I think, therefore, I am I'm not your friend Or anything, damn You think that you're the man I think, therefore, I am   I don't want press to put your name next to mine We're on different lines, so I Wanna be nice enough, they don't call my bluff 'Cause I hate to find Articles, articles, articles Rather you remain unremarkable (Got a lotta) Interviews, interviews, interviews When they say your name, I just act confused   Did you have fun? I really couldn't care less And you can give 'em my best, but just know You might also like I'm not your friend Or anything, damn You think that you're the man I think, therefore, I am I'm not your friend Or anything, damn You think that you're the man I think, therefore, I am  [Bridge] I'm sorry I don't think I caught your name I'm sorry I don't think I caught your name   I'm not your friend (I'm not your friend) Or anything, damn You think that you're the man (They wanna, they can try) I think, therefore, I am I'm not your friend (I'm not your friend) Or anything, damn (They wanna) You think that you're the man I think, therefore, I am"''')
song15A2 =  ('''"When I'm away from you I'm happier than ever Wish I could explain it better I wish it wasn't true   Give me a day or two to think of something clever To write myself a letter To tell me what to do, mm-mm Do you read my interviews? Or do you skip my avenue? When you said you were passin' through Was I even on your way? I knew when I asked you to (When I asked you to) Be cool about what I was tellin' you You'd do the opposite of what you said you'd do (What you said you'd do) And I'd end up more afraid Don't say it isn't fair You clearly wer 0435n't aware that you made me mis 0435rable So if you really wanna know  When I'm away from you (When I'm away from you) I'm happier than ever (Happier than ever) Wish I could explain it better (Wish I could explain it better) I wish it wasn't true, mm-mm   You call me again, drunk in your Benz Drivin' home under the influence You scared me to death, but I'm wastin' my breath 'Cause you only listen to your fuckin' friends I don't relate to you I don't relate to you, no 'Cause I'd never treat me this shitty You made me hate this city   And I don't talk shit about you on the internet Never told anyone anything bad 'Cause that shit's embarrassing, you were my everything And all that you did was make me fuckin' sad So don't waste the time I don't have And don't try to make me feel bad I could talk about every time that you showed up on time But I'd have an empty line 'cause you never did Never paid any mind to my mother or friends, so I Shut 'em all out for you 'cause I was a kid You might also like[Outro] You ruined everything good Always said you were misunderstood Made all my moments your own Just fuckin' leave me alone, yeah (Fuck you) (Ah) (Goddamn) (Ah) (Fuck you) (Fuck you)"''')


# In[55]:


# function calling
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# In[56]:


sentiment_scores(album1)


# In[11]:


sentiment_scores(album2)


# In[12]:


sentiment_scores(interview1)


# In[13]:


sentiment_scores(interview2)


# In[14]:


sentiment_scores(song1A1)


# In[ ]:





# import statistics

# In[33]:


import statistics
import pandas
#album1Median = median()
album1d={'Net Positive Sentiment':[sentiment_scores(song1A1), sentiment_scores(song2A1), sentiment_scores(song3A1), sentiment_scores(song4A1), sentiment_scores(song5A1), sentiment_scores(song6A1), sentiment_scores(song7A1), sentiment_scores(song8A1), sentiment_scores(song9A1), sentiment_scores(song10A1), sentiment_scores(song11A1), sentiment_scores(song12A1), sentiment_scores(song13A1)]}

album1Df=pandas.DataFrame(album1d)


# In[34]:


album1Median = statistics.median(album1Df["Net Positive Sentiment"])
print(album1Median)


# In[17]:


album2d={'Net Positive Sentiment':[sentiment_scores(song1A2), sentiment_scores(song2A2), sentiment_scores(song3A2), sentiment_scores(song4A2), sentiment_scores(song5A2), sentiment_scores(song6A2), sentiment_scores(song7A2), sentiment_scores(song8A2), sentiment_scores(song9A2), sentiment_scores(song10A2), sentiment_scores(song11A2), sentiment_scores(song12A2), sentiment_scores(song13A2), sentiment_scores(song14A2), sentiment_scores(song15A2)]}

album2Df=pandas.DataFrame(album2d)
album2Median = statistics.median(album2Df["Net Positive Sentiment"])
print(album2Median)


# In[26]:


import matplotlib.pyplot as plt
import numpy as np


# In[97]:


plt.hist(album1Df['Net Positive Sentiment'], bins=13)
x = statistics.median(album1Df["Net Positive Sentiment"])
w = sentiment_scores(album1)
plt.axvline(x, color='k', linestyle='dashed', linewidth=1)
plt.axvline(sentiment_scores(album1), color='k', linestyle='solid', linewidth=1)
min_ylim, max_ylim = plt.ylim()
plt.text(-x*7.4, max_ylim*0.85, 'Median Net Positive Sentiment: {:.2f}'.format(x) + " (dashed)")
plt.text(x*1.2, max_ylim*0.7, 'Total Album Net Positive Sentiment: {:.2f}'.format(w)+ " (solid)")
plt.title("'When We All Fall Asleep, Where Do We Go?' Net Positive Sentiment Histogram")
#plt.text(x.mean()*1.1, max_ylim*0.9, 'Median: {:.2f}'.format(statistics.median(x)))
plt.xlabel("Net Positive Sentiment (Positive Sentiment - Negative Sentiment)")
plt.ylabel("Number of Songs in Album")


# In[107]:


#plt.hist(album2Df['Net Positive Sentiment'], bins=15)
#x2 = statistics.median(album2Df["Net Positive Sentiment"])
#plt.axvline(x2, color='k', linestyle='dashed', linewidth=1)
#min_ylim, max_ylim = plt.ylim()
#plt.text(x2*1.1, max_ylim*0.9, 'Median: {:.2f}'.format(x2))


# In[106]:


plt.hist(album1Df['Net Positive Sentiment'], bins=15)
x = statistics.median(album2Df["Net Positive Sentiment"])
w = sentiment_scores(album2)
plt.axvline(x, color='k', linestyle='dashed', linewidth=1)
plt.axvline(sentiment_scores(album2), color='k', linestyle='solid', linewidth=1)
min_ylim, max_ylim = plt.ylim()
plt.text(x*1.1, max_ylim*0.85, 'Median Net Positive Sentiment: {:.2f}'.format(x) + " (dashed)")
plt.text(-x*9, max_ylim*0.67, 'Total Album Net' + "\n" + 'Positive Sentiment: {:.2f}'.format(w)+ " (solid)")
plt.title("'Happier Than Ever?' Net Positive Sentiment Histogram")
#plt.text(x.mean()*1.1, max_ylim*0.9, 'Median: {:.2f}'.format(statistics.median(x)))
plt.xlabel("Net Positive Sentiment (Positive Sentiment - Negative Sentiment)")
plt.ylabel("Number of Songs in Album")


# In[ ]:




