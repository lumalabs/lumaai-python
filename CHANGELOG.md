# Changelog

## 1.19.0 (2026-01-07)

Full Changelog: [v1.18.2...v1.19.0](https://github.com/lumalabs/lumaai-python/compare/v1.18.2...v1.19.0)

### Features

* **api:** api update ([6360134](https://github.com/lumalabs/lumaai-python/commit/6360134afa6bd6b2255006eada63cec14a31c83f))


### Chores

* **internal:** codegen related update ([ddae3b2](https://github.com/lumalabs/lumaai-python/commit/ddae3b2abd9a341c070e9541c9e5e5771f03bbd5))

## 1.18.2 (2025-12-19)

Full Changelog: [v1.18.1...v1.18.2](https://github.com/lumalabs/lumaai-python/compare/v1.18.1...v1.18.2)

### Bug Fixes

* **client:** close streams without requiring full consumption ([bb74e0e](https://github.com/lumalabs/lumaai-python/commit/bb74e0e1e9879226b035d48969e27a26106b9313))
* compat with Python 3.14 ([6c50b92](https://github.com/lumalabs/lumaai-python/commit/6c50b925da3bf7aa7f4230d6b2eee69fa310761e))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([195aebe](https://github.com/lumalabs/lumaai-python/commit/195aebe165bc24e0cbb94de7dbb39b61e0635a1e))
* ensure streams are always closed ([7c0964c](https://github.com/lumalabs/lumaai-python/commit/7c0964cc2a8a08618cc4fa46709e6546b6b50949))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([407770f](https://github.com/lumalabs/lumaai-python/commit/407770fa3b66a652dfeab7d5737b157735f47c88))
* use async_to_httpx_files in patch method ([04202cd](https://github.com/lumalabs/lumaai-python/commit/04202cd1984050063dfb04fc3e10e0757a7ad03d))


### Chores

* add missing docstrings ([e32f03a](https://github.com/lumalabs/lumaai-python/commit/e32f03ae9302de2b83a1aee55c75c6be8f35da61))
* add Python 3.14 classifier and testing ([df59a3e](https://github.com/lumalabs/lumaai-python/commit/df59a3eb574cd6d80999eec78336074cfefcbe46))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([509bb97](https://github.com/lumalabs/lumaai-python/commit/509bb971869279743360f4e4bb6054c68f1d9333))
* **docs:** use environment variables for authentication in code snippets ([8d332b4](https://github.com/lumalabs/lumaai-python/commit/8d332b468d3b48d32533021de27767064779d445))
* **internal/tests:** avoid race condition with implicit client cleanup ([0157eb1](https://github.com/lumalabs/lumaai-python/commit/0157eb1653e0ce84760b1dda5a87b83ec8acaf89))
* **internal:** add `--fix` argument to lint script ([12c0306](https://github.com/lumalabs/lumaai-python/commit/12c03067db5eb94b107078883d3b139c517be036))
* **internal:** add missing files argument to base client ([91b4b41](https://github.com/lumalabs/lumaai-python/commit/91b4b41773b5811dc60367218e8e14f3c6482c06))
* **internal:** grammar fix (it's -&gt; its) ([abbf8b2](https://github.com/lumalabs/lumaai-python/commit/abbf8b291a2e3f52eee9caf33f701b8cc9be4f67))
* **package:** drop Python 3.8 support ([13b55a3](https://github.com/lumalabs/lumaai-python/commit/13b55a332e6b348b4572b60c5efb352005c4ec52))
* speedup initial import ([b399d2f](https://github.com/lumalabs/lumaai-python/commit/b399d2f694a665aa5c28a1a90e9b44ebceb38e73))
* update lockfile ([c73c583](https://github.com/lumalabs/lumaai-python/commit/c73c5834c494214a3e02ea4654ec8866a639d19a))

## 1.18.1 (2025-10-18)

Full Changelog: [v1.18.0...v1.18.1](https://github.com/lumalabs/lumaai-python/compare/v1.18.0...v1.18.1)

### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([d5510ae](https://github.com/lumalabs/lumaai-python/commit/d5510ae0bee832e619c93db9a4c43ee8fade791c))
* **internal:** detect missing future annotations with ruff ([b7f9ede](https://github.com/lumalabs/lumaai-python/commit/b7f9ede6d3ad8f6d42b6d726ee4cf7608c9133c5))

## 1.18.0 (2025-09-20)

Full Changelog: [v1.17.2...v1.18.0](https://github.com/lumalabs/lumaai-python/compare/v1.17.2...v1.18.0)

### Features

* improve future compat with pydantic v3 ([81e50ec](https://github.com/lumalabs/lumaai-python/commit/81e50ec1ccc146880857c0d3ae53db6799152722))
* **types:** replace List[str] with SequenceNotStr in params ([ef79710](https://github.com/lumalabs/lumaai-python/commit/ef797106cb84a311dea7159dd141836225857595))


### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([7444c4e](https://github.com/lumalabs/lumaai-python/commit/7444c4e953704dd0d691efbb89bd39cda233270d))
* **internal:** move mypy configurations to `pyproject.toml` file ([f92365c](https://github.com/lumalabs/lumaai-python/commit/f92365c915f3e720890ba6e4ecdcdc958f458124))
* **internal:** update pydantic dependency ([58cb6aa](https://github.com/lumalabs/lumaai-python/commit/58cb6aa0a9fb27eed8a667ad7a91dd416ef70ba1))
* **tests:** simplify `get_platform` test ([8db8236](https://github.com/lumalabs/lumaai-python/commit/8db82362ec34723d1d6a17a29aa02f245e312073))
* **types:** change optional parameter type from NotGiven to Omit ([e347327](https://github.com/lumalabs/lumaai-python/commit/e347327f9ad5c34ac7bc5cf923c773007ce286ad))

## 1.17.2 (2025-08-30)

Full Changelog: [v1.17.1...v1.17.2](https://github.com/lumalabs/lumaai-python/compare/v1.17.1...v1.17.2)

### Bug Fixes

* avoid newer type syntax ([4c7e849](https://github.com/lumalabs/lumaai-python/commit/4c7e849ff9b0efbabba24aab8f4c3ad182756940))


### Chores

* **internal:** add Sequence related utils ([dc85243](https://github.com/lumalabs/lumaai-python/commit/dc8524308fe02225a82c0ef9ad3b424920e416e4))
* **internal:** change ci workflow machines ([eb1b9a6](https://github.com/lumalabs/lumaai-python/commit/eb1b9a6fb577b0577fc812d68d1d96cd38d3f3d1))
* **internal:** update pyright exclude list ([413b33b](https://github.com/lumalabs/lumaai-python/commit/413b33b4a4805b1e45a8986e05ab7800ca08d277))
* update github action ([e4e2029](https://github.com/lumalabs/lumaai-python/commit/e4e20297f21e3e87806939216aff01803f387d19))

## 1.17.1 (2025-08-14)

Full Changelog: [v1.17.0...v1.17.1](https://github.com/lumalabs/lumaai-python/compare/v1.17.0...v1.17.1)

### Chores

* **internal:** update comment in script ([dca67fb](https://github.com/lumalabs/lumaai-python/commit/dca67fb93dd6c999356f3d91403eb673155403e1))
* update @stainless-api/prism-cli to v5.15.0 ([5c8641c](https://github.com/lumalabs/lumaai-python/commit/5c8641c895858ade3f24c8c1876f5969824538d8))

## 1.17.0 (2025-08-06)

Full Changelog: [v1.16.2...v1.17.0](https://github.com/lumalabs/lumaai-python/compare/v1.16.2...v1.17.0)

### Features

* **client:** support file upload requests ([34a3cfb](https://github.com/lumalabs/lumaai-python/commit/34a3cfb3ca6655c5014fcebf8fb6fbee157cf202))


### Chores

* **internal:** fix ruff target version ([eb0161d](https://github.com/lumalabs/lumaai-python/commit/eb0161d4e30ec79cb2e6193b508af6e9bfd36668))

## 1.16.2 (2025-07-25)

Full Changelog: [v1.16.1...v1.16.2](https://github.com/lumalabs/lumaai-python/compare/v1.16.1...v1.16.2)

### Bug Fixes

* **parsing:** ignore empty metadata ([cc3dcfd](https://github.com/lumalabs/lumaai-python/commit/cc3dcfda83fb923c4841642a6efbd47e87b52920))
* **parsing:** parse extra field types ([096e433](https://github.com/lumalabs/lumaai-python/commit/096e433a7fb3d04f82b72b2db0ed2ee6c09d418c))


### Chores

* **project:** add settings file for vscode ([e2867b5](https://github.com/lumalabs/lumaai-python/commit/e2867b50de439679e686996f1e5eef45a9608c14))

## 1.16.1 (2025-07-19)

Full Changelog: [v1.16.0...v1.16.1](https://github.com/lumalabs/lumaai-python/compare/v1.16.0...v1.16.1)

### Features

* clean up environment call outs ([397b649](https://github.com/lumalabs/lumaai-python/commit/397b649ac39bf63d0e052207e9dc87266a49caf5))


### Bug Fixes

* **client:** don't send Content-Type header on GET requests ([bb09d4d](https://github.com/lumalabs/lumaai-python/commit/bb09d4df6e2b7fe741848e3986aa310c39a1bf6d))

## 1.16.0 (2025-07-11)

Full Changelog: [v1.15.1...v1.16.0](https://github.com/lumalabs/lumaai-python/compare/v1.15.1...v1.16.0)

### Features

* **api:** api update ([575ffcf](https://github.com/lumalabs/lumaai-python/commit/575ffcfc00f6f5069192d782c25bf3a01c2d893d))

## 1.15.1 (2025-07-11)

Full Changelog: [v1.15.0...v1.15.1](https://github.com/lumalabs/lumaai-python/compare/v1.15.0...v1.15.1)

### Bug Fixes

* **ci:** correct conditional ([7cd4571](https://github.com/lumalabs/lumaai-python/commit/7cd4571c6553c4f540bff998e14dc871cc58271e))
* **ci:** release-doctor — report correct token name ([adda4e4](https://github.com/lumalabs/lumaai-python/commit/adda4e42e705f849c2c73e6ebb61f0753bd23745))
* **parsing:** correctly handle nested discriminated unions ([d97d872](https://github.com/lumalabs/lumaai-python/commit/d97d872c579e363844a941cc8318d5e54de342c5))


### Chores

* **ci:** change upload type ([351a0e8](https://github.com/lumalabs/lumaai-python/commit/351a0e8c979c206a8f94a5b68f1fdd5793bcb278))
* **ci:** only run for pushes and fork pull requests ([50b8ecb](https://github.com/lumalabs/lumaai-python/commit/50b8ecb28a5e6c65e681467b9787b7bc23661556))
* **internal:** bump pinned h11 dep ([2f98b9a](https://github.com/lumalabs/lumaai-python/commit/2f98b9a4afdcb76c12221c660d43dbdaff9741af))
* **internal:** codegen related update ([b89b147](https://github.com/lumalabs/lumaai-python/commit/b89b1470c88c4825b3b52ab15fccd8a1587334ba))
* **package:** mark python 3.13 as supported ([7f37491](https://github.com/lumalabs/lumaai-python/commit/7f374916e24833705e85f06788ea24c5eec15b43))
* **readme:** fix version rendering on pypi ([24f04ae](https://github.com/lumalabs/lumaai-python/commit/24f04aeeca03973aece5756f563cb48b4fd0e8a1))

## 1.15.0 (2025-06-25)

Full Changelog: [v1.14.0...v1.15.0](https://github.com/lumalabs/lumaai-python/compare/v1.14.0...v1.15.0)

### Features

* **api:** api update ([e8ba8cb](https://github.com/lumalabs/lumaai-python/commit/e8ba8cbf95ab37c503dc8716cc7fceff301c6f5e))
* **api:** api update ([915b0ce](https://github.com/lumalabs/lumaai-python/commit/915b0cee4ba32ca833f96f01c04a0cbe807c1bde))
* **client:** add support for aiohttp ([dd16fb2](https://github.com/lumalabs/lumaai-python/commit/dd16fb287e518048a3d8f7783bc0d821fb9b8607))


### Chores

* **tests:** skip some failing tests on the latest python versions ([995da3c](https://github.com/lumalabs/lumaai-python/commit/995da3c212cbf2d2c11c71fcbc6d800b606962f3))

## 1.14.0 (2025-06-20)

Full Changelog: [v1.13.0...v1.14.0](https://github.com/lumalabs/lumaai-python/compare/v1.13.0...v1.14.0)

### Bug Fixes

* **client:** correctly parse binary response | stream ([fae6341](https://github.com/lumalabs/lumaai-python/commit/fae6341296fcbe31a09744d40f2864e59eb99ab8))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([d90e9be](https://github.com/lumalabs/lumaai-python/commit/d90e9bec0b8fea5f4e701faba952e481cfbc6c7b))


### Chores

* **ci:** enable for pull requests ([d994fec](https://github.com/lumalabs/lumaai-python/commit/d994feca7a0f23001b71d2f7a36c9d863dec7643))
* **internal:** update conftest.py ([9020c14](https://github.com/lumalabs/lumaai-python/commit/9020c1474becbac389c78ba0daa813798d9c0208))
* **readme:** update badges ([5d50b56](https://github.com/lumalabs/lumaai-python/commit/5d50b56b3d5d4ebc81bdea4b3f1e9de552a6c082))
* **tests:** add tests for httpx client instantiation & proxies ([5257ece](https://github.com/lumalabs/lumaai-python/commit/5257ece47e45ae5cc8d2a0ea590a7e52203b4834))
* **tests:** run tests in parallel ([b7fca9f](https://github.com/lumalabs/lumaai-python/commit/b7fca9f8613bdac4d4a84642b5e21801d5a9003d))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([39be672](https://github.com/lumalabs/lumaai-python/commit/39be6723f033b65fa4fcc86fb4069f785d077171))

## 1.13.0 (2025-06-03)

Full Changelog: [v1.12.0...v1.13.0](https://github.com/lumalabs/lumaai-python/compare/v1.12.0...v1.13.0)

### Features

* **client:** add follow_redirects request option ([43ed202](https://github.com/lumalabs/lumaai-python/commit/43ed202c630e08ec6ac5522b5b7151ee7d1d1c47))


### Chores

* **docs:** remove reference to rye shell ([9285d7f](https://github.com/lumalabs/lumaai-python/commit/9285d7fefa3515a6c533513dfe5deef0d2beca20))

## 1.12.0 (2025-06-02)

Full Changelog: [v1.11.0...v1.12.0](https://github.com/lumalabs/lumaai-python/compare/v1.11.0...v1.12.0)

### Features

* **api:** api update ([789bfde](https://github.com/lumalabs/lumaai-python/commit/789bfde7cd005e0a9d7e61755917a9a78ba9b402))

## 1.11.0 (2025-05-28)

Full Changelog: [v1.10.0...v1.11.0](https://github.com/lumalabs/lumaai-python/compare/v1.10.0...v1.11.0)

### Features

* **api:** api update ([ddc15c8](https://github.com/lumalabs/lumaai-python/commit/ddc15c8b14ed1cd6bd52c3980c73d00b782d8450))

## 1.10.0 (2025-05-28)

Full Changelog: [v1.9.2...v1.10.0](https://github.com/lumalabs/lumaai-python/compare/v1.9.2...v1.10.0)

### Features

* **api:** api update ([9e107a1](https://github.com/lumalabs/lumaai-python/commit/9e107a10e1100e2d91adabae9724b01d8f7000b0))


### Chores

* **docs:** grammar improvements ([eb54b7e](https://github.com/lumalabs/lumaai-python/commit/eb54b7eaa65e1285b3883dffb04add9606867af5))

## 1.9.2 (2025-05-16)

Full Changelog: [v1.9.1...v1.9.2](https://github.com/lumalabs/lumaai-python/compare/v1.9.1...v1.9.2)

### Bug Fixes

* **package:** support direct resource imports ([55e8fae](https://github.com/lumalabs/lumaai-python/commit/55e8fae586d878a5644e5094c00828aa41726d8b))


### Chores

* **ci:** fix installation instructions ([5b4d1d0](https://github.com/lumalabs/lumaai-python/commit/5b4d1d02e00aaeb37c49831601363db447ec5ded))
* **ci:** upload sdks to package manager ([06ea25f](https://github.com/lumalabs/lumaai-python/commit/06ea25f3cee5ae3817e1eb24db972166362fd589))

## 1.9.1 (2025-05-09)

Full Changelog: [v1.9.0...v1.9.1](https://github.com/lumalabs/lumaai-python/compare/v1.9.0...v1.9.1)

### Chores

* **internal:** avoid errors for isinstance checks on proxies ([1947fc7](https://github.com/lumalabs/lumaai-python/commit/1947fc7379daad3d3652b98eb194f9815834b411))

## 1.9.0 (2025-05-08)

Full Changelog: [v1.8.2...v1.9.0](https://github.com/lumalabs/lumaai-python/compare/v1.8.2...v1.9.0)

### Features

* **api:** api update ([2dc1691](https://github.com/lumalabs/lumaai-python/commit/2dc1691c912bf4f9f12ef5bf6680425c500d18a5))

## 1.8.2 (2025-04-30)

Full Changelog: [v1.8.1...v1.8.2](https://github.com/lumalabs/lumaai-python/compare/v1.8.1...v1.8.2)

### Features

* **api:** api update ([55aa631](https://github.com/lumalabs/lumaai-python/commit/55aa63162f75def3c96e3e7389c0488efda1fcde))

## 1.8.1 (2025-04-28)

Full Changelog: [v1.8.0...v1.8.1](https://github.com/lumalabs/lumaai-python/compare/v1.8.0...v1.8.1)

### Features

* **api:** api update ([97fd303](https://github.com/lumalabs/lumaai-python/commit/97fd3039908bd0bbd8c4249fd19914c8d660fba1))

## 1.8.0 (2025-04-28)

Full Changelog: [v1.7.4...v1.8.0](https://github.com/lumalabs/lumaai-python/compare/v1.7.4...v1.8.0)

### Features

* **api:** api update ([db3cff7](https://github.com/lumalabs/lumaai-python/commit/db3cff7b86830e8cc65b42c06450eb5f4447d757))


### Bug Fixes

* **pydantic v1:** more robust ModelField.annotation check ([fcdce1c](https://github.com/lumalabs/lumaai-python/commit/fcdce1c362df7d9d0a6d7174e29076836de5c5d3))


### Chores

* broadly detect json family of content-type headers ([de64b0d](https://github.com/lumalabs/lumaai-python/commit/de64b0d6aaea7867bf9a24b81c6428dea4db2e2a))
* **ci:** add timeout thresholds for CI jobs ([0e37d88](https://github.com/lumalabs/lumaai-python/commit/0e37d8830294e79625e4f4cf8463300cbab6c6a6))
* **ci:** only use depot for staging repos ([2bd7be2](https://github.com/lumalabs/lumaai-python/commit/2bd7be2af79eb3bad3acbef7750891120997057e))
* **internal:** codegen related update ([c6529eb](https://github.com/lumalabs/lumaai-python/commit/c6529eb59316a4158387edb7f929a644c2905c71))
* **internal:** fix list file params ([26dfbdf](https://github.com/lumalabs/lumaai-python/commit/26dfbdf659a0ebc85426fd4b2f6045b2ebf858e1))
* **internal:** import reformatting ([ce53b89](https://github.com/lumalabs/lumaai-python/commit/ce53b89c0b333092e549d3d1a64b0e627675c957))
* **internal:** minor formatting changes ([178d389](https://github.com/lumalabs/lumaai-python/commit/178d389745b360462cc91a4a6e37603e8c9a4118))
* **internal:** refactor retries to not use recursion ([14d2209](https://github.com/lumalabs/lumaai-python/commit/14d22095115b943b94e59f6e8cae7cbab9db251f))

## 1.7.4 (2025-04-19)

Full Changelog: [v1.7.3...v1.7.4](https://github.com/lumalabs/lumaai-python/compare/v1.7.3...v1.7.4)

### Chores

* **client:** minor internal fixes ([68e1d2f](https://github.com/lumalabs/lumaai-python/commit/68e1d2f9af6bf09abfdfa371866708e18fa302f5))
* **internal:** base client updates ([67b1b18](https://github.com/lumalabs/lumaai-python/commit/67b1b18ca71382adc68a018203b18fd08b7e1be2))
* **internal:** bump pyright version ([56afae7](https://github.com/lumalabs/lumaai-python/commit/56afae7fdfc5b3b2677e4504f13b7ea2e10c90a3))
* **internal:** update models test ([f1d8b96](https://github.com/lumalabs/lumaai-python/commit/f1d8b96680fcf539a937f9a0e9cbf5854dbc4b53))
* **internal:** update pyright settings ([f8da796](https://github.com/lumalabs/lumaai-python/commit/f8da796eede330a39599f66771dc74bb3a68aeb7))

## 1.7.3 (2025-04-12)

Full Changelog: [v1.7.2...v1.7.3](https://github.com/lumalabs/lumaai-python/compare/v1.7.2...v1.7.3)

### Bug Fixes

* **perf:** optimize some hot paths ([ae01192](https://github.com/lumalabs/lumaai-python/commit/ae01192924c54d4a2a7d9a70d0df88e209163989))
* **perf:** skip traversing types for NotGiven values ([43ac98d](https://github.com/lumalabs/lumaai-python/commit/43ac98d293f3e373ac986a4cabd036a54b1e8213))


### Chores

* **internal:** expand CI branch coverage ([a006432](https://github.com/lumalabs/lumaai-python/commit/a00643219c4eebcfe34eca5046e5380a96945257))
* **internal:** reduce CI branch coverage ([7c6570e](https://github.com/lumalabs/lumaai-python/commit/7c6570e1e1a9cd62d67017d62af8375b8eb6a145))
* **internal:** slight transform perf improvement ([#149](https://github.com/lumalabs/lumaai-python/issues/149)) ([b95d415](https://github.com/lumalabs/lumaai-python/commit/b95d415fb6f3a92b90e78044c3756b84611a9179))
* **tests:** improve enum examples ([#151](https://github.com/lumalabs/lumaai-python/issues/151)) ([dc358d1](https://github.com/lumalabs/lumaai-python/commit/dc358d17dc810dc8e1de849679a618c61a626cd5))

## 1.7.2 (2025-04-04)

Full Changelog: [v1.7.1...v1.7.2](https://github.com/lumalabs/lumaai-python/compare/v1.7.1...v1.7.2)

### Chores

* **internal:** remove trailing character ([#146](https://github.com/lumalabs/lumaai-python/issues/146)) ([e5d38ff](https://github.com/lumalabs/lumaai-python/commit/e5d38ffecf56e7c1bc70724545ad24a34700dc97))

## 1.7.1 (2025-03-27)

Full Changelog: [v1.7.0...v1.7.1](https://github.com/lumalabs/lumaai-python/compare/v1.7.0...v1.7.1)

### Chores

* fix typos ([#143](https://github.com/lumalabs/lumaai-python/issues/143)) ([2b47cdc](https://github.com/lumalabs/lumaai-python/commit/2b47cdc2b25ed98263f7fd97c2b2a09e8bb3b984))

## 1.7.0 (2025-03-19)

Full Changelog: [v1.6.3...v1.7.0](https://github.com/lumalabs/lumaai-python/compare/v1.6.3...v1.7.0)

### Features

* **api:** api update ([#140](https://github.com/lumalabs/lumaai-python/issues/140)) ([7da8844](https://github.com/lumalabs/lumaai-python/commit/7da884428ba97e58f9fc20941472a0c88856cdf7))

## 1.6.3 (2025-03-17)

Full Changelog: [v1.6.2...v1.6.3](https://github.com/lumalabs/lumaai-python/compare/v1.6.2...v1.6.3)

### Bug Fixes

* **ci:** remove publishing patch ([#136](https://github.com/lumalabs/lumaai-python/issues/136)) ([3e94589](https://github.com/lumalabs/lumaai-python/commit/3e9458990500b8de744e2528cbc8012d7b390812))
* **ci:** undo rye version revert ([d6722a9](https://github.com/lumalabs/lumaai-python/commit/d6722a90b3a470e60fa63b50d071887aba55b830))

## 1.6.2 (2025-03-17)

Full Changelog: [v1.6.1...v1.6.2](https://github.com/lumalabs/lumaai-python/compare/v1.6.1...v1.6.2)

### Bug Fixes

* **ci:** revert rye version change ([9e4f00c](https://github.com/lumalabs/lumaai-python/commit/9e4f00ca379aba7aed502f12ccedac8edbfd9bf8))

## 1.6.1 (2025-03-17)

Full Changelog: [v1.6.0...v1.6.1](https://github.com/lumalabs/lumaai-python/compare/v1.6.0...v1.6.1)

### Bug Fixes

* **ci:** ensure pip is always available ([#131](https://github.com/lumalabs/lumaai-python/issues/131)) ([975fb6f](https://github.com/lumalabs/lumaai-python/commit/975fb6f2650a6beb8e30d4a758d0d96bd9b7d8bd))

## 1.6.0 (2025-03-17)

Full Changelog: [v1.5.2...v1.6.0](https://github.com/lumalabs/lumaai-python/compare/v1.5.2...v1.6.0)

### Features

* **api:** api update ([#128](https://github.com/lumalabs/lumaai-python/issues/128)) ([3d278af](https://github.com/lumalabs/lumaai-python/commit/3d278af129bc751b578fefffcbb24e5242466c53))

## 1.5.2 (2025-03-15)

Full Changelog: [v1.5.1...v1.5.2](https://github.com/lumalabs/lumaai-python/compare/v1.5.1...v1.5.2)

### Bug Fixes

* **types:** handle more discriminated union shapes ([#126](https://github.com/lumalabs/lumaai-python/issues/126)) ([71a98c0](https://github.com/lumalabs/lumaai-python/commit/71a98c0718c44688074031d45df765cc5e5dae8b))


### Chores

* **internal:** bump rye to 0.44.0 ([#125](https://github.com/lumalabs/lumaai-python/issues/125)) ([20a924b](https://github.com/lumalabs/lumaai-python/commit/20a924bcae62c24e9990c3418c03d62fbefbff3a))
* **internal:** codegen related update ([#124](https://github.com/lumalabs/lumaai-python/issues/124)) ([658c121](https://github.com/lumalabs/lumaai-python/commit/658c121252e128962caaf382f9748da8f30e46c0))
* **internal:** remove extra empty newlines ([#123](https://github.com/lumalabs/lumaai-python/issues/123)) ([82d0867](https://github.com/lumalabs/lumaai-python/commit/82d0867956d52dec920f3693ec8bc89a0b7fd6a6))


### Documentation

* revise readme docs about nested params ([#120](https://github.com/lumalabs/lumaai-python/issues/120)) ([424187b](https://github.com/lumalabs/lumaai-python/commit/424187bd35b540d56aef9fec0eaae13346d3abd0))

## 1.5.1 (2025-03-04)

Full Changelog: [v1.5.0...v1.5.1](https://github.com/lumalabs/lumaai-python/compare/v1.5.0...v1.5.1)

### Chores

* **docs:** update client docstring ([#117](https://github.com/lumalabs/lumaai-python/issues/117)) ([33e4b1c](https://github.com/lumalabs/lumaai-python/commit/33e4b1caa0856141fddf96c1f0f11eded04b37b8))
* **internal:** fix devcontainers setup ([#113](https://github.com/lumalabs/lumaai-python/issues/113)) ([51d77c4](https://github.com/lumalabs/lumaai-python/commit/51d77c41886232b0fa1e3e82ed9fec3a08204b56))
* **internal:** properly set __pydantic_private__ ([#115](https://github.com/lumalabs/lumaai-python/issues/115)) ([b9c7a3f](https://github.com/lumalabs/lumaai-python/commit/b9c7a3ff7f20f3bf06aeb85452235a6a6176e778))
* **internal:** remove unused http client options forwarding ([#118](https://github.com/lumalabs/lumaai-python/issues/118)) ([b68b130](https://github.com/lumalabs/lumaai-python/commit/b68b130141096a575f893136721bf62cb792b4fe))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([#116](https://github.com/lumalabs/lumaai-python/issues/116)) ([b7ee94c](https://github.com/lumalabs/lumaai-python/commit/b7ee94c17aa885c4b7f8d01d6c0b172cbf205a07))

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
