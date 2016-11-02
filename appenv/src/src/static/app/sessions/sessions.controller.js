function SessionsController(sessionService) {
    var self = this;
    var service = sessionService;

    self.list = [];

    load();

    function load() {
        service.sessions().then(function(sessions){
            self.list = sessions;
        });
    };
}

SessionsController.$inject = ['sessionService'];
angular.module('appMain').controller('SessionsController', SessionsController);