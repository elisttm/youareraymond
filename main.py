import flask, waitress, markupsafe, os, json, re, urllib, urllib.request, requests, itertools
from flask import Flask, render_template, send_from_directory, request, redirect, make_response, url_for, session, abort
from markupsafe import Markup
from waitress import serve
from requests import get
from pages.pages import p
from pages.extra import e
from pages.beta import bp

# 		========================

app = Flask(__name__, 
	static_folder='static', 
	template_folder="templates"
) 
app.secret_key=os.getenv("FLASK_KEY")
cookie_age = 60*60*24*365*2 # 2 years

def load_db(path:str): 
	with open(path) as data_json: 
		return json.load(data_json)

def dump_db(path:str, data): 
	with open(path, 'w') as outfile: 
		json.dump(data, outfile)

r_re = r'\[{}(.*?)\]'
replacements_0 = ['br','hr','h1','h2','h3','h4','h5','h6','b','i','u','s','sup','sub']
replacements_1 = {
	'c:': '<span style="color:{}">{}</span>',
	'f:': '<span style="font-family:{}">{}</span>',
	'a:': '<a href="{}">{}</a>',
}

def cformat(c):
	for img_params in re.findall(r_re.format('img:'), c):
		params = img_params.split(":", 1)
		img_class = ''
		if len(params) == 2: 
			img_class = params[1]
		c = c.replace(f'[img:{img_params}]', f'<img src="{params[0]}" class="{img_class}"/>')
	for embed_url in re.findall(r_re.format('embed:'), c):
		if embed_url[-3:].lower() == 'wav' or embed_url[-3:].lower() == 'mp4':
			av_format = 'video'
			if embed_url[-3:].lower() == 'wav':
				av_format = 'audio'
			av_type = av_format+"/"+embed_url[-3:].lower()
			embed_replacement = f'<{av_format} controls><source src="{embed_url}" type="{av_type}"></{av_format}>'
		else:
			embed_replacement = f'<div class="iframe-c"><iframe src="{embed_url}" frameborder="0"></iframe></div>'
		c = c.replace(f'[embed:{embed_url}]', embed_replacement)
	for x, y in replacements_1.items():
		for x_params in re.findall(r_re.format(x), c):
			params = x_params.split(":", 1)
			c = c.replace(f'[{x}{x_params}]', y.format(params[0], params[1]))
	for x in replacements_0:
		for y in re.findall(r_re.format(x), c):
			if y[0] == ':': 
				c = c.replace(f'[{x}{y}]', f'<{x}>{y[1:]}</{x}>')
			else: 
				c = c.replace(f'[{x}]', f'<{x}>')
	return Markup(c)

class a():
	title = "You Are Raymond" 
	desc = "A webcomic that follows the quirky misadventures of Raymond from Animal Crossing."
	discord = "https://discord.gg/DrqqEFpNva"
	
	submissions = "https://discord.com/channels/695967253900034048/757368684460376198"
	
	header_items = {
		"story": "/page/1",
		"pages": "/page/list",
		"extras": "/extras"
	}

# 		========================

@app.route('/')
def yar_index():
	style = p.styles["default"]
	recent_page = list(p.pages.keys())[-1]
	while 'hidden' in p.pages[recent_page]:
		recent_page -= 1 
	return render_template('index.html', p = p, recent_page = recent_page, style = style, cformat = cformat, a = a)

@app.route('/page/<page>')
@app.route('/page/<page>/')
def yar_page(page):
	if not page:
		page = 1
	pstr = False; style = None
	if page != 'list':
		try: 
			page = int(page)
		except: 
			pstr = True
		if page not in p.pages: # or ('hidden' in p.pages[page] and p.pages[page]['hidden']) 
			page = 'error'
			pstr = True
		if ('style' in p.pages[page]):
			style = p.pages[page]['style']
		else:
			for chapter in p.chapters:
				if page in p.chapters[chapter]['pages']:
					style = p.chapters[chapter]['style']
	if not style:
		style = p.styles['default']
	return render_template('page.html', page = page, p = p, pstr = pstr, style = style, cformat = cformat, a = a)
	 
@app.route('/beta/page/<page>')
@app.route('/beta/page/<page>/')
def yar_beta_page(page):
	if not page:
		page = 1
	pstr = False; style = None
	if page != 'list':
		try: 
			page = int(page)
		except: 
			pstr = True
		if page not in bp.pages: 
			page = 'error'
			pstr = True
		if ('style' in bp.pages[page]):
			style = bp.pages[page]['style']
		else:
			for chapter in bp.chapters:
				if page in bp.chapters[chapter]['pages']:
					style = bp.chapters[chapter]['style']
	if not style:
		style = bp.styles['default']
	return render_template('extras/betapage.html', beta = True, page = page, bp = bp, pstr = pstr, style = style, cformat = cformat, a = a)


@app.route('/extras')
@app.route('/extras/')
@app.route('/extras/<extra>')
def yar_extra_page(extra=None):
	if extra is None:
		extra = 'list'
	return render_template('extras/extra.html', e = e, extra = extra, cformat = cformat, a = a)

#			------------------------

@app.route('/secret/secretfolder/homework/donotopen/youareraymond/ideas.txt')
def static_from_root():
	return send_from_directory(app.static_folder+'/content/extra/', "ideas.txt")

# 		========================

if __name__ == '__main__':
	serve(app, host='0.0.0.0', port=8080)