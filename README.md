# Webull OpenAPI Python SDK

Webull OpenAPI aims to provide quantitative trading investors with convenient, fast and secure services. Webull aims to help every quant traders achieve flexible and changeable trading or market strategies.

The main function:

Trading management: create, modify, cancel orders, etc.

Market information: You can query stocks/ETFs and other related market information through the HTTP interface.

Account Information: Query account balance and position information.

Subscription to real-time information: Subscribe to order status changes, market information, etc.

## Requirements

- Please first generate the app key and app secret on the [Webull Hong Kong official website](https://www.webull.hk).
- Requires Python 3.7 and above.

## Interface Protocol

The bottom layer of Webull OpenAPI provides three protocols, HTTP / GRPC / MQTT, to support functions and features like trading, subcriptions for changes of order status and real-time market quotes.

HTTP: It mainly provides interface services for data such as tradings, accounts, candlestick charts, snapshots, etc.

GRPC: Currently provides real-time messages for order status changes.

MQTT: Provides data services for real-time market conditions.

## Developer documentation

https://developer.webull.hk/api-doc/

## Documentation

- [Requirements](./docs/0-Requirement_CN.md)
- [SDK installation](./docs/1-Installation.md)
- [Timeout mechanism](./docs/2-Timeout.md)
- [Proxy configuration](./docs/3-Proxy.md)
- [Log](./docs/4-Log.md)
- [Domain](./docs/5-Endpoint.md)
- [SSL/TLS](./docs/6-TLS.md)
- [Exception and retry mechanism](./docs/7-ExceptionAndRetry.md)
