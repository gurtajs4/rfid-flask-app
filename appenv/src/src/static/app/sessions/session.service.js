function SessionService($http) {

    var service = {
        sessions: sessions,
        session: session,
    };

    return service;

    function sessions() {
        return $http.get('/api/sessions').then(function(response) {
            var rawSessions = response.data;
            var sessions = [];
            for (i = 0; i < rawSessions.length; i++) {
                var nextSession = {
                    sessionId: rawSessions[i]._session_id,
                    keyId: rawSessions[i]._key_id,
                    userId: rawSessions[i]._user_id,
                    timestamp: rawSessions[i]._time_stamp
                };
                sessions.push(nextSession);
            }
            return sessions;
        });
//        return $http.get('/api/sessions');
//        return $http.get('/api/sessions').then(function(response){
//            return response.data;
//        });
    };

    function session(id) {
        return $http.get('/api/sessions/', id).then(function(response) {
            var singleSession = {
                sessionId: response.data[i]._session_id,
                keyId: response.data[i]._key_id,
                userId: response.data[i]._user_id,
                timestamp: response.data[i]._time_stamp
            };
            return singleSession;
        });
//        return $http.get('/api/sessions/', { params: {session_id: id} }).then(function(response){
//            var session = {
//                sessionId: response.data[i]._session_id,
//                keyId: response.data[i]._key_id,
//                userId: response.data[i]._user_id,
//                timestamp: response.data[i]._time_stamp
//            };
//            return session;
////            return response.data;
//        });
    };
}

SessionService.$inject = ['$http'];
angular.module('appMain').service('sessionService', SessionService);