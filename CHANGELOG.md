# Changelog

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
