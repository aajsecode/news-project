from .models import Page


class ViewCounterMiddleWare:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print("View Counter Middleware")
        print(request.path)
        page = Page.objects.get_or_create(url=request.path, views=0)
        page[0].views = page[0].views + 1
        page[0].save()
        print(page[0].views)

        return response
