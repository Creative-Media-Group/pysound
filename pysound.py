import toga


def pysound(file):
    platform = toga.platform.current_platform
    if platform == "android":
        pass
    if platform == "ios":
        print("IOS is not supported at the moment")
    else:
        import pygame

if __name__ == "__main__":
    pysound(file=)