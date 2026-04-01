const router = require('express').Router();
const Claim = require('../models/Claim');

router.post('/', async (req,res)=>{
  const c = await Claim.create(req.body);
  res.json(c);
});

router.get('/', async (req,res)=>{
  res.json(await Claim.find());
});

module.exports = router;