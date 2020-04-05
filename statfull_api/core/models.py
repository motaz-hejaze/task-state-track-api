from django.db import models

# Create your models here.

class NewTaskManager(models.Manager):
    created = None
    task_id = None
    task = None

    def create(self, **kwargs):
        kwargs.update({'state': 'new'})
        self.created = super(NewTaskManager, self).create(**kwargs)
        self.task_id = self.created.id
        return self.created

    def get_a_task(self,id):
        self.task = Task.objects.get(id=id)
        self.task_id = self.task.id
        return self.task

    def edit_a_task(self, id ,title,description):
        self.task = Task.objects.get(id=self.task_id)
        self.task.title = title
        self.task.description = description
        self.task.save()
        return self.task




class InProgressTaskManager(models.Manager):
    task1 = None
    task2 = None

    def link_two_tasks(self , task_id_1 , task_id_2):
        self.task1 = Task.objects.get(id=task_id_1)
        self.task2 = Task.objects.get(id=task_id_2)
        self.task1.linked_id = task_id_2
        self.task1.save()
        return True


    def find_related_task(self , id):
        self.task1 = Task.objects.get(id=id)
        return self.task1


class DoneTaskManager(models.Manager):
    pass



class Task(models.Model):
    STATE = (
        ('new','new'),
        ('in_progress', 'in_progress'),
        ('done','done')
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    state = models.CharField(choices=STATE,default='new',max_length=20)
    linked_id = models.IntegerField(null=True)

    objects = models.Manager()

    new = NewTaskManager()
    inprogress = InProgressTaskManager()
    done = DoneTaskManager()

    def __str__(self):
        return "{}".format(self.title)







