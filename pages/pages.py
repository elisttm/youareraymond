class p():

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
			"pages": [27],
			"style": styles['default'],
		},
	}

	#		------------------------

	#			CONTENT FORMATTING
	# [br] for line breaks and [hr] for horizonal rules
	# [h1:text], [h2:text], [h3:text], [h4:text], [h5:text] and [h6:text] for header text
	# [b:bold text], [i:italic text], [u:underline text], [s:strikethrough text], [sup:superscript text], [sub:subscript text]
	# [c:color:text] where "color" can be any color code or name recognized by html
	# [f:font family:text] where "font family" is a group of fonts as you would do in css
	# [a:url/path:text]; "text" would be displayed as a hyperlink and take you to the given url/path
	# [img:image url/path:class]; "class" (optional) is the name of a css class
	# [embed:url/path]; will auto detect and embed video (mp4) audio (wav) or basic page iframe

	pages = {
		
		"error": {
			"title": "the provided page does not exist!",
			"style": styles['dark'],
			"hidden": True, 
			"text": [
				"The page you have entered does not exist!",
				"Please check if the url you entered is correct or if the page is in the [a:/page/list: page list]",
				"If neither of these are the issue and you feel this is in error, please contact eli",
			]
		},

		"button": {
			"hidden": True,
			"title": "test page lol",
			"embeds": ["/static/content/1.gif"],
			"chatlog": {
				"name": "chat log",
				"text": [
					"this is an eample of the chat log button thing that i implimented! super cool and awesome lololollololloolololol",
					"fuck 2fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck ",
					"fuck 3fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck fuck ",
				]
			}
		},

		1: {
			"title": "You are Raymond.",
			"embeds": ["/static/content/1.gif"],
			"text": [
				"You are Raymond. You are currently standing the middle of your richly laid out home. Around your room are several pieces of furniture, such as your safe, your desk, and your workbench.  Today the 4th of April, 2021, is the day a package you've been anticipating for finally arrives.", 
				"What will you do?",
			]
		},
		2: {
			"title": "Raymond: Check Pockets.",
			"embeds": ["/static/content/2.gif"],
			"text": [
				"Before you start out, you might as well get a refresher on your pockets.",
				"You open your pockets and see that, apart from the clothes on your back, your wallet, and your NookPhone, you are carrying absolutely nothing.",
			]
		},
		3: {
			"title": "Raymond: Check Safe.",
			"embeds": ["/static/content/3.gif"],
			"text": [
				"You walk over to check out the safe on the far side of the room.",
				"Despite it being a high security safe, you prefer to keep it unlocked and just use it for regular storage.",
			]
		},
		4: {
			"title": "Raymond: Open it.",
			"embeds": ["/static/content/4.gif"],
			"text": [
				"You open the safe and peruse the contents. Inside is a SUITCASE, a PEN, a ROLL OF DUCT TAPE, a CLIPBOARD, a BACKUP NOOKPHONE, a copy of HARRY POTTER AND THE PHILOSOPHER'S STONE on DVD, and 100 BELLS.",
				"Yeah, this is pretty much just a bunch of junk."
			]
		},
		5: {
			"title": "Raymond: Take Everything.",
			"embeds": ["/static/content/5.gif"],
			"text": [
				"It occurs to you for a second to pick up all the junk in your safe, but you quickly dismiss this as extremely stupid. You don't even have enough space in your pockets to do this!",\
				"You will, however, pick up the SUITCASE, 100 BELLS, CLIPBOARD, and PEN. A pen and paper can be very useful.",
				"By picking up and equipping the suitcase, your pockets gain 4 extra slots.",
			]
		},
		6: {
			"title": "Raymond: Check NookPhone.",
			"embeds": ["/static/content/6.gif"],
			"text": [
				"Oh, you almost forgot! While you're down here scrambling around and checking things, you might as well check your trusty NookPhone.",
				"On here are several useful apps. Your current favorite is Discord, a sleek messaging app that you use to keep in contact with all your friends. Your best friend Marshal suggested you download it recently and you thought you'd give it a try.",
				"Speaking of which, he's sent you a bunch of messages since you started mucking about your house. You'd better check them right away!"
			]
 		},
		7: {
			"title": "Raymond: Read Messages.",
			"embeds": ["/static/content/7.gif"],
			"chatlog": {
				"name": "Message Log",
				"text": [
					"[c:#026F5C:MARSHAL: yoooo hey]",
					"[c:#026F5C:MARSHAL: raymond]",
					"[c:#026F5C:MARSHAL: whatsup]",
					"[c:#626262:RAYMOND: Hello Marshal.]",
					"[c:#626262:RAYMOND: Sorry for the late response, I was a little busy.]",
					"[c:#026F5C:MARSHAL: yeah hey]",
					"[c:#026F5C:MARSHAL: what're you up to]",
					"[c:#626262:RAYMOND: I'm waiting on a package that was said to arrive today.]",
					"[c:#026F5C:MARSHAL: oh yeah]",
					"[c:#026F5C:MARSHAL: i heard about that]",
					"[c:#026F5C:MARSHAL: isn't it from like someone anonymous??]",
					"[c:#626262:RAYMOND: Yeah.]",
					"[c:#026F5C:MARSHAL: hm]",
					"[c:#026F5C:MARSHAL: ok well to be honest if i were you i don't think i'd open that package]",
					"[c:#026F5C:MARSHAL: knowing your reputation it probably has like a pipe bomb in it]",
				  "[c:#026F5C:MARSHAL: doesn't it seem a bit fishy to you?]",
					"[c:#626262:RAYMOND: Relax, Marshal, there's absolutely no way.]",
					"[c:#626262:RAYMOND: Why would someone send me of all people a bomb?]",
					"[c:#626262:RAYMOND: Seems like a bit too much effort, don't you think?]",
					"[c:#626262:RAYMOND: I mean, if it were up to me, I'd blow up something much more interesting.]",
					"[c:#626262:RAYMOND: Not just some random house inhabited by some random ass dude.]",
					"[c:#026F5C:MARSHAL: ok well nevermind then]",
					"[c:#026F5C:MARSHAL: what do you think could even be in it]",
					"[c:#026F5C:MARSHAL: i don't know i'm just a little concerned about this]",
					"[c:#626262:RAYMOND: I really have no idea.]",
					"[c:#626262:RAYMOND: The both of us are just gonna have to wait and find out, I guess.]",
				]
			},
		},
		8: {
			"title": "Raymond: Send Marshal Dank Meme.",
			"hidden": True,
			"embeds": ["/static/content/8.gif"],
			"text": [
				"An awkward silence in the conversation follows and you decide to loosen the mood by sending a very dank meme. You search your phone and find an image you give a quick chuckle before sending to Marshal.",
				"Unfortunately, this only serves to make the situation more awkward and you continue to get completely ignored.",
				"You decide it's time to get back to doing what you were doing before.",
				"also this is probably going to be the last page of the comic ever made because the team kind of just abandoned it lol",
			]
 		},
	}