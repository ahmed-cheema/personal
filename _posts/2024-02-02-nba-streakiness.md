---
layout: single
title: "Quantifying the Streakiness of NBA Shooters "
category: projects
permalink: /projects/streakiness/
---

*The following analysis was originally published on [December 23rd, 2021](https://www.thespax.com/nba/quantifying-the-streakiness-of-nba-shooters/).*

Over the course of his ongoing NBA career, Danny Green has hit 1504 regular season three-pointers at an elite 40% clip. His combination of shooting and defensive ability have made him a valuable 3&D role player, leading to NBA titles for the San Antonio Spurs, Toronto Raptors, and Los Angeles Lakers. Needless to say, Green is one of the better catch-and-shoot perimeter players in recent memory.

However, Green is also known for the inconsistency of his shooting. While his career 40% three-point percentage casts no doubt on the general effectiveness of his jumper, it doesn’t tell us anything about his streakiness as a shooter. Green’s nickname “Icy-Hot” represents his reputation as a player who can be prone to extremely poor stretches of shooting or stretches where he seemingly can’t miss.

We know that we can measure a shooter’s efficiency by simply computing their made three-point field goals divided by their attempts. But how can we measure their consistency (or lack thereof)? How can we determine whether Green is actually a particularly inconsistent shooter or if his reputation just comes from the increased spotlight of a player almost always on a contending team?

We will represent a series of shot attempts as a binary sequence, or a series of ones and zeros. A one will represent a successful three-point shot while a zero will represent an unsuccessful three-point shot. We will only be considering three-point shots because while they do vary in terms of difficulty (shot distance, location, level of contest, catch-and-shoot vs. off the dribble, etc), their circumstances are generally more consistent than for other types of shots.

Consider the following sequence of ten successive shots.

$$x=\begin{bmatrix}1 & 1 & 1 & 0 & 0 & 1 & 0 & 1 & 1 & 0\end{bmatrix}$$

We'll quantify the streakiness of this binary sequence as $$\text{SSG}=\sum_{i=1}^{n} g_{i}^2$$ where $$g_i$$ represents the length of the $i$th gap between successes (ones) in $$x$$ and $$n$$ is equal to the total number of gaps. Thus, in this example we see that $$g=\begin{bmatrix}0 & 0 & 0 & 2 & 1 & 0 & 1\end{bmatrix}$$. Three consecutive successes at the start of the sequence correspond with three gaps of length zero, then we see a gap of length two followed by a gap of length one, and so on. Finally, we compute $$\sum_{i=1}^{n} g_{i}^2=6$$.

The number $$6$$ doesn't tell us much on its own. The next step is to derive a p-value for this observed value by running a randomization test based on $$10000$$ permutations of the binary sequence $$x$$. In other words, we will randomize the order of the values in $$x$$ and repeat the process above to calculate $$\text{SSG}$$. By doing this for $$10000$$ iterations, we will be able to determine how extreme our observed value is compared to expectation.

Shown below is the histogram of the sum of squared gaps for all $$10000$$ iterations of the randomization test.

<img src="/assets/StreakySampleRandTest.svg" alt="Histogram of the sum of squared gaps for all 10,000 iterations of the randomization test" style="margin: auto; border: dotted 0.5px black;">

Given the short length of $x$ in this example, there are only five possible values of $$\text{SSG}$$. In total, $$\text{SSG}\geq6$$ for $$7890$$ of the $$10000$$ iterations, yielding a p-value of $$0.789$$. A p-value of $$1$$ represents perfect consistency while p-values closer to $$0$$ are indicative of greater streakiness. There is no reason to think that the example binary sequence $$x$$ is inconsistent at all, but we're interested in larger sample sizes. Let's move on to the focus of this article.

I calculated the aforementioned p-value for the players in the top 100 for three-point attempts since the 2015-16 season. I also only analyzed the three-point attempts for each player from that 2015-16 season to today's date. The choice of the 2015-16 season as a cutoff was somewhat arbitrary, but it felt appropriate as it was the first season after the Warriors proved that a jumpshooting team could win the Finals (or at least that was the mainstream narrative following the 2015 Finals).

Let's go back to the example of Danny Green. The sum of squared gaps for the binary sequence representing his $$2710$$ attempts in this dataset is equal to $$7441$$. It's not a particularly meaningful number on its own, but we can run our randomization test to determine just how abnormal this value is.

<img src="/assets/StreakyDannyRandTest.svg" alt="SSG randomization test histogram for Danny Green" style="margin: auto; border: dotted 0.5px black;">

The p-value for this test is $$0.0949$$, suggesting that Green's shooting over the past seven seasons has been streakier than we'd expect on average assuming that he was a perfectly consistent shooter (i.e. all of the permutations of the binary sequence would be equally likely).

We can repeat the same process for each player and have the p-value represent their consistency (as a lower p-value suggests greater streakiness). A plot of the results is shown below (the full data is at the bottom of the article).

<img src="/assets/StreakyScatterPlot.svg" alt="Scatter plot of each player's 3PT% vs. consistency" style="margin: auto; border: dotted 0.5px black;">

I plotted the p-value from the randomization test for each player on the x-axis and their three-point percentage on the y-axis. It should be noted that that three-point percentage isn't a perfect measure of shooting ability because different players attempt shots of varying difficulty. For example, Joe Harris' attempts are certainly easier to convert than Steph Curry's. Still, 3PT% is a good estimate of shooting ability for this sample size.

The players on the left side of the plot tend to be streakier shooters, and a lot of those names aren't super unexpected. Harden, Bertans, Thompson, Oubre, Smart, etc are all players who would generally be considered streaky by NBA fans and it seems that this reputation is justified. Of course, the shooting ability among these names varies a lot. Klay Thompson may be streaky, but he's still one of the greatest shooters of all-time. When he's hot, he's hot. 

On the other side, we see the shooters that have generally been more consistent. The top right includes some of the better shooters in recent memory, including the best shooter ever in Steph Curry. Curry's combination of elite efficiency & consistency on his difficult shot selection is truly remarkable.

The bottom right has players who are poor shooters and, well, consistently poor. You don't really hear about Aaron Gordon or Dennis Schroder's recurring hot streaks from deep, so it makes sense to see them have high consistency. 

This raises an interesting question regarding the value in consistency. I would think that a great shooter who is consistent would be preferable to a streakier elite shooter. You're less likely to have to deal with poor shooting slumps and instead getting consistent production from the perimeter. What about inefficient shooters? Would you rather have a consistent poor shooter or an inconsistent poor shooter? Is it possible that inconsistency would be beneficial in this situation because a streaky player would have the potential to be a worthwhile shooter at times? Or is consistency always preferable?

Anyway, the full data for the 100 players with the most three-point attempts since 2016 is shown below.

<table id="csvDataTable" class="table table-hover" style="width:100%">
    <thead>
        <tr>
            <th>Player</th>
            <th>Consistency</th>
            <th>3PM</th>
            <th>3PA</th>
            <th>3P%</th>
        </tr>
    </thead>
</table>

<script>
$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: "/assets/streakyresults-csv.csv",
        dataType: "text",
        success: function(data) {
            var csvData = Papa.parse(data, {
                header: true,
                skipEmptyLines: true,
                complete: function(results) {
                    $('#csvDataTable').DataTable({
                        data: results.data,
                        order: [[3, 'desc']],
                        info: false,
                        lengthChange: false,
                        columns: [
                            { data: "Player" },
                            { data: "Consistency" },
                            { data: "3PM" },
                            { data: "3PA" },
                            { data: "3P%" },
                        ],
                        "dom": "<'row'<'col-sm-12 col-md-4'f>>" +
                                "<'row'<'col-sm-12'tr>>" +
                                "<'row'<'col-sm-12 col-md-8'p>>",
                    });
                }
            });
        }
     });
});
</script>