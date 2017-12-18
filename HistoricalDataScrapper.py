#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:14:35 2017

@author: Aman
"""

# Used to extract DOM
import requests
# Used to parse DOM
from bs4 import BeautifulSoup
# Used to create data frame
import pandas as pd
# Used to get current date
import datetime

# Page you want to parse
LANDING_PAGE = "https://coinmarketcap.com"
BASE_URL = "/coins/views/all/"
HISTORICAL_DATA_URL_EXTENSION = "historical-data/?start="
CURRENT_DATE = datetime.datetime.today().strftime('%Y%m%d')
DEFAULT_START_DATE = "20130428"
AVAILABLE_SYMBOLS = ['BTC', 'ETH', 'BCH', 'XRP', 'LTC', 'ADA', 'MIOTA', 'DASH', 'XEM', 'XMR', 'BTG', 'XLM', 'NEO', 'ETC', 'QTUM', 'BCC', 'ZEC', 'LSK', 'WAVES', 'STRAT', 'BTS', 'HSR', 'BCN', 'NXT', 'MONA', 'XVG', 'DOGE', 'ARK', 'STEEM', 'DCR', 'KMD', 'SC', 'EMC2', 'PIVX', 'GBYTE', 'VTC', 'FCT', 'DGB', 'ETN', 'VEN', 'XRB', 'SYS', 'BTCD', 'CNX', 'XZC', 'NXS', 'GXS', 'GAME', 'NAV', 'ETP', 'PPC', 'BAY', 'BLOCK', 'PURA', 'SKY', 'MNX', 'UBQ', 'ZEN', 'ACT', 'GRS', 'XAS', 'XCP', 'SMART', 'RDD', 'PART', 'FTC', 'POT', 'XDN', 'LKK', 'VIA', 'RISE', 'VOX', 'KCS', 'NMC', 'XBY', 'AEON', 'FAIR', 'CLOAK', 'EMC', 'XWC', 'LBC', 'BURST', 'NEBL', 'ION', 'CRW', 'NLG', 'IOC', 'DMD', 'SIB', 'SBD', 'BCO', 'OK', 'RMC', 'SHIFT', 'DCT', 'XP', 'OMNI', 'XEL', 'BTX', 'BLK', 'NLC2', 'GRC', 'SLS', 'FRST', 'PHR', 'MUE', 'THC', 'FLO', 'GOLOS', 'VRC', 'CLAM', 'GAM', 'GCR', 'RBY', 'PASC', 'ATB', 'RADS', 'NEOS', 'BSD', 'EXP', 'XSPEC', 'LEO', 'HEAT', 'TX', 'MOON', 'TCC', 'SLR', 'UNO', 'BBR', 'XVC', 'LMC', 'BTM', 'DIME', 'SPHR', 'ONION', 'ENRG', 'NVC', 'OXY', 'BITB', 'BDL', 'PPY', 'MEME', 'PINK', 'TIPS', 'MTNC', 'ZNY', 'CURE', 'MUSIC', 'SEQ', 'SXC', 'POSW', 'ECC', 'EAC', 'ODN', 'XMY', 'XTO', 'AUR', 'MXT', 'BRK', 'XBC', 'XST', 'BTDX', 'TOA', 'PZM', 'IOP', 'ZEPH', 'EDR', 'PTC', 'ABY', 'DYN', 'KORE', 'SYNX', 'DBIX', 'XSH', 'RIC', 'XPM', 'DOPE', 'PUT', 'BIS', 'BELA', 'NTRN', 'EXCL', 'ATMS', 'ZCL', 'BLU', 'SWIFT', 'HTML5', 'SNRG', 'BRX', '2GIVE', 'YOC', 'TRUST', 'ERC', 'GLD', 'GCC', 'TZC', 'NYC', 'EGC', 'CANN', 'PIRL', 'AC', 'ONX', 'GEO', 'CHC', 'KRB', 'CREA', 'INN', 'GBX', 'PKB', 'BLITZ', 'ANC', 'CHIPS', 'VIVO', 'MINT', 'PAC', 'RUP', 'HUC', 'VTR', 'VRM', 'START', 'TRC', 'DOT', 'SUPER', 'UFO', 'UNIT', 'EFL', 'BPL', 'BASH', 'BTB', 'QRK', 'SPR', 'XMG', 'ALQO', 'HUSH', 'CNT', 'ESP', 'LUX', 'IXC', 'XCN', 'ADC', 'CRAVE', 'HYP', 'ZOI', 'NOTE', 'WDC', 'ZENI', 'MEC', 'GB', 'CBX', 'BXT', 'ELE', '1337', 'PND', 'LINX', 'ITNS', 'XFT', 'FCN', 'BTCZ', 'EQT', 'GRE', 'EBST', 'ZET', 'DEM', 'LOG', 'KOBO', 'SPRTS', 'ZEIT', 'BWK', 'BTA', 'XLR', 'ORB', 'SUMO', 'BUZZ', 'ELLA', 'MAG', 'UNB', 'PROC', 'XMCC', 'GCN', 'CDN', 'UIS', 'BYC', 'BRIT', 'FST', '42', 'CNO', 'GRWI', 'BTCS', 'ADZ', 'UNITS', 'KEK', 'RNS', 'CARBON', 'LINDA', 'INFX', 'PURE', 'FJC', 'SMLY', 'IFLT', 'XHI', 'VISIO', 'NUKO', 'BIGUP', 'DCY', 'UNIFY', 'TROLL', 'ARC', 'HOLD', 'J', 'DNR', 'DFT', 'ZER', 'SIGT', 'CCRB', 'XIOS', 'ECA', 'MOIN', 'BBP', 'DP', 'NETKO', 'MAO', 'INSN', 'UTC', 'V', 'LTB', 'POP', 'RAIN', 'MZC', 'XCPO', 'CPC', 'ZZC', 'DSH', 'XJO', 'VSX', 'NET', 'USNBT', 'TES', 'ATOM', 'NOBL', 'CRC', 'XGOX', 'LCP', 'LDOGE', 'MAX', 'BRO', 'SMC', 'TRUMP', 'BTCR', 'FC2', 'BUN', 'HPC', 'ZUR', 'CRM', 'TAG', 'MUT', 'FLT', 'UNIC', 'PXC', 'BRIA', 'BCF', 'UNI', 'DGC', 'XPD', 'NYAN', '8BIT', 'KLC', 'SPACE', 'TIT', 'COLX', 'ITI', 'FUNK', 'BUCKS', 'LOT', 'BSTY', 'WHL', 'ALTCOM', 'DAXX', 'OHM', 'CHESS', 'PAK', 'CCN', 'ABJ', 'VLT', 'SLG', 'EMB', 'CORG', 'BITS', 'SWING', 'TYCHO', 'XPTX', 'PASL', 'JIN', 'TRI', 'KUSH', 'XLC', 'ENT', 'CNNC', 'CUBE', 'BOLI', 'VIDZ', 'PIGGY', 'C2', 'MRJA', 'HNC', 'DRXNE', 'SAGA', 'BLAS', 'REE', 'MAD', 'MEOW', 'EL', 'CMPCO', 'QCN', 'POST', 'LANA', 'PHS', 'BTG', '4CHN', 'DUO', 'MNC', 'TRK', 'XPY', 'BUMBA', 'ETHD', 'RED', '888', '808', 'PHO', 'CAT', 'PXI', 'XVP', 'TTC', 'BTPL', 'QTL', 'LTCR', 'TSE', 'XCXT', 'USDE', 'DBTC', 'XCT', 'COAL', 'HONEY', 'BOST', 'AERM', 'EUC', 'ARG', 'CJ', 'SCORE', 'ECO', 'GP', 'CMT', 'DRM', 'RPC', 'ANTI', 'MONK', 'CACH', 'GPU', 'VUC', 'GTC', 'URO', 'AMMO', '611', 'BIP', 'MAR', 'SRC', 'GLT', 'PRC', 'LTCU', 'CPN', 'GPL', '$$$', 'ACP', 'SOIL', 'MILO', 'KAYI', 'KURT', 'SONG', 'CXT', 'ASAFE2', 'CRDNC', 'ERY', 'NRO', 'TOR', 'SPT', 'WOMEN', 'KRONE', 'GRIM', 'LBTC', 'MSCN', 'FRAZ', 'RBT', 'ICON', 'XCS', 'ELS', 'LVPS', 'ROOFS', 'ARGUS', 'XRC', 'EBT', 'GSR', 'HMC', 'NANOX', 'ABN', 'DMB', 'APW', 'ECN', 'CSC', 'STCN', 'XC', 'SDC', 'FIMK', 'CV2', 'YASH', 'RC', 'CRYPT', 'HTC', 'SHORTY', 'OPAL', 'METAL', 'USC', 'HBN', 'VAL', 'MAC', 'NKA', 'GAIA', 'STS', 'AU', 'I0C', 'TALK', 'STV', 'WAY', 'BERN', 'SPEX', 'SAC', 'Q2C', 'SH', 'GLC', 'FLY', 'WYV', 'GUN', 'MNM', 'XGR', 'TGC', 'PR', 'ICN', 'EMD', 'HODL', 'FNC', 'HAL', 'AMBER', 'CYP', 'YAC', 'WMC', 'GAP', 'EVIL', 'FRC', 'EVO', 'XBTC21', 'RBIES', 'URC', 'ACOIN', 'ISL', 'XRA', 'MOJO', 'PX', 'BLC', 'GRT', 'FRK', 'ARI', 'HMP', 'LEA', 'MARS', 'XCRE', 'KED', 'FIRE', 'ARCO', 'SOON', 'DLC', 'VC', 'CON', 'NEVA', 'TAJ', 'IMS', 'XRE', 'SLING', 'CRX', 'VEC2', 'BITZ', 'MTLMC3', 'SCRT', 'ALL', 'CF', 'BTQ', 'MCRN', 'GCC', 'BLZ', 'MST', 'PRX', 'JWL', 'XBTS', 'HXX', 'BSTAR', 'CTO', 'ZMC', 'MND', 'BVC', 'PULSE', 'SLM', 'ICOB', 'VOT', 'VPRC', 'WARP', 'EMP', 'BLRY', 'DRS', 'RUPX', 'MAY', 'XCO', 'PIE', 'ATX', 'BENJI', 'IMPS', 'OFF', 'VIP', 'DLISK', 'TEK', 'BSC', 'ZYD', 'CRT', 'ORLY', 'STEPS', 'OS76', 'EGO', 'ITZ', 'WORM', 'IMX', 'PLNC', 'FLAX', 'FLVR', 'ADCN', 'CWXT', 'PONZI', 'CESC', 'CAGE', 'LUNA', 'TAGR', 'BIOS', 'ARB', 'SFC', 'CNC', 'BOAT', 'PEX', 'DPAY', 'FUZZ', 'CASH', 'KIC', 'WBB', 'BNX', 'GBT', 'JOBS', 'PLACO', 'SLEVIN', 'XOC', 'VLTC', 'CREVA', 'KNC', 'ZNE', 'IBANK', 'SCS', 'DES', 'BIOB', 'BRAIN', 'HVCO', 'G3N', 'DOLLAR', 'AGLC', 'LIR', 'CAB', 'SDP', 'GEERT', 'ALTC', 'VOLT', 'RSGP', 'GBC', 'SOCC', 'SLFI', 'SANDG', 'MGM', 'RIDE', 'VTA', 'P7C', 'DAS', 'WBC', 'NODC', 'CTIC2', 'TOKEN', 'TRADE', 'TSTR', 'XNG', 'ULA', 'CONX', 'PIZZA', 'DGCS', 'SOJ', 'MRNG', 'MNC', 'ENV', 'CALC', 'FAL', 'FDC', 'ATMC', 'BCX', 'BCD', 'XTZ', 'SBTC', 'CLUB', 'REC', 'WC', 'FRGC', 'INF', 'HWC', 'STC', 'FIL', 'SHND', 'XIN', 'B2X', 'THS', 'BTU', 'BT1', 'BT2', 'SBC', 'IFC', 'VASH', 'GBG', 'B3', 'BOS', 'DSR', 'TOK', 'FOR', 'SEND', 'OCOW', 'MSD', 'SIGMA', 'EAG', 'OMC', 'MGC', 'VOYA', 'MAVRO', 'AKY', 'PEC', 'FLASH', 'BSR', 'DEUS', 'NBIT', 'CMP', 'PCOIN', 'SKR', 'TELL', 'APC', 'TER', 'MOTO', 'PRM', 'GLS', 'ZBC', 'BUB', 'BEST', 'DFS', 'PNX', 'SHA', 'GAY', 'AIB', 'DMC', 'ACC', 'XRY', 'MGC', 'BTBc', 'ANI', 'SKULL', 'BAT', 'RBBT', 'BSN', 'INDIA', 'SAK', 'HNC', 'VULC', 'BCCS', 'BET', 'WOW', 'FLAP', 'TCOIN', 'PCS', 'KARMA', 'LDCN', 'PRIMU', 'QORA', 'WINK', 'RCN', 'MAGN', 'FRN', 'WA', 'LAZ', 'UNRC', 'RUPX', 'FONZ', 'ACN', 'XQN', 'RUBIT', 'CME', '9COIN', 'DBG', 'COUPE', 'GMX', 'HIGH', 'REGA', 'RHFC', 'ZSE', 'UR', 'AMS', 'NAMO', 'MARX', 'BIRDS', 'QBT', 'GBRC', 'AXIOM', 'BIT', 'LTH', 'HALLO', 'DON', 'DASHS', 'STARS', 'HCC', 'POKE', 'MONETA', 'DUTCH', 'BXC', 'FFC', 'CHEAP', 'UNC', 'LKC', 'BLAZR', 'SKC', 'EDRC', 'GRN', 'ROYAL', 'TOP', 'MMXVI', 'PRN', 'BGR', 'PI', 'TODAY', 'IRL', 'AV', 'TOPAZ', 'IVZ', 'LEPEN', 'YES', 'CYDER', 'ANTX', 'HYPER', 'PCN', 'CBD', 'XAU', 'FRWC', 'ACES', 'ASN', 'FUTC', 'GAIN', 'CYC', 'TRICK', 'VGC', 'PDG', 'UTA', 'X2', 'TEAM', 'TCR', 'QBC', 'DUB', 'XVE', 'BITOK', 'RUNNERS', 'MBL', 'XID', 'EGG', 'SPORT', 'CC', 'BAC', 'OP', 'RICHX', 'FAZZ', 'KASHH', 'CLINT', 'DISK', 'PAYP', 'XTD', 'FID', 'NBE', 'ELC', 'SYNC', 'GML', 'WSX', 'SHELL', 'DCRE', 'OPES', 'PSY', 'SFE', 'GOLF', 'MONEY', 'XSTC', 'TERA', 'XDE2', 'BIXC', 'TLE', 'TYC', 'ADK', 'TURBO', 'MEN', 'MAGE', 'XYLO', 'WEC', 'SIC']

# Possible values of cc_symbol
def historical_data_scrapper(cc_symbol, start_date=DEFAULT_START_DATE, end_date=CURRENT_DATE):
    dfColumns = []
    symbolData = []
    subUrl = ""
    symbolFound = False
    
    # Collect and parse first page
    page = requests.get(LANDING_PAGE + BASE_URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    # Extract rows from table body
    rows = soup.body.table.tbody.find_all('tr')

    # Parsing individual rows
    for val in rows:        
        for symbol,symbol_ref in zip(val.find_all(class_="currency-symbol"), val.find_all(class_="currency-name-container")): 
            if cc_symbol == symbol.a.get_text():
                symbolFound = True
                subUrl = symbol_ref.get('href') + HISTORICAL_DATA_URL_EXTENSION + start_date + "&end=" + end_date
                print (cc_symbol + " data from: " + start_date + " to: " + end_date)
                break
            
    if symbolFound:
        subPage = requests.get(LANDING_PAGE + subUrl)
        subSoup = BeautifulSoup(subPage.text, 'html.parser')
        
        # Extract table header from DOM
        tableHead = subSoup.body.table.thead.find_all('th')
        
        # Get value of individual headers
        for header in tableHead:
            dfColumns.append(header.get_text())
            #print (header.get_text())
    
        #Extract rows from body
        subPageRows = subSoup.body.table.tbody.find_all('tr')
        
        #Parsing individual rows
        for val in subPageRows:
            data_row = []
            for cols in val.find_all('td'):    
                data_row.append(cols.get_text().strip())
            symbolData.append(data_row) 
                            
        # Collating data in DataFrame
        df = pd.DataFrame(symbolData, columns=dfColumns).to_string(index=False)
        print (df)

    else:
        print ("ERROR: Symbol Invalid, list of available symbols: ", AVAILABLE_SYMBOLS)


#historical_data_scrapper("BTC")
historical_data_scrapper("ATOM", start_date="20171201", end_date="20171217")