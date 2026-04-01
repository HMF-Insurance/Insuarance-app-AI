const mongoose = require('mongoose');
module.exports = mongoose.model('Claim', new mongoose.Schema({
  userId: String,
  amount: Number,
  status: { type: String, default: 'pending' }
}));