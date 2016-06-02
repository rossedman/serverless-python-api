'use strict';

var lib = require('../../lib');

module.exports.handler = function(event, context, cb) {
  var parameterValue = lib.encrypt(event.password); // the querystring parameter

  var response = {
    data: {
      password: parameterValue
    }
  };

  return cb(null, response);
};
