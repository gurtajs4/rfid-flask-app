function NavController($scope) {

    $scope.tab = 0;
    $scope.setActive = setActive;
    $scope.isActive = isActive;

    function setActive(tabId) {
        $scope.tab = tabId;
    };

    function isActive(tabId) {
        return $scope.tab === tabId;
    };
}

NavController.$inject = ['$scope'];
angular.module('appMain').controller('NavController', NavController);