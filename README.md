trying to understand nft. they're cool. not too cool though 


```
brownie run scripts/advancedCollectible/deploy_and_create.py --network rinkeby 
```
wait ~2 minuts


upload ./img (create one) images.png to IPFS
```
brownie run scripts/advancedCollectible/create_metadata.py --network rinkeby 
```

set token URI to be seen in marketplaces
```
brownie run scripts/advancedCollectible/set_tokenuri.py  --network rinkeby
```
