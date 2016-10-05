function SessionInfoController($routeParams, sessionService) {
    var self = this;
    var service = sessionService;

    self.sessionId = $routeParams.id;
    self.userId = 0;
    self.keyId = 0;
    self.timestamp = "";

    load();

    function load(){
        id = self.sessionId;
        service.session(id).then(function(session){
            self.userId = session.userId;
            self.keyId = session.keyId;
            self.timestamp = session.timestamp;
        });
    };
}

SessionInfoController.$inject = ['$routeParams', 'sessionService'];
angular.module('appMain').controller('SessionInfoController', SessionInfoController);