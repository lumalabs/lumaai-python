# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import LumaAIError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import ping, credits, generations
    from .resources.ping import PingResource, AsyncPingResource
    from .resources.credits import CreditsResource, AsyncCreditsResource
    from .resources.generations.generations import GenerationsResource, AsyncGenerationsResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "LumaAI", "AsyncLumaAI", "Client", "AsyncClient"]


class LumaAI(SyncAPIClient):
    # client options
    auth_token: str

    def __init__(
        self,
        *,
        auth_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous LumaAI client instance.

        This automatically infers the `auth_token` argument from the `LUMAAI_API_KEY` environment variable if it is not provided.
        """
        if auth_token is None:
            auth_token = os.environ.get("LUMAAI_API_KEY")
        if auth_token is None:
            raise LumaAIError(
                "The auth_token client option must be set either by passing auth_token to the client or by setting the LUMAAI_API_KEY environment variable"
            )
        self.auth_token = auth_token

        if base_url is None:
            base_url = os.environ.get("LUMAAI_BASE_URL")
        if base_url is None:
            base_url = f"https://api.lumalabs.ai/dream-machine/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def generations(self) -> GenerationsResource:
        from .resources.generations import GenerationsResource

        return GenerationsResource(self)

    @cached_property
    def ping(self) -> PingResource:
        from .resources.ping import PingResource

        return PingResource(self)

    @cached_property
    def credits(self) -> CreditsResource:
        from .resources.credits import CreditsResource

        return CreditsResource(self)

    @cached_property
    def with_raw_response(self) -> LumaAIWithRawResponse:
        return LumaAIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LumaAIWithStreamedResponse:
        return LumaAIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        auth_token = self.auth_token
        return {"Authorization": f"Bearer {auth_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        auth_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            auth_token=auth_token or self.auth_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncLumaAI(AsyncAPIClient):
    # client options
    auth_token: str

    def __init__(
        self,
        *,
        auth_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncLumaAI client instance.

        This automatically infers the `auth_token` argument from the `LUMAAI_API_KEY` environment variable if it is not provided.
        """
        if auth_token is None:
            auth_token = os.environ.get("LUMAAI_API_KEY")
        if auth_token is None:
            raise LumaAIError(
                "The auth_token client option must be set either by passing auth_token to the client or by setting the LUMAAI_API_KEY environment variable"
            )
        self.auth_token = auth_token

        if base_url is None:
            base_url = os.environ.get("LUMAAI_BASE_URL")
        if base_url is None:
            base_url = f"https://api.lumalabs.ai/dream-machine/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def generations(self) -> AsyncGenerationsResource:
        from .resources.generations import AsyncGenerationsResource

        return AsyncGenerationsResource(self)

    @cached_property
    def ping(self) -> AsyncPingResource:
        from .resources.ping import AsyncPingResource

        return AsyncPingResource(self)

    @cached_property
    def credits(self) -> AsyncCreditsResource:
        from .resources.credits import AsyncCreditsResource

        return AsyncCreditsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncLumaAIWithRawResponse:
        return AsyncLumaAIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLumaAIWithStreamedResponse:
        return AsyncLumaAIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        auth_token = self.auth_token
        return {"Authorization": f"Bearer {auth_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        auth_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            auth_token=auth_token or self.auth_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class LumaAIWithRawResponse:
    _client: LumaAI

    def __init__(self, client: LumaAI) -> None:
        self._client = client

    @cached_property
    def generations(self) -> generations.GenerationsResourceWithRawResponse:
        from .resources.generations import GenerationsResourceWithRawResponse

        return GenerationsResourceWithRawResponse(self._client.generations)

    @cached_property
    def ping(self) -> ping.PingResourceWithRawResponse:
        from .resources.ping import PingResourceWithRawResponse

        return PingResourceWithRawResponse(self._client.ping)

    @cached_property
    def credits(self) -> credits.CreditsResourceWithRawResponse:
        from .resources.credits import CreditsResourceWithRawResponse

        return CreditsResourceWithRawResponse(self._client.credits)


class AsyncLumaAIWithRawResponse:
    _client: AsyncLumaAI

    def __init__(self, client: AsyncLumaAI) -> None:
        self._client = client

    @cached_property
    def generations(self) -> generations.AsyncGenerationsResourceWithRawResponse:
        from .resources.generations import AsyncGenerationsResourceWithRawResponse

        return AsyncGenerationsResourceWithRawResponse(self._client.generations)

    @cached_property
    def ping(self) -> ping.AsyncPingResourceWithRawResponse:
        from .resources.ping import AsyncPingResourceWithRawResponse

        return AsyncPingResourceWithRawResponse(self._client.ping)

    @cached_property
    def credits(self) -> credits.AsyncCreditsResourceWithRawResponse:
        from .resources.credits import AsyncCreditsResourceWithRawResponse

        return AsyncCreditsResourceWithRawResponse(self._client.credits)


class LumaAIWithStreamedResponse:
    _client: LumaAI

    def __init__(self, client: LumaAI) -> None:
        self._client = client

    @cached_property
    def generations(self) -> generations.GenerationsResourceWithStreamingResponse:
        from .resources.generations import GenerationsResourceWithStreamingResponse

        return GenerationsResourceWithStreamingResponse(self._client.generations)

    @cached_property
    def ping(self) -> ping.PingResourceWithStreamingResponse:
        from .resources.ping import PingResourceWithStreamingResponse

        return PingResourceWithStreamingResponse(self._client.ping)

    @cached_property
    def credits(self) -> credits.CreditsResourceWithStreamingResponse:
        from .resources.credits import CreditsResourceWithStreamingResponse

        return CreditsResourceWithStreamingResponse(self._client.credits)


class AsyncLumaAIWithStreamedResponse:
    _client: AsyncLumaAI

    def __init__(self, client: AsyncLumaAI) -> None:
        self._client = client

    @cached_property
    def generations(self) -> generations.AsyncGenerationsResourceWithStreamingResponse:
        from .resources.generations import AsyncGenerationsResourceWithStreamingResponse

        return AsyncGenerationsResourceWithStreamingResponse(self._client.generations)

    @cached_property
    def ping(self) -> ping.AsyncPingResourceWithStreamingResponse:
        from .resources.ping import AsyncPingResourceWithStreamingResponse

        return AsyncPingResourceWithStreamingResponse(self._client.ping)

    @cached_property
    def credits(self) -> credits.AsyncCreditsResourceWithStreamingResponse:
        from .resources.credits import AsyncCreditsResourceWithStreamingResponse

        return AsyncCreditsResourceWithStreamingResponse(self._client.credits)


Client = LumaAI

AsyncClient = AsyncLumaAI
