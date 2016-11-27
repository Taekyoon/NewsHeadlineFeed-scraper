#!/bin/bash
function run_crawl() {
  while :
  do
    scrapy crawl bbcrss
    scrapy crawl abcrss
    scrapy crawl latrss
    scrapy crawl nytrss
    scrapy crawl timerss
    scrapy crawl wstrss

    sleep 3600
  done
}

nohup run_crawl &
