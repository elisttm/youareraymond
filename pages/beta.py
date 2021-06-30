class bp():

	#		------------------------

	styles = {
		"default": {
			"bodycolor": "#535353",
			"midcolor": "#c6c6c6",
			"divcolor": "#efefef",
			"textcolor": "#000",
			"text2color": "#444", 
			"bodyclass": None,
		},
		"dark": {
			"bodycolor": "#000",
			"midcolor": "#2c2c2c",
			"divcolor": "#000",
			"textcolor": "#fff",
			"text2color": "#aaa", 
		},
		"blur": {
			"bodyclass": "blur",
		},
	}
		
	for style_a in styles:
		for style_b in styles["default"]:
			if style_b not in styles[style_a]:
				styles[style_a][style_b] = styles["default"][style_b]
	
	#		------------------------


	chapters = {
		"home stuck": {
			"desc": "",
			"pages": [1,2,3,4,5,6,7,8,9,10,11,12,13,28,29,30,31,32,33,34],
			"style": styles['default'],
		},
		"blurry": {
			"desc": "",
			"pages": [14,15,16,17,18,19,20,21,22,23,24,25,26,27],
			"style": styles['blur'],
		},
	}

	pages = {
		
		"error": {
			"title": "the provided page does not exist!",
			"style": styles['dark'],
			"hidden": True, 
			"text": [
				"The page you have entered does not exist!",
				"Please check if the URL you entered is correct or if the page is in the [a:/beta/page/list: page list]",
				"If neither of these are the issue and you feel this is in error, please contact eli",
			]
		},

		1: {
			"title": "You Are Raymond.",
			"embeds": ["/static/content/extra/beta/1.png"],
			"text": [
				"You are raymond. You're standing in an almost empty room.",
				"What do you do?",
			]
		},
		2: {
			"title": "Raymond: Kill self.",
			"embeds": ["/static/content/extra/beta/2.png", "/static/content/extra/beta/3.png"],
			"text": [
				"Uh oh.",
				"THE VOICES ARE BACK",
			]
		},
		3: {
			"title": "Raymond: Inspect room.",
			"embeds": ["/static/content/extra/beta/5.png", "/static/content/extra/beta/8.png", "/static/content/extra/beta/6.png", "/static/content/extra/beta/4.png", "/static/content/extra/beta/7.png"],
			"text": [
				"You look around your room.",
				"From your window you see nothing interesting. Only other notable things in here are your door and... a box?",
			]
		},
		4: {
			"title": "Raymond: Be the other guy.",
			"embeds": ["/static/content/extra/beta/9.png"],
			"text": [
				"This drivel means nothing to you. There is no \"other guy\", and for all you know, there never will be.",
			]
		},
		5: {
			"title": "Raymond: Give to urge of crashing across the window.",
			"embeds": ["/static/content/extra/beta/10.gif"], 
			"text": [ 
				"This idea is so unbelievably stupid. You hate yourself a little for even entertaining such a frivolous and self-destructive idea.",
			]
		},
		6: {
			"title": "Raymond: [S] Unless...?",
			"embeds": ["https://www.youtube.com/embed/iqgcXC67dn0"], 
		},
		7: {
			"title": "Raymond: Try again.",
			"embeds": ["/static/content/extra/beta/11.png"], 
			"text": [
				"There's no way you're doing that again, that shit hurted!",
			]
		},
		8: {
			"title": "Raymond: Fine, be a boring sack of shit and casually walk to that door.",
			"embeds": ["/static/content/extra/beta/12.png", "/static/content/extra/beta/13.png"], 
			"text": [
				"C'mon, there's no need to be rude.",
				"There, now what?",
			]
		},
		9: {
			"title": "Raymond: Open it.",
			"embeds": ["/static/content/extra/beta/14.png", "/static/content/extra/beta/15.png"], 
			"text": [
				"You grip the handle and make a sturdy attempt to twist it.",
				"Unfortunately, the door is locked ...even though you're already inside the house?",
			]
		},
		10: {
			"title": "Raymond: Kick it open, then.", 
			"embeds": ["/static/content/extra/beta/16.png"], 
			"text": [
				"The artist didn't anticipate your feet being visible in this perspective so they were not drawn.",
				"As a result, you are unable to kick down the door as you are now.",
			]
		},
		11: {
			"title": "Raymond: Ok, do some kind of zoom-out thingy and THEN kick it open.", 
			"embeds": ["/static/content/extra/beta/17.png", "/static/content/extra/beta/18.png"], 
			"text": [
				"You successfully do some kind of zoom-out thingy.",
				"This is definitely an improvement, but even you know that trying to kick open a LOCKED DOOR is a bad idea.",
				"At this point, it should be apparent to anyone that the idea of using brute strength for things hasn't worked out a single time thus far. Maybe try thinking beyond the scope of a 2 year old.",
			]
		},
		12: {
			"title": "Raymond: Lockpick the door", 
			"embeds": ["/static/content/extra/beta/19.png", "/static/content/extra/beta/20.gif"], 
			"text": [
				"Hey, that's actually a pretty reasonable idea.",
        "You search your inventory for anything useful, but... wait, were your GLASSES always this dirty? Wow...you [i:really] should clean these.",
			]
		},
		13: {
			"title": "Raymond: Unequip glasses.",
			"embeds": ["/static/content/extra/beta/21.gif"], 
			"text": [
				"You unequip your GLASSES.",
			]
		},
		14: {
			"title": "Next",
			"embeds": ["/static/content/extra/beta/22.png", "/static/content/extra/beta/23.png"], 
			"text": [
        "You can't see shit.",
				"In fact, your eyesight is so unbelievably shitty that it somehow managed to seep into the website hosting the comic.",
				"[h2:NEW QUEST ADDED: Find a cloth or towel or whatever]",
			]
		},
		15: {
			"title": "Raymond: Look for a glass wipe.",
			"embeds": ["/static/content/extra/beta/24.gif"], 
			"text": [
				"That is such a stupid idea. Do you have any idea how big those things are? It's not like you even own one, you hardly do any cleaning, you aren't some kind of maid.",
			]
		},
		16: {
			"title": "Raymond: Use your blurry vision to see into the secret dimensions we haven't talked about yet.",
			"embeds": ["/static/content/extra/beta/25.gif"], 
			"text": [
				"You successfully use your blurry vision to see into the secret dimensions we haven't talked about yet.",
				"[a:/secret/secretfolder/homework/donotopen/youareraymond/ideas.txt:You have no idea what any of this means].",
			]
		},
		17: {
			"title": "Raymond: Slip on a banana peel.",
			"embeds": ["/static/content/extra/beta/26.gif"], 
			"text": [
				"While distracted by what you're seeing, you slip on a banana peel and hit your head on the floor.",
				"[h2:-5 HEALTH POINTS!]",
			]
		},
    18: {
			"title": "Raymond: The banana peel will suffice. Wipe your glasses with it.",
			"embeds": ["/static/content/extra/beta/28.gif"], 
			"text": [
        "Well it doesn't hurt to try right?",
				"Because of your recent fall, it doesn't occur to you how terrible of an idea this is.",
			]
		},
    19: {
			"title": "Next",
			"embeds": ["/static/content/extra/beta/29.gif", "/static/content/extra/beta/30.gif"], 
			"text": [
				"[h2:ITEM GOT: BANANA PEEL!]",
        "You furiously rub the BANANA PEEL against the GLASSES",
			]
		},
    20: {
			"title": "Next",
			"embeds": ["/static/content/extra/beta/31.jpeg"], 
			"text": [
        "You have definitely had better ideas than this",
			]
		},
		21: {
			"title": "Raymond: Use maximum vision power to make out where the door is",
			"embeds": ["/static/content/extra/beta/27.gif"], 
			"text": [
				"You attempt to look for a door, but there does not seem to be one anywhere nearby. was there ever even a door in this room to begin with?",
			]
		},
		22: {
			"title": "Raymond: Wipe your glasses off with your shirt you fucking dumbass",
			"embeds": ["/static/content/extra/beta/33.gif"], 
			"text": [
				"No! You would not under any circumstances wrinkle your shirt! You don't even know if there's an iron in this room.",
			]
		},
		23: {
			"title": "Raymond: You stupid son of a bitch i hate you so much just use your fucking shirt oh my god i hate you i hate you i hate you go die die die die die die die die use your shirt use it use it use it its not that fucking hard it is your only option you ugly bastard",
			"embeds": ["/static/content/extra/beta/34.gif"], 
			"text": [
				"[h2:EMOTIONAL CRIT!!!]",
				"[h2:-3 SELF ESTEEM!]",
			]
		},
		24: {
			"title": "Raymond: Use heterochromia powers to see better, give up on the glasses",
			"embeds": ["/static/content/extra/beta/35.gif"], 
			"text": [
				"First of all, that's not how heterochromia works.",
        "Second, if you haven't noticed before, both of your eyes are black!",
        "You know what? this is not going anywhere. if you want to progress you'll need to start thinking for yourself.",
			]
		},
		25: {
			"title": "Next",
			"embeds": ["/static/content/extra/beta/36.gif", "/static/content/extra/beta/37.gif", "/static/content/extra/beta/38.gif"], 
			"text": [
        "So... about that BOX. is there anything useful on it? it has just been staring menacingly all this time",
				"[h2:ITEM GOT:?!]",
        "You have no idea what this is but it definitely won't clean your glasses",
			]
		},
		26: {
    	"title": "Next",
			"embeds": ["/static/content/extra/beta/39.gif"],
      "text": [
        "You're definetly stuck, you would have never thought that it would have come to this but you are in desesperate times and you know what has to be done",
      ]
    },
    27: {
    	"title": "Raymond: Pray to Saul Goodman",
			"embeds": ["/static/content/extra/beta/40.gif", "/static/content/extra/beta/41.gif", "/static/content/extra/beta/42.gif"],
      "text": [
        "You pray and pray andp pray harder that you've ever done, hopefully he will hear you and bless you with his powers...",
        "And just like that, he's gone.",
        "You have truly been blessed",
    	]
    },
		28: {
    	"title": "Next",
			"embeds": ["/static/content/extra/beta/44.gif", "/static/content/extra/beta/45.gif"],
      "text": [
        "You know what, not much changed, this was a waste of your precious time",
        "So anyways.",
        "You can now clearly see that the mysterious item was a button all along.",
      ]
    },
		29: {
    	"title": "Raymond: Dissect button you need to see whats inside before pressing it",
			"embeds": ["/static/content/extra/beta/46.gif", "/static/content/extra/beta/47.gif"],
      "text": [
        "Sadly you can't open it, it's sealed pretty damn well plus you don't have any tools",
        "But there's this thing at the bottom, you might need to plug something in for the button to work",
      ]
    },
		30: {
    	"title": "Raymond: Stare directly and uncomfortably at the reader",
		 	"embeds": ["/static/content/extra/beta/48.gif"],
      "text": [
        "You have finally snapped. What do you mean by READER?? There is no \"reader\". You are alone.",
				"Stop mucking around and find a way out already!",
      ]
    },
		31: {
    	"title": "Next",
		 	"embeds": ["/static/content/extra/beta/50.gif", "/static/content/extra/beta/49.gif", "/static/content/extra/beta/51.gif", "/static/content/extra/beta/52.gif"],
      "text": [
        "You are going to go completely insane. You have been here for so long and you need to escape NOW.",
        "Is there anything in these god forsaken walls? A key? A Secret button?? An attic???",
        "Oh my god there is one.",
			]
  	},
		32: {
     	"title": "You Are Raymond: im dead",
		 	"embeds": ["/static/content/extra/beta/53.gif", "/static/content/extra/beta/54.gif"],
      "text": [
        "You're starting to have second thoughts about going inside the attic",
        "Well, you know what they say, you only live once!",
			]
  	},
	}