function SessionInfoController($routeParams, sessionService) {
    var self = this;
    var service = sessionService;

    self.sessionId = $routeParams.id;
    self.userId = 0;
    self.keyId = 0;
    self.timestamp = "";

    function load(){
        id = self.sessionId;
        console.log("Session ID is " + id);
        service.session(id).then(function(session){
            self.userId = session.user_id;
            self.keyId = session.key_id;
            self.timestamp = session.time_stamp;
            console.log("Session user ID is " + self.userId);
        });
    };

    load();
}

SessionInfoController.$inject = ['$routeParams', 'sessionService'];
angular.module('appMain').controller('SessionInfoController', SessionInfoController);