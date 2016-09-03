function SessionService($http) {
    service = {
        sessions: Sessions,
        session: Session
    }

    return service;

    function Sessions() {
        return $http.get('/api/sessions').then(function(response){
            return response.data;
        });
    };

    function Session(session_id) {
        return $http.get('/api/sessions', session_id).then(function(response){
            return response.data;
        });
    };
}

SessionService.$inject = ['$http'];
angular.module('appMain').service('sessionService', SessionService);