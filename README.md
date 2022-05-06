# Сервис, реализующий поиск по текстовым документам

### Модель данных
## Пост
- `id` - уникальный для каждого поста;
- `rubrics` - массив рубрик;
- `text` - текст поста;
- `created_date` - дата создания поста.

Эндпойнты

1) Поиск по тексту поста, возвращает 20 найденных документов, упорядоченных по дате создания, в текстах которых указанный в параметре текст встречается как подстрока:

```url
http://127.0.0.1:5000/api/v1/text_docs/?search=информация&order=asc
```
Параметр order управляет тем, будет ли упорядочиваться результат по убыванию (desc) или по возрастанию (asc)

2) Удаление поста по его id:
```url
http://127.0.0.1:5000/api/v1/text_docs/1104
```
#  Порядок развёртывания сервиса
Для работы с сервисом в режиме отладки вам понадобится установить менеджер пакетов poetry. Таргеты, предназначенные для отладки вы можете посмотреть в Makefile.

Для установки контейнеров сервиса запустите:

```bash
make install
```
После этого нужно немного подождать, чтобы успел подняться контейнер в Elasticsearch. Для проверки Elasticsearch можно запустить ping и посмтреть health
```bash
make es.check
```

```bash
make es.logs
```

Когда Elasticsearch будет готов, можно создать индекс и Б.Д. командой:

```bash
make db.create
```
Далее заполнить её из *post.csv*, который нужно разместить в директории */backend_data*
```bash
make db.fill
```
Запустить бэкенд можно так:
```bash
make app.run
```
Проверить логи бэкенда:
```bash
app.logs
```
Остановить контейнеры:
```bash
make down
```
Удалить контейнеры:
```bash
make remove.images
```
Удалить директорию с данными Б.Д. и индекса:
```bash
make clean
```
---
## Возможная проблема в работе elasticsearch - нехватка памяти. Способ устранения

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
