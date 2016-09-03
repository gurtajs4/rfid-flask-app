function NavController() {
    var self = this;

    self.tab = 0;
    self.setActive = setActive;
    self.isActive = isActive;

    function setActive(tabId) {
        self.tab = tabId;
    };

    function isActive(tabId) {
        return self.tab === tabId;
    };
}

angular.module('mainApp').controller('NavController', NavController);