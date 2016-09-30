function SessionsController(sessionService) {
    var self = this;
    var service = sessionService;

    self.list = [];

    activate();

    function activate() {
        service.sessions().then(function(result){
            self.list = result.data;
        });
    };
}

SessionsController.$inject = ['sessionService'];
angular.module('appMain').controller('SessionsController', SessionsController);