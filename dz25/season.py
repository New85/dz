class Season:
    def __init__(self, name: str = '', number_of_episodes: int = 1, episode_list: list = []):
        self.__name = name
        self.__number_of_episodes = number_of_episodes
        self.__episode_list = episode_list

    def show(self):
        print(self.__name, self.__number_of_episodes, self.__episode_list)
