import web

urls = (
    '/', 'Index',
    '/foo', 'Foo',
	'/hello', 'Index'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class Index(object):
    def GET(self):
        #greeting = "We demand Jenny McNeal"
	form = web.input(name = "Nobody", greet = "Howdy")
	greeting = "%s, %s" % (form.greet, form.name)
        return render.index(greeting = greeting)


class Foo(object):
    def GET(self):
        name = "Jenny McNeal"
        return render.foo(foobar = name)

if __name__ == "__main__":
    app.run()
