function SessionsController($location, sessionService) {
    var self = this;
    var service = sessionService;

    self.list = [];
    self.view = view;

    load();

    function load() {
        service.sessions().then(function(sessions){
            self.list = sessions;
        });
    };

    function view(session_id) {
        viewPath = $location.path + '/' + session_id;
        $location.url(viewPath);
    };
}

SessionsController.$inject = ['$location', 'sessionService'];
angular.module('appMain').controller('SessionsController', SessionsController);