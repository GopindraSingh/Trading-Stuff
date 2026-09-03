from datetime import datetime
import os
import sys
import pandas as pd
import requests
import yfinance as yf


def get_dynamic_nse_universe():
  """Dynamically pulls a broad, liquid stock universe with a comprehensive pool."""
  try:
    response = requests.get(
        "https://raw.githubusercontent.com/AnishDe1202/nifty-stocks-data/master/nifty500.json",
        timeout=5,
    )
    if response.status_code == 200:
      symbols = response.json()
      return [f"{s}.NS" for s in symbols]
  except Exception:
    pass

  automated_pool = [
      "AARTIDRUGS",
      "AAVAS",
      "ABBOTINDIA",
      "ABCAPITAL",
      "ABFRL",
      "ABSLAMC",
      "ACC",
      "ACADEMY",
      "ADANIENT",
      "ADANIGREEN",
      "ADANIPORTS",
      "ATGL",
      "ADANIPOWER",
      "ABCAS",
      "AegisLOG",
      "AFFLE",
      "AIAENG",
      "AJANTPHARM",
      "APLAPOLLO",
      "ALKEM",
      "ALKYLAMINE",
      "ALLCARGO",
      "AMARAJABAT",
      "AMBUJACEM",
      "ANANDRATHI",
      "ANGELONE",
      "ANURAS",
      "APARINDS",
      "APOLLOHOSP",
      "APOLLOTYRE",
      "APTUS",
      "ASAHIINDIA",
      "ASHOKLEY",
      "ASIANPAINT",
      "ASTERDM",
      "ASTRAZEN",
      "ASTRAL",
      "ATUL",
      "AUBANK",
      "AUROPHARMA",
      "AVAS",
      "AXISBANK",
      "BAJAJ-AUTO",
      "BAJFINANCE",
      "BAJAJFINSV",
      "BAJAJHLDNG",
      "BALAMINES",
      "BALKRISIND",
      "BALRAMCHIN",
      "BANDHANBNK",
      "BANKBARODA",
      "BANKINDIA",
      "BATAINDIA",
      "BAYERCROP",
      "BBL",
      "BDL",
      "BEL",
      "BEML",
      "BEPL",
      "BERGEPAINT",
      "BFUTILITIE",
      "BHARATFORG",
      "BHARTIARTL",
      "BHEL",
      "BIOCON",
      "BIRLACORPN",
      "BSOFT",
      "BLS",
      "BLUESTARCO",
      "BORORENEW",
      "BOSCHLTD",
      "BPCL",
      "BRIGADE",
      "BRITANNIA",
      "MAPMYINDIA",
      "BSE",
      "BURGERKING",
      "CAMPUS",
      "CANBK",
      "CANFINHOME",
      "CAPLIPOINT",
      "CARBORUNIV",
      "CASTROLIND",
      "CEATLTD",
      "CELEBRITY",
      "CENTRALBK",
      "CDSL",
      "CENTURYPLY",
      "CERA",
      "CESC",
      "CGCL",
      "CHALET",
      "CHAMBLFERT",
      "CHOLAFIN",
      "CHOLAHLDNG",
      "CIPLA",
      "CUB",
      "CIEINDIA",
      "COALINDIA",
      "COCHINSHIP",
      "COFORGE",
      "COLPAL",
      "CAMS",
      "CONCOR",
      "COROMANDEL",
      "CRAFTSMAN",
      "CREDITACC",
      "CROMPTON",
      "CUMMINSIND",
      "CYIENT",
      "DABUR",
      "DalBHARAT",
      "DATAPATTNS",
      "DBL",
      "DCBBANK",
      "DCMSHRIRAM",
      "DEEPAKFERT",
      "DEEPAKNTR",
      "DELHIVERY",
      "DEVYANI",
      "DIVISLAB",
      "DIXON",
      "LALPATHLAB",
      "DRREDDY",
      "EIDPARRY",
      "EIHOTEL",
      "EICHERMOT",
      "ELGIEQUIP",
      "EMAMILTD",
      "ENDURANCE",
      "ESCORTS",
      "EXIDEIND",
      "NYKAA",
      "FEDERALBNK",
      "FACT",
      "FINEORG",
      "FINCABLES",
      "FINPIPE",
      "FSL",
      "FIVESTAR",
      "FORTIS",
      "GAIL",
      "GALAXYSURF",
      "GARFIBRES",
      "GESHIP",
      "GHCL",
      "GICRE",
      "GILLETTE",
      "GLAND",
      "GLAXO",
      "GLENMARK",
      "MEDANTA",
      "GOCOLORS",
      "GODREJCP",
      "GODREJIND",
      "GODREJPROP",
      "GRANULES",
      "GRASIM",
      "GRAVITA",
      "GRINDWELL",
      "GUJGASLTD",
      "GNFC",
      "GPPL",
      "GSFC",
      "GSPL",
      "HEG",
      "HCLTECH",
      "HDFCAMC",
      "HDFCBANK",
      "HDFCLIFE",
      "HFCL",
      "HATSUN",
      "HAVELLS",
      "HCG",
      "HIL",
      "HEMIPROPERTIES",
      "HINDALCO",
      "HINDCOPPER",
      "HINDPETRO",
      "HINDUNILVR",
      "HINDZINC",
      "POWERMECH",
      "HSCL",
      "HUDCO",
      "ICICIBANK",
      "ICICIGI",
      "ICICIPRULI",
      "IDBI",
      "IDFC",
      "IDFCFIRSTB",
      "IEX",
      "IFBIND",
      "IIFL",
      "INDAMCO",
      "INDHOTEL",
      "INDIACEM",
      "INDIAMART",
      "INDIANB",
      "INDOCO",
      "INDUSINDBK",
      "INDUSTOWER",
      "INFIBEAM",
      "INFY",
      "INGV",
      "INSECTICID",
      "IOB",
      "IOC",
      "IPCALAB",
      "IRB",
      "IRCON",
      "IRCTC",
      "ITC",
      "ITI",
      "JANDJ",
      "JCHAC",
      "JBCHEPHARM",
      "JKCEMENT",
      "JKIL",
      "JKLAKSHMI",
      "JKPAPER",
      "JMFINANCIL",
      "JSWENERGY",
      "JSWSTEEL",
      "JTEKTINDIA",
      "JINDALSTEL",
      "JISLJALEQS",
      "JUBLFOOD",
      "JUBLINGRIA",
      "JUSTDIAL",
      "JYOTHYLAB",
      "KAJARIACER",
      "KALPATPOWR",
      "KALYANKJIL",
      "KANSAINER",
      "KARURVYSYA",
      "KEC",
      "KEI",
      "KNRCON",
      "KOTAKBANK",
      "KPRMILL",
      "KRBL",
      "KSCL",
      "KSB",
      "LODHA",
      "LTIM",
      "LTTS",
      "LICHSGFIN",
      "LICI",
      "LINDEINDIA",
      "LUPIN",
      "LUXIND",
      "MMTC",
      "MOIL",
      "MRF",
      "MGL",
      "M&M",
      "M&MFIN",
      "MAHABANK",
      "MAHICKM",
      "MAHLOG",
      "MANAPPURAM",
      "MRPL",
      "MARICO",
      "MARUTI",
      "MASTEK",
      "MAXHEALTH",
      "MAZDOCK",
      "METROPOLIS",
      "MINDACORP",
      "MOTHERSON",
      "MPHASIS",
      "MCX",
      "MUTHOOTFIN",
      "NESCO",
      "NESTLEIND",
      "NETWORK18",
      "NAM-INDIA",
      "NCC",
      "NLCINDIA",
      "NMDC",
      "NTPC",
      "NH",
      "NUVAMA",
      "OBEROIRLTY",
      "ONGC",
      "OIL",
      "OLECTRA",
      "PAYTM",
      "OFSS",
      "PCJEWELLER",
      "PEL",
      "PIIND",
      "PNBHOUSING",
      "PNCINFRA",
      "PVRINOX",
      "PageIND",
      "PERSISTENT",
      "PETRONET",
      "PFIZER",
      "PHOENIXLTD",
      "PIDILITIND",
      "POLYCAB",
      "POONAWALLA",
      "PFC",
      "POWERGRID",
      "PRAJIND",
      "PRESTIGE",
      "PRINCEPIPE",
      "PRSMJOHNSN",
      "PSS",
      "QUESS",
      "RBLBANK",
      "RECLTD",
      "RITES",
      "RADICO",
      "RAIN",
      "RAJESHEXPO",
      "RALLIS",
      "RCF",
      "RELIANCE",
      "ROUTE",
      "SBICARD",
      "SBILIFE",
      "SBIN",
      "SHREECEM",
      "SRF",
      "SANOFI",
      "SFL",
      "SHK",
      "SHOPERSTOP",
      "SHRIRAMFIN",
      "SIEMENS",
      "SOBHA",
      "SOLARINDS",
      "SONACOMS",
      "SONATSOFTW",
      "SPARC",
      "STAR",
      "SBCL",
      "SUDARSCHEM",
      "SUMICHEM",
      "SUNDARMFIN",
      "SUNDRMFAST",
      "SUNPHARMA",
      "SUNTV",
      "SUPRAJIT",
      "SUPREMEIND",
      "SUZLON",
      "SWANENERGY",
      "SYMPHONY",
      "SYNGENE",
      "TVSMOTOR",
      "TATACHEM",
      "TATACOFFEE",
      "TATACOMM",
      "TCS",
      "TATACONSUM",
      "TATAELXSI",
      "TATAINVEST",
      "TATAMOTORS",
      "TATAPOWER",
      "TATASTEEL",
      "TTML",
      "TeamLease",
      "TECHM",
      "TECHNOE",
      "TEJASNET",
      "NIACL",
      "RAMCOCEM",
      "THERMAX",
      "THYROCARE",
      "TIDEWATER",
      "TIMKEN",
      "TITAN",
      "TORNTPHARM",
      "TORNTPOWER",
      "TRENT",
      "TRIDENT",
      "TRIVENI",
      "TRITURBINE",
      "UCOBANK",
      "UFLEX",
      "UJJIVANSFB",
      "ULTRACEMCO",
      "UNICHEMLAB",
      "UPL",
      "UTIAMC",
      "VGUARD",
      "VMART",
      "VODAFONE",
      "VOLTAS",
      "VRLLOG",
      "VSTIND",
      "WABAG",
      "WELCORP",
      "WELSPUNIND",
      "WESTLIFE",
      "WHIRLPOOL",
      "WIPRO",
      "WOCKPHARMA",
      "YESBANK",
      "ZENSARTECH",
      "ZOMATO",
      "ZYDUSLIFE",
      "ZYDUSWELL",
  ]
  return [f"{sym}.NS" for sym in automated_pool]


def scan_momentum_sellers():
  current_date = datetime.now().strftime("%Y-%m-%d")
  print(f"📅 Scan Date: {current_date}")

  tickers = get_dynamic_nse_universe()
  print(
      f"⏳ Downloading intraday data for {len(tickers)} equities in progress..."
  )

  original_stderr = sys.stderr
  sys.stderr = open(os.devnull, "w")
  try:
    data = yf.download(
        tickers, period="2d", interval="15m", group_by="ticker", progress=False
    )
  finally:
    sys.stderr.close()
    sys.stderr = original_stderr

  all_losers = []
  shortlisted_losers = []
  market_open_time = datetime.strptime("09:15:00", "%H:%M:%S").time()

  for ticker in tickers:
    try:
      if len(tickers) > 1:
        if ticker not in data.columns.levels[0]:
          continue
        ticker_df = data[ticker].dropna()
      else:
        ticker_df = data.dropna()

      if ticker_df.empty:
        continue

      if isinstance(ticker_df.columns, pd.MultiIndex):
        ticker_df.columns = ticker_df.columns.get_level_values(0)

      ticker_df = ticker_df.dropna()
      opening_candle = ticker_df[ticker_df.index.time == market_open_time]

      if not opening_candle.empty:
        latest_candle = opening_candle.iloc[-1]

        open_p = float(latest_candle["Open"])
        close_p = float(latest_candle["Close"])
        high_p = float(latest_candle["High"])
        low_p = float(latest_candle["Low"])
        vol = int(latest_candle["Volume"])

        candle_drop_pct = ((close_p - open_p) / open_p) * 100
        turnover_cr = (vol * close_p) / 10_000_000

        candle_range = high_p - low_p
        close_location = (
            (close_p - low_p) / candle_range if candle_range > 0 else 1.0
        )

        row_data = {
            "Ticker": ticker.replace(".NS", ""),
            "Date": current_date,
            "15m_Open": round(open_p, 2),
            "15m_Close_Entry": round(close_p, 2),
            "Candle_Drop_%": round(candle_drop_pct, 2),
            "Turnover_Cr": round(turnover_cr, 2),
            "1%_Profit_Target": round(close_p * 0.99, 2),
            "Hard_Stop_Loss": round(high_p, 2),
        }

        # Tier 1: General Losers (Drop < -0.5%, Turnover >= 4 Cr, Close Location <= 0.25)
        if (
            candle_drop_pct < -0.5
            and turnover_cr >= 4.0
            and close_location <= 0.25
        ):
          all_losers.append(row_data)

        # Tier 2: Shortlisted Most Falling (Drop < -1.5%, Turnover >= 15 Cr, Close Location <= 0.15)
        if (
            candle_drop_pct < -1.5
            and turnover_cr >= 15.0
            and close_location <= 0.15
        ):
          shortlisted_losers.append(row_data)

    except Exception:
      continue

  df_all = pd.DataFrame(all_losers)
  if not df_all.empty:
    df_all = df_all.sort_values(by="Candle_Drop_%", ascending=True).reset_index(
        drop=True
    )

  df_short = pd.DataFrame(shortlisted_losers)
  if not df_short.empty:
    df_short = df_short.sort_values(
        by="Candle_Drop_%", ascending=True
    ).reset_index(drop=True)

  return df_all, df_short


if __name__ == "__main__":
  all_candidates, shortlisted_candidates = scan_momentum_sellers()

  print("\n🔥 ALL REAL-TIME 15-MINUTE MOMENTUM LOSERS:")
  if not all_candidates.empty:
    print(all_candidates.to_string(index=False))
  else:
    print("No stocks matched the general breakdown criteria today.")

  print("\n" + "=" * 80)
  print("🎯 HIGH-CONVICTION SHORTLISTED (MOST FALLING) SELLERS:")
  if not shortlisted_candidates.empty:
    print(shortlisted_candidates.to_string(index=False))
  else:
    print("No stocks matched the strict shortlisting criteria today.")
