function SessionService($http) {

    var service = {
        sessions: sessions,
        session: session,
    };

    return service;

    function sessions() {
        return $http.get('/api/sessions');
//        return $http.get('/api/sessions').then(function(response){
//            return response.data;
//        });
    };

    function session(session_id) {
        return $http.get('/api/sessions/', { params: {session_id: session_id} }).then(function(response){
            return response.data;
        });
    };
}

SessionService.$inject = ['$http'];
angular.module('appMain').service('sessionService', SessionService);