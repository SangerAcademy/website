// https://css-tricks.com/fluid-width-youtube-videos/  Might have problems with WebKit and need this:
// http://www.paulirish.com/2009/throttled-smartresize-jquery-event-handler/
$(function() {

	// Find all YouTube videos
	var $allVideos = $("iframe[src^='https://www.youtube.com']"),

	// The element that is fluid width
	$fluidEl = $("#content");

	// Figure out and save aspect ratio for each video
	$allVideos.each(function() {

		$(this)
			.data('aspectRatio', this.height / this.width)

			// and remove the hard coded width/height
			.removeAttr('height')
			.removeAttr('width');
	});

	// When the window is resized
	// (You'll probably want to debounce this)
	$(window).resize(function() {

		var newWidth = 560;
		if ($fluidEl.width() < 560) {
			newWidth = $fluidEl.width();
		}

		// Resize all videos according to their own aspect ratio
		$allVideos.each(function() {

			var $el = $(this);
			$el
				.width(newWidth)
				.height(newWidth * $el.data('aspectRatio'));

		});

	// Kick off one resize to fix all videos on page load
	}).resize();

});