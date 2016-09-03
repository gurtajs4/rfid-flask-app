function SessionsController($location, sessionService) {
    self = this;
    service = sessionService;
    _session_list = [];

    self.get = get;
    self.view = view;

    load();

    function load() {
        service.sessions().then(function(sessions){
            _session_list = sessions;
        });
    };

    function get() {
        return _session_list;
    };

    function view(session_id) {
        viewPath = $location.path + '/' + session_id;
        $location.url(viewPath);
    };
}

SessionsController.$inject = ['$location', 'sessionService'];
angular.module('appMain').controller('SessionsController', SessionsController);