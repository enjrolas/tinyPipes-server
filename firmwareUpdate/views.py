from django.shortcuts import render_to_response

def firmware(request):
    return render_to_response("firmwareUpdate/firmware.html")
