- download the CA certificate using this command
  ```bash
  curl --create-dirs -o $HOME/.postgresql/root.crt -O https://cockroachlabs.cloud/clusters/f75a0d30-05e2-4edb-b443-a11596fc3fab/cert
  ```

- pip3 install psycopg2-binary Flask python-decouple