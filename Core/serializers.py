from .models import Customer,Technician,ServiceRequest,Bill,User,TechnicianApplication
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    
class TechnicianUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class TechnicianSerializer(serializers.ModelSerializer):

    user = TechnicianUserSerializer(
        read_only=True
    )

    user_id = serializers.PrimaryKeyRelatedField(
    queryset=User.objects.all(),
    source='user',
    write_only=True
    )

    class Meta:
        model = Technician
        fields = '__all__'

class ServiceRequestSerializer(serializers.ModelSerializer):

    customer_name = serializers.CharField(
        source="customer.user.username",
        read_only=True
    )

    technician_name = serializers.SerializerMethodField()

    class Meta:
        model = ServiceRequest
        fields = "__all__"

        read_only_fields = (
            "customer",
            "status",
            "created_at",
        )

    def get_technician_name(self, obj):

        if obj.assigned_technician:

            return obj.assigned_technician.user.username

        return None
    
class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class TechnicianApplicationSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = TechnicianApplication

        fields = '__all__'