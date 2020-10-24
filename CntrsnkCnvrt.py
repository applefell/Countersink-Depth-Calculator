convert_to_feed_angle = float(input("What is the angle of the countersink?"))
convert_to_feed_desired = float(input("What is the desired countersink diameter?"))
convert_to_feed_existing = float(input("What is the size of the existing hole?"))

if convert_to_feed_angle == 60:
    feed = ((convert_to_feed_desired - convert_to_feed_existing)/ 2) * 1.732
    print("The countersink has to go " + str(feed) + " inches deep.")
elif convert_to_feed_angle == 82:
    feed = ((convert_to_feed_desired - convert_to_feed_existing)/ 2) * 1.15
    print("The countersink has to go " + str(feed) + " inches deep.")
elif convert_to_feed_angle == 90:
    feed = (convert_to_feed_desired - convert_to_feed_existing) / 2
    print("The countersink has to go " + str(feed) + " inches deep.")
elif convert_to_feed_angle == 100:
    feed = ((convert_to_feed_desired - convert_to_feed_existing) / 2) * 0.839
    print("The countersink has to go " + str(feed) + " inches deep.")
else:
    print("There was an error :(")
