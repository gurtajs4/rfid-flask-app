function KeysLookupController($location, keysService) {
    var self = this;
    var service = keysService;

    self.title = "Keys lookup page";
    self.note = "Check for keys by entering Key ID number";
    self.lookup = lookup;
    self.cancel = cancel;

    function lookup() {
        var session = service.lookup(self.queryset);
        if (session != undefined) {
            $location.url("/sessions/" + session.id);
        }
        else {
            console.log('Request didn\'t came through...');
            $window.alert("Key not registered!");
        }
    }

    function cancel() {
        $location.url("/home");
    }
}

KeysLookupController.$inject = ['$location', 'keysService'];
angular.module('appMain').controller('KeysLookupController', KeysLookupController);