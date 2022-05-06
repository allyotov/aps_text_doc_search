# aps_text_doc_search

```logs
max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]
```

Надо в системе, в которой УСТАНОВЛЕН докер (НЕ в контейнере!) увеличить память. Сначала проверим:

```bash
more /proc/sys/vm/max_map_count
```

Если показывает 65530, значит все верно. Для убунту выполняем:

```bash
sudo sh -c 'echo "vm.max_map_count = 262144" >> /etc/sysctl.conf'
sudo sysctl -p
```
