function PeopleLookupController($location, peopleService) {
    var self = this;
    var service = peopleService;

    self.title = "People Lookup Page";
    self.note = "Check for people by entering Person ID";
    self.lookup = lookup;
    self.cancel = cancel;

    function lookup() {
        var session = service.lookup(self.queryset);
        if (session != undefined) {
            $location.url("/sessions/" + session.id);
        }
        else {
            console.log('Request didn\'t came through...');
            $window.alert("User not registered!");
        }
    }

    function cancel() {
        $location.url("/home");
    }
}

PeopleLookupController.$inject = ['$location', 'peopleService'];
angular.module('appMain').controller('PeopleLookupController', PeopleLookupController);