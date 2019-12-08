import re, requests, bs4, csv, datetime
import pandas as pd

pd.set_option('display.max_columns',1000)
pd.set_option('display.max_rows',50)
pd.set_option('display.width',1000)
pd.set_option('display.max_colwidth', 100)

def weeklyPBPScrape(yr,wkNum):
    print(datetime.datetime.now())
    #Scrape CBS NFL schedule for week "wkNum", and generate boxscore links
    #Scrape each boxscore link from above and write to csv
    #Ex, https://www.cbssports.com/nfl/gametracker/boxscore/NFL_20171210_IND@BUF

    cbs_url = 'https://www.cbssports.com'
    #https://www.pro-football-reference.com/years/2019/week_1.htm
    schedule_url = '/nfl/schedule/'+str(yr)+'/regular/'(

    seasonDF = pd.DataFrame(columns=['Week','Date','Road','Home','url'])
    # Ex, 1, YYYY-MM-DD, AWY, @HME, http://...AWY@HME/

    
    for i in range(1,18): #17 weeks
        weekURL = cbs_url+schedule_url+str(i)
        wkSoup = bs4.BeautifulSoup(requests.get(weekURL).text,'html.parser')
        gameURLs = wkSoup.select('.CellGame a[href]')
        numGm = len(gameURLs)
        
        #create DF of one week's games
        thisWkDF = pd.DataFrame(columns=['Week','Date','Road','Home','url'])
        
        for j in range(numGm):
            link = gameURLs[j].get('href')
            p = link.find('NFL_')+4
            thisWkDF.loc[j] = [i] + \
                              [str(link[p:p+4]+'-'+link[p+4:p+6]+'-'+link[p+6:p+8])]+\
                              [link[p+9:(link.find('@'))]]+\
                              [link[(link.find('@')):-1]]+\
                              [cbs_url+link] 

        seasonDF = seasonDF.append(thisWkDF)        
        #del(thisWkDF)
        #append above DF to schedDF

    gmURLs = seasonDF[seasonDF['Week']==wkNum]['url']
    numGm = len(gmURLs)

    #for i in range(numGm):
    #    gmURLs.loc[i] = cbs_url+str(wkSchedSoup.select('.CellGame a[href]')[i].get('href')).replace('recap','boxscore')

#    soupOutput = []
#    tagDump = open('nflPlayByPlayScrape2019(Tags).csv','a',newline='') #change to append
#    tagCSVWriter = csv.writer(tagDump,delimiter=',',lineterminator='\n') #change to append

#    realOutput = []
#    realDump = open('nflPlayByPlayScrape2019.csv','a',newline='')
#    realCSVWriter = csv.writer(realDump,delimiter=',',lineterminator='\n')

    seasonDF.drop('url',axis=1).to_csv('2019_schedule_single.csv', sep = ',', encoding = 'utf-8', index = False)

    #######################################################

    tagPick_lines = '#TableBase .TableBase-bodyTd'
    #tagPick_lines = '.team-stats tr'

    #tagPick_stat_feld/valu = '.team-stats td'
    #print('\n'+str(len(url_game))+'\n')
    #print(url_game[-1])

    gmPbpDF = pd.DataFrame(columns=['Week','Date','Road','Home','url','playResult','play'])

    for i in range(len(gmURLs)): #numgames
        url=str(gmURLs.loc[i])
        
        pbpSoup = bs4.BeautifulSoup(requests.get(url).text,'html.parser')
        
        #gameURLs = wkSoup.select('.CellGame a[href]')
        numPlays = len(pbpSoup.select(tagPick_lines))
        print('Scraping plays for: '+url+' numPlays: '+str(numPlays))

        #create DF of one game's plays
        thisGmDF = pd.DataFrame(columns=['Week','Date','Road','Home','url','playResult','play'])
        
        for j in range(0,numPlays,2):
            link = gmURLs.loc[i]
            p = link.find('NFL_')+4
            thisGmDF.loc[j]=[wkNum]+\
                            [str(link[p:p+4]+'-'+link[p+4:p+6]+'-'+link[p+6:p+8])]+\
                            [link[p+9:(link.find('@'))]]+\
                            [link[(link.find('@')):-1]]+\
                            [link]+\
                            [pbpSoup.select(tagPick_lines)[j].getText().splitlines()[1]]+\
                            [pbpSoup.select(tagPick_lines)[j+1].getText().splitlines()[1]]
            
        gmPbpDF = gmPbpDF.append(thisGmDF)

    print("Scraping Completed. Writing Files.")
    print(datetime.datetime.now())

    if(wkNum<10):
        file='nflPlayByPlayScrape'+str(yr)+'wk0'+str(wkNum)+'.csv'
    else:
        file='nflPlayByPlayScrape'+str(yr)+'wk'+str(wkNum)+'.csv'
        
    gmPbpDF.to_csv(file, sep = ',', encoding = 'utf-8', index = False)    

    #gmPbpDF = pd.read_csv('nflPlayByPlayScrape2019wk06.csv')
    #week6 = gmPbpDF[gmPbpDF['play'].contains('^(')]
    print("Completed.")
    print(datetime.datetime.now())

    startField = '.+?[(]'  #includes the open bracket though
    clock = '[(].+?[)]'

    player = '[)].+?[/s]'

    rushPlay = '[)].+?[/s]'
    '1 & 10 - GB 25(14:18 - 2nd) A.Jones left guard to GB 28 for 3 yards (D.Wolfe).'
    #re.search('.+?[(]',gmPbpDF.play[1]).group(0)

    #gmPbpDF['player'] = gmPbpDF.apply(lambda x: re.search(player, x['play']).group(0), axis=1)
    
    
    #test = gmPbpDF[gmPbpDF['play'].str.contains('J.Flacco')]
