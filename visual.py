from datetime import datetime, timedelta
import os
import sys
import time
import matplotlib.pyplot as plt
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


def save_stock_chart(
    ticker_df, ticker_name, current_date, stop_loss, target_price
):
    """Generates and saves an intraday price chart highlighting SL and Target levels."""
    os.makedirs("momentum_charts", exist_ok=True)
    target_dt_obj = pd.to_datetime(current_date).date()
    day_df = ticker_df[ticker_df.index.date == target_dt_obj]

    if day_df.empty:
        return

    plt.figure(figsize=(10, 5))
    plt.plot(
        day_df.index,
        day_df["Close"],
        label="15m Close Price",
        color="royalblue",
        linewidth=2,
    )

    # Plot Stop Loss and Target lines
    plt.axhline(
        y=stop_loss,
        color="red",
        linestyle="--",
        label=f"Stop Loss (High): {stop_loss}",
    )
    plt.axhline(
        y=target_price,
        color="green",
        linestyle="--",
        label=f"1% Target: {target_price}",
    )

    plt.title(f"Intraday Breakdown Chart: {ticker_name} ({current_date})")
    plt.xlabel("Time")
    plt.ylabel("Price (INR)")
    plt.legend(loc="upper left")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()

    filename = f"momentum_charts/{ticker_name}_{current_date}.png"
    plt.savefig(filename)
    plt.close()


def scan_momentum_sellers(mode="1", target_date_str=None):
    if mode == "1":
        current_date = datetime.now().strftime("%Y-%m-%d")
        download_kwargs = {"period": "5d"}
    else:
        current_date = target_date_str
        target_dt = datetime.strptime(current_date, "%Y-%m-%d")
        start_dt = target_dt - timedelta(days=7)
        end_dt = target_dt + timedelta(days=1)
        download_kwargs = {
            "start": start_dt.strftime("%Y-%m-%d"),
            "end": end_dt.strftime("%Y-%m-%d"),
        }

    print(f"📅 Scan Date: {current_date}")

    tickers = get_dynamic_nse_universe()
    print(f"⏳ Downloading intraday data and volume baselines in batches...")

    original_stderr = sys.stderr
    sys.stderr = open(os.devnull, "w")

    dataframes = []
    batch_size = 50

    try:
        for i in range(0, len(tickers), batch_size):
            batch = tickers[i : i + batch_size]
            df_batch = yf.download(
                batch,
                interval="15m",
                group_by="ticker",
                progress=False,
                threads=True,
                **download_kwargs,
            )
            if not df_batch.empty:
                dataframes.append(df_batch)
            time.sleep(1)

        if dataframes:
            data = pd.concat(dataframes, axis=1)
        else:
            data = pd.DataFrame()

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
                ticker_df = data[ticker].dropna(how="all")
            else:
                ticker_df = data.dropna(how="all")

            if ticker_df.empty:
                continue

            if isinstance(ticker_df.columns, pd.MultiIndex):
                ticker_df.columns = ticker_df.columns.get_level_values(0)

            ticker_df.index = pd.to_datetime(ticker_df.index)

            opening_candles_mask = ticker_df.index.time == market_open_time
            all_openings = ticker_df[opening_candles_mask]

            if len(all_openings) < 2:
                continue

            target_dt_obj = pd.to_datetime(current_date).date()
            past_openings = all_openings[
                all_openings.index.date < target_dt_obj
            ]
            avg_opening_vol = (
                past_openings["Volume"].mean()
                if not past_openings.empty
                else all_openings["Volume"].mean()
            )

            today_mask = (ticker_df.index.date == target_dt_obj) & (
                ticker_df.index.time == market_open_time
            )
            opening_candle = ticker_df[today_mask]

            if not opening_candle.empty:
                latest_candle = opening_candle.iloc[0]

                open_p = float(latest_candle["Open"])
                close_p = float(latest_candle["Close"])
                high_p = float(latest_candle["High"])
                low_p = float(latest_candle["Low"])
                vol = int(latest_candle["Volume"])

                if open_p == 0 or avg_opening_vol == 0:
                    continue

                volume_spike_ratio = round(vol / avg_opening_vol, 2)
                candle_drop_pct = ((close_p - open_p) / open_p) * 100
                turnover_cr = (vol * close_p) / 10_000_000

                candle_range = high_p - low_p
                close_location = (
                    (close_p - low_p) / candle_range if candle_range > 0 else 1.0
                )

                subsequent_candles = ticker_df[
                    (ticker_df.index.date == target_dt_obj)
                    & (ticker_df.index.time > market_open_time)
                ]

                target_price = round(close_p * 0.99, 2)
                stop_loss = round(high_p, 2)

                outcome = "Unresolved"
                for _, row in subsequent_candles.iterrows():
                    c_high = float(row["High"])
                    c_low = float(row["Low"])

                    hit_sl = c_high >= stop_loss
                    hit_target = c_low <= target_price

                    if hit_sl and hit_target:
                        outcome = "SL Hit First (Loss)"
                        break
                    elif hit_sl:
                        outcome = "SL Hit (Loss)"
                        break
                    elif hit_target:
                        outcome = "Target Hit (Win)"
                        break

                clean_ticker = ticker.replace(".NS", "")
                row_data = {
                    "Ticker": clean_ticker,
                    "Date": current_date,
                    "15m_Open": round(open_p, 2),
                    "15m_Close_Entry": round(close_p, 2),
                    "Candle_Drop_%": round(candle_drop_pct, 2),
                    "Turnover_Cr": round(turnover_cr, 2),
                    "Vol_Spike_x": volume_spike_ratio,
                    "Outcome": outcome,
                }

                # Tier 1: General Losers
                if (
                    candle_drop_pct < -0.5
                    and turnover_cr >= 4.0
                    and close_location <= 0.25
                    and volume_spike_ratio >= 1.2
                ):
                    all_losers.append(row_data)

                # Tier 2: Shortlisted Most Falling (Also triggers automatic visual chart generation)
                if (
                    candle_drop_pct < -1.5
                    and turnover_cr >= 15.0
                    and close_location <= 0.15
                    and volume_spike_ratio >= 2.0
                ):
                    shortlisted_losers.append(row_data)
                    save_stock_chart(
                        ticker_df,
                        clean_ticker,
                        current_date,
                        stop_loss,
                        target_price,
                    )

        except Exception:
            continue

    df_all = pd.DataFrame(all_losers)
    if not df_all.empty:
        df_all = df_all.sort_values(
            by="Candle_Drop_%", ascending=True
        ).reset_index(drop=True)

    df_short = pd.DataFrame(shortlisted_losers)
    if not df_short.empty:
        df_short = df_short.sort_values(
            by="Candle_Drop_%", ascending=True
        ).reset_index(drop=True)

    return df_all, df_short


if __name__ == "__main__":
    print("Select Market Analysis Mode:")
    print("1. Current Market Data (Live/Latest)")
    print("2. Past Date Market Data & Backtest")
    choice = input("Enter your choice (1 or 2): ").strip()

    target_date = None
    match choice:
        case "1":
            pass
        case "2":
            target_date = input(
                "Enter the target date in format YYYY-MM-DD (e.g., 2026-08-15): "
            ).strip()
            try:
                datetime.strptime(target_date, "%Y-%m-%d")
            except ValueError:
                print("❌ Invalid date format provided. Please use YYYY-MM-DD.")
                sys.exit(1)
        case _:
            print("⚠️ Invalid selection. Defaulting to Current Market Data (Mode 1).")
            choice = "1"

    all_candidates, shortlisted_candidates = scan_momentum_sellers(
        choice, target_date
    )

    print("\n🔥 ALL REAL-TIME 15-MINUTE MOMENTUM LOSERS:")
    if not all_candidates.empty:
        print(all_candidates.to_string(index=False))
    else:
        print("No stocks matched the breakdown and volume criteria on this date.")

    print("\n" + "=" * 80)
    print("🎯 HIGH-CONVICTION SHORTLISTED SELLERS & BACKTEST RESULTS:")
    if not shortlisted_candidates.empty:
        print(shortlisted_candidates.to_string(index=False))
        print(
            "\n📊 Charts for shortlisted stocks have been saved automatically to the './momentum_charts/' folder."
        )
    else:
        print("No stocks matched the strict shortlisting criteria on this date.")
