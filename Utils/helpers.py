from math import ceil


def chunk(ls: list, amount: int):
    ceiling = ceil(len(ls) / amount)
    return [ls[x * amount : min(len(ls), (x + 1) * amount)] for x in range(ceiling)]


def flatten(l, condition=lambda e: True, switch=lambda e: e) -> list:
    return [switch(e) for t in l for e in t if condition(e)]


def named_flatten(l, names, condition=lambda e: True, switch=lambda e: e) -> dict:
    return dict(zip(names, [switch(e) for t in l for e in t if condition(e)]))


def pretty_dt(s: float) -> str:
    if s < 1:
        return f"{round(s * 1000)} miliseconds"
    elif s < 60:
        return f"{round(s)} second{'s' if round(s) != 1 else ''}"

    y, s = divmod(s, 3.154e7)
    mm, s = divmod(s, 2.628e6)
    d, s = divmod(s, 86400)
    h, s = divmod(s, 3600)
    m, s = divmod(s, 60)

    au = {"year": y, "month": mm, "day": d, "hour": h, "minute": m}
    ex = []
    for u in au:
        if au[u] > 0:
            return ", ".join(
                (
                    f"{round(au[i])} {i}{'s' if round(au[i]) != 1 else ''}"
                    if round(au[i]) != 0
                    else ""
                )
                for i in au
                if i not in ex
            ) + (
                f", {round(s)} second{'s' if round(s) != 1 else ''}"
                if round(s) != 0
                else ""
            )
        else:
            ex.append(u)
