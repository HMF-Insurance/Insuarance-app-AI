const router = require('express').Router();

router.post('/', async (req,res)=>{
  res.json({message:'accident received', data:req.body});
});

module.exports = router;