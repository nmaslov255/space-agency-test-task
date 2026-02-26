## Тестовое задание, лендинг космического агенства со слайдером и админкой

### Deploy
- docker compose up --build
- docker compose exec web python manage.py migrate 
- docker compose exec web python manage.py collectstatic
- docker compose exec web python manage.py createsuperuser

В http://localhost:8000 выводятся загруженные слайды (пока черновик без верстки)
В http://localhost:8000/admin/ в разделе слайдера можно загрузить картинки для слайдов & изменить порядок перетаскиванием