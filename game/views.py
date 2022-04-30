from django.shortcuts import render

from django.http import HttpResponse


from django.shortcuts import render

# Create your views here.
import requests
import re
from django.shortcuts import render, redirect

 
def index(request):
  return render(request, 'board/board.html', {})

  # return HttpResponse("Hello Geeks")'

# Bc4; Kg3; e3(pawn)
# towards. Castling kingside (with the rook that begins on the “h” file), is written as “0-0”. Castling queenside (with the rook that begins on the “a” file) is notated with “0-0-0”.
# https://www.ichess.net/blog/chess-notation/