


#   The first line of a file contains the column headings. The columns are
#
# Team – The name of the county
#
# Wins – The number of times that county won the All-Ireland final
#
# Last final won – The year of the county’s most recent win (- means they never won it)
#
# Runners-up – The number of finals they lost
#
# Last final lost – The year of the county’s most recent final loss (- means they never lost)
#
# Total final appearances – The number of finals they appeared in

teams = []
wins = []
last_final_wons = []
runners_ups = []
last_final_losts = []
total_final_appearances = []

# win/appearance
highest_win_ratios = []

with open("camogie.csv", "r") as data_file:

    _ = data_file.readline()

    for line in data_file:

        team, win, last_final_won, runners_up, last_final_lost, total_final_appearance = line.split(",")

        teams.append(team)

        wins.append(int(win))

        if last_final_won == "-":
            last_final_wons.append(0)
        else:
            last_final_wons.append(float(last_final_won))

        runners_ups.append(int(runners_up))

        last_final_losts.append(int(last_final_lost))

        total_final_appearances.append(int(total_final_appearance))

        highest_win_ratios.append(int(win)/int(total_final_appearance))

number_of_counties = len(teams)

total_finals = sum(runners_ups)

average_wins_per_county = sum(wins)/len(wins)

current_champions = teams[last_final_wons.index(2022)]

sorted_wins = sorted(wins)

most_wins_amount = sorted_wins[-1]

most_wins_county = teams[wins.index(most_wins_amount)]

most_recent_win_for_most_winner = int(last_final_wons[teams.index(most_wins_county)])

sorted_highest_total_ratios = sorted(highest_win_ratios)

highest_total_ratio = sorted_highest_total_ratios[-1]

county_with_highest_t_ratio = teams[highest_win_ratios.index(highest_total_ratio)]

most_recent_win_for_highest_ratio_county = int(last_final_wons[teams.index(county_with_highest_t_ratio)])

print("Number of Counties:", number_of_counties)
print("Total number of All-Ireland finals:", total_finals)
print("Average number of wins per county:", average_wins_per_county)
print("Current champions (winners in 2022):", current_champions)
print("Most wins: {} with {} wins, most recently in {}".format(most_wins_county, most_wins_amount, most_recent_win_for_most_winner))
print("Highest Win Ratio: {} with {}%, most recently in {}".format(county_with_highest_t_ratio, int(highest_total_ratio*100), most_recent_win_for_highest_ratio_county))
