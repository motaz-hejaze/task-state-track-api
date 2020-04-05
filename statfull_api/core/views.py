from .serializers import NewTaskSerializer , NewTaskEditSerializer , LinkTaskSerializer , ChangeTaskStateSerializer , ShowTaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from drf_yasg.utils import swagger_auto_schema


##########################
# Common Response status
##########################
# HTTP_200_OK
# HTTP_201_CREATED
# HTTP_202_ACCEPTED
# HTTP_400_BAD_REQUEST
# HTTP_401_UNAUTHORIZED
# HTTP_403_FORBIDDEN
# HTTP_404_NOT_FOUND
# HTTP_406_NOT_ACCEPTABLE
##########################


# Create your views here.

@swagger_auto_schema(method='post',tags=["Create New Task"] ,  request_body=NewTaskSerializer , responses={201: 'success', 400: 'errors'})
@api_view(['POST'])
def create_task(request):
    data = request.data
    title = request.data.get("title")
    description = request.data.get("description")
    new_task = Task.new.create(title=title,description=description)
    print(new_task)
    if new_task != None:
        return Response({'message':'Task Created'} , status=status.HTTP_201_CREATED )
    else:
        return Response({'message': 'Task not created'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='get',tags=["Get New Task"] , responses={201: 'success', 400: 'errors'})
@api_view(['GET'])
def get_task(request, id):
    task = Task.new.get_a_task(id)
    if task:
        if task.state == 'new':
            return Response({'task':task.title} , status=status.HTTP_302_FOUND)
        else:
            return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'message': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(method='put',tags=["Edit New Task"] ,  request_body=NewTaskEditSerializer , responses={201: 'success', 400: 'errors'})
@api_view(['PUT'])
def edit_task(request):
    data = request.data
    id = request.data.get("id")
    title = request.data.get("title")
    description = request.data.get("description")

    if id and id != None:
        task = Task.new.get_a_task(id)
        if task:
            if task.state == 'new':
                edited_task = Task.new.edit_a_task(id, title, description)
                if edited_task:
                    return Response({'message':'Task Edited Successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'Task not updated'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'message': 'Task not Found'}, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(method='post',tags=["Link Two Tasks"] ,  request_body=LinkTaskSerializer , responses={201: 'success', 400: 'errors'})
@api_view(['POST'])
def link_tasks(request):
    data = request.data
    first_id = request.data.get("first_id")
    sec_id = request.data.get("sec_id")
    task1 = Task.new.get_a_task(first_id)
    task2 = Task.new.get_a_task(sec_id)
    if task1 and task2:
        if task1.state == 'in_progress' and task2.state == 'in_progress':
            linked_task = Task.inprogress.link_two_tasks(first_id,sec_id)
            if linked_task:
                return Response({'message': 'Tasks linked Successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Tasks not linked'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'message': 'One or Both of Tasks not Found'}, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(method='get',tags=["Show Linked Tasks"] , responses={201: 'success', 400: 'errors'})
@api_view(['GET'])
def show_linked_task(request , id):
    task = Task.inprogress.find_related_task(id)
    print(task)
    if task:
        if task.state == 'in_progress':
            linked_id = task.linked_id
            return Response({'linked_id': linked_id}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'message': 'Task not Found'}, status=status.HTTP_404_NOT_FOUND)



@swagger_auto_schema(method='post',tags=["Change Task Status"] ,  request_body=ChangeTaskStateSerializer , responses={201: 'success', 400: 'errors'})
@api_view(['POST'])
def change_task_state(request):
    data = request.data
    id = request.data.get("id")
    state = request.data.get("state")
    task = Task.objects.get(id=id)
    if task:
        task.state = state
        task.save()
        return Response({'message':'Task status changed'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Task not Found'}, status=status.HTTP_404_NOT_FOUND)







