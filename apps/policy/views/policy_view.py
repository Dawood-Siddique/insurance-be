from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from apps.policy.models import PolicyModel, InsuranceCompanyModel, ClientModel, AgentModel

class PolicyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            data = request.data
            
            # Assuming the frontend sends the IDs for the foreign key relationships
            insurance_company_id = data.get('insurance_company_id')
            client_id = data.get('client_id')
            agent_id = data.get('agent_id')

            # Fetching the related model instances
            insurance_company = InsuranceCompanyModel.objects.get(id=insurance_company_id)
            client = ClientModel.objects.get(id=client_id)
            agent = AgentModel.objects.get(id=agent_id)

            # Creating the PolicyModel instance
            policy = PolicyModel.objects.create(
                issue_date=data.get('issue_date'),
                insurance_company=insurance_company,
                policy_number=data.get('policy_number'),
                client=client,
                car_model=data.get('car_model'),
                engine_type=data.get('engine_type'),
                agent=agent,
                gross_price=data.get('gross_price'),
                co_rate=data.get('co_rate'),
                client_price=data.get('client_price'),
                payment_method=data.get('payment_method'),
                payment_status=data.get('payment_status'),
                remarks=data.get('remarks'),
                reference_number=data.get('reference_number')
            )
            
            return JsonResponse({'message': 'Policy created successfully!', 'policy_id': policy.id}, status=201)

        except InsuranceCompanyModel.DoesNotExist:
            return JsonResponse({'error': 'Insurance company not found.'}, status=400)
        except ClientModel.DoesNotExist:
            return JsonResponse({'error': 'Client not found.'}, status=400)
        except AgentModel.DoesNotExist:
            return JsonResponse({'error': 'Agent not found.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

        