import pandas as pd
from pathlib import Path
from .fetch_data import get_historical_stock_data
from .features import build_features

BASE_DIR = Path(__file__).resolve().parent.parent
csv_path = BASE_DIR / "ALL_STOCK_LIST.csv"


def run_scanner():
    df_symbols = pd.read_csv(csv_path)

    symbol_meta = (
        df_symbols.set_index("Ticker")[["Sector", "Industry"]]
        .to_dict("index")
    )
    stock_list = df_symbols["Ticker"].to_list()

    all_data = []
    full_history = []

    Path("data").mkdir(parents=True, exist_ok=True)

    for i, tic in enumerate(stock_list, 1):
        data = get_historical_stock_data(tic, interval="1d")

        if data is None or len(data) < 120:
            continue

        if tic not in symbol_meta:
            continue

        try:
            stock_df = build_features(data, tic, symbol_meta[tic])

            if stock_df is None or stock_df.empty:
                continue

            full_history.append(stock_df)
            all_data.append(stock_df.tail(1))

            print(f"{i}/{len(stock_list)} ✔ {tic}")

        except Exception as e:
            print(f"{tic} ❌ {e}")

    results = {}

    if all_data:
        latest_df = pd.concat(all_data, ignore_index=True).round(2)
        latest_df.to_parquet("data/all_data.parquet", index=False)
        results["latest"] = latest_df

    if full_history:
        history_df = pd.concat(full_history, ignore_index=True).round(2)
        history_df.to_parquet("data/full_history.parquet", index=False)
        results["history"] = history_df

    return results
