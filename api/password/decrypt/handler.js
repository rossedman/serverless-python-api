'use strict';

var lib = require('../../lib');

module.exports.handler = function(event, context, cb) {
  var parameterValue = lib.decrypt(event.password); // the querystring parameter

  var response = {
    data: {
      password: parameterValue
    }
  };

  return cb(null, response);
};
