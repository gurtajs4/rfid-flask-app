function SessionsController($scope, $location, sessionService) {
    var service = sessionService;

    $scope.list = [];
//    self.view = view;

    load();

    function load() {
        service.sessions().then(function(sessions){
            $scope.list = sessions;
        });
    };

//    function view(session_id) {
//        viewPath = $location.path + '/' + session_id;
//        $location.url(viewPath);
//    };
}

SessionsController.$inject = ['$scope', '$location', 'sessionService'];
angular.module('appMain').controller('SessionsController', SessionsController);