from rest_framework import serializers

from api.companies.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def validate(self, obj):
        print(obj)

        return obj