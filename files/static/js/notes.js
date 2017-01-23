/* Module for Notes application */
var notes = function () {

	/* the note model */
	    var note = {

			title: ko.observable(),
			content: ko.observable(),
		        	author: ko.observable()

		};
	/* array of notes */
	/*var initialData = ko.observableArray([
					{title:"title 1",content:"adsf afd afd john@content.com",author:"bineet"},
					{title:"title 2",content:"bfsda sadfadsdftm",author:"gurmukh"},
					{title: "title 3", content: "sdfkalsh kahfkasdklf jasdfj akdljf laksjdf;laksjdf ", author: "test"}
	]);*/
	var initialData = ko.observableArray();
	var authors = ko.observableArray(["User1", "User2", "User3", "User4"]);
	var selectedAuthor =ko.observable(authors()[2]);

	/* method to clear the note observable */
	var clearNote = function () {
	    note.title(null);
	    note.content(null);
	    note.author(null);
	};

	/* method to add note to initialData array */
	var addNote = function () {
		//add the note to the notes array
	    initialData.push({ title: note.title(), content: note.content(), author: selectedAuthor()});
		//clear the note
		clearNote();
	};

	self.removeNote = function(note) {
		console.log(note.title);
	          initialData.remove(note);
	};

	var init = function () {
		/* add code to initialise this module */
		ko.applyBindings(initialData);
	};

	/* execute the init function when the DOM is ready */
	$(init);

	return {
		/* add members that will be exposed publicly */
		initialData: initialData,
		note: note,
		addNote: addNote,
		removeNote: removeNote,
		authors: authors,
		selectedAuthor: selectedAuthor
	};

}();
