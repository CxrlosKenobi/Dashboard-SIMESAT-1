# yourapp/assets/clientside.js

if (!window.dash_clientside) { window.dash_clientside = {}; }
window.dash_clientside.clientside = {
    update_timer: function (value) {
        return new Date().toUTCString();
    }
}
