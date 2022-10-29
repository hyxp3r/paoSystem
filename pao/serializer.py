from dataclasses import field
from rest_framework import serializers




class TrackerSerializer(serializers.Serializer):

    createdTime = serializers.DateTimeField()
    nobody = serializers.IntegerField(default = 0)
    soglDecan = serializers.IntegerField( default = 0)
    decanFinans = serializers.IntegerField(default = 0)
    bezRectorVisa = serializers.IntegerField(default = 0)
    paoCan = serializers.IntegerField(default = 0)

    naSoglDecan = serializers.IntegerField(default = 0)
    fbp = serializers.IntegerField(default = 0)
    fgs = serializers.IntegerField(default = 0)
    fcep = serializers.IntegerField(default = 0)
    uf = serializers.IntegerField(default = 0)

    remake = serializers.IntegerField(default = 0)
    remakeDecan = serializers.IntegerField(default = 0)
    remakeAup = serializers.IntegerField(default = 0)
    remakeRector = serializers.IntegerField(default = 0)

    naSoglAdv = serializers.IntegerField(default = 0)
    naSoglProdject = serializers.IntegerField(default = 0)
    naSoglYung = serializers.IntegerField(default = 0)
    naSoglLearn = serializers.IntegerField(default = 0)
    naSoglHr = serializers.IntegerField( default = 0)
    naSoglScience = serializers.IntegerField(default = 0)
    naSoglredact = serializers.IntegerField(default = 0)