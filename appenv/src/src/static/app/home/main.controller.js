function MainController() {
    var self = this;

    self.tab = 0;
    self.message = "At least AngularJS is working in main controller...";
}

angular.module('appMain').controller('MainController', MainController);