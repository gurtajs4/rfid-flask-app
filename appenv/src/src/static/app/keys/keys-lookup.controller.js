function KeysLookupController($location, keysService) {
    var self = this;
    var service = keysService;

    self.title = "Keys lookup page";
    self.note = "Check for keys by entering Key ID number";
    self.lookup = lookup;
    self.cancel = cancel;

    function lookup() {
        var kid = service.lookup(self.queryset);
        if (kid.status != undefined) {
            $window.alert("The key " + kid + " you were looking for is available...");
            $location.url("/home");
        }
        else {
            $window.alert("Key not registered!");
        }
        // $window.alert("server is trying to find that key...");
        // var result = 7;
        // $location.url("/sessions/" + result);
    }

    function cancel() {
        $location.url("/home");
    }
}

KeysLookupController.$inject = ['$location', 'keysService'];
angular.module('appMain').controller('KeysLookupController', KeysLookupController);