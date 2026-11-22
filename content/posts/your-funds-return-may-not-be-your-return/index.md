---
title: "Your Fund's Return May Not Be Your Return: Time-Weighted vs Dollar-Weighted Returns"
aliases: ["/posts/what-investors-do-to-themselves/"]
summary: "A fund's advertised return is not necessarily what its investors earn. This post explains the difference between time-weighted and dollar-weighted returns, and why investors who buy after a rise and sell after a fall can earn less than the funds they own."
description: "Time-weighted vs dollar-weighted returns explained with a simple two-year fund and three investors, why trying to time the market is so hard, and Morningstar's Mind the Gap data on the gap between fund and investor returns."
tags: ["investing", "finance"]
date: 2026-11-23T00:59:00+01:00
draft: false
showTableOfContents: true
---
{{< katex >}}

In my post [The Arithmetic You Can't Beat](/posts/the-arithmetic-you-cannot-beat/), I explained why investors as a group must trail the market by the costs they pay. In this post, I want to explore a second reason why investors can earn less than the market, one that applies even to investors in the cheapest index fund: reacting to the market, by adding money after prices have gone up and taking money out after they have gone down.

To understand it, we first need to see that there are two different ways to measure a return.

## Two Ways to Measure a Return

When a fund reports that it returned 10% a year over the past 10 years, it is answering a specific question: how much would $1 have grown if it had been invested at the start and never touched? This is called the [time-weighted return](https://en.wikipedia.org/wiki/Time-weighted_return). It measures how well the *fund* did, no matter when anyone bought or sold it.

However, an investor may also add money over time, or take some out. What the investor earns then depends on how much money they had in the fund each year. This is measured by the *dollar-weighted* (or money-weighted) return: the single yearly rate that, applied to every dollar for as long as it was invested, gives exactly the amount the investor ended up with. (Technically, it is the [internal rate of return](https://en.wikipedia.org/wiki/Internal_rate_of_return) of the investor's cash flows.) It measures how well the *investor* did.

The two are equal only for an investor who puts all the money in at the start and never touches it. For everyone else, they can differ, sometimes by a lot.

## One Fund, Three Investors

Let's revisit the fund from my post [The Double-Edged Sword of Compounding](/posts/the-double-edged-sword-of-compounding/#misconceptions): it drops by 10% in one year and grows by 20% in the next. Its time-weighted return is about 3.92% a year (\(\sqrt{0.9 \times 1.2} - 1\)). It would be the same if the fund first rose by 20% and then dropped by 10%, because multiplication doesn't care about order. So 3.92% a year is what this fund would report.

Now, let's look at three investors in this fund.

**Investor A** invests $1,000 at the start and holds it. After the first year, the $1,000 drops to $900 ($1,000 x (1 - 10%)), and after the second year, it grows to $1,080 ($900 x (1 + 20%)). Growing $1,000 to $1,080 over two years is exactly 3.92% a year, so investor A earns what the fund reports.

**Investor B** sees the two years in the order +20%, then -10%. After the first year, the $1,000 has grown to $1,200. Encouraged by the good result, investor B adds another $1,000 after the price has gone up: in other words, investor B *buys high*. Now $2,200 is invested in the second year, which drops by 10% to $1,980. In total, investor B put in $2,000 and ended with $1,980: a small loss. As a yearly rate, that is about -0.67% a year, while the fund reported 3.92%. The reason is that the second $1,000 was only invested during the bad year.

**Investor C** sees the two years in the order -10%, then +20%. After the first year, the $1,000 has dropped to $900. Worried about further losses, investor C sells half after the price has gone down, *selling low*, and takes $450 out. Only the remaining $450 is invested in the second year, which grows by 20% to $540. In total, investor C put in $1,000 and got back $450 + $540 = $990: again a small loss, about -0.65% a year. The reason is that half of the money was taken out just before the good year.

{{< chart >}}
type: 'bar',
data: {
  labels: ['The Fund', 'Investor A (Holds)', 'Investor B (Buy High)', 'Investor C (Sell Low)'],
  datasets: [
    {
      label: 'Return per year (%)',
      data: [3.92, 3.92, -0.67, -0.65],
      backgroundColor: ['rgba(54, 162, 235, 0.6)', 'rgba(34, 139, 34, 0.6)', 'rgba(220, 53, 69, 0.6)', 'rgba(220, 53, 69, 0.6)'],
      borderColor: ['rgb(54, 162, 235)', 'rgb(34, 139, 34)', 'rgb(220, 53, 69)', 'rgb(220, 53, 69)'],
      borderWidth: 2
    }
  ]
},
options: {
  scales: {
    x: {
      title: {
        display: true,
        text: ''
      }
    },
    y: {
      title: {
        display: true,
        text: 'Return per Year (%)'
      },
      ticks: {
        callback: function(value) {
          return value + '%';
        }
      }
    }
  },
  plugins: {
    legend: {
      display: false
    },
    tooltip: {
      callbacks: {
        label: function(context) {
          return context.parsed.y + '%';
        }
      }
    }
  }
}
{{< /chart >}}

<small>**Figure 1.** One fund that returns 3.92% a year over two years (-10% and +20%, in either order), and the return per year that each of three investors in it actually earns</small>

As the chart shows, the same fund, with the same 3.92% a year, gave three investors three different results. Investors B and C both lost money in a fund that made money, because they added money after a rise and took money out after a fall: they bought high and sold low. In other words, more of their money was invested during the bad year, and less during the good one.

## What If You Time It Right?

Looking at investors B and C, you might ask: what if they had done the opposite? Wouldn't a well-timed move beat the fund?

It would. Take the same fund, first dropping by 10% and then rising by 20%. Suppose an investor adds another $1,000 after the drop instead of after a rise. Then $1,900 is invested in the good year, which grows to $2,280 ($1,900 x (1 + 20%)). As a yearly rate, that is about 9.06% a year, more than twice the fund's 3.92%. So timing *can* pay off.

But now put yourself in the investor's shoes at the end of the first year. All you know is what has already happened: the price has just gone up, or it has just gone down. Whether adding money is a good move or a bad one depends entirely on what happens *next* year, and that is exactly what you don't know when you have to decide. Investor B added money after a rise and lost; the same move would have won if the next year had been another rise. To time the market well, you have to predict it.

And one good prediction is not enough. Investor C, who sold after the drop, would also have needed to know when to buy back in, before the rise. That is two correct predictions in a row. As Bogle wrote in [*The Clash of the Cultures*](https://johncbogle.com/wordpress/wp-content/uploads/2013/05/c09.pdf) (2012): "One correct decision is tough enough. Two correct decisions in a row are nigh on impossible."

Investor A, on the other hand, didn't need to predict anything. Of the three, investor A's result was the only one that didn't depend on guessing the next year correctly.

## What the Real Data Show

Morningstar measures this gap every year in its *Mind the Gap* study, which compares the time-weighted returns of US mutual funds and [ETFs](https://en.wikipedia.org/wiki/Exchange-traded_fund) with the dollar-weighted returns of the money invested in them. In the [2026 edition](https://www.morningstar.com/funds/winning-formula-fund-investors-why-others-left-money-table), covering the 10 years to the end of 2025, the funds returned 9.9% a year, while the average invested dollar earned 8.7% a year: a gap of about 1.2 percentage points a year. This is the same kind of gap we saw in our example: the difference between what the funds earned and what the money invested in them earned, given when it went in and out.

A gap of 1.2 percentage points might not sound like much, but just like costs, it compounds. Let's see what it would mean for $10,000 over 30 years, if the gap stayed the same:

{{< chart >}}
type: 'line',
data: {
  labels: ['0', '5', '10', '15', '20', '25', '30'],
  datasets: [
    {
      label: 'Fund Return (9.9%)',
      data: [10000.0, 16032.03, 25702.59, 41206.47, 66062.32, 105911.3, 169797.3],
      borderColor: 'rgb(54, 162, 235)',
      backgroundColor: 'rgba(54, 162, 235, 0.15)',
      borderWidth: 2,
      tension: 0.3,
      pointRadius: 4
    },
    {
      label: 'Investor Return (8.7%)',
      data: [10000.0, 15175.66, 23030.08, 34949.68, 53038.46, 80489.38, 122147.99],
      borderColor: 'rgb(220, 53, 69)',
      backgroundColor: 'rgba(220, 53, 69, 0.15)',
      borderWidth: 2,
      tension: 0.3,
      pointRadius: 4,
      fill: '-1'
    }
  ]
},
options: {
  scales: {
    x: {
      title: {
        display: true,
        text: 'Years'
      }
    },
    y: {
      title: {
        display: true,
        text: 'Value ($)'
      },
      ticks: {
        callback: function(value) {
          return '$' + value.toLocaleString();
        }
      }
    }
  },
  plugins: {
    legend: {
      labels: {
        usePointStyle: true,
        pointStyle: 'line'
      }
    },
    tooltip: {
      callbacks: {
        label: function(context) {
          return context.dataset.label + ': $' + context.parsed.y.toLocaleString();
        }
      }
    }
  }
}
{{< /chart >}}

<small>**Figure 2.** $10,000 over 30 years at the funds' 9.9% a year versus the average investor's 8.7% (Morningstar, Mind the Gap 2026, 10 years ended 2025), assuming the gap persisted; an illustration, not a forecast</small>

At the funds' 9.9%, the $10,000 would grow to $169,797.30. At the investors' 8.7%, it would grow to $122,147.99, about 72% as much. In other words, over 30 years, a gap of 1.2 percentage points a year would cost more than a quarter of the final result, and the longer the investment lasts, the larger the fraction of the final result that is lost.

The data also show that the gap differs a lot between funds. Investors in broad US stock funds kept nearly all of their funds' return: 12.8% a year, against the funds' 13.3%. Investors in narrower and more volatile funds, on average, left more of their funds' return behind.

John Bogle pointed out the same kind of gap years earlier. In a [2014 *Financial Analysts Journal* article](https://johncbogle.com/wordpress/wp-content/uploads/2010/04/FAJ-All-In-Investment-Expenses-Jan-Feb-2014.pdf), he compared the reported returns of actively managed funds over 15 years with what Morningstar calculated their investors had earned, and found "a 'behavior gap' of 1.91 percentage points in return per year."

## Why Care About the Gap

By now, it should be clear that a fund's reported return is not necessarily what its investors earn. Looking back at our three investors, the one who earned the full return of the fund is investor A, the one who simply bought and held. This approach is known as [buy and hold](https://en.wikipedia.org/wiki/Buy_and_hold): invest, then leave the money alone, whatever the market does. Every dollar of the gap for investors B and C came from an action: adding money after a rise, or taking money out after a fall.

Bogle summed this up at the end of a [2005 talk to the American Association of Individual Investors](https://johncbogle.com/speeches/JCB_AAII0505.pdf): "don't do something, just stand there. Stay the course."

## Summary

A fund's reported return is a time-weighted return, which measures the fund. An investor's dollar-weighted return measures the investor, and it depends on when money goes in and out. Adding money after a rise and taking it out after a fall means more money is invested at the wrong time, so investors can earn less than the funds they own. In Morningstar's data, the gap was about 1.2 percentage points a year over the 10 years to 2025, and like costs, it compounds. The advice to "stay the course" is [John C. Bogle](https://en.wikipedia.org/wiki/John_C._Bogle)'s, and the investor-return data are Morningstar's.

## Disclaimers

I am not a professional investor or financial advisor, nor do I claim to be. You are solely responsible for your financial decisions. I do not accept responsibility for any inaccuracies in this blog post. The content reflects my personal research and understanding and should not be interpreted as professional advice.
