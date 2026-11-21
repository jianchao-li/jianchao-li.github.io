---
title: "Bagels and Doughnuts: Where Stock Returns Actually Come From"
summary: "When a stock fund returns 10% a year, where does that money actually come from? This post breaks a stock's return into its three sources (dividends, earnings growth, and the change in what investors are willing to pay) and shows why the third one can swing a single decade a lot but fades over a lifetime."
description: "John Bogle's bagel-and-doughnut model of stock returns: dividend yield plus earnings growth, plus or minus the change in the P/E ratio, worked through step by step with a simple example."
tags: ["investing", "finance"]
date: 2026-11-21T22:57:00+01:00
draft: false
showTableOfContents: true
---
{{< katex >}}

When people talk about the stock market, they usually quote a single number: "stocks returned X% last year", or "stocks return about Y% a year over the long run". For a long time, I took such numbers at face value. But a return is not a law of nature. If my fund grows by 10% this year, that money has to come from *somewhere*.

So where does it come from? In this post, I will explore the answer that [John C. Bogle](https://en.wikipedia.org/wiki/John_C._Bogle), the founder of Vanguard, gave in his books. It turns out there are only three sources, and once you see them, it becomes much easier to tell which parts of a stock's return you can count on and which you can't.

## What Do You Own When You Own a Stock?

A share of stock is a small slice of a business. As a part-owner, you are entitled to a part of the business's profits, which are called its *earnings*. The business can do two things with them:

1. Pay some of them out to you in cash. This is called a [dividend](https://en.wikipedia.org/wiki/Dividend).
2. Keep the rest and reinvest it in the business, hopefully so that it earns more in the future.

There is one more thing to know: how much people are willing to pay for the share. This is measured by the [price-earnings ratio](https://en.wikipedia.org/wiki/Price%E2%80%93earnings_ratio) (P/E): the share price divided by the yearly earnings per share. For example, if a share earns $5 a year and costs $100, its P/E is 20 (\(\frac{\$100}{\$5}\)). In other words, investors pay $20 for every $1 of yearly earnings.

Turning the P/E around gives a simple but powerful relationship:

Share price = Earnings per share x P/E

This little formula is really the whole story of this post. A share price can only go up for two reasons: the earnings went up, or investors became willing to pay more for each dollar of earnings (the P/E went up). Add the dividends you receive along the way, and you have every possible source of a stock's return:

1. **Dividend yield**: the dividends you receive.
2. **Earnings growth**: the business earning more.
3. **Change in P/E**: investors paying more (or less) for the same earnings.

Let's look at them one at a time, using one imaginary share.

## Source 1: Dividend Yield

Let's meet our share. It costs $100. The business earns $5 per share a year, so the P/E is 20. It pays out most of its earnings, $4.50 per share, as a dividend.

The dividend divided by the share price is called the [dividend yield](https://en.wikipedia.org/wiki/Dividend_yield). Here it is 4.5% (\(\frac{\$4.50}{\$100}\)). If nothing else ever changed, the share price would stay at $100, and you would earn 4.5% a year in cash, a bit like interest on a bank deposit.

(These are made-up numbers chosen to keep the arithmetic easy, not a real company. Real dividend yields are often lower, and some companies pay no dividend at all; some of these return money to shareholders by buying back their own shares instead.)

## Source 2: Earnings Growth

Now suppose the business grows, and its earnings rise by 5% over the year, from $5 to $5.25 per share ($5 x (1 + 5%)). Investors still pay 20 times earnings, so the share price rises to $105 ($5.25 x 20). The price grew by exactly the same 5% as the earnings.

Your return for the year is the price gain plus the dividend, divided by what you paid:

$$\frac{\$105 - \$100 + \$4.50}{\$100} = 9.5\%$$

That is 4.5% from the dividend yield plus 5% from earnings growth. Nothing else changed, so nothing else contributed.

### Over 10 Years

Let's extend this to 10 years. The business keeps growing its earnings by 5% a year, investors keep paying 20 times earnings, and every year you use your dividend to buy a little more of the share. Just as in the compound interest example of my post [The Double-Edged Sword of Compounding](/posts/the-double-edged-sword-of-compounding/), the 9.5% now compounds every year.

{{< chart >}}
type: 'line',
data: {
  labels: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
  datasets: [
    {
      label: 'Share Price Only',
      data: [100.0, 105.0, 110.25, 115.76, 121.55, 127.63, 134.01, 140.71, 147.75, 155.13, 162.89],
      borderColor: 'rgb(54, 162, 235)',
      backgroundColor: 'rgba(54, 162, 235, 0.1)',
      borderWidth: 2,
      tension: 0.3,
      pointRadius: 4
    },
    {
      label: 'With Dividends Reinvested',
      data: [100.0, 109.5, 119.9, 131.29, 143.77, 157.42, 172.38, 188.76, 206.69, 226.32, 247.82],
      borderColor: 'rgb(34, 139, 34)',
      backgroundColor: 'rgba(34, 139, 34, 0.1)',
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
        text: 'Year'
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

<small>**Figure 1.** The toy $100 share over 10 years at a constant P/E of 20: the price grows with earnings (5% a year), the holding grows with earnings plus reinvested dividends (9.5% a year)</small>

After 10 years, your $100 has grown to $247.82 ($100 x (1 + 9.5%)<sup>10</sup>). Meanwhile, the share price alone, which only grows with earnings, has reached $162.89 ($100 x (1 + 5%)<sup>10</sup>).

Notice the gap between the two curves. The other $84.93 of your money came from the reinvested dividends. That is about 57% of your $147.82 gain, and it is a part of the return you would never see if you only looked at a chart of the share price.

This is the magic of compounding at work again: each reinvested dividend buys more shares, and those new shares pay dividends of their own, just like interest earning interest. If you spent the dividends instead, you would still collect them, but they would stop compounding, and the gap between the two choices would keep widening the longer you hold.

## Source 3: Change in P/E

So far, investors have always paid 20 times earnings. But the P/E is not fixed. It reflects how optimistic or pessimistic investors feel about the future, and that changes all the time.

Let's go back to the first year. The business does exactly the same as before: earnings grow from $5 to $5.25, and it pays the same $4.50 dividend. But this time, investors become more enthusiastic and are willing to pay 22 times earnings instead of 20. The share price becomes $115.50 ($5.25 x 22), and your return for the year is:

$$\frac{\$115.50 - \$100 + \$4.50}{\$100} = 20\%$$

The business is exactly the same, yet your return more than doubled, from 9.5% to 20%. The extra 10.5 percentage points came from nothing but a change in investor mood. Of course, it works in the other direction too: if investors had become gloomy and the P/E had fallen, your return would have been lower than 9.5%, or even negative.

### Turning a P/E Change into a Yearly Return

To compare the three sources, it helps to express a change in P/E as a yearly return as well. If the P/E goes from P/E<sub>start</sub> to P/E<sub>end</sub> over n years, the price gets multiplied by an extra factor of \(\frac{\text{P/E}_{\text{end}}}{\text{P/E}_{\text{start}}}\). Spreading that factor evenly over n years (the same "equivalent compound rate" idea I described for the annualized rate of return in [the compounding post](/posts/the-double-edged-sword-of-compounding/#misconceptions)) gives:

$$\text{Yearly return from the P/E change} = \left(\frac{\text{P/E}_{\text{end}}}{\text{P/E}_{\text{start}}}\right)^{1/n} - 1$$

For example, if the P/E doubles from 10 to 20 over 10 years, that adds:

$$\left(\frac{20}{10}\right)^{1/10} - 1 = 7.18\% \text{ a year}$$

That is a lot for something that has nothing to do with the business: over those 10 years, the change of mood alone doubles the share price. For comparison, everything the business itself delivers, its dividends and earnings growth at 9.5% a year, grew our $100 to $247.82 over the same 10 years (Figure 1).

This is not just a toy example. In a 2005 talk to the American Association of Individual Investors ("[In Troubled Times . . . The Arithmetic of Mutual Fund Investing is More Important Than Ever](https://johncbogle.com/speeches/JCB_AAII0505.pdf)"), Bogle described exactly this happening to the US stock market in the 1990s:

> "When the price-earnings ratio rose from 16 times to 32 times during the 1990s—a 100 percent increase—that change in investor sentiment alone added fully 7 percent per year to the investment return of 10 ½ percent in that glorious decade of speculation, bringing the total return to a robust 17.8 percent." — John C. Bogle, 2005

### Same Business, Three Moods

To see how much the P/E alone can matter, let's invest $10,000 in our share and hold it for 10 years under three scenarios. The business is identical in all three: same earnings growth, same dividends, all reinvested. The only difference is what investors are willing to pay at the end:

* **The P/E rises from 20 to 25**, adding \(\left(\frac{25}{20}\right)^{1/10} - 1 = 2.26\%\) a year.
* **The P/E stays at 20**, adding nothing.
* **The P/E falls from 20 to 15**, subtracting \(\left(\frac{15}{20}\right)^{1/10} - 1 = -2.84\%\) a year.

{{< chart >}}
type: 'line',
data: {
  labels: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
  datasets: [
    {
      label: 'P/E Rises 20 → 25',
      data: [10000.0, 11186.93, 12503.64, 13963.18, 15579.83, 17369.19, 19348.28, 21535.69, 23951.7, 26618.39, 29559.88],
      borderColor: 'rgb(34, 139, 34)',
      backgroundColor: 'rgba(34, 139, 34, 0.1)',
      borderWidth: 2,
      tension: 0.3,
      pointRadius: 4
    },
    {
      label: 'P/E Stays at 20',
      data: [10000.0, 10950.0, 11990.25, 13129.32, 14376.61, 15742.39, 17237.91, 18875.52, 20668.69, 22632.22, 24782.28],
      borderColor: 'rgb(54, 162, 235)',
      backgroundColor: 'rgba(54, 162, 235, 0.1)',
      borderWidth: 2,
      tension: 0.3,
      pointRadius: 4
    },
    {
      label: 'P/E Falls 20 → 15',
      data: [10000.0, 10652.24, 11361.01, 12132.29, 12972.82, 13890.15, 14892.81, 15990.44, 17193.92, 18515.6, 19969.49],
      borderColor: 'rgb(220, 53, 69)',
      backgroundColor: 'rgba(220, 53, 69, 0.1)',
      borderWidth: 2,
      tension: 0.3,
      pointRadius: 4
    }
  ]
},
options: {
  scales: {
    x: {
      title: {
        display: true,
        text: 'Year'
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

<small>**Figure 2.** $10,000 in the same toy business over 10 years, with dividends reinvested, under three changes in the P/E</small>

With an unchanged P/E, your $10,000 grows to $24,782.28, the same 9.5% a year as before. If the P/E rises, you end up with $29,559.88. If it falls, you end up with $19,969.49. The investor in the first scenario ends the decade with 48% more money than the investor in the last one, from the *same* business with the *same* earnings.

## The Bagel and the Doughnut

Bogle turned these three sources into a simple model of stock market returns:

Stock return ≈ Dividend yield + Earnings growth ± Change in P/E

He called the first two together the **investment return**, because they come from the business itself. He called the third the **speculative return**, because it comes from what other investors are willing to pay. In Rule 4 of his "Ten Simple Rules for Investors", in [*The Clash of the Cultures*](https://johncbogle.com/wordpress/wp-content/uploads/2013/05/c09.pdf) (2012), he gave them a memorable image:

> "the bagel of the stock market is investment return—dividend yields plus earnings growth. The investment return on stocks reflects the bagel's underlying character: nutritious, crusty, and hard-boiled." [...] "the spongy doughnut of the market is speculative return wrought by any material change in the price that investors are willing to pay for each dollar of earnings." — John C. Bogle, *The Clash of the Cultures*, 2012

The bagel is solid: as long as businesses pay dividends and grow their earnings, it keeps delivering. The doughnut is spongy: it can puff up for years, and it can collapse just as quickly.

## Why the Doughnut Fades Over Time

So far, the doughnut looks powerful: in the three scenarios above, it made the difference between ending the decade with $19,969.49 or $29,559.88, from the same business. But what does it look like in real markets, and over a much longer time?

To find out, I split more than a century of US stock returns into the three sources, decade by decade, using Bogle's method on [Robert Shiller's public data](https://shillerdata.com/) for the [S&P 500](https://en.wikipedia.org/wiki/S%26P_500), an index of about 500 large US companies.

{{< chart >}}
type: 'bar',
data: {
  labels: ['1900s', '1910s', '1920s', '1930s', '1940s', '1950s', '1960s', '1970s', '1980s', '1990s', '2000s', '2010s'],
  datasets: [
    {
      label: 'Dividend yield',
      data: [3.57, 4.39, 5.98, 4.47, 5.07, 6.81, 3.22, 3.5, 5.14, 3.28, 1.17, 1.98],
      borderColor: 'rgb(54, 162, 235)',
      backgroundColor: 'rgba(54, 162, 235, 0.6)',
      borderWidth: 2,
      order: 1
    },
    {
      label: 'Earnings growth',
      data: [4.67, 1.95, 5.41, -5.02, 9.65, 3.79, 5.39, 10.1, 4.13, 8.12, 1.01, 9.27],
      borderColor: 'rgb(34, 139, 34)',
      backgroundColor: 'rgba(34, 139, 34, 0.6)',
      borderWidth: 2,
      order: 1
    },
    {
      label: 'Change in P/E',
      data: [0.46, -3.21, 3.8, -0.53, -5.87, 9.01, -0.82, -7.29, 7.42, 6.75, -3.33, 1.86],
      borderColor: 'rgb(255, 165, 0)',
      backgroundColor: 'rgba(255, 165, 0, 0.6)',
      borderWidth: 2,
      order: 1
    },
    {
      type: 'line',
      label: 'Actual total return',
      data: [9.9, 4.66, 15.49, -0.17, 9.23, 18.76, 7.87, 6.25, 16.63, 18.24, -0.58, 13.53],
      borderColor: 'rgb(220, 53, 69)',
      backgroundColor: 'rgb(220, 53, 69)',
      showLine: false,
      pointRadius: 6,
      pointStyle: 'rectRot',
      stack: 'total',
      order: 0
    }
  ]
},
options: {
  scales: {
    x: {
      stacked: true,
      title: {
        display: true,
        text: 'Decade'
      }
    },
    y: {
      stacked: true,
      title: {
        display: true,
        text: 'Yearly return (%)'
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
      labels: {
        usePointStyle: true
      }
    },
    tooltip: {
      callbacks: {
        label: function(context) {
          return context.dataset.label + ': ' + context.parsed.y + '%';
        }
      }
    }
  }
}
{{< /chart >}}

<small>**Figure 3.** US stock returns by decade, split into dividend yield, earnings growth and the change in P/E (my calculation with Bogle's method on Robert Shiller's S&P 500 data; the red diamonds are the actual total returns)</small>

Look at the orange bars, the change in P/E. They jump up and down from one decade to the next. In the 1950s, investors grew more optimistic, and the rising P/E added about 9% a year. In the 1970s, they grew gloomy, and the falling P/E took away about 7% a year. The blue and green bars, the dividends and earnings growth, are much steadier: earnings grew in every decade except the 1930s, and dividends were paid in all of them.

Now step back and look at the whole period. The good decades and the bad decades largely cancel out. In 1900, investors paid about 13 times earnings for US stocks; by 2020, they paid about 25 times. That is a big change, but spread over 120 years, it adds up to only about 0.56% a year, tiny next to the swings of up to 9% a year in single decades.

The reason is simple: the bagel delivers every single year, but the P/E can't keep rising forever. Optimism and pessimism come and go, so over a long time, most of the doughnut washes out.

Bogle found the same when he looked at US stocks from 1900 to 2005. In a [2007 speech at New York University](https://johncbogle.com/wordpress/wp-content/uploads/2006/02/NYU-11-14-07.pdf), he summarized:

> "The average annual total return on stocks was 9.6 percent, virtually identical to the investment return of 9.5 percent—4.5 percent from dividend yield and 5 percent from earnings growth. That tiny difference of 0.1 percent per year arose from what I call speculative return." — John C. Bogle, 2007

Over a decade, the doughnut can make a big difference. Over a century, it almost disappeared. As he put it in the same speech: "It is economics that controls long-term equity returns; emotions, so dominant in the short-term, dissolve."

## Why Care About the Bagel and the Doughnut

Knowing where returns come from changes how I read return numbers.

First, **a great decade is often a decade of doughnut**. When a market has returned, say, 15% a year for ten years, it is worth asking how much of that came from a rising P/E. If a big part did, then expecting the next ten years to repeat it means expecting the P/E to keep rising at the same pace, which, as we saw above, it can't do forever.

Second, **the bagel is the part you can reason about**. Dividends and earnings growth come from real businesses, and they are what is left once the moods average out. The doughnut, on the other hand, depends on how other people will feel in the future, and nobody knows that. Bogle himself said, in the NYU speech, that he had "little conviction about how to forecast these swings in investor emotions, nor when they will occur." A high P/E can stay high, or rise even higher, for a long time.

## Caveats

### Caveat 1: The Formula Is an Approximation

Bogle's formula adds the three sources together, but in reality they multiply, and the dividend yield changes whenever the price does. That is why our share's 20% year was not exactly 4.5% + 5% + 10%, and why the bars in Figure 3 don't add up exactly to the red diamonds. For returns of this size, the difference is small enough that the simple addition still tells you where a return came from.

### Caveat 2: Before Costs, Taxes, and Inflation

All returns in this post are before fund costs, trading costs, taxes, and inflation. As I explored in [The Double-Edged Sword of Compounding](/posts/the-double-edged-sword-of-compounding/), costs come out of these returns before you get to keep them.

## Summary

A stock's return comes from only three sources: the dividends it pays, the growth of its earnings, and the change in what investors are willing to pay for those earnings. [John C. Bogle](https://en.wikipedia.org/wiki/John_C._Bogle) called the first two the *investment return*, the bagel, and the third the *speculative return*, the doughnut. The doughnut can swing a single decade a lot, but because the P/E can't keep rising forever, it fades over a long horizon, leaving the bagel to do the work. This post is heavily inspired by Mr. Bogle's insights.

## Disclaimers

I am not a professional investor or financial advisor, nor do I claim to be. You are solely responsible for your financial decisions. I do not accept responsibility for any inaccuracies in this blog post. The content reflects my personal research and understanding and should not be interpreted as professional advice.
