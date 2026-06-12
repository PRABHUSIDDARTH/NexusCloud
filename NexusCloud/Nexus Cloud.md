#### `config.py` — Centralised Configuration

Instead of hardcoding values like database URLs, secret keys, or token expiry times anywhere in the code, we created one single place where all configuration lives — `settings`.

Every file in the project imports from `settings` instead of having its own hardcoded values. This means if you want to change the token expiry from 30 minutes to 60 minutes, you change it in one place — the `.env` file — and the entire app picks it up. No hunting through files.

This pattern is called **12-Factor App configuration** — it's the industry standard for production software.

#### `security.py` — Authentication Foundation

Two things happen here:

**Password Hashing** — When a user registers, we never store their raw password. We run it through `bcrypt` which is a one-way hashing algorithm. Even if your database gets leaked, the attacker can't reverse the hash back to the original password.

**JWT Tokens** — When a user logs in successfully, we give them two tokens:

- **Access Token** — short-lived (30 mins). Used for every API request.
- **Refresh Token** — long-lived (7 days). Used only to get a new access token when the old one expires.

This is the standard auth pattern for stateless APIs. The server doesn't store sessions — it just verifies the token signature on every request.

#### `vault.py` — Credential Encryption

This is specific to NexusCloud and critical. When a user connects their AWS or GCP account, they give us their IAM keys. We cannot store those as plain text in the database — if the DB is ever breached, every user's cloud account is compromised.

So before saving any credential to PostgreSQL, we encrypt it using **Fernet symmetric encryption** (AES-128 under the hood). The encryption key lives in `.env`, never in the database. When we need to use the credential to make an SDK call, we decrypt it in memory, use it, and discard it — it's never logged or stored in decrypted form.