const voting=artifacts.require('voting');

module.exports=function(deployer) {
    deployer.deploy(voting); //deployer is deploying the artifacts.
}