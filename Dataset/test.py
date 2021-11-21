import sys
league, year, match = [""]*3
if len(sys.argv) >= 4:
    league, year, match = sys.argv[1], sys.argv[2], " ".join(sys.argv[3:])
print("HI", league, "YEAR", year, "MATCH", match)