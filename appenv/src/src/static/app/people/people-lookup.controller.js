function PeopleLookupController($location, peopleService) {
    var self = this;
    var service = peopleService;

    self.title = "People Lookup Page";
    self.note = "Check for people by entering Person ID";
    self.lookup = lookup;
    self.cancel = cancel;

    function lookup() {
        var uid = service.lookup(self.queryset);
        if (uid.status != undefined) {
            $window.alert("The user " + uid + " you were looking for is registered here...");
            $location.url("/home");
        }
        else {
            $window.alert("User not registered!");
        }
        // $window.alert("server is trying to find that person...");
        // var result = 7;
        // $location.url("/sessions/" + result);
    }

    function cancel() {
        $location.url("/home");
    }
}

PeopleLookupController.$inject = ['$location', 'peopleService'];
angular.module('appMain').controller('PeopleLookupController', PeopleLookupController);