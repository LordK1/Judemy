from joins.models import Join

__author__ = 'k1'


class ReferMiddleware():
    def process_request(self, request):
        ref_id = request.GET.get('ref')
        try:
            join_obj = Join.objects.get(ref_id=ref_id)
        except:
            join_obj = None
        if join_obj:
            request.session['join_id'] = join_obj.id
