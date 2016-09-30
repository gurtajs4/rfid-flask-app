function SessionService($http) {

    var service = {
        sessions: sessions,
        getSession: getSession,
    };

    return service;

    function sessions() {
        return $http.get('/api/sessions');
    };

    function getSession(session_id) {
        return $http.get('/api/sessions/', { params: {session_id: session_id} }).then(function(response){
            return {
                session_id: response.data.session_id,
                key_id: response.data.key_id,
                user_id: response.data.user_id,
                time_stamp: response.data.time_stamp
            };
        });
    };
}

SessionService.$inject = ['$http'];
angular.module('appMain').service('sessionService', SessionService);