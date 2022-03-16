# ships_tracker
Test task (django, celery)

# Setup project
```
poetry shell
poetry install
```

# For run server 
`./manage.py runserver`

# For schedule task for updating ships and movement history
1) with schedule:
`python ships_tracker/utils/scheduler.py `
2) with celery:
`celery -A ships_tracker.ships beat`
