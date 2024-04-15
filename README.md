<--- Chat History --->

https://community.openai.com/t/how-do-you-maintain-historical-context-in-repeat-api-calls/34395/27
https://blinkdata.com/continuing-a-conversation-with-a-chatbot-using-gpt/

<-------------------->
scram password encryption for localhost
https://stackoverflow.com/questions/76781095/how-do-i-fix-scram-authentication-errors-when-connecting-dbeaver-to-a-docker-pos

Postgres start db and login

sudo service postgresql start
sudo service postgresql stop
sudo -u postgres psql
alter user postgres with password 'postgres';

allowing wsl2
sudo ufw allow 5432/tcp
sudo service postgresql restart

https://medium.com/@magda7817/better-together-openai-embeddings-api-with-postgresql-pgvector-extension-7a34645bdac2

https://blog.gopenai.com/rag-with-pg-vector-with-sql-alchemy-d08d96bfa293

installing dbeaver locally fixed issues when running from wsl and dbeaver

<-------------------->
pip install langchain

for error with punkt

python -m nltk.downloader punkt

<-------------------->

python main.py --name "me" --question "blah"

<--------------------->
notepad wsl alias
alias npp="/mnt/c/Program\ Files/Notepad++/Notepad++.exe"
<--------------------->
src/util includes a property generator taken from a txt extract of pdf