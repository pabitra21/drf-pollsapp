from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from polls.api import TrackSerializer
from polls.models import Question,Track,Answer,Choice

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class TrackView(APIView):
    def post(self, request):
        print(request.data)
        serializer = TrackSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request,format=None):
        track = Track.objects.all()
        print(track)
        serializer = TrackSerializer(track, many=True)
        return Response(serializer.data)
    #
    # def delete(self, request, pk, format=None):
    #     track = Track.objects.filter(id=pk)
    #     track.delete()
    #     return Response("Deleted")



@api_view(['GET'])
def fetch_questions_list(request):
    input_name = (request.GET.get('name'))
    print(input_name)
    question_list = Question.objects.filter(tracks__name=input_name).values('question_text')
    print(question_list)
    return Response(question_list)

@api_view(['GET'])
def total_count(request):
    q_id = request.GET.get('q_id')
    print(q_id)
    try:
        correct_answer = Choice.objects.filter(question_id=q_id).order_by('-votes')[0]
        count_of_id = Answer.objects.filter(questions_id=q_id).count()
        if not count_of_id:
            Answer.objects.create(questions_id=q_id, correct_answer=correct_answer)
        else:
            Answer.objects.filter(questions_id=q_id).update(correct_answer=str(correct_answer))

        total_count_for_qid=Choice.objects.filter(question_id=q_id).count()

        correct_answers_pairs=Answer.objects.filter(questions_id=q_id).values('questions_id','correct_answer')

        total_correct_count=Choice.objects.filter(question_id=correct_answers_pairs[0]['questions_id'],choice_text=correct_answers_pairs[0]['correct_answer']).count()

        total_count_wrong=total_count_for_qid-int(total_correct_count)

        return Response({"total_correct_count":total_correct_count,"total_wrong_count":total_count_wrong})
    except:
        return Response("Question ID does not exist")
