import toga


def mypysound(file):
    platform = toga.platform.current_platform
    if platform == "android":
        pass
    if platform == "ios":
        print("IOS is not supported at the moment")
    else:
        import pygame

        pygame.mixer.init()
        pygame.mixer.music.load(filename=file)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()


if __name__ == "__main__":
    pysound(file="happy-birthday-whistled.wav")
