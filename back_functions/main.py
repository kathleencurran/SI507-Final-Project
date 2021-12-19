# import caching
# from pprint import pprint
#
# from back_functions import tree
#
# from tree import TreeNode, BinarySearchTree as bst, songtree
# import os
# from playlist import Playlist, url_parser
#
# def main():
#
#
#     pass
#
#
#     # user_input_playlist = '37i9dQZF1DXcBWIGoYBM5M'
#     # # checking_playlist = Playlist(user_input_playlist)
#     # # checking_playlist.retrieve_from_id()
#     #
#     # #
#     # def get_id(url):
#     #     url = url.split("/")
#     #     last_bit = url[-1]
#     #     id = last_bit.split("?")
#     #     return id[0]
#     #
#     #
#     # # def songs_w_cache(id):
#     # #     n_key = str(id)
#     # #     if n_key in SONG_CACHE:
#     # #         return SONG_CACHE[n_key]
#     # #     else:
#     # #         # SONG_CACHE[n_key] = retrieve_playlist(id)
#     # #         SONG_CACHE[n_key] = checking_playlist
#     # #         caching.save_cache(SONG_CACHE)
#     # #         return SONG_CACHE[n_key]
#     #
#     #
#     #
#     # '''This is the user input part of all of this '''
#     # playlist_uri = input('Enter the URL of the playlist you want to check \n')
#     # selection = input('Select the number of the vibe you\'re going for: '
#     #                   '\n 1. Party \n2. Car Jams \n3. Kickback \n4. Quiet Time \n')
#
#     # url = 'https://open.spotify.com/track/12VzUUrRwSGJmpAaFkjDcm?si=74ac51d20f554abb'
#
#     # url = 'https://open.spotify.com/playlist/4HIiPAmsWXTrmv6pfRLQHb?si=2e4c6c10fc644f73'
#     # url = 'https://open.spotify.com/playlist/1lBJ68syJlYWq6iNjSnygm?si=329f69db34444a00'
#     # pl_id = get_id(url)
#     #
#     # test_pl = Playlist(pl_id)
#     #
#     # whole_pl = test_pl.retrieve_from_id()
#     # # print(whole_pl.__dict__)
#     # pl_songs = whole_pl.playlist_tracks
#     # # print(type(pl_songs))
#     #
#     #
#     # # add them to the tree
#     # for songs in pl_songs:
#     #     print (songs.score)
#     #
#     # # print(test_pl.calc_playlist_score())
#     #
#     # print(whole_pl.determine_song_vibe())
#     #
#     # print(whole_pl.__dict__)
#     #
#     #
#     # #
#     # test_playlist_id = '1lBJ68syJlYWq6iNjSnygm'
#     # #
#     # the_playlist = Playlist(test_playlist_id).retrieve_from_id()
#     #
#
#
#
#
#     file = 'song_data.json'
#     # #
#     # my_tree = bst()
#     # #
#     # main_tree = the_playlist.create_or_add_tree(bst())
#     # # print(some_var, type(some_var))
#     # #
#     # #
#     # caching.cache_playlist(main_tree, file)
#     #
#     # def make_tree_from_cache():
#     #     pass
#     #
#     # #
#     # id = '0ydK0BtZX9Dor3lBe25bw2'
#     # #
#     # otherpl = Playlist(id).retrieve_from_id()
#     # new_tree = otherpl.create_or_add_tree(bst())
#
#     #
#     # id = '37i9dQZF1DXcBWIGoYBM5M'
#
#
#
#     url = 'https://open.spotify.com/playlist/4ZkR6u2ZfGWj1UwT7i6MwI?si=d0a52c8f46ad4941'
#     # url = 'https://open.spotify.com/playlist/6qd48xm5P7JXCxSdIQe4Ur?si=f658b17f35434106'
#
#     id = url_parser(url)
#     print('playlist id', id)
#     top_40_pl = Playlist(id).retrieve_from_id()
#     # print(top_40_pl.__dict__)
#     #
#     #
#     top_40_pl.cache_all_songs()
#
#     test_tree = tree.BinarySearchTree()
#
#     pprint(test_tree.create_tree_from_cache(filename))
#
#     print('TREE', test_tree.inorderTraversal(test_tree.root))
#     # print(test_tree.inorderTraversal(test_tree.root))
#     #
#     recs = test_tree.access_and_recommend(filename)
#     print(recs)
#
#
#
#     # pprint(content.)
#     # print(top_40_pl.score, top_40_pl.vibe)
#     # for i in top_40_pl.playlist_tracks:
#     #     print(i.score)
#     #     print(i.score)
#     # print(top_40_pl.__dict__)
#
#
#     #
#     # tree_40 = top_40_pl.create_or_add_tree(bst())
#     # caching.cache_playlist(tree_40, file)
#     #
#     # content = caching.open_cache(file)
#     # print('content\n ', len(content))
#
#
#
#     # def create_tree_from_cache():
#     #     newBST = bst()
#     #     content = caching.open_cache(file)
#     #     keys = list(content.keys())
#     #     list_of_songs = []
#     #     for item in keys:
#     #         list_of_songs.append(content.get(item))
#     #
#     #     for song in list_of_songs[0]:
#     #         newBST.put(list(song.keys())[0], list(song.values())[0])
#     #
#     #     return newBST
#     #
#     # cached_tree = create_tree_from_cache()
#     # print(cached_tree.inorderTraversal(cached_tree.root))
#
#
#     # cached_tree = tree.BinarySearchTree().create_tree_from_cache(file)
#     # print(cached_tree.inorderTraversal(cached_tree.root))
#     #
#     #
#     # score_range = cached_tree.find_range(cached_tree.root, 69,75)
#     # print(score_range)
#     # rec = cached_tree.find_recommendation(score_range)
#     # print(rec)
#
#     # main_tree.put(new_tree.inorderTraversal(new_tree.root.payload.score),
#     #               new_tree.inorderTraversal(new_tree.root.payload))
#     #
#     # print('the new tree\n')
#     # print(main_tree.inorderTraversal(main_tree.root))
#
#
#     # #
#     # # caching.cache_playlist(new_tree, file)
#     #
#     # # file[]= []
#     #
#     # new_tree.put()
#     #
#     #
#     #
#     #
#     # content = caching.open_cache(file)
#     # print('content\n ', content.get())
#     #
#     # caching.clear_cache(file)
#
#     # song_tree = bst()
#     #
#
#
#     #
#     # # print('see all og pl', the_playlist.__dict__)
#     # print('songtree')
#     #
#     # print(song_tree.inorderTraversal(song_tree.root))
#     #
#     # the_playlist.cache_playlist(song_tree, tree_file)
#     # content = caching.open_cache(tree_file)
#     #
#     # print('content\n ', type(content))
#
#
#     # print('\n\n\n again \n\n\n')
#     # ~~~~~~~~~~~~~~`
#     #
#     # new_id = '0ydK0BtZX9Dor3lBe25bw2'
#     # new_pl = Playlist(new_id).retrieve_from_id()
#     # new_pl.vibe = new_pl.determine_song_vibe()
#     #
#     # new_pl.cache_playlist(song_tree, tree_file)
#     #
#     # print('\n')
#     # new_content = caching.open_cache(tree_file)
#     # print('content\n ', new_content)
#     #
#     # caching.clear_cache(tree_file)
#     # new_content = caching.open_cache(tree_file)
#
#     # list_of_songs = checking_playlist.playlist_tracks
#     # # print(list_of_songs)
#     #
#     # for i in list_of_songs:
#     #     print('traversing')
#     #     song_tree.add_more_than_one(i)
#     # # key = 84.0
#     # print('\n\n\n\n')
#     # a = None
#     #
#     #
#     # print(song_tree.inorderTraversal(song_tree.root))
#     #
#     #
#     # # print('getting', song_tree.get(key).name, song_tree.get(key).score)
#     #
#     # TREE_CACHE = caching.open_cache(tree_file)
#
#     # print(caching.store_cache_data(song_tree, TREE_CACHE, tree_file))
#     #
#     #
#     # # caching.clear_cache(tree_file)
#     #
#     # content = caching.open_cache(tree_file)
#     # print(type(content))
#     # # content
#     # # branch = list(content.values())
#     # # print('branch', branch )
#     # for item in branch[0]:
#     #     print('otem ', int(item.keys()))
#     # # print('trying to open', caching.open_cache(tree_file))
#     #
#     #
#     # SONG_CACHE = caching.open_cache(song_file)
#
#
# if __name__ == "__main__":
#     main()
#
