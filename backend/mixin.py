
class GetMixin:
    def get_success_url(self,url):
        return url

    def get_redirect_url(self,url):
        return url

    def get_object_all(self,model):
        return model.objects.all()