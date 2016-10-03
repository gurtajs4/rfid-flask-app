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
            self.list = sessions.data;
        });
    };

//    function view(session_id) {
//        viewPath = $location.path + '/' + session_id;
//        $location.url(viewPath);
//    };
}

SessionsController.$inject = ['$scope', '$location', 'sessionService'];
angular.module('appMain').controller('SessionsController', SessionsController);