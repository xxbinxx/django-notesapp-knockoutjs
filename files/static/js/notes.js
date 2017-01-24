var ModelNote = function(id, title, content, author, image){
	var self = this;
	self.id = id;
	self.title = title;
	self.content = content;
	self.author = author;
	self.image = image;
}

var ViewModelNotes = function() {

	var self = this;

	self.note = {
		id: ko.observable(0),
		title: ko.observable(),
		content: ko.observable()
	};

	self.notes = ko.observableArray([]);

	self.authors = ko.observableArray([]);

	self.uniqueAuthors = ko.utils.arrayGetDistinctValues(self.authors).sort();

	self.selectedAuthor =ko.observable(self.authors()[0]);

	self.loadNotes = function(){
		console.log('Getting data from API');
		$.get( 'api/notes/', function(response, status){
		        	console.log("Status: " + status);
	 		var newNotes = ko.utils.arrayMap(response.results, function(notesData){
	 			var note = new ModelNote(notesData.id,
	 			                         notesData.title,
	 			                         notesData.content,
	 			                         notesData.Author,
	 			                         notesData.image);
	 			self.notes.push(note);
	 			self.authors.push(note.author);
	 			return note
	 		});

		    });
		console.log('Done');
	}

	self.clearNote = function () {
		note.title(null);
		note.content(null);
		note.author(null);
	};

	self.removeNote = function(note) {
		console.log(note.title);
		$.ajax({
			type: 'DELETE',
			url: 'api/notes/' + note.id + '/',
				success: function(result) {
				console.log('Delete succes! ');
				self.notes.remove(note);
			},
			error: function(error) {
				alert('Failed to delete! ');
			}
		  });
	};

	self.addNote = function(){
		$.ajax("/api/notes/", {
		            data: ko.toJSON({ title: self.note.title(), content: self.note.content(), Author:1 }),
		            type: "post", contentType: "application/json",
		            success: function (result) {
		            	console.log(result)
				self.notes.push({
					id: result.id,
					title: result.title,
					content: result.content,
					author: self.selectedAuthor()
				});
		            }
		        });
		console.log(self.note.title());
	}

	self.setup = function(){
		self.loadNotes();
	}
};

var ViewModelNotes = new ViewModelNotes();
ko.applyBindings(ViewModelNotes);
ViewModelNotes.setup();

