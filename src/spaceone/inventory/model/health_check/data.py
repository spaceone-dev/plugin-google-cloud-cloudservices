from schematics import Model
from schematics.types import ModelType, ListType, StringType, IntType, DateTimeType, BooleanType, FloatType, DictType, \
    UnionType, MultiType


class HealthCheckSpec(Model):
    port = IntType()
    port_name = StringType(deserialize_from='portName')
    port_specification = StringType(choices=('USE_FIXED_PORT', 'USE_NAMED_PORT', 'USE_SERVING_PORT'),
                                    deserialize_from='portSpecification')
    request = StringType()
    response = StringType()
    proxy_header = StringType(choices=('NONE', 'PROXY_V1'), deserialize_from='proxyHeader')


class GrpcHealthCheckSpec(Model):
    port = IntType()
    port_name = StringType()
    port_specification = StringType(choices=('USE_FIXED_PORT', 'USE_NAMED_PORT', 'USE_SERVING_PORT'),
                                    deserialize_from='portSpecification')
    grpc_service_name = StringType()


class LogConfig(Model):
    enable = BooleanType()


class HealthCheck(Model):
    id = StringType()
    name = StringType()
    description = StringType()
    scope = StringType()
    host = StringType()
    path = StringType()
    check_interval_sec = IntType(deserialize_from='checkIntervalSec')
    timeout_sec = IntType(deserialize_from='timeoutSec')
    unhealthy_threshold = IntType(deserialize_from='unhealthyThreshold')
    healthy_threshold = IntType(deserialize_from='healthyThreshold')
    type = StringType(choices=('TCP', 'SSL', 'HTTP', 'HTTPS', 'HTTP2'))
    tcp_health_check = ModelType(HealthCheckSpec, deserialize_from='tcpHealthCheck')
    ssl_health_check = ModelType(HealthCheckSpec, deserialize_from='sslHealthCheck')
    http_health_check = ModelType(HealthCheckSpec, deserialize_from='httpHealthCheck')
    https_health_check = ModelType(HealthCheckSpec, deserialize_from='httpsHealthCheck')
    http2_health_check = ModelType(HealthCheckSpec, deserialize_from='http2HealthCheck')
    grpc_health_check = ModelType(GrpcHealthCheckSpec, deserialize_from='grpcHealthCheck')
    project = StringType()
    region = StringType()
    log_config = ModelType(LogConfig, deserialize_from='logConfig')
    kind = StringType()

    self_link = StringType(deserialize_from='selfLink')
    creation_time = DateTimeType(deserialize_from='creationTimestamp')

    def reference(self):
        return {
            "resource_id": self.self_link,
            "external_link": f"https://console.cloud.google.com/compute/healthChecks/details/{self.name}?project={self.project}"
        }

