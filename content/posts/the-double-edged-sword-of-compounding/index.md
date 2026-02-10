---
title: "The Double-Edged Sword of Compounding"
summary: "While many investors understand the power of compound returns, they may not fully grasp that compounding can also result in a significant downside. This post explores this double-edged sword."
description: "Understanding how compound returns work both for and against investors — the mathematical reality behind compounding gains and losses."
tags: ["investing", "finance"]
date: 2025-01-03T22:08:00+01:00
lastmod: 2025-01-03T22:08:00+01:00
draft: false
---
Starting with this post, I want to venture into a new area — investing — distinct from my usual topics of computer vision, deep learning, etc. Investing has become my latest hobby, and after diving into it, I have found it both fascinating and inspiring.

In this first post, I will explore a fundamental concept in the world of investing: [compound interest](https://en.wikipedia.org/wiki/Compound_interest). To me, it represents the ["first principle"](https://en.wikipedia.org/wiki/First_principle) of investing.

## What is Compound Interest?
 
Compound interest is a form of [interest](https://en.wikipedia.org/wiki/Interest). When you deposit money into a bank account or lend it to someone, you typically earn interest. The amount you deposit or lend is called the *principal*, and the interest is calculated as a percentage (*interest rate*) of the principal. For example, if you have a principal of $100 and an interest rate of 10%, your interest would be $10 ($100 x 10% = $10).

Interest is typically paid at fixed intervals. In the example above, let's assume the $10 is paid annually. After the first year, you would have $100 in principal and $10 in interest. Now, imagine that the $10 interest is added to the $100 principal. This means that, in the next period, interest will be calculated based on the new principal amount of $110. If the interest rate remains at 10%, your next interest payment will be $11 ($110 x 10% = $11).

Here, you may notice a [snowball effect](https://en.wikipedia.org/wiki/Snowball_effect): as your interest payments are added to your principal (increasing it from $100 to $110), your interest payments also grow (from $10 to $11). This cycle continues, with the interest added to your principal, which increases the principal further, leading to higher interest payments and, in turn, an even higher principal, and so on.

If we continue the above calculations for 10 years, the principal, interest earned, and total would look as follows (with rounding errors). The principal represents the total amount at the beginning of each year, which is the same as the total at the end of the previous year. The interest is the amount earned at the end of each year. For year n + 1, the principal is simply the principal from year n plus the interest earned in year n.

{{< chart >}}
type: 'line',
data: {
  labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
  datasets: [
    {
      label: 'Principal',
      data: [100, 110, 121, 133.1, 146.41, 161.05, 177.16, 194.87, 214.36, 235.79],
      borderColor: 'rgb(54, 162, 235)',
      backgroundColor: 'rgba(54, 162, 235, 0.1)',
      borderWidth: 2,
      tension: 0.3,
      pointRadius: 4
    },
    {
      label: 'Interest Earned',
      data: [10, 11, 12.1, 13.31, 14.64, 16.11, 17.72, 19.49, 21.44, 23.58],
      borderColor: 'rgb(255, 165, 0)',
      backgroundColor: 'rgba(255, 165, 0, 0.1)',
      borderWidth: 2,
      tension: 0.3,
      pointRadius: 4
    },
    {
      label: 'Total',
      data: [110, 121, 133.1, 146.41, 161.05, 177.16, 194.87, 214.36, 235.79, 259.37],
      borderColor: 'rgb(34, 139, 34)',
      backgroundColor: 'rgba(34, 139, 34, 0.1)',
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

<small>**Figure 1.** Compound interest on a $100 principal at 10% over 10 years</small>

## The magic of Compound Interest

> "Compound interest is the eighth wonder of the world. He who understands it, earns it... he who doesn't... pays it." - Albert Einstein

Looking at the chart above, you might realize the magic of compound interest: starting with $100 in principal, earning 10% interests per year, by the beginning of the 9th year, you have doubled your money. If this doesn't amaze you, let's explore two more calculations to help you fully appreciate it.

### Compounding Over 30 Years

Let's extend the view to 30 years to see the bigger picture.

{{< chart >}}
type: 'line',
data: {
  labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'],
  datasets: [
    {
      label: 'Principal',
      data: [100, 110, 121, 133.1, 146.41, 161.05, 177.16, 194.87, 214.36, 235.79, 259.37, 285.31, 313.84, 345.23, 379.75, 417.72, 459.50, 505.45, 555.99, 611.59, 672.75, 740.03, 814.03, 895.43, 984.97, 1083.47, 1191.82, 1311.00, 1442.10, 1586.31],
      borderColor: 'rgb(54, 162, 235)',
      backgroundColor: 'rgba(54, 162, 235, 0.1)',
      borderWidth: 2,
      tension: 0.3,
      pointRadius: 4
    },
    {
      label: 'Interest Earned',
      data: [10, 11, 12.1, 13.31, 14.64, 16.11, 17.72, 19.49, 21.44, 23.58, 25.94, 28.53, 31.38, 34.52, 37.98, 41.77, 45.95, 50.54, 55.60, 61.16, 67.28, 74.00, 81.40, 89.54, 98.50, 108.35, 119.18, 131.10, 144.21, 158.63],
      borderColor: 'rgb(255, 165, 0)',
      backgroundColor: 'rgba(255, 165, 0, 0.1)',
      borderWidth: 2,
      tension: 0.3,
      pointRadius: [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 4, 4, 4, 4],
      pointBackgroundColor: ['rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(220, 53, 69)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)'],
      pointBorderColor: ['rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(220, 53, 69)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)', 'rgb(255, 165, 0)']
    },
    {
      label: 'Total',
      data: [110, 121, 133.1, 146.41, 161.05, 177.16, 194.87, 214.36, 235.79, 259.37, 285.31, 313.84, 345.23, 379.75, 417.72, 459.50, 505.45, 555.99, 611.59, 672.75, 740.03, 814.03, 895.43, 984.97, 1083.47, 1191.82, 1311.00, 1442.10, 1586.31, 1744.94],
      borderColor: 'rgb(34, 139, 34)',
      backgroundColor: 'rgba(34, 139, 34, 0.1)',
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

<small>**Figure 2.** Compound interest on a $100 principal at 10% over 30 years</small>

As you can see, at the beginning of the 10th year, your principal is around $236. By the start of the 20th year, it has grown (non-linearly) to approximately $612, and by the 30th year, it reaches about $1,586. More strikingly, notice the Interest Earned curve at year 26 (the red dot): this is the first time your annual interest payment ($108.35) exceeds your initial $100 principal! The longer you continue the calculations, the wilder the numbers become.

### The Case of Non-Compounding

Now, let's consider the non-compounding case, where the annual interest payment is not added back to the principal. In this scenario, you receive interest based on the initial $100 principal, meaning you earn $10 in interest each year. After 10 years, your total amount would be $200 ($100 + $100 x 0.1 x 10). While this is not too far from the compounded case, where your total would be around $259, the gap widens significantly over time. After 20 years, the non-compounding case yields $300 ($100 + $100 x 0.1 x 20), while the compounding case reaches approximately $673. After 30 years, the gap is even more dramatic: $400 versus about $1,745. The longer you continue the calculations, the more drastic the gap becomes.

### Exponential Explosion

The snowball effect of compound interest described above is known as [exponential growth](https://en.wikipedia.org/wiki/Exponential_growth), or more dramatically, [exponential explosion](https://www.stewartmath.com/dp_fops_samples/dp7.html). This is the essence of the magic of compound interest — over time, the amount of your money grows exponentially to a "formidable" sum (though not so dramatic in the example above, largely due to the small $100 principal).

If we chart the results of compounding versus non-compounding over 50 years, the "explosion" or magic of compound interest becomes much more evident. After 50 years, your initial $100 principal grows to around $11,739! And remember, this 117-fold growth comes from a "modest" 10% compound interest rate. Take a moment to think about it: a 117-times increase from just 0.1, and you will start to appreciate the magic of compound interest. By comparison, in the non-compounding case, it would take 1,164 years to grow to $11,739!

{{< chart >}}
type: 'line',
data: {
  labels: ['0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50'],
  datasets: [
    {
      label: 'Compounding',
      data: [100, 161.05, 259.37, 417.72, 672.75, 1083.47, 1744.94, 2810.24, 4525.93, 7289.05, 11739.09],
      borderColor: 'rgb(34, 139, 34)',
      backgroundColor: 'rgba(34, 139, 34, 0.1)',
      borderWidth: 2,
      tension: 0.3,
      pointRadius: 4
    },
    {
      label: 'Non-compounding',
      data: [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600],
      borderColor: 'rgb(220, 53, 69)',
      backgroundColor: 'rgba(220, 53, 69, 0.1)',
      borderWidth: 2,
      tension: 0,
      pointRadius: 4
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

<small>**Figure 3.** Compounding vs non-compounding over 50 years ($100 principal, 10% interest rate)</small>

For what it's worth, the non-compounding case is also known as [simple interest](https://en.wikipedia.org/wiki/Interest#Simple_interest).

## Why Care About Compound Interest

Now that we understand compound interest, why is it important to investing? The answer is simple: it measures your return on investment. If you are familiar with investing, you have likely heard terms like "the annualized rate of return is X% over the past Y years". This "annualized rate of return" is similar (but not identical) to the compound interest rate we discussed earlier. As we have seen, compound interest has the magic to grow your money into a formidable sum over time.

### Misconceptions

While the "annualized rate of return" is similar to the compound interest rate in our example, there is a crucial difference that often leads to misconceptions. In our compound interest example, the 10% interest rate is fixed every year. However, in real-world investing, the rate is almost never fixed. For instance, an annualized rate of return of 10% does NOT mean you are guaranteed to earn 10% each year! Instead, the annualized rate of return is calculated by comparing the starting and ending values of an investment over a given time period and determining the *equivalent* compound interest rate. If you are interested in how it is computated, you can play with it using [this calculator](https://www.buyupside.com/calculators/annualizedreturn.htm).

It is crucial for all investors to dispel this misconception and set realistic expectations.

## Why Compounding Is a Double-Edged Sword

From the discussions above, I hope you now appreciate the magic of compounding in investing. However, it is equally important to understand why compounding can become a double-edged sword. The reason is simple: while compounding can work wonders, it can also work against you.

In the real world, investing is not free. While the market might generate an annualized return of 10%, you don't get to keep all of it. A portion is deducted as investment costs. A common example of such costs is the [total expense ratio](https://en.wikipedia.org/wiki/Total_expense_ratio) (TER) of investment funds, where you pay a percentage of your money to the fund providers each year. When it comes to costs, compounding works against you.

Let’s revisit the compound interest example of 10% and consider a principal of $10,000. Suppose the TER is 1%. After one year, your gross amount would grow to $11,000 ($10,000 x 10%). However, you would pay $100 ($10,000 x 1%) in fees to the fund providers, leaving you with a net amount of $10,900. Effectively, your net compound interest rate is 9%. This leads to the following simple and clean formula:

Net annualized rate of return = Gross annualized rate of return - Total expense ratio

or

Investment return rate = Market return rate - Total expense ratio

Now, let's perform similar calculations to compare a 10% market return with a 9% investment return. Specifically, we will compare the total amount of money (with rounding errors) at 10-year intervals for both cases.

{{< chart >}}
type: 'line',
data: {
  labels: ['10', '20', '30', '40', '50'],
  datasets: [
    {
      label: 'Market Value (10%)',
      data: [25937.42, 67275.00, 174494.02, 452592.56, 1173908.53],
      borderColor: 'rgb(34, 139, 34)',
      backgroundColor: 'rgba(34, 139, 34, 0.1)',
      borderWidth: 2,
      tension: 0.3,
      pointRadius: 4,
      yAxisID: 'y'
    },
    {
      label: 'Investment Value (9%)',
      data: [23673.64, 56044.11, 132676.78, 314094.20, 743575.20],
      borderColor: 'rgb(220, 53, 69)',
      backgroundColor: 'rgba(220, 53, 69, 0.15)',
      borderWidth: 2,
      tension: 0.3,
      pointRadius: 4,
      fill: '-1',
      yAxisID: 'y'
    },
    {
      label: 'Percentage Kept',
      data: [91.27, 83.31, 76.04, 69.40, 63.34],
      borderColor: 'rgb(255, 165, 0)',
      backgroundColor: 'rgba(255, 165, 0, 0.1)',
      borderWidth: 2,
      borderDash: [5, 5],
      tension: 0.3,
      pointRadius: 4,
      yAxisID: 'y1'
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
      position: 'left',
      title: {
        display: true,
        text: 'Value ($)'
      },
      ticks: {
        callback: function(value) {
          return '$' + value.toLocaleString();
        }
      }
    },
    y1: {
      position: 'right',
      title: {
        display: true,
        text: 'Percentage Kept (%)'
      },
      min: 50,
      max: 100,
      ticks: {
        callback: function(value) {
          return value + '%';
        }
      },
      grid: {
        drawOnChartArea: false
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
          if (context.dataset.yAxisID === 'y1') {
            return context.dataset.label + ': ' + context.parsed.y + '%';
          }
          return context.dataset.label + ': $' + context.parsed.y.toLocaleString();
        }
      }
    }
  }
}
{{< /chart >}}

<small>**Figure 4.** Impact of 1% TER on a $10,000 investment over 50 years</small>

From the chart, it is clear that over time, you retain less and less of the market value. After 10 years, you keep over 91%, but after 50 years, this drops to just over 63%. In other words, after 10 years, you lose around 9% of the market value, and after 50 years, the loss grows to 37%. Where does this 37% go? You guessed it - it's consumed by fees.

Now, consider this: the 37% loss stems from a seemingly "small" 1% annual fee. To better understand the impact, let’s look at the absolute dollar amounts lost due to these fees over time.

{{< chart >}}
type: 'bar',
data: {
  labels: ['10', '20', '30', '40', '50'],
  datasets: [
    {
      label: 'Value Lost to Fees',
      data: [2263.79, 11230.89, 41817.24, 138498.36, 430333.32]
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
        text: 'Value Lost ($)'
      },
      ticks: {
        callback: function(value) {
          return '$' + value.toLocaleString();
        }
      }
    }
  },
  plugins: {
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

<small>**Figure 5.** Value lost to 1% TER fees over 50 years ($10,000 principal)</small>

As shown in the chart, over 50 years, you lose a staggering $430,333 to fees — more than 43 times your initial $10,000 principal! Once again, this immense loss results from a seemingly "small" 1% annual fee.

By now, it should be clear: costs also compound, and over time, they can amount to a formidable loss. This is why compounding can be a double-edged sword.

### Caveat 1: Losses Are Not Equal to Fees

It is important to clarify that while the loss is caused by fees, the loss itself is not equal to the fees you pay. In the above example, although you lose $430,333 over 50 years, this doesn't mean the fund providers receive fees totaling this amount. They actually collect a much smaller sum, around $81,508. This difference arises because the fees you pay stop compounding along with the rest of your investment. If those fees were not deducted, they would have compounded as well, resulting in a significantly higher total value.

### Caveat 2: Variable Actual Returns

It is important to note that, for simplicity, we use the annualized rate of return similar to a fixed compound interest rate to illustrate how costs impact returns. However, the math demonstrating the effect of costs remains valid even when applied to variable actual returns.

Let’s consider a simple example where the market drops by 10% in the first year and grows by 20% in the second year. This results in an annualized rate of return of approximately 3.92% over two years (you can verify it using [this calculator](https://www.buyupside.com/calculators/annualizedreturn.htm)). Assuming a TER of 1%, we will calculate the end value using both the variable actual returns and the annualized rate of return in the following tables.

#### Using Variable Actual Returns

| Year | Market Value ($) | Investment Value ($) |
| ------- | ------- | ------- |
| 1 | 900 | 890 |
| 2 | 1,068 | 1,059.1|

<small>**Table 1.** Market and investment values using variable actual returns ($1,000 principal, 1% TER)</small>

* In the first year, the market value drops by 10% ($1000 x (1 - 10%) = $900). And deducting a 1% fee ($1000 x 1% = $10), the investment value is $890 ($900 - $10).
* In the second year, the market grows by 20% ($890 x (1 + 20%) = $1,068). And deducting a 1% fee on the initial investment value ($890 x 1% = $8.9) , the final investment value is $1,059.1 ($1,068 - $8.9).

#### Using Annualized Rate of Return

| Year | Market Value ($) | Investment Value ($) |
| ------- | ------- | ------- |
| 1 | 1039.2 | 1029.2 |
| 2 | 1069.54 | 1059.25|

<small>**Table 2.** Market and investment values using annualized rate of return ($1,000 principal, 1% TER)</small>

* Here, we apply the annualized rate of return (3.92%), reduced by the TER of 1%, resulting in a net return of 2.92%. The calculations follow the same logic as the fixed compound interest example.

As shown in the tables above, the final values are very similar (up to rounding differences), regardless of whether we use the variable actual returns and the fixed annualized rate of return. This demonstrates that using the annualized rate still accurately reflects the impact of costs while simplifying the calculations.

### Caveat 3: Costs Based on Final Value

In our examples, costs are calculated based on the initial value at the beginning of each year, which allows for the clean formulas presented above. However, if costs are instead calculated based on the final value at the end of each year, the results will differ, though the impact of costs would still be similar.

Let's revisit the example with fixed 10% annual rate of return and an initial principal of $10,000. This time, a 1% cost is deducted at the end of the year.

{{< chart >}}
type: 'line',
data: {
  labels: ['10', '20', '30', '40', '50'],
  datasets: [
    {
      label: 'Cost on Initial Value',
      data: [23694.28, 55580.49, 130377.06, 305829.94, 717395.74],
      borderColor: 'rgb(34, 139, 34)',
      backgroundColor: 'rgba(34, 139, 34, 0.1)',
      borderWidth: 2,
      tension: 0.3,
      pointRadius: 4
    },
    {
      label: 'Cost on Final Value',
      data: [23457.34, 55024.69, 129073.29, 302771.64, 710221.78],
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

<small>**Figure 6.** Costs deducted based on final value ($10,000 principal, 10% return, 1% TER)</small>

In this scenario, the net rate of return drops to approximately 8.9% (you can verify it using [this calculator](https://www.buyupside.com/calculators/annualizedreturn.htm)), which is slightly lower than (but similar to) the 9% achieved when costs are calculated based on the initial value.

### How to Avoid the Double-Edged Sword

The solution is simple: minimize investment costs, or at the very least, reduce them to a level you can accept. For instance, if the fund cost is reduced to a TER of 0.03% (and such low-cost funds do exist), you would still be able to retain over 98% of the market value after 50 years! As the chart below shows, the market value and investment value curves nearly overlap — a stark contrast to the widening gap we saw with a 1% TER.

{{< chart >}}
type: 'line',
data: {
  labels: ['10', '20', '30', '40', '50'],
  datasets: [
    {
      label: 'Market Value (10%)',
      data: [25937.42, 67275.00, 174494.02, 452592.56, 1173908.53],
      borderColor: 'rgb(34, 139, 34)',
      backgroundColor: 'rgba(34, 139, 34, 0.1)',
      borderWidth: 2,
      tension: 0.3,
      pointRadius: 4,
      yAxisID: 'y'
    },
    {
      label: 'Investment Value (9.97%)',
      data: [25866.77, 66908.99, 173071.98, 447681.35, 1158007.18],
      borderColor: 'rgb(220, 53, 69)',
      backgroundColor: 'rgba(220, 53, 69, 0.15)',
      borderWidth: 2,
      tension: 0.3,
      pointRadius: 4,
      fill: '-1',
      yAxisID: 'y'
    },
    {
      label: 'Percentage Kept',
      data: [99.73, 99.46, 99.19, 98.91, 98.65],
      borderColor: 'rgb(255, 165, 0)',
      backgroundColor: 'rgba(255, 165, 0, 0.1)',
      borderWidth: 2,
      borderDash: [5, 5],
      tension: 0.3,
      pointRadius: 4,
      yAxisID: 'y1'
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
      position: 'left',
      title: {
        display: true,
        text: 'Value ($)'
      },
      ticks: {
        callback: function(value) {
          return '$' + value.toLocaleString();
        }
      }
    },
    y1: {
      position: 'right',
      title: {
        display: true,
        text: 'Percentage Kept (%)'
      },
      min: 50,
      max: 100,
      ticks: {
        callback: function(value) {
          return value + '%';
        }
      },
      grid: {
        drawOnChartArea: false
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
          if (context.dataset.yAxisID === 'y1') {
            return context.dataset.label + ': ' + context.parsed.y + '%';
          }
          return context.dataset.label + ': $' + context.parsed.y.toLocaleString();
        }
      }
    }
  }
}
{{< /chart >}}

<small>**Figure 7.** Impact of 0.03% TER on a $10,000 investment over 50 years</small>

### Is My Fund Cost High?

I have seen people ask this question when evaluating whether to select a fund: "Is this X% fund cost high?" To answer this question, you can simply repeat the calculations I provided earlier. Determine the percentage of money that you would lose to fees over your investment horizon and decide whether that percentage is acceptable to you. If you find it unacceptable, the fund cost might be considered high, and you may want to consider looking for one with lower fees.

## Summary

[John C. Bogle](https://en.wikipedia.org/wiki/John_C._Bogle) aptly summarized the concepts discussed in this post as "The magic of compounding investment returns" and "The tyranny of compounding investment costs" in his book, [The Little Book of Common Sense Investing](https://en.wikipedia.org/wiki/The_Little_Book_of_Common_Sense_Investing). This post is heavily inspired by Mr. Bogle's insights.

## Disclaimers

I am not a professional investor or financial advisor, nor do I claim to be. You are solely responsible for your financial decisions. I do not accept responsibility for any inaccuracies in this blog post. The content reflects my personal research and understanding and should not be interpreted as professional advice.