function KeysLookupController($location) {
    var self = this;

    self.title = "Keys lookup page"
    self.note = "Check for keys by entering Key ID number"
    self.lookup = lookup;
    self.cancel = cancel;

    function lookup() {
        $window.alert("server is trying to find that key...");
        var result = 7;
        $location.url("/sessions/" + result);
    }

    function cancel() {
        $location.url("/home");
    }
}

KeysLookupController.$inject = ['$location'];
angular.module('appMain').controller('KeysLookupController', KeysLookupController);