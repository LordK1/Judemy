import uuid
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from joins.forms import EmailForm, JoinForm
from joins.models import Join
from django.conf import settings


def get_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip


def get_ref_id():
    ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
    try:
        id_exsits = Join.objects.get(ref_id=ref_id)
        # we have to do something
        get_ref_id()
    except:
        return ref_id


def share(request, ref_id):
    try:
        join_obj = Join.objects.get(ref_id=ref_id)
        friends_referred = Join.objects.filter(friends=join_obj)
        count = join_obj.referral.all().count()
        ref_url = settings.SHARE_URL % join_obj.ref_id
        template = 'share.html'
        context = {"ref_id": join_obj.ref_id,
                   "friends_count": count,
                   "friends_referred": friends_referred,
                   "ref_url": ref_url}
        return render(request, template, context)

    except:
        raise Http404


def home(request):
    message = ""
    try:
        join_id = request.session['join_id']
        obj = Join.objects.get(id=join_id)
        print("The Join is %s " % obj.email)
    except:
        obj = None

    form = JoinForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        email = form.cleaned_data['email']
        new_join_old, created = Join.objects.get_or_create(email=email)
        if created:
            new_join_old.ref_id = get_ref_id()
            # add our friend who referred us to our join model or a related
            if not obj is None:
                new_join_old.friends = obj

            new_join_old.ip_address = get_ip(request)
            new_join_old.save()
            # print all friends that joined as a result owner (main sharer) email .
            # print Join.objects.filter(friends=obj).count()
            # print obj.referral.all().count()

            # Redirect here
        return HttpResponseRedirect("/%s" % new_join_old.ref_id)

    context = {"form": form, "message": message}
    template = "home.html"
    return render(request, template, context)
