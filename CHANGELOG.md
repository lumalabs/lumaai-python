# Changelog

## 1.5.0 (2025-02-22)

Full Changelog: [v1.4.1...v1.5.0](https://github.com/lumalabs/lumaai-python/compare/v1.4.1...v1.5.0)

### Features

* **api:** api update ([#111](https://github.com/lumalabs/lumaai-python/issues/111)) ([4db81fc](https://github.com/lumalabs/lumaai-python/commit/4db81fc9a3a4c4440e509e601e618c808de8145f))
* **client:** allow passing `NotGiven` for body ([#109](https://github.com/lumalabs/lumaai-python/issues/109)) ([75d1543](https://github.com/lumalabs/lumaai-python/commit/75d15435597671ccf955f685428b9873c26bae9d))


### Bug Fixes

* **client:** mark some request bodies as optional ([75d1543](https://github.com/lumalabs/lumaai-python/commit/75d15435597671ccf955f685428b9873c26bae9d))

## 1.4.1 (2025-02-14)

Full Changelog: [v1.4.0...v1.4.1](https://github.com/lumalabs/lumaai-python/compare/v1.4.0...v1.4.1)

### Bug Fixes

* asyncify on non-asyncio runtimes ([#106](https://github.com/lumalabs/lumaai-python/issues/106)) ([709fa16](https://github.com/lumalabs/lumaai-python/commit/709fa16f75e180f6e5e6e7b293411bbd05018046))


### Chores

* **internal:** update client tests ([#104](https://github.com/lumalabs/lumaai-python/issues/104)) ([729ec4c](https://github.com/lumalabs/lumaai-python/commit/729ec4c52a5b4d2dd4e8a99af7b28e9cd2c7de6f))

## 1.4.0 (2025-02-07)

Full Changelog: [v1.3.0...v1.4.0](https://github.com/lumalabs/lumaai-python/compare/v1.3.0...v1.4.0)

### Features

* **client:** send `X-Stainless-Read-Timeout` header ([#100](https://github.com/lumalabs/lumaai-python/issues/100)) ([7480f79](https://github.com/lumalabs/lumaai-python/commit/7480f79ca503c4ee5005eec52db090c29cd61547))


### Chores

* **internal:** bummp ruff dependency ([#98](https://github.com/lumalabs/lumaai-python/issues/98)) ([41e619b](https://github.com/lumalabs/lumaai-python/commit/41e619b49f434efe1ab2ab1043d63ccf4e304bc7))
* **internal:** change default timeout to an int ([#97](https://github.com/lumalabs/lumaai-python/issues/97)) ([5fe41dc](https://github.com/lumalabs/lumaai-python/commit/5fe41dc009c55c3ae8d19317c7ab85fcce26f8e0))
* **internal:** fix type traversing dictionary params ([#101](https://github.com/lumalabs/lumaai-python/issues/101)) ([941c012](https://github.com/lumalabs/lumaai-python/commit/941c0125bb9d081ee3491d5b010ec0aa93f65cc7))
* **internal:** minor type handling changes ([#102](https://github.com/lumalabs/lumaai-python/issues/102)) ([2913923](https://github.com/lumalabs/lumaai-python/commit/2913923d103c17f1e117bf96c35a940cafd43f8d))

## 1.3.0 (2025-01-27)

Full Changelog: [v1.2.3...v1.3.0](https://github.com/lumalabs/lumaai-python/compare/v1.2.3...v1.3.0)

### Features

* **api:** api update ([#94](https://github.com/lumalabs/lumaai-python/issues/94)) ([8faa53d](https://github.com/lumalabs/lumaai-python/commit/8faa53dfdb2b7e6899fa2c08dd5a3bf7f15160be))

## 1.2.3 (2025-01-25)

Full Changelog: [v1.2.2...v1.2.3](https://github.com/lumalabs/lumaai-python/compare/v1.2.2...v1.2.3)

### Bug Fixes

* **client:** only call .close() when needed ([#86](https://github.com/lumalabs/lumaai-python/issues/86)) ([edfe052](https://github.com/lumalabs/lumaai-python/commit/edfe052f365e25084dc5fc3fcd6536e8ca7caad8))
* correctly handle deserialising `cls` fields ([#88](https://github.com/lumalabs/lumaai-python/issues/88)) ([05474de](https://github.com/lumalabs/lumaai-python/commit/05474de956b6fbf237a5024fe1bf52c43619ab49))


### Chores

* add missing isclass check ([#84](https://github.com/lumalabs/lumaai-python/issues/84)) ([0f25a20](https://github.com/lumalabs/lumaai-python/commit/0f25a2007de69c2c86fdf6ce3cd354a68371d06f))
* **internal:** bump httpx dependency ([#85](https://github.com/lumalabs/lumaai-python/issues/85)) ([7fc347f](https://github.com/lumalabs/lumaai-python/commit/7fc347ff9d25901b1066feeddcf7992db392486d))
* **internal:** codegen related update ([#81](https://github.com/lumalabs/lumaai-python/issues/81)) ([4b141ed](https://github.com/lumalabs/lumaai-python/commit/4b141ed4e9dc448a5f5a4365d90d251ecd3f4534))
* **internal:** codegen related update ([#83](https://github.com/lumalabs/lumaai-python/issues/83)) ([f2eb603](https://github.com/lumalabs/lumaai-python/commit/f2eb603e6f936ee987d1dcdcee7126d0fdb16111))
* **internal:** codegen related update ([#87](https://github.com/lumalabs/lumaai-python/issues/87)) ([e8d60ba](https://github.com/lumalabs/lumaai-python/commit/e8d60ba7d411d640610462fc792612e9ecc22365))
* **internal:** codegen related update ([#89](https://github.com/lumalabs/lumaai-python/issues/89)) ([6bf0844](https://github.com/lumalabs/lumaai-python/commit/6bf0844b8601e49697e7ac0552333e1a271a4be3))
* **internal:** codegen related update ([#90](https://github.com/lumalabs/lumaai-python/issues/90)) ([1b4f8a8](https://github.com/lumalabs/lumaai-python/commit/1b4f8a88c251437472e41a4ed44c827ceb5cbcf8))
* **internal:** codegen related update ([#92](https://github.com/lumalabs/lumaai-python/issues/92)) ([9aca177](https://github.com/lumalabs/lumaai-python/commit/9aca177ee2028c96b47ec79c660ff6c1de335470))
* **internal:** minor style changes ([#91](https://github.com/lumalabs/lumaai-python/issues/91)) ([afb1e46](https://github.com/lumalabs/lumaai-python/commit/afb1e468f2f65ed5a8ab6e9ba2654a801ac813a4))

## 1.2.2 (2024-12-17)

Full Changelog: [v1.2.1...v1.2.2](https://github.com/lumalabs/lumaai-python/compare/v1.2.1...v1.2.2)

### Chores

* **internal:** add support for TypeAliasType ([#75](https://github.com/lumalabs/lumaai-python/issues/75)) ([487ea05](https://github.com/lumalabs/lumaai-python/commit/487ea05a5a5a1e25d311049b58c43e0b781fcb11))
* **internal:** bump pyright ([#74](https://github.com/lumalabs/lumaai-python/issues/74)) ([684e61b](https://github.com/lumalabs/lumaai-python/commit/684e61b45dd704c13b38585a307a1fbc39796fe5))
* **internal:** codegen related update ([#72](https://github.com/lumalabs/lumaai-python/issues/72)) ([2b28fc6](https://github.com/lumalabs/lumaai-python/commit/2b28fc615f654f7b87efc24f712390be53775141))
* **internal:** codegen related update ([#76](https://github.com/lumalabs/lumaai-python/issues/76)) ([d16f720](https://github.com/lumalabs/lumaai-python/commit/d16f720b4c14d5de970808840e1621924a7bd1fa))
* **internal:** codegen related update ([#77](https://github.com/lumalabs/lumaai-python/issues/77)) ([9bf4a43](https://github.com/lumalabs/lumaai-python/commit/9bf4a435ac0be28c6db5fb2950ff650e1584332a))
* **internal:** updated imports ([#78](https://github.com/lumalabs/lumaai-python/issues/78)) ([3f247e8](https://github.com/lumalabs/lumaai-python/commit/3f247e8c1f1be4927bbc85d51f12de6ab7308496))


### Documentation

* **readme:** example snippet for client context manager ([#79](https://github.com/lumalabs/lumaai-python/issues/79)) ([ddf9360](https://github.com/lumalabs/lumaai-python/commit/ddf9360a133c06f5ff1271cea46ec202c2b989cb))

## 1.2.1 (2024-12-04)

Full Changelog: [v1.2.0...v1.2.1](https://github.com/lumalabs/lumaai-python/compare/v1.2.0...v1.2.1)

### Chores

* **internal:** bump pyright ([#67](https://github.com/lumalabs/lumaai-python/issues/67)) ([a31f5ad](https://github.com/lumalabs/lumaai-python/commit/a31f5ad57c6c44f794c68b7eb946a35a8195961d))
* make the `Omit` type public ([#69](https://github.com/lumalabs/lumaai-python/issues/69)) ([59ff5b0](https://github.com/lumalabs/lumaai-python/commit/59ff5b0d9d6aef5a8f79034f86454f498803ef6c))

## 1.2.0 (2024-12-02)

Full Changelog: [v1.1.2...v1.2.0](https://github.com/lumalabs/lumaai-python/compare/v1.1.2...v1.2.0)

### Features

* **api:** api update ([#60](https://github.com/lumalabs/lumaai-python/issues/60)) ([fab600d](https://github.com/lumalabs/lumaai-python/commit/fab600d43fbacd8d1bdeef6b1a657fcbb5ffed82))

## 1.1.2 (2024-12-01)

Full Changelog: [v1.1.1...v1.1.2](https://github.com/lumalabs/lumaai-python/compare/v1.1.1...v1.1.2)

### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([#57](https://github.com/lumalabs/lumaai-python/issues/57)) ([0665416](https://github.com/lumalabs/lumaai-python/commit/06654167cd1dfcaf6f759ef10a2a4806f207f2bb))

## 1.1.1 (2024-11-28)

Full Changelog: [v1.1.0...v1.1.1](https://github.com/lumalabs/lumaai-python/compare/v1.1.0...v1.1.1)

### Chores

* **internal:** codegen related update ([#54](https://github.com/lumalabs/lumaai-python/issues/54)) ([e799eff](https://github.com/lumalabs/lumaai-python/commit/e799efff8b54359b6f065c704a283f336037c0b2))
* **internal:** exclude mypy from running on tests ([#55](https://github.com/lumalabs/lumaai-python/issues/55)) ([1f82733](https://github.com/lumalabs/lumaai-python/commit/1f827331631f05ebefabf372398536a75291b658))
* **internal:** fix compat model_dump method when warnings are passed ([#52](https://github.com/lumalabs/lumaai-python/issues/52)) ([38a854e](https://github.com/lumalabs/lumaai-python/commit/38a854ecee6fcf8373d0c024242b6949e5fb11b4))
* rebuild project due to codegen change ([#47](https://github.com/lumalabs/lumaai-python/issues/47)) ([e59029a](https://github.com/lumalabs/lumaai-python/commit/e59029af7a089ae322f230365309b76579a4e336))
* rebuild project due to codegen change ([#49](https://github.com/lumalabs/lumaai-python/issues/49)) ([9d05dc0](https://github.com/lumalabs/lumaai-python/commit/9d05dc05ba43a236d369c75926f199d31df17d46))
* rebuild project due to codegen change ([#50](https://github.com/lumalabs/lumaai-python/issues/50)) ([1951e9d](https://github.com/lumalabs/lumaai-python/commit/1951e9d82921d41675d32e4e0406fae05e4c20eb))
* rebuild project due to codegen change ([#51](https://github.com/lumalabs/lumaai-python/issues/51)) ([5b0dc70](https://github.com/lumalabs/lumaai-python/commit/5b0dc702a4394e9ae3d5d32c1c14066e091f1f28))


### Documentation

* add info log level to readme ([#53](https://github.com/lumalabs/lumaai-python/issues/53)) ([f7ba397](https://github.com/lumalabs/lumaai-python/commit/f7ba397b039b460ee377b6eddd5c5c6f2fa7487f))

## 1.1.0 (2024-10-08)

Full Changelog: [v1.0.2...v1.1.0](https://github.com/lumalabs/lumaai-python/compare/v1.0.2...v1.1.0)

### Features

* **api:** OpenAPI spec update via Stainless API ([#44](https://github.com/lumalabs/lumaai-python/issues/44)) ([2420ce0](https://github.com/lumalabs/lumaai-python/commit/2420ce0da8c9b46a37f85344df7ca090e3118f5b))
* **api:** OpenAPI spec update via Stainless API ([#45](https://github.com/lumalabs/lumaai-python/issues/45)) ([d16b8e6](https://github.com/lumalabs/lumaai-python/commit/d16b8e6d783510924e90faab1ed0967bb060d604))


### Bug Fixes

* **client:** avoid OverflowError with very large retry counts ([#42](https://github.com/lumalabs/lumaai-python/issues/42)) ([f8fce51](https://github.com/lumalabs/lumaai-python/commit/f8fce51fad45155c26999b9eaca3616e770fd98d))


### Chores

* add repr to PageInfo class ([#43](https://github.com/lumalabs/lumaai-python/issues/43)) ([73fd7da](https://github.com/lumalabs/lumaai-python/commit/73fd7dac856b86587968807d5d26a5c0923c9161))
* **internal:** add support for parsing bool response content ([#41](https://github.com/lumalabs/lumaai-python/issues/41)) ([066e7d5](https://github.com/lumalabs/lumaai-python/commit/066e7d5343adbfa2dd91323e8ce0111c5e169d3a))
* remove custom code ([b62185e](https://github.com/lumalabs/lumaai-python/commit/b62185ec6ff7e4ffe398053ffb63a370dcdaa500))
