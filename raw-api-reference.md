# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [FinnhubApiClient](finnhub_api/client.py)

## Bond

> Source: [Bond](finnhub_api/apis/bond.py)

<details>
<summary><code>def bond_price(isin: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BondCandles, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Get bond's price data. The following datasets are supported:</p><table class="table table-hover">
  <thead>
    <tr>
      <th>Exchange</th>
      <th>Segment</th>
      <th>Delay</th>
    </tr>
  </thead>
  <tbody>
  <tr>
      <td class="text-blue">US Government Bonds</td>
      <td>Government Bonds</td>
      <td>End-of-day</td>
    </tr>
    <tr>
      <td class="text-blue">FINRA Trace</td>
      <td>BTDS: US Corporate Bonds</td>
      <td>Delayed 4h</td>
    </tr>
    <tr>
      <td class="text-blue">FINRA Trace</td>
      <td>144A Bonds</td>
      <td>Delayed 4h</td>
    </tr>
    <tr>
  	  <td class="text-blue">International Bonds</td>
      <td>International Bonds</td>
      <td>End-of-day</td>
    </tr>
</tbody>
</table>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bond.with_raw_response.bond_price(isin, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BondCandles
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bond.with_raw_response.bond_price(isin, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BondCandles
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>isin</code> | <code>str</code> | ISIN. |
| <code>from_</code> | <code>int</code> | UNIX timestamp. Interval initial value. |
| <code>to</code> | <code>int</code> | UNIX timestamp. Interval end value. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[BondCandles](finnhub_api/models/bond_candles.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BondCandles](finnhub_api/models/bond_candles.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bond_profile(*, isin: str | None = None, cusip: str | None = None, figi: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BondProfile, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get general information of a bond. You can query by FIGI, ISIN or CUSIP. A list of supported bonds can be found <a href="/api/v1/bond/list?type=csv&token=" target="_blank">here</a>.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bond.with_raw_response.bond_profile()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BondProfile
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bond.with_raw_response.bond_profile()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BondProfile
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>isin</code> | <code>str \| None</code> | ISIN<br>**Default**: <code>None</code> |
| <code>cusip</code> | <code>str \| None</code> | CUSIP<br>**Default**: <code>None</code> |
| <code>figi</code> | <code>str \| None</code> | FIGI<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[BondProfile](finnhub_api/models/bond_profile.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BondProfile](finnhub_api/models/bond_profile.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bond_tick(isin: str, date: Date, limit: int, skip: int, exchange: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BondTickData, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Get trade-level data for bonds. The following datasets are supported:</p><table class="table table-hover">
  <thead>
    <tr>
      <th>Exchange</th>
      <th>Segment</th>
      <th>Delay</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="text-blue">FINRA Trace</th>
      <td>BTDS: US Corporate Bonds</td>
      <td>Delayed 4h</td>
    </tr>
    <tr>
      <td class="text-blue">FINRA Trace</th>
      <td>144A Bonds</td>
      <td>Delayed 4h</td>
    </tr>
  </tbody>
</table>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bond.with_raw_response.bond_tick(isin, date, limit, skip, exchange)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BondTickData
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bond.with_raw_response.bond_tick(isin, date, limit, skip, exchange)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BondTickData
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>isin</code> | <code>str</code> | ISIN. |
| <code>date</code> | <code>Date</code> | Date: 2020-04-02. |
| <code>limit</code> | <code>int</code> | Limit number of ticks returned. Maximum value: <code>25000</code> |
| <code>skip</code> | <code>int</code> | Number of ticks to skip. Use this parameter to loop through the entire data. |
| <code>exchange</code> | <code>str</code> | Currently support the following values: <code>trace</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[BondTickData](finnhub_api/models/bond_tick_data.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BondTickData](finnhub_api/models/bond_tick_data.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bond_yield_curve(code: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BondYieldCurve, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get yield curve data for Treasury bonds.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bond.with_raw_response.bond_yield_curve(code)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BondYieldCurve
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bond.with_raw_response.bond_yield_curve(code)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BondYieldCurve
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>code</code> | <code>str</code> | Bond's code. You can find the list of supported code <a href="https://docs.google.com/spreadsheets/d/1iA-lM0Kht7lsQZ7Uu_s6r2i1BbQNUNO9eGkO5-zglHg/edit?usp=sharing" target="_blank" rel="noopener">here</a>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[BondYieldCurve](finnhub_api/models/bond_yield_curve.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BondYieldCurve](finnhub_api/models/bond_yield_curve.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Calendar

> Source: [Calendar](finnhub_api/apis/calendar.py)

<details>
<summary><code>def earnings_calendar(*, from_: Date | None = None, to: Date | None = None, symbol: str | None = None, international: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EarningsCalendar, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get historical and coming earnings release. EPS and Revenue in this endpoint are non-GAAP, which means they are adjusted to exclude some one-time or unusual items. This is the same data investors usually react to and talked about on the media. Estimates are sourced from both sell-side and buy-side analysts.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.calendar.with_raw_response.earnings_calendar()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EarningsCalendar
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.calendar.with_raw_response.earnings_calendar()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EarningsCalendar
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>from_</code> | <code>Date \| None</code> | From date: 2020-03-15.<br>**Default**: <code>None</code> |
| <code>to</code> | <code>Date \| None</code> | To date: 2020-03-16.<br>**Default**: <code>None</code> |
| <code>symbol</code> | <code>str \| None</code> | Filter by symbol: AAPL.<br>**Default**: <code>None</code> |
| <code>international</code> | <code>bool \| None</code> | Set to <code>true</code> to include international markets. Default value is <code>false</code><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[EarningsCalendar](finnhub_api/models/earnings_calendar.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[EarningsCalendar](finnhub_api/models/earnings_calendar.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def economic_calendar(*, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EconomicCalendar, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Get recent and upcoming economic releases.</p><p>Historical events and surprises are available for Enterprise clients.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.calendar.with_raw_response.economic_calendar()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EconomicCalendar
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.calendar.with_raw_response.economic_calendar()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EconomicCalendar
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>from_</code> | <code>Date \| None</code> | From date <code>YYYY-MM-DD</code>.<br>**Default**: <code>None</code> |
| <code>to</code> | <code>Date \| None</code> | To date <code>YYYY-MM-DD</code>.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[EconomicCalendar](finnhub_api/models/economic_calendar.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[EconomicCalendar](finnhub_api/models/economic_calendar.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def ipo_calendar(from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Ipocalendar, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get recent and upcoming IPO.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.calendar.with_raw_response.ipo_calendar(from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Ipocalendar
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.calendar.with_raw_response.ipo_calendar(from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Ipocalendar
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>from_</code> | <code>Date</code> | From date: 2020-03-15. |
| <code>to</code> | <code>Date</code> | To date: 2020-03-16. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[Ipocalendar](finnhub_api/models/ipocalendar.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Ipocalendar](finnhub_api/models/ipocalendar.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## CorporateActions

> Source: [CorporateActions](finnhub_api/apis/corporate_actions.py)

<details>
<summary><code>def isin_change(from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IsinChange, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of ISIN changes for EU-listed securities. Limit to 2000 events at a time.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.corporate_actions.with_raw_response.isin_change(from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IsinChange
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.corporate_actions.with_raw_response.isin_change(from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IsinChange
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>from_</code> | <code>str</code> | From date <code>YYYY-MM-DD</code>. |
| <code>to</code> | <code>str</code> | To date <code>YYYY-MM-DD</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[IsinChange](finnhub_api/models/isin_change.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IsinChange](finnhub_api/models/isin_change.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def symbol_change(from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SymbolChange, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of symbol changes for US-listed, EU-listed, NSE and ASX securities. Limit to 2000 events at a time.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.corporate_actions.with_raw_response.symbol_change(from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SymbolChange
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.corporate_actions.with_raw_response.symbol_change(from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SymbolChange
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>from_</code> | <code>str</code> | From date <code>YYYY-MM-DD</code>. |
| <code>to</code> | <code>str</code> | To date <code>YYYY-MM-DD</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[SymbolChange](finnhub_api/models/symbol_change.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SymbolChange](finnhub_api/models/symbol_change.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Crypto

> Source: [Crypto](finnhub_api/apis/crypto.py)

<details>
<summary><code>def crypto_candles(symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CryptoCandles, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get candlestick data for crypto symbols.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.crypto.with_raw_response.crypto_candles(symbol, resolution, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CryptoCandles
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.crypto.with_raw_response.crypto_candles(symbol, resolution, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CryptoCandles
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Use symbol returned in <code>/crypto/symbol</code> endpoint for this field. |
| <code>resolution</code> | <code>str</code> | Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not be available depending on the exchange. |
| <code>from_</code> | <code>int</code> | UNIX timestamp. Interval initial value. |
| <code>to</code> | <code>int</code> | UNIX timestamp. Interval end value. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[CryptoCandles](finnhub_api/models/crypto_candles.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CryptoCandles](finnhub_api/models/crypto_candles.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def crypto_exchanges(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[str], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List supported crypto exchanges

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.crypto.with_raw_response.crypto_exchanges()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[str]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.crypto.with_raw_response.crypto_exchanges()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[str]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;list&#91;str&#93;, [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;str&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def crypto_profile(symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CryptoProfile, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get crypto's profile.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.crypto.with_raw_response.crypto_profile(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CryptoProfile
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.crypto.with_raw_response.crypto_profile(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CryptoProfile
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Crypto symbol such as BTC or ETH. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[CryptoProfile](finnhub_api/models/crypto_profile.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CryptoProfile](finnhub_api/models/crypto_profile.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def crypto_symbols(exchange: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[CryptoSymbol], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List supported crypto symbols by exchange

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.crypto.with_raw_response.crypto_symbols(exchange)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[CryptoSymbol]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.crypto.with_raw_response.crypto_symbols(exchange)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[CryptoSymbol]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>exchange</code> | <code>str</code> | Exchange you want to get the list of symbols from. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;list&#91;[CryptoSymbol](finnhub_api/models/crypto_symbol.py)&#93;, [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[CryptoSymbol](finnhub_api/models/crypto_symbol.py)&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Economic

> Source: [Economic](finnhub_api/apis/economic.py)

<details>
<summary><code>def economic_code(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[EconomicCode], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List codes of supported economic data.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.economic.with_raw_response.economic_code()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[EconomicCode]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.economic.with_raw_response.economic_code()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[EconomicCode]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;list&#91;[EconomicCode](finnhub_api/models/economic_code.py)&#93;, [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[EconomicCode](finnhub_api/models/economic_code.py)&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def economic_data(code: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EconomicData, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get economic data.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.economic.with_raw_response.economic_data(code)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EconomicData
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.economic.with_raw_response.economic_data(code)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EconomicData
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>code</code> | <code>str</code> | Economic code. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[EconomicData](finnhub_api/models/economic_data.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[EconomicData](finnhub_api/models/economic_data.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Etf

> Source: [Etf](finnhub_api/apis/etf.py)

<details>
<summary><code>def etfs_allocation(*, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EtfsAllocation, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get ETF equity allocation based on the characteristics of the holdings.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.etf.with_raw_response.etfs_allocation()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EtfsAllocation
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.etf.with_raw_response.etfs_allocation()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EtfsAllocation
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | ETF symbol.<br>**Default**: <code>None</code> |
| <code>isin</code> | <code>str \| None</code> | ETF isin.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[EtfsAllocation](finnhub_api/models/etfs_allocation.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[EtfsAllocation](finnhub_api/models/etfs_allocation.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def etfs_country_exposure(*, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EtfsCountryExposure, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get ETF country exposure data.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.etf.with_raw_response.etfs_country_exposure()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EtfsCountryExposure
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.etf.with_raw_response.etfs_country_exposure()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EtfsCountryExposure
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | ETF symbol.<br>**Default**: <code>None</code> |
| <code>isin</code> | <code>str \| None</code> | ETF isin.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[EtfsCountryExposure](finnhub_api/models/etfs_country_exposure.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[EtfsCountryExposure](finnhub_api/models/etfs_country_exposure.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def etfs_holdings(*, symbol: str | None = None, isin: str | None = None, skip: int | None = None, date: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EtfsHoldings, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get full ETF holdings/constituents. This endpoint has global coverage. Widget only shows top 10 holdings. A list of supported ETFs can be found <a href="/api/v1/etf/list?token=" target="_blank">here</a>.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.etf.with_raw_response.etfs_holdings()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EtfsHoldings
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.etf.with_raw_response.etfs_holdings()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EtfsHoldings
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | ETF symbol.<br>**Default**: <code>None</code> |
| <code>isin</code> | <code>str \| None</code> | ETF isin.<br>**Default**: <code>None</code> |
| <code>skip</code> | <code>int \| None</code> | Skip the first n results. You can use this parameter to query historical constituents data. The latest result is returned if skip=0 or not set.<br>**Default**: <code>None</code> |
| <code>date</code> | <code>str \| None</code> | Query holdings by date. You can use either this param or <code>skip</code> param, not both.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[EtfsHoldings](finnhub_api/models/etfs_holdings.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[EtfsHoldings](finnhub_api/models/etfs_holdings.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def etfs_profile(*, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EtfsProfile, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get ETF profile information. This endpoint has global coverage. A list of supported ETFs can be found <a href="/api/v1/etf/list?type=csv&token=" target="_blank">here</a>.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.etf.with_raw_response.etfs_profile()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EtfsProfile
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.etf.with_raw_response.etfs_profile()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EtfsProfile
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | ETF symbol.<br>**Default**: <code>None</code> |
| <code>isin</code> | <code>str \| None</code> | ETF isin.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[EtfsProfile](finnhub_api/models/etfs_profile.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[EtfsProfile](finnhub_api/models/etfs_profile.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def etfs_sector_exposure(*, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EtfsSectorExposure, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get ETF sector exposure data.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.etf.with_raw_response.etfs_sector_exposure()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EtfsSectorExposure
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.etf.with_raw_response.etfs_sector_exposure()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EtfsSectorExposure
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | ETF symbol.<br>**Default**: <code>None</code> |
| <code>isin</code> | <code>str \| None</code> | ETF isin.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[EtfsSectorExposure](finnhub_api/models/etfs_sector_exposure.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[EtfsSectorExposure](finnhub_api/models/etfs_sector_exposure.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Forex

> Source: [Forex](finnhub_api/apis/forex.py)

<details>
<summary><code>def forex_candles(symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ForexCandles, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get candlestick data for forex symbols.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.forex.with_raw_response.forex_candles(symbol, resolution, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ForexCandles
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.forex.with_raw_response.forex_candles(symbol, resolution, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ForexCandles
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Use symbol returned in <code>/forex/symbol</code> endpoint for this field. |
| <code>resolution</code> | <code>str</code> | Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not be available depending on the exchange. |
| <code>from_</code> | <code>int</code> | UNIX timestamp. Interval initial value. |
| <code>to</code> | <code>int</code> | UNIX timestamp. Interval end value. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[ForexCandles](finnhub_api/models/forex_candles.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ForexCandles](finnhub_api/models/forex_candles.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def forex_exchanges(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[str], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List supported forex exchanges

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.forex.with_raw_response.forex_exchanges()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[str]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.forex.with_raw_response.forex_exchanges()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[str]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;list&#91;str&#93;, [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;str&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def forex_rates(*, base: str | None = None, date: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Forexrates, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get rates for all forex pairs. Ideal for currency conversion

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.forex.with_raw_response.forex_rates()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Forexrates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.forex.with_raw_response.forex_rates()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Forexrates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>base</code> | <code>str \| None</code> | Base currency. Default to EUR.<br>**Default**: <code>None</code> |
| <code>date</code> | <code>str \| None</code> | Date. Leave blank to get the latest data.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[Forexrates](finnhub_api/models/forexrates.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Forexrates](finnhub_api/models/forexrates.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def forex_symbols(exchange: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[ForexSymbol], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List supported forex symbols.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.forex.with_raw_response.forex_symbols(exchange)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[ForexSymbol]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.forex.with_raw_response.forex_symbols(exchange)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[ForexSymbol]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>exchange</code> | <code>str</code> | Exchange you want to get the list of symbols from. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;list&#91;[ForexSymbol](finnhub_api/models/forex_symbol.py)&#93;, [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[ForexSymbol](finnhub_api/models/forex_symbol.py)&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## GlobalFilings

> Source: [GlobalFilings](finnhub_api/apis/global_filings.py)

<details>
<summary><code>def global_filings_download(document_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Download filings using document ids.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.global_filings.with_raw_response.global_filings_download(document_id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.global_filings.with_raw_response.global_filings_download(document_id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>document_id</code> | <code>str</code> | Document's id. Note that this is different from filingId as 1 filing can contain multiple documents. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;None, [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def global_filings_search(*, search: SearchBody | SearchBodyDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Search for best-matched filings across global companies' filings, transcripts and press releases. You can filter by anything from symbol, ISIN to form type, and document sources.</p><p>This endpoint will return a list of documents that match your search criteria. If you would like to get the excerpts as well, please set <code>highlighted</code> to <code>true</code>. Once you have the list of documents, you can get a list of excerpts and positions to highlight the document using the <code>/search-in-filing</code> endpoint</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.global_filings.with_raw_response.global_filings_search()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.global_filings.with_raw_response.global_filings_search()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>search</code> | <code>[SearchBody](finnhub_api/models/search_body.py) \| [SearchBodyDict](finnhub_api/models/search_body.py) \| None</code> | Search body<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[SearchResponse](finnhub_api/models/search_response.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchResponse](finnhub_api/models/search_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def global_filings_search_filter(field: str, *, source: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchFilter, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Get available values for each filter in search body.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.global_filings.with_raw_response.global_filings_search_filter(field)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchFilter
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.global_filings.with_raw_response.global_filings_search_filter(field)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchFilter
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>field</code> | <code>str</code> | Field to get available filters. Available filters are "countries", "exchanges", "exhibits", "forms", "gics", "naics", "caps", "acts", and "sort". |
| <code>source</code> | <code>str \| None</code> | Get available forms for each source.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[SearchFilter](finnhub_api/models/search_filter.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchFilter](finnhub_api/models/search_filter.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_in_filing(*, search: InFilingSearchBody | InFilingSearchBodyDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[InFilingResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Get a list of excerpts and highlight positions within a document using your query.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.global_filings.with_raw_response.search_in_filing()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InFilingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.global_filings.with_raw_response.search_in_filing()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InFilingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>search</code> | <code>[InFilingSearchBody](finnhub_api/models/in_filing_search_body.py) \| [InFilingSearchBodyDict](finnhub_api/models/in_filing_search_body.py) \| None</code> | Search body<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[InFilingResponse](finnhub_api/models/in_filing_response.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[InFilingResponse](finnhub_api/models/in_filing_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Index

> Source: [Index](finnhub_api/apis/index.py)

<details>
<summary><code>def indices_constituents(symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IndicesConstituents, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of index's constituents. A list of supported indices for this endpoint can be found <a href="/api/v1/index/list?token=" target="_blank">here</a>.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.index.with_raw_response.indices_constituents(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IndicesConstituents
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.index.with_raw_response.indices_constituents(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IndicesConstituents
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | symbol |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[IndicesConstituents](finnhub_api/models/indices_constituents.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IndicesConstituents](finnhub_api/models/indices_constituents.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def indices_historical_constituents(symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IndicesHistoricalConstituents, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get full history of index's constituents including symbols and dates of joining and leaving the Index. A list of supported indices for this endpoint can be found <a href="/api/v1/index/historical-list?token=" target="_blank">here</a>.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.index.with_raw_response.indices_historical_constituents(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IndicesHistoricalConstituents
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.index.with_raw_response.indices_historical_constituents(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IndicesHistoricalConstituents
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | symbol |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[IndicesHistoricalConstituents](finnhub_api/models/indices_historical_constituents.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IndicesHistoricalConstituents](finnhub_api/models/indices_historical_constituents.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Institutional

> Source: [Institutional](finnhub_api/apis/institutional.py)

<details>
<summary><code>def institutional_ownership(symbol: str, cusip: str, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[InstitutionalOwnership, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list institutional investors' positions for a particular stock overtime. Data from 13-F filings. Limit to 1 year of data at a time.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.institutional.with_raw_response.institutional_ownership(symbol, cusip, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InstitutionalOwnership
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.institutional.with_raw_response.institutional_ownership(symbol, cusip, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InstitutionalOwnership
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Filter by symbol. |
| <code>cusip</code> | <code>str</code> | Filter by CUSIP. |
| <code>from_</code> | <code>str</code> | From date <code>YYYY-MM-DD</code>. |
| <code>to</code> | <code>str</code> | To date <code>YYYY-MM-DD</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[InstitutionalOwnership](finnhub_api/models/institutional_ownership.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[InstitutionalOwnership](finnhub_api/models/institutional_ownership.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def institutional_portfolio(cik: str, from_: str, to: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[InstitutionalPortfolio, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the holdings/portfolio data of institutional investors from 13-F filings. Limit to 1 year of data at a time. You can get a list of supported CIK <a href="/api/v1/institutional/list?token=" target="_blank">here</a>.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.institutional.with_raw_response.institutional_portfolio(cik, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InstitutionalPortfolio
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.institutional.with_raw_response.institutional_portfolio(cik, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InstitutionalPortfolio
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>cik</code> | <code>str</code> | Fund's CIK. |
| <code>from_</code> | <code>str</code> | From date <code>YYYY-MM-DD</code>. |
| <code>to</code> | <code>str</code> | To date <code>YYYY-MM-DD</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[InstitutionalPortfolio](finnhub_api/models/institutional_portfolio.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[InstitutionalPortfolio](finnhub_api/models/institutional_portfolio.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def institutional_profile(*, cik: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[InstitutionalProfile, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of well-known institutional investors. Currently support 60+ profiles.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.institutional.with_raw_response.institutional_profile()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InstitutionalProfile
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.institutional.with_raw_response.institutional_profile()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InstitutionalProfile
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>cik</code> | <code>str \| None</code> | Filter by CIK. Leave blank to get the full list.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[InstitutionalProfile](finnhub_api/models/institutional_profile.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[InstitutionalProfile](finnhub_api/models/institutional_profile.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Misc

> Source: [Misc](finnhub_api/apis/misc.py)

<details>
<summary><code>def ai_chat(*, search: AichatBody | AichatBodyDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AichatResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Chat with our AI copilot trained on the extensive Finnhub's global data. You can ask it any finance-related questions just like with other LLM models and receive results in texts and widgets.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.misc.with_raw_response.ai_chat()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AichatResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.misc.with_raw_response.ai_chat()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AichatResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>search</code> | <code>[AichatBody](finnhub_api/models/aichat_body.py) \| [AichatBodyDict](finnhub_api/models/aichat_body.py) \| None</code> | Search body<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[AichatResponse](finnhub_api/models/aichat_response.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AichatResponse](finnhub_api/models/aichat_response.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def airline_price_index(airline: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AirlinePriceIndexData, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>The Flight Ticket Price Index API provides comprehensive data on airline ticket prices, including the average daily ticket price and its percentage change (price index). This data, collected weekly and projected two weeks ahead, aggregates daily prices and indexes from the 50 busiest and largest airports across the USA. The dataset includes detailed information on airlines, dates, and average ticket prices, offering valuable insights for market analysis and pricing strategies.</p><p>The price index is calculated as percentage change of average daily ticket price from the previous weekly reading. Raw ticket prices data is available for Enterprise users. <a href="mailto:support@finnhub.io">Contact us</a> to inquire about the raw price data.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.misc.with_raw_response.airline_price_index(airline, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AirlinePriceIndexData
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.misc.with_raw_response.airline_price_index(airline, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AirlinePriceIndexData
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>airline</code> | <code>str</code> | Filter data by airline. Accepted values: <code>united</code>,<code>delta</code>,<code>american_airlines</code>,<code>southwest</code>,<code>southern_airways_express</code>,<code>alaska_airlines</code>,<code>frontier_airlines</code>,<code>jetblue_airways</code>,<code>spirit_airlines</code>,<code>sun_country_airlines</code>,<code>breeze_airways</code>,<code>hawaiian_airlines</code> |
| <code>from_</code> | <code>Date</code> | From date <code>YYYY-MM-DD</code>. |
| <code>to</code> | <code>Date</code> | To date <code>YYYY-MM-DD</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[AirlinePriceIndexData](finnhub_api/models/airline_price_index_data.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AirlinePriceIndexData](finnhub_api/models/airline_price_index_data.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bank_branch(symbol: Any, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BankBranchRes, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve list of US bank branches information for a given symbol.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.misc.with_raw_response.bank_branch(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankBranchRes
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.misc.with_raw_response.bank_branch(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BankBranchRes
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>Any</code> | Symbol. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[BankBranchRes](finnhub_api/models/bank_branch_res.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BankBranchRes](finnhub_api/models/bank_branch_res.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def country(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[CountryMetadata], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List all countries and metadata.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.misc.with_raw_response.country()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[CountryMetadata]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.misc.with_raw_response.country()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[CountryMetadata]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;list&#91;[CountryMetadata](finnhub_api/models/country_metadata.py)&#93;, [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[CountryMetadata](finnhub_api/models/country_metadata.py)&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def covid_19(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[CovidInfo], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get real-time updates on the number of COVID-19 (Corona virus) cases in the US with a state-by-state breakdown. Data is sourced from CDC and reputable sources. You can also access this API <a href="https://rapidapi.com/Finnhub/api/finnhub-real-time-covid-19" target="_blank" rel="nofollow">here</a>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.misc.with_raw_response.covid_19()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[CovidInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.misc.with_raw_response.covid_19()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[CovidInfo]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;list&#91;[CovidInfo](finnhub_api/models/covid_info.py)&#93;, [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[CovidInfo](finnhub_api/models/covid_info.py)&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fda_committee_meeting_calendar(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[FdacomitteeMeeting], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

FDA's advisory committees are established to provide functions which support the agency's mission of protecting and promoting the public health, while meeting the requirements set forth in the Federal Advisory Committee Act. Committees are either mandated by statute or established at the discretion of the Department of Health and Human Services. Each committee is subject to renewal at two-year intervals unless the committee charter states otherwise.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.misc.with_raw_response.fda_committee_meeting_calendar()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[FdacomitteeMeeting]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.misc.with_raw_response.fda_committee_meeting_calendar()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[FdacomitteeMeeting]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;list&#91;[FdacomitteeMeeting](finnhub_api/models/fdacomittee_meeting.py)&#93;, [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[FdacomitteeMeeting](finnhub_api/models/fdacomittee_meeting.py)&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def quote(symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Quote, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Get real-time quote data for US stocks. Constant polling is not recommended. Use websocket if you need real-time updates.</p><p>Real-time stock prices for international markets are supported for Enterprise clients via our partner's feed. <a href="mailto:support@finnhub.io">Contact Us</a> to learn more.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.misc.with_raw_response.quote(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Quote
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.misc.with_raw_response.quote(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Quote
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[Quote](finnhub_api/models/quote.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Quote](finnhub_api/models/quote.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sector_metric(region: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SectorMetric, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get ratios for different sectors and regions/indices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.misc.with_raw_response.sector_metric(region)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SectorMetric
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.misc.with_raw_response.sector_metric(region)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SectorMetric
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>region</code> | <code>str</code> | Region. A list of supported values for this field can be found <a href="https://docs.google.com/spreadsheets/d/1afedyv7yWJ-z7pMjaAZK-f6ENY3mI3EBCk95QffpoHw/edit?usp=sharing" target="_blank">here</a>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[SectorMetric](finnhub_api/models/sector_metric.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SectorMetric](finnhub_api/models/sector_metric.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def symbol_search(q: str, *, exchange: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SymbolLookup, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Search for best-matching symbols based on your query. You can input anything from symbol, security's name to ISIN and Cusip.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.misc.with_raw_response.symbol_search(q)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SymbolLookup
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.misc.with_raw_response.symbol_search(q)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SymbolLookup
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>q</code> | <code>str</code> | Query text can be symbol, name, isin, or cusip. |
| <code>exchange</code> | <code>str \| None</code> | Exchange limit.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[SymbolLookup](finnhub_api/models/symbol_lookup.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SymbolLookup](finnhub_api/models/symbol_lookup.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def technical_indicator(symbol: str, resolution: str, from_: int, to: int, indicator: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Return technical indicator with price data. List of supported indicators can be found <a href="https://docs.google.com/spreadsheets/d/1ylUvKHVYN2E87WdwIza8ROaCpd48ggEl1k5i5SgA29k/edit?usp=sharing" target="_blank">here</a>.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.misc.with_raw_response.technical_indicator(symbol, resolution, from_, to, indicator)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.misc.with_raw_response.technical_indicator(symbol, resolution, from_, to, indicator)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | symbol |
| <code>resolution</code> | <code>str</code> | Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not be available depending on the exchange. |
| <code>from_</code> | <code>int</code> | UNIX timestamp. Interval initial value. |
| <code>to</code> | <code>int</code> | UNIX timestamp. Interval end value. |
| <code>indicator</code> | <code>str</code> | Indicator name. Full list can be found <a href="https://docs.google.com/spreadsheets/d/1ylUvKHVYN2E87WdwIza8ROaCpd48ggEl1k5i5SgA29k/edit?usp=sharing" target="_blank">here</a>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;Any, [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## MutualFund

> Source: [MutualFund](finnhub_api/apis/mutual_fund.py)

<details>
<summary><code>def mutual_fund_country_exposure(*, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[MutualFundCountryExposure, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Mutual Funds country exposure data.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.mutual_fund.with_raw_response.mutual_fund_country_exposure()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MutualFundCountryExposure
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.mutual_fund.with_raw_response.mutual_fund_country_exposure()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MutualFundCountryExposure
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | Symbol.<br>**Default**: <code>None</code> |
| <code>isin</code> | <code>str \| None</code> | Fund's isin.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[MutualFundCountryExposure](finnhub_api/models/mutual_fund_country_exposure.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[MutualFundCountryExposure](finnhub_api/models/mutual_fund_country_exposure.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def mutual_fund_eet(isin: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[MutualFundEet, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get EET data for EU funds. For PAIs data, please see the EET PAI endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.mutual_fund.with_raw_response.mutual_fund_eet(isin)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MutualFundEet
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.mutual_fund.with_raw_response.mutual_fund_eet(isin)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MutualFundEet
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>isin</code> | <code>str</code> | ISIN. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[MutualFundEet](finnhub_api/models/mutual_fund_eet.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[MutualFundEet](finnhub_api/models/mutual_fund_eet.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def mutual_fund_eet_pai(isin: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[MutualFundEetPai, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get EET PAI data for EU funds.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.mutual_fund.with_raw_response.mutual_fund_eet_pai(isin)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MutualFundEetPai
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.mutual_fund.with_raw_response.mutual_fund_eet_pai(isin)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MutualFundEetPai
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>isin</code> | <code>str</code> | ISIN. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[MutualFundEetPai](finnhub_api/models/mutual_fund_eet_pai.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[MutualFundEetPai](finnhub_api/models/mutual_fund_eet_pai.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def mutual_fund_holdings(*, symbol: str | None = None, isin: str | None = None, skip: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[MutualFundHoldings, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get full Mutual Funds holdings/constituents. This endpoint covers both US and global mutual funds. For international funds, you must query the data using ISIN. A list of supported funds can be found <a href="/api/v1/mutual-fund/list?token=" target="_blank">here</a>.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.mutual_fund.with_raw_response.mutual_fund_holdings()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MutualFundHoldings
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.mutual_fund.with_raw_response.mutual_fund_holdings()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MutualFundHoldings
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | Fund's symbol.<br>**Default**: <code>None</code> |
| <code>isin</code> | <code>str \| None</code> | Fund's isin.<br>**Default**: <code>None</code> |
| <code>skip</code> | <code>int \| None</code> | Skip the first n results. You can use this parameter to query historical constituents data. The latest result is returned if skip=0 or not set.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[MutualFundHoldings](finnhub_api/models/mutual_fund_holdings.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[MutualFundHoldings](finnhub_api/models/mutual_fund_holdings.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def mutual_fund_profile(*, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[MutualFundProfile, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get mutual funds profile information. This endpoint covers both US and global mutual funds. For international funds, you must query the data using ISIN. A list of supported funds can be found <a href="/api/v1/mutual-fund/list?type=csv&token=" target="_blank">here</a>.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.mutual_fund.with_raw_response.mutual_fund_profile()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MutualFundProfile
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.mutual_fund.with_raw_response.mutual_fund_profile()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MutualFundProfile
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | Fund's symbol.<br>**Default**: <code>None</code> |
| <code>isin</code> | <code>str \| None</code> | Fund's isin.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[MutualFundProfile](finnhub_api/models/mutual_fund_profile.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[MutualFundProfile](finnhub_api/models/mutual_fund_profile.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def mutual_fund_sector_exposure(*, symbol: str | None = None, isin: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[MutualFundSectorExposure, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Mutual Funds sector exposure data.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.mutual_fund.with_raw_response.mutual_fund_sector_exposure()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MutualFundSectorExposure
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.mutual_fund.with_raw_response.mutual_fund_sector_exposure()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MutualFundSectorExposure
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | Mutual Fund symbol.<br>**Default**: <code>None</code> |
| <code>isin</code> | <code>str \| None</code> | Fund's isin.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[MutualFundSectorExposure](finnhub_api/models/mutual_fund_sector_exposure.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[MutualFundSectorExposure](finnhub_api/models/mutual_fund_sector_exposure.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## News

> Source: [News](finnhub_api/apis/news.py)

<details>
<summary><code>def company_news(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[CompanyNews], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List latest company news by symbol. This endpoint is only available for North American companies.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.news.with_raw_response.company_news(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[CompanyNews]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.news.with_raw_response.company_news(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[CompanyNews]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Company symbol. |
| <code>from_</code> | <code>Date</code> | From date <code>YYYY-MM-DD</code>. |
| <code>to</code> | <code>Date</code> | To date <code>YYYY-MM-DD</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;list&#91;[CompanyNews](finnhub_api/models/company_news.py)&#93;, [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[CompanyNews](finnhub_api/models/company_news.py)&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def market_news(category: str, *, min_id: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[MarketNews], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get latest market news.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.news.with_raw_response.market_news(category)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[MarketNews]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.news.with_raw_response.market_news(category)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[MarketNews]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>category</code> | <code>str</code> | This parameter can be 1 of the following values <code>general, forex, crypto, merger</code>. |
| <code>min_id</code> | <code>int \| None</code> | Use this field to get only news after this ID. Default to 0<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;list&#91;[MarketNews](finnhub_api/models/market_news.py)&#93;, [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[MarketNews](finnhub_api/models/market_news.py)&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def news_sentiment(symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[NewsSentiment, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get company's news sentiment and statistics. This endpoint is only available for US companies.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.news.with_raw_response.news_sentiment(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type NewsSentiment
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.news.with_raw_response.news_sentiment(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type NewsSentiment
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Company symbol. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[NewsSentiment](finnhub_api/models/news_sentiment.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[NewsSentiment](finnhub_api/models/news_sentiment.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def press_releases(symbol: str, *, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PressRelease, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Get latest major press releases of a company. This data can be used to highlight the most significant events comprised of mostly press releases sourced from the exchanges, BusinessWire, AccessWire, GlobeNewswire, Newsfile, and PRNewswire.</p><p>Full-text press releases data is available for Enterprise clients. <a href="mailto:support@finnhub.io">Contact Us</a> to learn more.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.news.with_raw_response.press_releases(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PressRelease
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.news.with_raw_response.press_releases(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PressRelease
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Company symbol. |
| <code>from_</code> | <code>Date \| None</code> | From time: 2020-01-01.<br>**Default**: <code>None</code> |
| <code>to</code> | <code>Date \| None</code> | To time: 2020-01-05.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[PressRelease](finnhub_api/models/press_release.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PressRelease](finnhub_api/models/press_release.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Scan

> Source: [Scan](finnhub_api/apis/scan.py)

<details>
<summary><code>def aggregate_indicator(symbol: str, resolution: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AggregateIndicators, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get aggregate signal of multiple technical indicators such as MACD, RSI, Moving Average v.v. A full list of indicators can be found <a href="https://docs.google.com/spreadsheets/d/1MWuy0WuT2yVlxr1KbPdggVygMZtJfunDnhe-C0GEXYM/edit?usp=sharing" target="_blank">here</a>.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.scan.with_raw_response.aggregate_indicator(symbol, resolution)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AggregateIndicators
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.scan.with_raw_response.aggregate_indicator(symbol, resolution)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AggregateIndicators
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | symbol |
| <code>resolution</code> | <code>str</code> | Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not be available depending on the exchange. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[AggregateIndicators](finnhub_api/models/aggregate_indicators.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AggregateIndicators](finnhub_api/models/aggregate_indicators.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def pattern_recognition(symbol: str, resolution: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PatternRecognition, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Run pattern recognition algorithm on a symbol. Support double top/bottom, triple top/bottom, head and shoulders, triangle, wedge, channel, flag, and candlestick patterns.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.scan.with_raw_response.pattern_recognition(symbol, resolution)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PatternRecognition
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.scan.with_raw_response.pattern_recognition(symbol, resolution)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PatternRecognition
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol |
| <code>resolution</code> | <code>str</code> | Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not be available depending on the exchange. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[PatternRecognition](finnhub_api/models/pattern_recognition.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PatternRecognition](finnhub_api/models/pattern_recognition.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def support_resistance(symbol: str, resolution: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SupportResistance, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get support and resistance levels for a symbol.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.scan.with_raw_response.support_resistance(symbol, resolution)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SupportResistance
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.scan.with_raw_response.support_resistance(symbol, resolution)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SupportResistance
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol |
| <code>resolution</code> | <code>str</code> | Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not be available depending on the exchange. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[SupportResistance](finnhub_api/models/support_resistance.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SupportResistance](finnhub_api/models/support_resistance.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## StockEstimates

> Source: [StockEstimates](finnhub_api/apis/stock_estimates.py)

<details>
<summary><code>def company_capex_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CapexEstimates, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get company's capital expenditure estimates.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_estimates.with_raw_response.company_capex_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CapexEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_estimates.with_raw_response.company_capex_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CapexEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>freq</code> | <code>str \| None</code> | Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[CapexEstimates](finnhub_api/models/capex_estimates.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CapexEstimates](finnhub_api/models/capex_estimates.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def company_dps_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DpsEstimates, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get company's Dividend per Share estimates.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_estimates.with_raw_response.company_dps_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DpsEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_estimates.with_raw_response.company_dps_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DpsEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>freq</code> | <code>str \| None</code> | Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[DpsEstimates](finnhub_api/models/dps_estimates.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DpsEstimates](finnhub_api/models/dps_estimates.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def company_earnings(symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[EarningResult], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get company historical quarterly earnings surprise going back to 2000.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_estimates.with_raw_response.company_earnings(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[EarningResult]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_estimates.with_raw_response.company_earnings(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[EarningResult]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>limit</code> | <code>int \| None</code> | Limit number of period returned. Leave blank to get the full history.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;list&#91;[EarningResult](finnhub_api/models/earning_result.py)&#93;, [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[EarningResult](finnhub_api/models/earning_result.py)&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def company_earnings_quality_score(symbol: str, freq: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CompanyEarningsQualityScore, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>This endpoint provides Earnings Quality Score for global companies.</p><p> Earnings quality refers to the extent to which current earnings predict future earnings. "High-quality" earnings are expected to persist, while "low-quality" earnings do not. A higher score means a higher earnings quality</p><p>Finnhub uses a proprietary model which takes into consideration 4 criteria:</p> <ul style="list-style-type: unset; margin-left: 30px;"><li>Profitability</li><li>Growth</li><li>Cash Generation & Capital Allocation</li><li>Leverage</li></ul><br/><p>We then compare the metrics of each company in each category against its peers in the same industry to gauge how quality its earnings is.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_estimates.with_raw_response.company_earnings_quality_score(symbol, freq)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CompanyEarningsQualityScore
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_estimates.with_raw_response.company_earnings_quality_score(symbol, freq)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CompanyEarningsQualityScore
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol. |
| <code>freq</code> | <code>str</code> | Frequency. Currently support <code>annual</code> and <code>quarterly</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[CompanyEarningsQualityScore](finnhub_api/models/company_earnings_quality_score.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CompanyEarningsQualityScore](finnhub_api/models/company_earnings_quality_score.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def company_ebit_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EbitEstimates, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get company's ebit estimates.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_estimates.with_raw_response.company_ebit_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EbitEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_estimates.with_raw_response.company_ebit_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EbitEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>freq</code> | <code>str \| None</code> | Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[EbitEstimates](finnhub_api/models/ebit_estimates.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[EbitEstimates](finnhub_api/models/ebit_estimates.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def company_ebitda_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EbitdaEstimates, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get company's ebitda estimates.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_estimates.with_raw_response.company_ebitda_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EbitdaEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_estimates.with_raw_response.company_ebitda_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EbitdaEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>freq</code> | <code>str \| None</code> | Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[EbitdaEstimates](finnhub_api/models/ebitda_estimates.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[EbitdaEstimates](finnhub_api/models/ebitda_estimates.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def company_eps_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EarningsEstimates, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get company's EPS estimates.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_estimates.with_raw_response.company_eps_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EarningsEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_estimates.with_raw_response.company_eps_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EarningsEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>freq</code> | <code>str \| None</code> | Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[EarningsEstimates](finnhub_api/models/earnings_estimates.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[EarningsEstimates](finnhub_api/models/earnings_estimates.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def company_fcf_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FcfEstimates, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get company's free cash flow estimates.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_estimates.with_raw_response.company_fcf_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FcfEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_estimates.with_raw_response.company_fcf_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FcfEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>freq</code> | <code>str \| None</code> | Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[FcfEstimates](finnhub_api/models/fcf_estimates.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[FcfEstimates](finnhub_api/models/fcf_estimates.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def company_gross_income_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GrossIncomeEstimates, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get company's gross income estimates.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_estimates.with_raw_response.company_gross_income_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GrossIncomeEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_estimates.with_raw_response.company_gross_income_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GrossIncomeEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>freq</code> | <code>str \| None</code> | Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[GrossIncomeEstimates](finnhub_api/models/gross_income_estimates.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GrossIncomeEstimates](finnhub_api/models/gross_income_estimates.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def company_net_income_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[NetIncomeEstimates, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get company's net income estimates.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_estimates.with_raw_response.company_net_income_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type NetIncomeEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_estimates.with_raw_response.company_net_income_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type NetIncomeEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>freq</code> | <code>str \| None</code> | Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[NetIncomeEstimates](finnhub_api/models/net_income_estimates.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[NetIncomeEstimates](finnhub_api/models/net_income_estimates.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def company_ocf_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[OcfEstimates, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get company's operating cash flow estimates.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_estimates.with_raw_response.company_ocf_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OcfEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_estimates.with_raw_response.company_ocf_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OcfEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>freq</code> | <code>str \| None</code> | Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[OcfEstimates](finnhub_api/models/ocf_estimates.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[OcfEstimates](finnhub_api/models/ocf_estimates.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def company_pretax_income_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PretaxIncomeEstimates, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get company's pretax income estimates.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_estimates.with_raw_response.company_pretax_income_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PretaxIncomeEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_estimates.with_raw_response.company_pretax_income_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PretaxIncomeEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>freq</code> | <code>str \| None</code> | Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[PretaxIncomeEstimates](finnhub_api/models/pretax_income_estimates.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PretaxIncomeEstimates](finnhub_api/models/pretax_income_estimates.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def company_revenue_estimates(symbol: str, *, freq: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RevenueEstimates, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get company's revenue estimates.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_estimates.with_raw_response.company_revenue_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RevenueEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_estimates.with_raw_response.company_revenue_estimates(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RevenueEstimates
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>freq</code> | <code>str \| None</code> | Can take 1 of the following values: <code>annual, quarterly</code>. Default to <code>quarterly</code><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[RevenueEstimates](finnhub_api/models/revenue_estimates.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RevenueEstimates](finnhub_api/models/revenue_estimates.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def price_target(symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PriceTarget, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get latest price target consensus.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_estimates.with_raw_response.price_target(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PriceTarget
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_estimates.with_raw_response.price_target(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PriceTarget
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[PriceTarget](finnhub_api/models/price_target.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PriceTarget](finnhub_api/models/price_target.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def recommendation_trends(symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[RecommendationTrend], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get latest analyst recommendation trends for a company.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_estimates.with_raw_response.recommendation_trends(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[RecommendationTrend]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_estimates.with_raw_response.recommendation_trends(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[RecommendationTrend]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;list&#91;[RecommendationTrend](finnhub_api/models/recommendation_trend.py)&#93;, [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[RecommendationTrend](finnhub_api/models/recommendation_trend.py)&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def revenue_breakdown(*, symbol: str | None = None, cik: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RevenueBreakdown, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Get revenue breakdown as-reporetd by product and geography. Users on personal plans can access data for US companies which disclose their revenue breakdown in the annual or quarterly reports.</p><p>Global standardized revenue breakdown/segments data is available for Enterprise users. <a href="mailto:support@finnhub.io">Contact us</a> to inquire about the access for Global standardized data.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_estimates.with_raw_response.revenue_breakdown()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RevenueBreakdown
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_estimates.with_raw_response.revenue_breakdown()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RevenueBreakdown
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | Symbol.<br>**Default**: <code>None</code> |
| <code>cik</code> | <code>str \| None</code> | CIK.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[RevenueBreakdown](finnhub_api/models/revenue_breakdown.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RevenueBreakdown](finnhub_api/models/revenue_breakdown.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def revenue_breakdown2(symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RevenueBreakdown2, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Get standardized revenue breakdown and KPIs data for 30,000+ global companies.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_estimates.with_raw_response.revenue_breakdown2(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RevenueBreakdown2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_estimates.with_raw_response.revenue_breakdown2(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RevenueBreakdown2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[RevenueBreakdown2](finnhub_api/models/revenue_breakdown2.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RevenueBreakdown2](finnhub_api/models/revenue_breakdown2.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def upgrade_downgrade(*, symbol: str | None = None, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[UpgradeDowngrade], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get latest stock upgrade and downgrade.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_estimates.with_raw_response.upgrade_downgrade()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[UpgradeDowngrade]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_estimates.with_raw_response.upgrade_downgrade()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[UpgradeDowngrade]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | Symbol of the company: AAPL. If left blank, the API will return latest stock upgrades/downgrades.<br>**Default**: <code>None</code> |
| <code>from_</code> | <code>Date \| None</code> | From date: 2000-03-15.<br>**Default**: <code>None</code> |
| <code>to</code> | <code>Date \| None</code> | To date: 2020-03-16.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;list&#91;[UpgradeDowngrade](finnhub_api/models/upgrade_downgrade.py)&#93;, [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[UpgradeDowngrade](finnhub_api/models/upgrade_downgrade.py)&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## StockFundamentals

> Source: [StockFundamentals](finnhub_api/apis/stock_fundamentals.py)

<details>
<summary><code>def company_basic_financials(symbol: str, metric: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BasicFinancials, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get company basic financials such as margin, P/E ratio, 52-week high/low etc.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_fundamentals.with_raw_response.company_basic_financials(symbol, metric)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BasicFinancials
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_fundamentals.with_raw_response.company_basic_financials(symbol, metric)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BasicFinancials
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>metric</code> | <code>str</code> | Metric type. Can be 1 of the following values <code>all</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[BasicFinancials](finnhub_api/models/basic_financials.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BasicFinancials](finnhub_api/models/basic_financials.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def company_esg_score(symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CompanyEsg, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>This endpoint provides the latest ESG scores and important indicators for 7000+ global companies. The data is collected through company's public ESG disclosure and public sources.</p><p>Our ESG scoring models takes into account more than 150 different inputs to calculate the level of ESG risks and how well a company is managing them. A higher score means lower ESG risk or better ESG management. ESG scores are in the the range of 0-100. Some key indicators might contain letter-grade score from C- to A+ with C- is the lowest score and A+ is the highest score.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_fundamentals.with_raw_response.company_esg_score(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CompanyEsg
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_fundamentals.with_raw_response.company_esg_score(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CompanyEsg
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[CompanyEsg](finnhub_api/models/company_esg.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CompanyEsg](finnhub_api/models/company_esg.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def company_executive(symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CompanyExecutive, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of company's executives and members of the Board.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_fundamentals.with_raw_response.company_executive(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CompanyExecutive
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_fundamentals.with_raw_response.company_executive(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CompanyExecutive
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[CompanyExecutive](finnhub_api/models/company_executive.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CompanyExecutive](finnhub_api/models/company_executive.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def company_historical_esg_score(symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[HistoricalCompanyEsg, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>This endpoint provides historical ESG scores and important indicators for 7000+ global companies. The data is collected through company's public ESG disclosure and public sources.</p><p>Our ESG scoring models takes into account more than 150 different inputs to calculate the level of ESG risks and how well a company is managing them. A higher score means lower ESG risk or better ESG management. ESG scores are in the the range of 0-100. Some key indicators might contain letter-grade score from C- to A+ with C- is the lowest score and A+ is the highest score.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_fundamentals.with_raw_response.company_historical_esg_score(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type HistoricalCompanyEsg
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_fundamentals.with_raw_response.company_historical_esg_score(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type HistoricalCompanyEsg
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[HistoricalCompanyEsg](finnhub_api/models/historical_company_esg.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[HistoricalCompanyEsg](finnhub_api/models/historical_company_esg.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def company_profile(*, symbol: str | None = None, isin: str | None = None, cusip: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CompanyProfile, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get general information of a company. You can query by symbol, ISIN or CUSIP

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_fundamentals.with_raw_response.company_profile()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CompanyProfile
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_fundamentals.with_raw_response.company_profile()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CompanyProfile
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | Symbol of the company: AAPL e.g.<br>**Default**: <code>None</code> |
| <code>isin</code> | <code>str \| None</code> | ISIN<br>**Default**: <code>None</code> |
| <code>cusip</code> | <code>str \| None</code> | CUSIP<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[CompanyProfile](finnhub_api/models/company_profile.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CompanyProfile](finnhub_api/models/company_profile.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def company_profile2(*, symbol: str | None = None, isin: str | None = None, cusip: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CompanyProfile2, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get general information of a company. You can query by symbol, ISIN or CUSIP. This is the free version of <a href="#company-profile">Company Profile</a>.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_fundamentals.with_raw_response.company_profile2()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CompanyProfile2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_fundamentals.with_raw_response.company_profile2()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CompanyProfile2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | Symbol of the company: AAPL e.g.<br>**Default**: <code>None</code> |
| <code>isin</code> | <code>str \| None</code> | ISIN<br>**Default**: <code>None</code> |
| <code>cusip</code> | <code>str \| None</code> | CUSIP<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[CompanyProfile2](finnhub_api/models/company_profile2.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CompanyProfile2](finnhub_api/models/company_profile2.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def earnings_call_live(*, from_: Date | None = None, to: Date | None = None, symbol: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EarningsCallLive, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Stream live earnings calls with data provided in the calendar. The data will be available in m3u8 format. mp3 files will be available once the calls finish in the <code>recording</code> field.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_fundamentals.with_raw_response.earnings_call_live()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EarningsCallLive
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_fundamentals.with_raw_response.earnings_call_live()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EarningsCallLive
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>from_</code> | <code>Date \| None</code> | From date <code>YYYY-MM-DD</code>.<br>**Default**: <code>None</code> |
| <code>to</code> | <code>Date \| None</code> | To date <code>YYYY-MM-DD</code>.<br>**Default**: <code>None</code> |
| <code>symbol</code> | <code>str \| None</code> | Filter by symbol: AAPL.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[EarningsCallLive](finnhub_api/models/earnings_call_live.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[EarningsCallLive](finnhub_api/models/earnings_call_live.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def filings(*, symbol: str | None = None, cik: str | None = None, access_number: str | None = None, form: str | None = None, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Filing], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List company's filing. Limit to 250 documents at a time. This data is available for bulk download on <a href="https://www.kaggle.com/finnhub/sec-filings" target="_blank">Kaggle SEC Filings database</a>.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_fundamentals.with_raw_response.filings()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Filing]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_fundamentals.with_raw_response.filings()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Filing]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | Symbol. Leave <code>symbol</code>,<code>cik</code> and <code>accessNumber</code> empty to list latest filings.<br>**Default**: <code>None</code> |
| <code>cik</code> | <code>str \| None</code> | CIK.<br>**Default**: <code>None</code> |
| <code>access_number</code> | <code>str \| None</code> | Access number of a specific report you want to retrieve data from.<br>**Default**: <code>None</code> |
| <code>form</code> | <code>str \| None</code> | Filter by form. You can use this value <code>NT 10-K</code> to find non-timely filings for a company.<br>**Default**: <code>None</code> |
| <code>from_</code> | <code>Date \| None</code> | From date: 2023-03-15.<br>**Default**: <code>None</code> |
| <code>to</code> | <code>Date \| None</code> | To date: 2023-03-16.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;list&#91;[Filing](finnhub_api/models/filing.py)&#93;, [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Filing](finnhub_api/models/filing.py)&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def filings_sentiment(access_number: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SecsentimentAnalysis, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get sentiment analysis of 10-K and 10-Q filings from SEC. An abnormal increase in the number of positive/negative words in filings can signal a significant change in the company's stock price in the upcoming 4 quarters. We make use of <a href= "https://sraf.nd.edu/textual-analysis/resources/" target="_blank">Loughran and McDonald Sentiment Word Lists</a> to calculate the sentiment for each filing.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_fundamentals.with_raw_response.filings_sentiment(access_number)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SecsentimentAnalysis
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_fundamentals.with_raw_response.filings_sentiment(access_number)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SecsentimentAnalysis
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>access_number</code> | <code>str</code> | Access number of a specific report you want to retrieve data from. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[SecsentimentAnalysis](finnhub_api/models/secsentiment_analysis.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SecsentimentAnalysis](finnhub_api/models/secsentiment_analysis.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def financials(symbol: str, statement: str, freq: str, *, preliminary: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FinancialStatements, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Get standardized balance sheet, income statement and cash flow for global companies going back 30+ years. Data is sourced from original filings most of which made available through <a href="#filings">SEC Filings</a> and <a href="#international-filings">International Filings</a> endpoints.</p><p>Set <code>preliminary</code> param to true for faster updates for US companies.</p><p><i>Wondering why our standardized data is different from Bloomberg, Reuters, Factset, S&P or Yahoo Finance ? Check out our <a href="/faq">FAQ page</a> to learn more</i></p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_fundamentals.with_raw_response.financials(symbol, statement, freq)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FinancialStatements
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_fundamentals.with_raw_response.financials(symbol, statement, freq)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FinancialStatements
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>statement</code> | <code>str</code> | Statement can take 1 of these values <code>bs, ic, cf</code> for Balance Sheet, Income Statement, Cash Flow respectively. |
| <code>freq</code> | <code>str</code> | Frequency can take 1 of these values <code>annual, quarterly, ttm, ytd</code>.  TTM (Trailing Twelve Months) option is available for Income Statement and Cash Flow. YTD (Year To Date) option is only available for Cash Flow. |
| <code>preliminary</code> | <code>str \| None</code> | If set to <code>true</code>, it will return Preliminary financial statements for the latest period which are usually available within an hour of the earnings announcement if finalized data is not available yet. This preliminary data is currently available for US companies. You will see <code>"preliminary": true</code> in the data if that period is using preliminary data.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[FinancialStatements](finnhub_api/models/financial_statements.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[FinancialStatements](finnhub_api/models/financial_statements.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def financials_reported(*, symbol: str | None = None, cik: str | None = None, access_number: str | None = None, freq: str | None = None, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FinancialsAsReported, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get financials as reported. This data is available for bulk download on <a href="https://www.kaggle.com/finnhub/reported-financials" target="_blank">Kaggle SEC Financials database</a>.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_fundamentals.with_raw_response.financials_reported()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FinancialsAsReported
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_fundamentals.with_raw_response.financials_reported()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FinancialsAsReported
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | Symbol.<br>**Default**: <code>None</code> |
| <code>cik</code> | <code>str \| None</code> | CIK.<br>**Default**: <code>None</code> |
| <code>access_number</code> | <code>str \| None</code> | Access number of a specific report you want to retrieve financials from.<br>**Default**: <code>None</code> |
| <code>freq</code> | <code>str \| None</code> | Frequency. Can be either <code>annual</code> or <code>quarterly</code>. Default to <code>annual</code>.<br>**Default**: <code>None</code> |
| <code>from_</code> | <code>Date \| None</code> | From date <code>YYYY-MM-DD</code>. Filter for endDate.<br>**Default**: <code>None</code> |
| <code>to</code> | <code>Date \| None</code> | To date <code>YYYY-MM-DD</code>. Filter for endDate.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[FinancialsAsReported](finnhub_api/models/financials_as_reported.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[FinancialsAsReported](finnhub_api/models/financials_as_reported.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def historical_employee_count(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[HistoricalEmployeeCount, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get historical employee count for global companies.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_fundamentals.with_raw_response.historical_employee_count(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type HistoricalEmployeeCount
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_fundamentals.with_raw_response.historical_employee_count(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type HistoricalEmployeeCount
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Company symbol. |
| <code>from_</code> | <code>Date</code> | From date <code>YYYY-MM-DD</code>. |
| <code>to</code> | <code>Date</code> | To date <code>YYYY-MM-DD</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[HistoricalEmployeeCount](finnhub_api/models/historical_employee_count.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[HistoricalEmployeeCount](finnhub_api/models/historical_employee_count.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def international_filings(*, symbol: str | None = None, country: str | None = None, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[InternationalFiling], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List filings for international companies. Limit to 500 documents at a time. These are the documents we use to source our fundamental data. Enterprise clients who need access to the full filings for global markets should contact us for the access.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_fundamentals.with_raw_response.international_filings()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[InternationalFiling]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_fundamentals.with_raw_response.international_filings()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[InternationalFiling]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | Symbol. Leave empty to list latest filings.<br>**Default**: <code>None</code> |
| <code>country</code> | <code>str \| None</code> | Filter by country using country's 2-letter code.<br>**Default**: <code>None</code> |
| <code>from_</code> | <code>Date \| None</code> | From date: 2023-01-15.<br>**Default**: <code>None</code> |
| <code>to</code> | <code>Date \| None</code> | To date: 2023-12-16.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;list&#91;[InternationalFiling](finnhub_api/models/international_filing.py)&#93;, [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[InternationalFiling](finnhub_api/models/international_filing.py)&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def newsroom(symbol: str, *, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Newsroom, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Get latest articles posted directly on the companies' newsroom and investor relations page. Newsroom API along with the Press Releases API provide a comprehensive text-based dataset directly from the company. We currently cover 1,250 US Companies with this dataset.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_fundamentals.with_raw_response.newsroom(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Newsroom
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_fundamentals.with_raw_response.newsroom(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Newsroom
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Company symbol. |
| <code>from_</code> | <code>Date \| None</code> | From time: 2025-01-01.<br>**Default**: <code>None</code> |
| <code>to</code> | <code>Date \| None</code> | To time: 2026-01-05.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[Newsroom](finnhub_api/models/newsroom.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Newsroom](finnhub_api/models/newsroom.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def similarity_index(*, symbol: str | None = None, cik: str | None = None, freq: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SimilarityIndex, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Calculate the textual difference between a company's 10-K / 10-Q reports and the same type of report in the previous year using Cosine Similarity. For example, this endpoint compares 2019's 10-K with 2018's 10-K. Companies breaking from its routines in disclosure of financial condition and risk analysis section can signal a significant change in the company's stock price in the upcoming 4 quarters.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_fundamentals.with_raw_response.similarity_index()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SimilarityIndex
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_fundamentals.with_raw_response.similarity_index()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SimilarityIndex
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str \| None</code> | Symbol. Required if cik is empty<br>**Default**: <code>None</code> |
| <code>cik</code> | <code>str \| None</code> | CIK. Required if symbol is empty<br>**Default**: <code>None</code> |
| <code>freq</code> | <code>str \| None</code> | <code>annual</code> or <code>quarterly</code>. Default to <code>annual</code><br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[SimilarityIndex](finnhub_api/models/similarity_index.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SimilarityIndex](finnhub_api/models/similarity_index.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stock_presentation(symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StockPresentation, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Get presentations/slides data in PDF format that are usually used during earnings calls. You can get a list of supported symbols <a target="_blank" href="/api/v1/stock/presentation/symbol?token=">here</a></p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_fundamentals.with_raw_response.stock_presentation(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StockPresentation
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_fundamentals.with_raw_response.stock_presentation(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StockPresentation
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Company symbol. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[StockPresentation](finnhub_api/models/stock_presentation.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StockPresentation](finnhub_api/models/stock_presentation.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transcripts(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EarningsCallTranscripts, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Get earnings call transcripts, audio and participants' list. Data is available for US, UK, European, Australian and Canadian companies.<p>15+ years of data is available with 220,000+ audio which add up to 7TB in size.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_fundamentals.with_raw_response.transcripts(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EarningsCallTranscripts
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_fundamentals.with_raw_response.transcripts(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EarningsCallTranscripts
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | Transcript's id obtained with <a href="#transcripts-list">Transcripts List endpoint</a>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[EarningsCallTranscripts](finnhub_api/models/earnings_call_transcripts.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[EarningsCallTranscripts](finnhub_api/models/earnings_call_transcripts.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def transcripts_list(symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EarningsCallTranscriptsList, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List earnings call transcripts' metadata. This endpoint is available for Global companies. You can get a list of supported symbols <a target="_blank" href="/api/v1/stock/transcripts/symbol?token=">here</a>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_fundamentals.with_raw_response.transcripts_list(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EarningsCallTranscriptsList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_fundamentals.with_raw_response.transcripts_list(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EarningsCallTranscriptsList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Company symbol: AAPL. Leave empty to list the latest transcripts |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[EarningsCallTranscriptsList](finnhub_api/models/earnings_call_transcripts_list.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[EarningsCallTranscriptsList](finnhub_api/models/earnings_call_transcripts_list.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## StockOwnership

> Source: [StockOwnership](finnhub_api/apis/stock_ownership.py)

<details>
<summary><code>def congressional_trading(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CongressionalTrading, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get stock trades data disclosed by members of congress.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_ownership.with_raw_response.congressional_trading(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CongressionalTrading
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_ownership.with_raw_response.congressional_trading(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CongressionalTrading
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>from_</code> | <code>Date</code> | From date <code>YYYY-MM-DD</code>. |
| <code>to</code> | <code>Date</code> | To date <code>YYYY-MM-DD</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[CongressionalTrading](finnhub_api/models/congressional_trading.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CongressionalTrading](finnhub_api/models/congressional_trading.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def fund_ownership(symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FundOwnership, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a full list fund and institutional investors of a company in descending order of the number of shares held. Data is sourced from <code>13F form</code>, <code>Schedule 13D</code> and <code>13G</code> for US market, <code>UK Share Register</code> for UK market, <code>SEDI</code> for Canadian market and equivalent filings for other international markets.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_ownership.with_raw_response.fund_ownership(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FundOwnership
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_ownership.with_raw_response.fund_ownership(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FundOwnership
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>limit</code> | <code>int \| None</code> | Limit number of results. Leave empty to get the full list.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[FundOwnership](finnhub_api/models/fund_ownership.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[FundOwnership](finnhub_api/models/fund_ownership.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def insider_sentiment(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[InsiderSentiments, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get insider sentiment data for US companies calculated using method discussed <a href="https://medium.com/@stock-api/finnhub-insiders-sentiment-analysis-cc43f9f64b3a" target="_blank">here</a>. The MSPR ranges from -100 for the most negative to 100 for the most positive which can signal price changes in the coming 30-90 days.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_ownership.with_raw_response.insider_sentiment(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InsiderSentiments
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_ownership.with_raw_response.insider_sentiment(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InsiderSentiments
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>from_</code> | <code>Date</code> | From date: 2020-03-15. |
| <code>to</code> | <code>Date</code> | To date: 2020-03-16. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[InsiderSentiments](finnhub_api/models/insider_sentiments.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[InsiderSentiments](finnhub_api/models/insider_sentiments.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def insider_transactions(symbol: str, *, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[InsiderTransactions, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Company insider transactions data sourced from <code>Form 3,4,5</code>, SEDI and relevant companies' filings. This endpoint covers US, UK, Canada, Australia, India, and all major EU markets. Limit to 100 transactions per API call.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_ownership.with_raw_response.insider_transactions(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InsiderTransactions
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_ownership.with_raw_response.insider_transactions(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InsiderTransactions
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. Leave this param blank to get the latest transactions. |
| <code>from_</code> | <code>Date \| None</code> | From date: 2020-03-15.<br>**Default**: <code>None</code> |
| <code>to</code> | <code>Date \| None</code> | To date: 2020-03-16.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[InsiderTransactions](finnhub_api/models/insider_transactions.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[InsiderTransactions](finnhub_api/models/insider_transactions.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def investment_themes(theme: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[InvestmentThemes, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Thematic investing involves creating a portfolio (or portion of a portfolio) by gathering together a collection of companies involved in certain areas that you predict will generate above-market returns over the long term. Themes can be based on a concept such as ageing populations or a sub-sector such as robotics, and drones. Thematic investing focuses on predicted long-term trends rather than specific companies or sectors, enabling investors to access structural, one-off shifts that can change an entire industry.</p><p>This endpoint will help you get portfolios of different investment themes that are changing our life and are the way of the future.</p><p>A full list of themes supported can be found <a target="_blank" href="https://docs.google.com/spreadsheets/d/1ULj9xDh4iPoQj279M084adZ2_S852ttRthKKJ7madYc/edit?usp=sharing">here</a>. The theme coverage and portfolios are updated bi-weekly by our analysts. Our approach excludes penny, super-small cap and illiquid stocks.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_ownership.with_raw_response.investment_themes(theme)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InvestmentThemes
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_ownership.with_raw_response.investment_themes(theme)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InvestmentThemes
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>theme</code> | <code>str</code> | Investment theme. A full list of themes supported can be found <a target="_blank" href="https://docs.google.com/spreadsheets/d/1ULj9xDh4iPoQj279M084adZ2_S852ttRthKKJ7madYc/edit?usp=sharing">here</a>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[InvestmentThemes](finnhub_api/models/investment_themes.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[InvestmentThemes](finnhub_api/models/investment_themes.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def ownership(symbol: str, *, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Ownership, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a full list of shareholders of a company in descending order of the number of shares held. Data is sourced from <code>13F form</code>, <code>Schedule 13D</code> and <code>13G</code> for US market, <code>UK Share Register</code> for UK market, <code>SEDI</code> for Canadian market and equivalent filings for other international markets.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_ownership.with_raw_response.ownership(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Ownership
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_ownership.with_raw_response.ownership(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Ownership
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>limit</code> | <code>int \| None</code> | Limit number of results. Leave empty to get the full list.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[Ownership](finnhub_api/models/ownership.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Ownership](finnhub_api/models/ownership.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def social_sentiment(symbol: str, *, from_: Date | None = None, to: Date | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SocialSentiment, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Get social sentiment for stocks on Reddit and Twitter.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_ownership.with_raw_response.social_sentiment(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SocialSentiment
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_ownership.with_raw_response.social_sentiment(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SocialSentiment
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Company symbol. |
| <code>from_</code> | <code>Date \| None</code> | From date <code>YYYY-MM-DD</code>.<br>**Default**: <code>None</code> |
| <code>to</code> | <code>Date \| None</code> | To date <code>YYYY-MM-DD</code>.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[SocialSentiment](finnhub_api/models/social_sentiment.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SocialSentiment](finnhub_api/models/social_sentiment.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stock_lobbying(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LobbyingResult, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of reported lobbying activities in the Senate and the House.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_ownership.with_raw_response.stock_lobbying(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LobbyingResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_ownership.with_raw_response.stock_lobbying(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LobbyingResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol. |
| <code>from_</code> | <code>Date</code> | From date <code>YYYY-MM-DD</code>. |
| <code>to</code> | <code>Date</code> | To date <code>YYYY-MM-DD</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[LobbyingResult](finnhub_api/models/lobbying_result.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[LobbyingResult](finnhub_api/models/lobbying_result.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stock_usa_spending(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UsaSpendingResult, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Get a list of government's spending activities from USASpending dataset for public companies. This dataset can help you identify companies that win big government contracts which is extremely important for industries such as Defense, Aerospace, and Education. Only recent data is available via the API.</p><p>For historical data, you can download it here: <a href="/api/v1/stock/usa-spending?fileId=before_2021&token=" target="_blank">Pre-2021</a>, <a href="/api/v1/stock/usa-spending?fileId=2021&token=" target="_blank">2021</a>, <a href="/api/v1/stock/usa-spending?fileId=2022&token=" target="_blank">2022</a>, <a href="/api/v1/stock/usa-spending?fileId=2023&token=" target="_blank">2023</a>, <a href="/api/v1/stock/usa-spending?fileId=2024&token=" target="_blank">2024</a></p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_ownership.with_raw_response.stock_usa_spending(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UsaSpendingResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_ownership.with_raw_response.stock_usa_spending(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UsaSpendingResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol. |
| <code>from_</code> | <code>Date</code> | From date <code>YYYY-MM-DD</code>. Filter for <code>actionDate</code> |
| <code>to</code> | <code>Date</code> | To date <code>YYYY-MM-DD</code>. Filter for <code>actionDate</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[UsaSpendingResult](finnhub_api/models/usa_spending_result.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UsaSpendingResult](finnhub_api/models/usa_spending_result.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stock_uspto_patent(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UsptoPatentResult, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List USPTO patents for companies. Limit to 250 records per API call.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_ownership.with_raw_response.stock_uspto_patent(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UsptoPatentResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_ownership.with_raw_response.stock_uspto_patent(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UsptoPatentResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol. |
| <code>from_</code> | <code>Date</code> | From date <code>YYYY-MM-DD</code>. |
| <code>to</code> | <code>Date</code> | To date <code>YYYY-MM-DD</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[UsptoPatentResult](finnhub_api/models/uspto_patent_result.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UsptoPatentResult](finnhub_api/models/uspto_patent_result.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stock_visa_application(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[VisaApplicationResult, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of H1-B and Permanent visa applications for companies from the DOL. The data is updated quarterly.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_ownership.with_raw_response.stock_visa_application(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type VisaApplicationResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_ownership.with_raw_response.stock_visa_application(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type VisaApplicationResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol. |
| <code>from_</code> | <code>Date</code> | From date <code>YYYY-MM-DD</code>. Filter on the <code>beginDate</code> column. |
| <code>to</code> | <code>Date</code> | To date <code>YYYY-MM-DD</code>. Filter on the <code>beginDate</code> column. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[VisaApplicationResult](finnhub_api/models/visa_application_result.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[VisaApplicationResult](finnhub_api/models/visa_application_result.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def supply_chain_relationships(symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SupplyChainRelationships, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>This endpoint provides an overall map of public companies' key customers and suppliers. The data offers a deeper look into a company's supply chain and how products are created. The data will help investors manage risk, limit exposure or generate alpha-generating ideas and trading insights.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_ownership.with_raw_response.supply_chain_relationships(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SupplyChainRelationships
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_ownership.with_raw_response.supply_chain_relationships(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SupplyChainRelationships
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[SupplyChainRelationships](finnhub_api/models/supply_chain_relationships.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SupplyChainRelationships](finnhub_api/models/supply_chain_relationships.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## StockPrices

> Source: [StockPrices](finnhub_api/apis/stock_prices.py)

<details>
<summary><code>def company_peers(symbol: str, *, grouping: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[str], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get company peers. Return a list of peers operating in the same country and sector/industry.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_prices.with_raw_response.company_peers(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[str]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_prices.with_raw_response.company_peers(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[str]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>grouping</code> | <code>str \| None</code> | Specify the grouping criteria for choosing peers.Supporter values: <code>sector</code>, <code>industry</code>, <code>subIndustry</code>. Default to <code>subIndustry</code>.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;list&#91;str&#93;, [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;str&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def historical_market_cap(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[HistoricalMarketCapData, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get historical market cap data for global companies.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_prices.with_raw_response.historical_market_cap(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type HistoricalMarketCapData
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_prices.with_raw_response.historical_market_cap(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type HistoricalMarketCapData
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Company symbol. |
| <code>from_</code> | <code>Date</code> | From date <code>YYYY-MM-DD</code>. |
| <code>to</code> | <code>Date</code> | To date <code>YYYY-MM-DD</code>. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[HistoricalMarketCapData](finnhub_api/models/historical_market_cap_data.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[HistoricalMarketCapData](finnhub_api/models/historical_market_cap_data.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def market_holiday(exchange: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[MarketHoliday, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get a list of holidays for global exchanges.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_prices.with_raw_response.market_holiday(exchange)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MarketHoliday
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_prices.with_raw_response.market_holiday(exchange)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MarketHoliday
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>exchange</code> | <code>str</code> | Exchange code. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[MarketHoliday](finnhub_api/models/market_holiday.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[MarketHoliday](finnhub_api/models/market_holiday.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def market_status(exchange: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[MarketStatus, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get current market status for global exchanges (whether exchanges are open or close).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_prices.with_raw_response.market_status(exchange)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MarketStatus
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_prices.with_raw_response.market_status(exchange)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MarketStatus
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>exchange</code> | <code>str</code> | Exchange code. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[MarketStatus](finnhub_api/models/market_status.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[MarketStatus](finnhub_api/models/market_status.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def price_metrics(symbol: str, *, date: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PriceMetrics, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get company price performance statistics such as 52-week high/low, YTD return and much more.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_prices.with_raw_response.price_metrics(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PriceMetrics
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_prices.with_raw_response.price_metrics(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PriceMetrics
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol of the company: AAPL. |
| <code>date</code> | <code>str \| None</code> | Get data on a specific date in the past. The data is available weekly so your date will be automatically adjusted to the last day of that week.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[PriceMetrics](finnhub_api/models/price_metrics.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PriceMetrics](finnhub_api/models/price_metrics.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stock_basic_dividends(symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Dividends2, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get global dividends data.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_prices.with_raw_response.stock_basic_dividends(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Dividends2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_prices.with_raw_response.stock_basic_dividends(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Dividends2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[Dividends2](finnhub_api/models/dividends2.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Dividends2](finnhub_api/models/dividends2.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stock_bidask(symbol: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LastBidAsk, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get last bid/ask data for US stocks.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_prices.with_raw_response.stock_bidask(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LastBidAsk
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_prices.with_raw_response.stock_bidask(symbol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LastBidAsk
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[LastBidAsk](finnhub_api/models/last_bid_ask.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[LastBidAsk](finnhub_api/models/last_bid_ask.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stock_candles(symbol: str, resolution: str, from_: int, to: int, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StockCandles, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Get candlestick data (OHLCV) for stocks.</p><p>Daily data will be adjusted for Splits. Intraday data will remain unadjusted. Only 1 month of intraday will be returned at a time. If you need more historical intraday data, please use the from and to params iteratively to request more data.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_prices.with_raw_response.stock_candles(symbol, resolution, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StockCandles
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_prices.with_raw_response.stock_candles(symbol, resolution, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StockCandles
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol. |
| <code>resolution</code> | <code>str</code> | Supported resolution includes <code>1, 5, 15, 30, 60, D, W, M </code>.Some timeframes might not be available depending on the exchange. |
| <code>from_</code> | <code>int</code> | UNIX timestamp. Interval initial value. |
| <code>to</code> | <code>int</code> | UNIX timestamp. Interval end value. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[StockCandles](finnhub_api/models/stock_candles.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StockCandles](finnhub_api/models/stock_candles.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stock_dividends(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Dividends], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get dividends data for common stocks going back 30 years.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_prices.with_raw_response.stock_dividends(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Dividends]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_prices.with_raw_response.stock_dividends(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Dividends]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol. |
| <code>from_</code> | <code>Date</code> | YYYY-MM-DD. |
| <code>to</code> | <code>Date</code> | YYYY-MM-DD. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;list&#91;[Dividends](finnhub_api/models/dividends.py)&#93;, [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Dividends](finnhub_api/models/dividends.py)&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stock_nbbo(symbol: str, date: Date, limit: int, skip: int, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[HistoricalNbbo, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Get historical best bid and offer for US stocks, LSE, TSX, Euronext and Deutsche Borse.</p><p>For US market, this endpoint only serves historical NBBO from the beginning of 2023. To download more historical data, please visit our bulk download page in the Dashboard <a target="_blank" href="/dashboard/download",>here</a>.</p>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_prices.with_raw_response.stock_nbbo(symbol, date, limit, skip)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type HistoricalNbbo
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_prices.with_raw_response.stock_nbbo(symbol, date, limit, skip)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type HistoricalNbbo
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol. |
| <code>date</code> | <code>Date</code> | Date: 2020-04-02. |
| <code>limit</code> | <code>int</code> | Limit number of ticks returned. Maximum value: <code>25000</code> |
| <code>skip</code> | <code>int</code> | Number of ticks to skip. Use this parameter to loop through the entire data. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[HistoricalNbbo](finnhub_api/models/historical_nbbo.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[HistoricalNbbo](finnhub_api/models/historical_nbbo.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stock_splits(symbol: str, from_: Date, to: Date, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Split], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get splits data for stocks.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_prices.with_raw_response.stock_splits(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Split]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_prices.with_raw_response.stock_splits(symbol, from_, to)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Split]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol. |
| <code>from_</code> | <code>Date</code> | YYYY-MM-DD. |
| <code>to</code> | <code>Date</code> | YYYY-MM-DD. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;list&#91;[Split](finnhub_api/models/split.py)&#93;, [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Split](finnhub_api/models/split.py)&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stock_symbols(exchange: str, *, mic: str | None = None, security_type: str | None = None, currency: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[StockSymbol], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List supported stocks. We use the following symbology to identify stocks on Finnhub <code>Exchange_Ticker.Exchange_Code</code>. A list of supported exchange codes can be found <a href="https://docs.google.com/spreadsheets/d/1I3pBxjfXB056-g_JYf_6o3Rns3BV2kMGG1nCatb91ls/edit?usp=sharing" target="_blank">here</a>.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_prices.with_raw_response.stock_symbols(exchange)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[StockSymbol]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_prices.with_raw_response.stock_symbols(exchange)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[StockSymbol]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>exchange</code> | <code>str</code> | Exchange you want to get the list of symbols from. List of exchange codes can be found <a href="https://docs.google.com/spreadsheets/d/1I3pBxjfXB056-g_JYf_6o3Rns3BV2kMGG1nCatb91ls/edit?usp=sharing" target="_blank">here</a>. |
| <code>mic</code> | <code>str \| None</code> | Filter by MIC code.<br>**Default**: <code>None</code> |
| <code>security_type</code> | <code>str \| None</code> | Filter by security type used by OpenFigi standard.<br>**Default**: <code>None</code> |
| <code>currency</code> | <code>str \| None</code> | Filter by currency.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;list&#91;[StockSymbol](finnhub_api/models/stock_symbol.py)&#93;, [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[StockSymbol](finnhub_api/models/stock_symbol.py)&#93;</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stock_tick(symbol: str, date: Date, limit: int, skip: int, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TickData, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

<p>Get historical tick data for global exchanges.</p><p>For more historical tick data, you can visit our bulk download page in the Dashboard <a target="_blank" href="/dashboard/download",>here</a> to speed up the download process.</p><table class="table table-hover">
  <thead>
    <tr>
      <th>Exchange</th>
      <th>Segment</th>
      <th>Delay</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="text-blue">US CTA/UTP</th>
      <td>Full SIP</td>
      <td>End-of-day</td>
    </tr>
    <tr>
      <td class="text-blue">TSX</th>
      <td><ul><li>TSX</li><li>TSX Venture</li><li>Index</li></ul></td>
      <td>End-of-day</td>
    </tr>
    <tr>
      <td class="text-blue">LSE</th>
      <td><ul><li>London Stock Exchange (L)</li><li>LSE International (L)</li><li>LSE European (L)</li></ul></td>
      <td>15 minute</td>
    </tr>
    <tr>
      <td class="text-blue">Euronext</th>
      <td><ul> <li>Euronext Paris (PA)</li> <li>Euronext Amsterdam (AS)</li> <li>Euronext Lisbon (LS)</li> <li>Euronext Brussels (BR)</li> <li>Euronext Oslo (OL)</li> <li>Euronext London (LN)</li> <li>Euronext Dublin (IR)</li> <li>Index</li> <li>Warrant</li></ul></td>
      <td>End-of-day</td>
    </tr>
    <tr>
      <td class="text-blue">Deutsche Börse</th>
      <td><ul> <li>Frankfurt (F)</li> <li>Xetra (DE)</li> <li>Duesseldorf (DU)</li> <li>Hamburg (HM)</li> <li>Berlin (BE)</li> <li>Hanover (HA)</li> <li>Stoxx (SX)</li> <li>TradeGate (TG)</li> <li>Zertifikate (SC)</li> <li>Index</li> <li>Warrant</li></ul></td>
      <td>End-of-day</td>
    </tr>
  </tbody>
</table>

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.stock_prices.with_raw_response.stock_tick(symbol, date, limit, skip)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TickData
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.stock_prices.with_raw_response.stock_tick(symbol, date, limit, skip)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TickData
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>symbol</code> | <code>str</code> | Symbol. |
| <code>date</code> | <code>Date</code> | Date: 2020-04-02. |
| <code>limit</code> | <code>int</code> | Limit number of ticks returned. Maximum value: <code>25000</code> |
| <code>skip</code> | <code>int</code> | Number of ticks to skip. Use this parameter to loop through the entire data. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](finnhub_api/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](finnhub_api/core/results.py)&#91;[TickData](finnhub_api/models/tick_data.py), [RawError](finnhub_api/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TickData](finnhub_api/models/tick_data.py)</code> -- successful operation

**On `Failure`**: `error` is <code>[RawError](finnhub_api/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

