import utils
import re
from datetime import datetime as dt


def getLinks(url, resolution):
    if resolution == 720:
        # Define the pattern to replace
        pattern_to_replace = r"720p_\d+\.ts"
        # Define the replacement string with a placeholder; also used as Filename
        replacement_string = "720p_{}.ts"
    elif resolution == 480:
        pattern_to_replace = r"480p_\d+\.ts"
        replacement_string = "480p_{}.ts"
    else:
        print("The resolution was given incorrectly.")
        exit(1)

    # Use re.sub() to replace the pattern with the replacement string
    temp_url = re.sub(pattern_to_replace, replacement_string, url)
    allLinks = ""
    i = 1
    while True:
        if i < 10:
            number_with_zeros = "00" + str(i)
        elif i < 100:
            number_with_zeros = "0" + str(i)
        else:
            number_with_zeros = str(i)

        curr_filename = replacement_string.format(number_with_zeros)
        curr_url = temp_url.format(number_with_zeros)

        print(curr_filename, curr_url)

        if utils.url_checker(curr_url):
            allLinks += curr_url + "\n"
        else:
            print("URL not found: " + curr_url)
            # Stop the loop
            break

        i += 1

    name = "links_" + str(resolution) + ".txt"
    with open(name, "w") as f:
        f.write(allLinks)

    print("All links written to " + name)


def getLinksWithMeta(url, resolution, name, isTvShow):
    if resolution == 720:
        # Define the pattern to replace
        pattern_to_replace = r"720p_\d+\.ts"
        # Define the replacement string with a placeholder; also used as Filename
        replacement_string = "720p_{}.ts"
    elif resolution == 480:
        pattern_to_replace = r"480p_\d+\.ts"
        replacement_string = "480p_{}.ts"
    else:
        print("The resolution was given incorrectly.")
        exit(1)

    if isTvShow is True:
        print("Please enter the season number and episode number in the format S01E01")
        season_episode = input("Season and Episode: ")
        name += "_" + season_episode

    # replace all whitespaces with underscores
    name = name.replace(" ", "_")

    # check if the name is correct
    print("Is the information provided correct? " + name)
    confirmation = input("Y/N: ")
    if confirmation != "Y" and confirmation != "y":
        print("Exiting...")
        exit(1)

    timestamp = dt.now().isoformat()
    metadata = name + "_" + timestamp
    allLinks = ""

    # Use re.sub() to replace the pattern with the replacement string
    temp_url = re.sub(pattern_to_replace, replacement_string, url)
    i = 1
    while True:
        if i < 10:
            number_with_zeros = "00" + str(i)
        elif i < 100:
            number_with_zeros = "0" + str(i)
        else:
            number_with_zeros = str(i)

        curr_filename = replacement_string.format(number_with_zeros)
        curr_url = temp_url.format(number_with_zeros)

        print(curr_filename, curr_url)

        if utils.url_checker(curr_url):
            allLinks += curr_url + "\n"
        else:
            print("URL not found: " + curr_url)
            # Stop the loop
            break

        i += 1

    name = metadata + "_" + str(resolution) + "p.txt"
    content = metadata + allLinks
    with open(name, "w") as f:
        f.write(content)


# Example usage:
#getLinks("https://example.com/720p_009.ts", 720, 500)

#getLinksWithMeta("https://example.com/720p_009.ts", 720, 50, "Example Show", True)
