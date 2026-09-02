<!-- Generated file — do not edit; regenerated with the SDK. -->

# Calendar — operations

Accessor: `client.calendar` · Source: `finnhub_api/apis/calendar.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.calendar.earnings_calendar

- **Route**: `GET /calendar/earnings`
- **Auth**: `api_key`
- **Signature**: `def earnings_calendar(*, from_: Date | None = None, to: Date | None = None, symbol: str | None = None, international: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `from_` — query `from` · `to` — query · `symbol` — query · `international` — query
- **Returns (parsed)**: `EarningsCalendar`
- **Returns (raw)**: `ApiResult[EarningsCalendar, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EarningsCalendar` | `finnhub_api/models/earnings_calendar.py` |

### client.calendar.economic_calendar

- **Route**: `GET /calendar/economic`
- **Auth**: `api_key`
- **Signature**: `def economic_calendar(*, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `from_` — query `from` · `to` — query
- **Returns (parsed)**: `EconomicCalendar`
- **Returns (raw)**: `ApiResult[EconomicCalendar, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EconomicCalendar` | `finnhub_api/models/economic_calendar.py` |

### client.calendar.ipo_calendar

- **Route**: `GET /calendar/ipo`
- **Auth**: `api_key`
- **Signature**: `def ipo_calendar(from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `from_`, `to`
- **Params**: `from_` — query `from` · `to` — query
- **Returns (parsed)**: `Ipocalendar`
- **Returns (raw)**: `ApiResult[Ipocalendar, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Ipocalendar` | `finnhub_api/models/ipocalendar.py` |

