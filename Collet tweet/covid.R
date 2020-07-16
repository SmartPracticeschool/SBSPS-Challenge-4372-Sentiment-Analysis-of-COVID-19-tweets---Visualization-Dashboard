library(rtweet)
library(ggplot2)
library(dplyr)
library(tidytext)

appname <- "Abhinav_Miner"
key <- "7iK5Ti66cINpEg2XoFQyRNnOX"
secret <- "KhGFnEX7uzhrmERBhAhDyvYE3Ze9RR7Dz6FTTwGbsWEilAnsmK"

twitter_token <- create_token(
  consumer_key = "7iK5Ti66cINpEg2XoFQyRNnOX" ,
  consumer_secret ="KhGFnEX7uzhrmERBhAhDyvYE3Ze9RR7Dz6FTTwGbsWEilAnsmK" ,
  access_token = "1126894513992024064-E7rCoWfqusWy5Dux8L4wTE2hpSXrj1",
  access_secret ="Qdd43IwXoNg37EBxr0EetlXWiqrrc6KoRenvfHiPkjzHr" )

rstats_tweets <- search_tweets(q = "#COVID19",
                               n = 500)
data.df <- twListToDF(rstats_tweets) 
head(rstats_tweets$text)
