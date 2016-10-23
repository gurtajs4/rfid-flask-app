function PeopleLookupController($location) {
    var self = this;

    self.title = "People Lookup Page";
    self.note = "Check for people by entering Person ID";
    self.lookup = lookup;
    self.cancel = cancel;

    function lookup() {
        $window.alert("server is trying to find that person...");
        var result = 7;
        $location.url("/sessions/" + result);
    }

    function cancel() {
        $location.url("/home");
    }
}

PeopleLookupController.$inject = ['$location'];
angular.module('appMain').controller('PeopleLookupController', PeopleLookupController);