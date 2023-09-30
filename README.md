# Тестовое задание на позицию разработчика в тестировании в компании Тензор.

`pages` содержит описание классов страниц. Класс `BasePage` содержит базовую функциональность для всех страниц, остальные классы страниц наследуются от `BasePage`.

```
- SbisHomePage - домашняя страница sbis.ru
- SbisContactsPage - раздел Контакты sbis.ru
- SbisDownloadPage - раздел Скачать sbis.ru
- TensorHomePage - домашняя страница tensor.ru
- TensorAboutPage - раздел О компании tensor.ru
```

`tests` содержит сценарии тестирования.

#### Запустить все тесты можно следующей командой: 
```sh
python -m pytest --capture=no tests
```
