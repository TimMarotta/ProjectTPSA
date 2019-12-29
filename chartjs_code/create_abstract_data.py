import json
from datetime import datetime


def make_javascript_files(filename):
    f = open("text/" + filename + ".txt", "r")
    # separate dictionaries from text file
    raw = f.read()[1:].split("}__{")

    # separate each dictionary into its respective key value pairs
    dicts = []
    for j in range(len(raw)):
        tweet_dict = {}
        # add text
        # tweet_dict["\'text\'"] = raw[j][raw[j].find("\'text\'") + 8: raw[j].find("\'time\'") - 2]

        # add time
        tweet_dict["x"] = raw[j][raw[j].find("\'time\'") + 8: raw[j].find("\'sentiment\'") - 2]

        # add sentiment
        tweet_dict["y"] = raw[j][raw[j].find("\'sentiment\'") + 13:]
        dicts.append(tweet_dict)

    # convert sentiment string into float
    for x in range(len(dicts)):
        if "y" in dicts[x]:
            try:
                dicts[x]["y"] = float(dicts[x]["y"])
            except ValueError:
                if dicts[x]["y"][:1].isdigit() is False and dicts[x]["y"][
                                                                        :1].isdigit() is not ".":
                    dicts[x]["y"] = float(dicts[x]["y"][1:])
                elif dicts[x]["y"][-1].isdigit() is False and dicts[x]["y"][-1] is not ".":
                    dicts[x]["y"] = float(dicts[x]["y"][:-1])
        else:
            print("Cannot find sentiment. Index " + str(x))
            for a, y in dicts[x].items():
                print(a, y)

    # convert time from string to datetime
    for y in range(len(dicts)):
        stripped = dicts[y]["x"][1:-1]
        dicts[y]["x"] = datetime.strptime(stripped, '%Y-%m-%d %H:%M:%S').isoformat()

    # create averages for every 250 tweets
    average_sentiment = []
    average_time = []
    for i in range(0,50):
        average_time.append(dicts[(250*i)+125]["x"])
        sentiment = 0.0
        for j in range(0,250):
            sentiment += dicts[(250*i)+j]["y"]
        average_sentiment.append(sentiment/250)

    #pair elements of two lists into a dictionary
    abstracted = []
    for i in range(0,50):
        data = {}
        data["x"] = average_time[i]
        data["y"] = average_sentiment[i]
        abstracted.append(data)

    with open("js_abstract/" + filename + ".js", "w") as of:
        of.write(json.dumps(abstracted, indent=4, sort_keys=True))


def main():
    names = ["amy_klobuchar", "andrew_yang", "bernie_sanders", "democrat", "donald_trump",
             "elizabeth_warren", "joe_biden", "pete_buttigieg", "republican", "tom_steyer"]

    for i in range(len(names)):
        print(names[i])
        make_javascript_files(names[i])
    print("Done.")


if __name__ == '__main__':
    main()
