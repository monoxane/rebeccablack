#!/usr/bin/python
		
from random import randint

class Insults(object):
	def __init__(self):
		self.test="test"

	def adjective(self):
		adj = [
			"delusional",
			"disproven",
			"poorly-researched",
			"needhamish",
			"so-called",
			"jumped-up",
			"touch-typing",
			"randian",
			"tree-hugging",
			"bleeding-heart",
			"sickly",
			"primitive",
			"dell loving",
			"cunt faced",
			"bassoonist",
			"oboe-playing",
			"big fat",
			"freedom-hating",
			"functional gab",
			"excel-loving",
			"post-technical",
			"bowlcut",
			"dirigible-shaped",
			"enterprisey",
			"ruby threaded",
			"hipster",
			"DoctorDalek imitating",
			"tinsel cheeked",
			"stinky",
			"tiny-minded",
			"pea-brained",
			"heavily lidded",
			"muck minded",
			"flat footed"
			"antiquated",
			"asinine",
			"banal",
			"brazen",
			"catty",
			"churlish",
			"clammy",
			"contrary",
			"daft",
			"damned",
			"deceitful",
			"decrepit",
			"decrepit",
			"deficient",
			"degrading",
			"deleterious",
			"devoid",
			"dim",
			"dismal",
			"disreputable",
			"dopey",
			"dreary",
			"drunken",
			"dubious",
			"dysfunctional",
			"fatuous",
			"fatuous",
			"feckless",
			"glib",
			"grotesque",
			"imbecilic",
			"impertinent",
			"indecorous",
			"indiscreet",
			"infantile",
			"jejune",
			"lurid",
			"malevolent",
			"misshapen",
			"morbid",
			"moribund",
			"mundane",
			"petulant",
			"puerile",
			"rambunctious",
			"repugnant",
			"truculent",
			"unkempt",
			"vainglorious",
			"vapid"
		]
		rand = randint(1,len(adj)-1)
		return adj[rand]
	
	def nouns(self):
		noun = [
			"decepticon",
			"kief",
			"suit",
			"luser",
			"sharepoint-developer",
			"liberal",
			"socialist ",
			"Tutankhamun",
			"gimboid",
			"person who thinks digital watches are a really neat idea",
			"smeghead",
			"jobbie-face",
			"derpgineer",
			"urban dictionary contributor",
			"manager",
			"virgin cunt",
			"power point jockey",
			"windows user",
			"brogrammer",
			"long winded fun bus hater",
			"hipster",
			"windy nonsense talker",
			"category theory dumbass",
			"smeggy pants",
			"java programmer",
			"bog warbler",
			"tin pincher",
			"yeti",
			"whoo-har",
			"cunt",
			"nincompoop",
			"nazi cunt jew",
			"Tosser",
			"Wanker",
			"Slag",
			"Cheese Eating Surrender Monkeys",
			"Daft Cow",
			"Arsehole",
			"Barmy",
			"Chav",
			"Dodgy",
			"Git",
			"Gormless",
			"Manky",
			"Minger",
			"Muppet",
			"Naff",
			"Nutter",
			"Pikey",
			"Pillock",
			"Plonker",
			"Prat",
			"Scrubber",
			"Trollop",
			"Uphill Gardener",
			"Twit",
			"Knob Head",
			"Bell End",
			"Lazy Sod",
			"Skiver",
			"Knob",
			"Wazzock",
			"Ninny",
			"Berk",
			"Airy-fairy",
			"Ankle-biters",
			"Arse-licker",
			"Arsemonger",
			"Chuffer",
			"Gannet",
			"Gone to the dogs",
			"Ligger",
			"Maggot",
			"Mingebag",
		]
		rand = randint(1,len(noun)-1)
		return noun[rand].lower()
