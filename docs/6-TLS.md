# SSL/TLS

openapi enables SSL/TLS for all application protocols.

- The protocol used by the HTTP API is `HTTPS`.
- The protocol used for market subscription is `MQTTS`.
- The protocol used for trade events subscription/Quotes is `GRPC`, which supports SSL/TLS by default.

The verification of the server-side certificate is automatically completed by the built-in root certificate chain. During the process of using the SDK, if you encounter certificate-related errors, you can first confirm the root certificate path used in the python environment.

For example, view the root certificate path through the following code example.

```python
import ssl
print(ssl.get_default_verify_paths())
```

The output of the above code might be as follows.

```
DefaultVerifyPaths(cafile=None, capath='/usr/local/openssl/ssl/certs', openssl_cafile_env='SSL_CERT_FILE', openssl_cafile='/usr/local/openssl/ssl/cert.pem', openssl_capath_env='SSL_CERT_DIR', openssl_capath='/usr/local/openssl/ssl/certs')
```

According to the path, such as **/usr/local/openssl/ssl/certs**, you can manually confirm whether the directory exists and whether the certificate file exists.
