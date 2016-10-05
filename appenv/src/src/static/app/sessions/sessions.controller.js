function SessionsController($scope, $location, sessionService) {
    var self = this;
    var service = sessionService;

    self.list = [];
//    self.view = view;

//    $scope.list = [];

    load();

    function load() {
        service.sessions().then(function(sessions){
//            $scope.list = sessions.data;

//            var rawSessions = result.data;
//            var sessions = [];
//            for (i = 0; i < rawSessions.length; i++) {
//                var nextSession = {
//                    sessionId: rawSessions[i]._session_id,
//                    keyId: rawSessions[i]._key_id,
//                    userId: rawSessions[i]._user_id,
//                    timestamp: rawSessions[i]._time_stamp
//                };
//                sessions.push(nextSession);
//            }
//            self.list = sessions;

            self.list = sessions;
        });
    };

//    function view(session_id) {
//        viewPath = $location.path + '/' + session_id;
//        $location.url(viewPath);
//    };
}

SessionsController.$inject = ['$scope', '$location', 'sessionService'];
angular.module('appMain').controller('SessionsController', SessionsController);