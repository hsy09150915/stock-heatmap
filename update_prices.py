# -*- coding: utf-8 -*-
"""
codes.json 에 적힌 종목들의 '가장 최근 마감 종가'를 prices.json 으로 저장한다.
GitHub Actions 가 평일 장 마감 후 자동으로 실행한다. (PC에서 직접 돌려도 된다: python update_prices.py)
- 종목 하나가 실패해도 나머지는 계속하고, 실패한 종목은 이전 값을 그대로 둔다.
- 전부 실패하면 오류(종료코드 1)로 끝나서 GitHub 에 '실패'로 표시된다.
"""
import sys, os, json
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "prices.json")
KST = timezone(timedelta(hours=9))


def load_json(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def last_close(fdr, code, now):
    start = (now - timedelta(days=20)).strftime("%Y-%m-%d")
    df = fdr.DataReader(code, start).dropna(subset=["Close"])
    if df.empty:
        raise ValueError("데이터 없음")
    last_day = df.index[-1].strftime("%Y-%m-%d")
    market_open = now.weekday() < 5 and (now.hour, now.minute) < (15, 40)
    if last_day == now.strftime("%Y-%m-%d") and market_open and len(df) > 1:
        df = df.iloc[:-1]  # 장중이면 오늘 값은 종가가 아니므로 제외
    return int(round(float(df.iloc[-1]["Close"]))), df.index[-1].strftime("%Y-%m-%d")


def main():
    codes = load_json(os.path.join(HERE, "codes.json"), [])
    if isinstance(codes, dict):
        codes = list(codes.keys())
    codes = [str(c).strip() for c in codes if str(c).strip()]
    if not codes:
        print("codes.json 이 비어 있어요.")
        return 1
    import FinanceDataReader as fdr

    result = load_json(OUT, {})
    now = datetime.now(KST)
    ok, fail = 0, []
    for c in codes:
        try:
            close, day = last_close(fdr, c, now)
            result[c] = {"name": result.get(c, {}).get("name", ""), "prev_close": close, "date": day}
            ok += 1
            print(f"{c}: {close:,}원 ({day})")
        except Exception as e:
            fail.append(c)
            print(f"{c}: 실패 ({e})")
    result["_updated"] = now.strftime("%Y-%m-%d %H:%M KST")
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=1)
    print(f"성공 {ok}, 실패 {len(fail)} {fail if fail else ''}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
