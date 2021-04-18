from opster import command, dispatch

@command()
def devserver(
        bind=('b', '0.0.0.0', 'Bind address'),
        port=('p', 3000, 'Port number'),
        debug=('d', True, 'Debug mode'),
        cfg=('c', None, 'Override settings file'),
        ssl=('s', False, 'Enable SSL')):
    from app import init
    from werkzeug.serving import run_simple

    app = init()
    app.debug = debug

    ssl_context = None
    if ssl:
        ssl_context = 'adhoc'
    run_simple(bind, port, app,
               use_debugger=debug,
               use_reloader=True,
               ssl_context=ssl_context)

if __name__ == '__main__':
    dispatch()