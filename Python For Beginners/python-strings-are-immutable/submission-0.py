def remove_fourth_character(word: str) -> str:
    new = word[:3]
    new2 = word[4:]
    return new + new2


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
