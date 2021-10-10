# Test_Sentinel

### Prepare project virtual environment:
```bash
# Create project directory
mkdir ~/Sentinel && cd ~/Sentinel
git clone git@github.com:bebrainee/nfc.git sentinel
python3 -m venv venv
source venv/bin/activate && cd sentinel
pip install -r  requirements.txt
```

### Adding users to security.yml
```text
You need to send a message like \notify to @codex_bot
and get the URL and then put it in security.yml like:
```
```yaml
users:
  - name: "User_name"
    tg: "https://notify.bot.codex.so/u/A00P1A4Y"
```

### Run Project
```bash
cd ~/Sentinel
source venv/bin/activate && cd sentinel
python run_server.py
```

### cURL example
```text
For work with this program you need to send cURL request with json data:
curl -XPOST -H "Content-type: application/json" -d '{"message": "your message"}' 'http://localhost:5000/'
```