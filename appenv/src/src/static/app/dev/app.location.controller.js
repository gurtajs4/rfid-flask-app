var appBaseUrl = angular.element(document.querySelector('base')).attr('href');

function AppLocationController() {
    var self = this;
    self.label = appBaseUrl;
}

//AppLocationController.$inject = ['$scope'];
angular.module('appMain').controller('AppLocationController', AppLocationController);