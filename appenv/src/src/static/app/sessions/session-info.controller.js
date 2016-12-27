function SessionInfoController($routeParams, sessionService) {
    var self = this;
    var service = sessionService;

    self.sessionId = $routeParams.id;
    self.userId = 0;
    self.keyId = 0;
    self.timestamp = "";

    load();

    function load(){
        var id = self.sessionId;
        service.session(id).then(function(response){
            var session = JSON.parse(response.data)
            self.userId = session['user_id'];
            self.keyId = session['key_id'];
            self.timestamp = session['timestamp'];
        });
    }
}

SessionInfoController.$inject = ['$routeParams', 'sessionService'];
angular.module('appMain').controller('SessionInfoController', SessionInfoController);