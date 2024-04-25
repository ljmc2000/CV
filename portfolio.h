#ifndef PORTFOLIO_H
#define PORTFOLIO_H

var portfolio_projects = [
	{
		name: "Chessboard2Net",
		description: "A rewrite of Chessboard.Net in node and AngularJS with additional features such as custom colours on pieces, replays, spectating, all rules of chess working as expected and the entire additional game of checkers. This one is not intercompatible with the older one due to protocol and database changes",
		skills: "Node, AngularJS, PostgreSQL",
		preview: "Chessboard2Net.png",
		source: "https://github.com/ljmc2000/Chessboard2Net",
		demos: [
			['video', "https://www.youtube.com/watch?v=jRb4yOLAqn8"],
			['live', "https://chessboardnet.delilahsthings.ie"],
		],
	},
	{
		name: "Chessboard.net",
		description: "A project for android programming in 3rd year. Utilizing Android Studio, OpenJDK, TCPIP, python flask, MongoDB, XML and InkScape, I made a simple application to allow 2 human opponents to play chess. The application kept a tally of victories and losses and allowed extra chess sets to be unlocked upon winning a certain number of games.",
		skills: "Android, MongoDB",
		source: "https://github.com/ljmc2000/Chessboard.net",
		preview: "ChessboardPreview.png",
		demos: [
			['video', "https://youtu.be/MnvaOpltS2Y"],
		],
	},
	{
		name: "Soothing Noise Player",
		description: "So There's this app called blanket on flathub which lets you mix sound effects to create a calming atmosphere. I made an android port.",
		skills: "Android, Java",
		preview: "NoiseLooperPreview.png",
		source: "https://github.com/ljmc2000/NoiseLooper",
		demos: [
			['video', "https://youtu.be/LIJsYYhpsC0"],
			['fdroid', "https://f-droid.org/en/packages/ie.delilahsthings.soothingloop/"],
		],
	},
	{
		name: "Nothesia",
		description: "Visualize MIDI data using the QT5 framework. Pressed keys turn a shade of gray, and while held emit coloured rectangles.",
		skills: "Qt5, Midi",
		preview: "NothesiaPreview.png",
		source: "https://github.com/ljmc2000/nothesia",
		demos: [
			['video', "https://youtu.be/h44gcPVK7eA"],
		],
	},
	{
		name: "VirtualConcertHall",
		description: "My collage final year project. Utilizing the power of Microsoft Azure, the QT5 framework, python flask, MIDI, MongoDB, and Docker containers, this project allows musicians with MIDI compatible instruments to jam together across distinct geolocations.",
		skills: "Qt5, Docker",
		preview: "VirtualConcertHallPreview.png",
		source: "https://github.com/ljmc2000/VirtualConcertHall",
		demos: [
			['video', "https://www.youtube.com/watch?v=8XXBoIQZL4s"],
		],
	},
	{
		name: "Fishy Chips V1 & V2",
		description: "My first interactive website, developed in 2nd year for a collage module, for the fictional restaraunt \"Fishy Chips\". Utilizing HTML, PHP and MySQL, it allowed a user to order food, cancel an unfulfilled order or browse past orders. It was later rewritten in Python+CGI while maintaining database compatibility such that a v1 and v2 instance could share a database",
		skills: "PHP, MySQL",
		preview: "FishyChips.png",
		source: "https://github.com/ljmc2000/fishy-chips",
		demos: [
			['video', "https://youtube.com/watch?v=jvCFFNhoMMQ"],
			[ 'v1', "https://fishychipsv1.delilahsthings.ie"],
			[ 'v2', "https://fishychipsv2.delilahsthings.ie"],
		],
	},
	{
		name: "Oh Christmas-Tree",
		description: `An assignment for the "Game Engines" module. Generate a forest of trees with random heights and positions. Made in the Unity engine with C# Scripting.`,
		skills: "Unity, C#",
		preview: "ChristmasTreesPreview.png",
		source: "https://github.com/ljmc2000/GameEngines1Assignment",
		demos: [
			['video', "https://www.youtube.com/watch?v=ltsh8RBHQcY"],
		],
	},
	{
		name: "Solar System",
		description: "Generate an animated model of our solar system. Calculate absolute positions of planets and moons relative to their planets and the sun. Individual frames are drawn as SVG files then compiled into an animation using ImageMagick.",
		skills: "Python, SVG",
		preview: "SolarSystemPreview.png",
		source: "https://github.com/ljmc2000/solar-system",
		demos: [
			['video', "https://www.youtube.com/watch?v=0rkvRAaAAcE"],
		],
	},
]

#endif
