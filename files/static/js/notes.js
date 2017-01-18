
var ViewModalManageNotes = function(){
	var self = this; 
	self.id = ko.observableArray();
	self.title = ko.observableArray();
	self.content = ko.observable();
	self.author = ko.observable();
	self.image = ko.observable(0);
	self.created = ko.observable();
	
	/*------------------------------------------------------------------------------
	 * Load all notes from web service 
	 *----------------------------------------------------------------------------*/		
	self.loadNotes = function(){
		httpRestServices.specialEvent.notes.list({}, function(response){
			
			if (Object.keys(response).length > 0){
				if (response.results.length > 0){
					var newNotes = ko.utils.arrayMap(response.results, function(noteData){
						var note = new ModelNote(noteData.id, 
												     noteData.title, 
												     noteData.content,
												     noteData.author,
												     noteData.image);
						return note
					});
					self.notes.pushAll(newNotes);
				}
			}
		});
	}
	
	self.loadImage = function(e){
		self.noteFormImage(e.target.result);
		$('#txt-image-preview').attr('src', e.target.result);
	}
	
	/*------------------------------------------------------------------------------
	 * Function to run any initialization code necessary
	 *----------------------------------------------------------------------------*/	
	self.setup = function(){
		
		$(document).ajaxStart($.blockUI).ajaxStop($.unblockUI);
		
		$("#txt-image").change(function () {
	        if (this.files && this.files[0]) {
	            var reader = new FileReader();
	            reader.onload = self.loadImage;
	            reader.readAsDataURL(this.files[0]);
	        }
	    });
		self.loadNotes();
	};	
	
};