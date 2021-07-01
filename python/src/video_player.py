"""A video player class."""

from .video_library import VideoLibrary

is_playing = False
previous_video = None
is_paused = False
now_playing = False
playing_title = True
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.isPlaying = False
        self.video_playing_id = None
        self.playlist_id = 0
        self.playlist_list = []
        self.videoflag = False

    def video_name(self, video_id):
        video = self._video_library.get_video(video_id)
        return video.title

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videos = self._video_library.get_all_videos()
        print("Here's a list of all available videos:")
        temp_list = []

        for vid in videos:

            # Convoluted way to display tags in required format
            tags = "["
            for tag in vid.tags:
                tags = tags + tag + " "
            tags = tags + "]"

            if tags != "[]":
                tags = tags[0:len(tags) - 2] + "]"

            # Put all videos in a list for sorting
            temp_list += [f"{vid.title} ({vid.video_id}) {tags}"]

        # Sort the list and display
        sorted_list = sorted(temp_list)
        for x in sorted_list:
            print(x)


    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)

        # Use try function when it inevitably throws an error

        try:
            temp = video.title
            if self.is_playing == False:
                print(f'Playing video: {video.title}')
                self.is_playing = True
                self.is_paused = False
                self.Video_Playing_id = video_id
            else:
                print(f'Stopping video: {self.video_name(self.Video_Playing_id)}')
                print(f'Playing video: {video.title}')
                self.Video_Playing_id = video_id
                self.is_paused = False
        except:
            print('Cannot play video: Video does not exist')

    def stop_video(self):
        """Stops the current video."""

        print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""
        global is_playing
        global is_paused
        global previous_video
        global now_playing

        # Find all available videos and select random video from the list.
        now_playing = random.choice(self._video_library.get_all_videos())
        # Check if a video is playing, if yes then skip and play next video.
        if is_playing:
            print(f'stopping video: {previous_video}')
            print(f'Playing video: {now_playing.title}')
            is_playing = True
            is_paused = False
        # If no video is playing, find and play a random video
        else:
            print(f'Playing video: {now_playing.title}')
            is_playing = True
            is_paused = False
        # Change variable values
        previous_video = now_playing.title



    def pause_video(self):
        """Pauses the current video."""
        if self.is_paused == False:
            print(f'Pausing video: {previous_video}')
            self.is_paused = True
        else:
            print(f'Video already paused: {previous_video}')






    def continue_video(self):
        """Resumes playing the current video."""
        if self.is_paused == True:
            print(f'Continuing video: {previous_video}')
        if self.is_playing == None:
            print("Cannot continue video: no video is currently playing.")
        if self.is_paused == False and self.is_playing !=None:
            print("Cannot continue video: video is not paused")
        self.is_paused = False



    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
