// Code generated by protoc-gen-go-grpc. DO NOT EDIT.

package v1beta

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// ManifestExtractionServiceClient is the client API for ManifestExtractionService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type ManifestExtractionServiceClient interface {
	// Match matches files that we support extracting content from.
	Match(ctx context.Context, in *MatchRequest, opts ...grpc.CallOption) (*MatchResponse, error)
	// Extract parses supplied files and returns standard representations of manifests.
	Extract(ctx context.Context, in *ExtractRequest, opts ...grpc.CallOption) (*ExtractResponse, error)
}

type manifestExtractionServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewManifestExtractionServiceClient(cc grpc.ClientConnInterface) ManifestExtractionServiceClient {
	return &manifestExtractionServiceClient{cc}
}

func (c *manifestExtractionServiceClient) Match(ctx context.Context, in *MatchRequest, opts ...grpc.CallOption) (*MatchResponse, error) {
	out := new(MatchResponse)
	err := c.cc.Invoke(ctx, "/depscloud.api.v1beta.ManifestExtractionService/Match", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *manifestExtractionServiceClient) Extract(ctx context.Context, in *ExtractRequest, opts ...grpc.CallOption) (*ExtractResponse, error) {
	out := new(ExtractResponse)
	err := c.cc.Invoke(ctx, "/depscloud.api.v1beta.ManifestExtractionService/Extract", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ManifestExtractionServiceServer is the server API for ManifestExtractionService service.
// All implementations must embed UnimplementedManifestExtractionServiceServer
// for forward compatibility
type ManifestExtractionServiceServer interface {
	// Match matches files that we support extracting content from.
	Match(context.Context, *MatchRequest) (*MatchResponse, error)
	// Extract parses supplied files and returns standard representations of manifests.
	Extract(context.Context, *ExtractRequest) (*ExtractResponse, error)
	mustEmbedUnimplementedManifestExtractionServiceServer()
}

// UnimplementedManifestExtractionServiceServer must be embedded to have forward compatible implementations.
type UnimplementedManifestExtractionServiceServer struct {
}

func (UnimplementedManifestExtractionServiceServer) Match(context.Context, *MatchRequest) (*MatchResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Match not implemented")
}
func (UnimplementedManifestExtractionServiceServer) Extract(context.Context, *ExtractRequest) (*ExtractResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Extract not implemented")
}
func (UnimplementedManifestExtractionServiceServer) mustEmbedUnimplementedManifestExtractionServiceServer() {
}

// UnsafeManifestExtractionServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to ManifestExtractionServiceServer will
// result in compilation errors.
type UnsafeManifestExtractionServiceServer interface {
	mustEmbedUnimplementedManifestExtractionServiceServer()
}

func RegisterManifestExtractionServiceServer(s grpc.ServiceRegistrar, srv ManifestExtractionServiceServer) {
	s.RegisterService(&ManifestExtractionService_ServiceDesc, srv)
}

func _ManifestExtractionService_Match_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(MatchRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ManifestExtractionServiceServer).Match(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/depscloud.api.v1beta.ManifestExtractionService/Match",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ManifestExtractionServiceServer).Match(ctx, req.(*MatchRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ManifestExtractionService_Extract_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ExtractRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ManifestExtractionServiceServer).Extract(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/depscloud.api.v1beta.ManifestExtractionService/Extract",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ManifestExtractionServiceServer).Extract(ctx, req.(*ExtractRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// ManifestExtractionService_ServiceDesc is the grpc.ServiceDesc for ManifestExtractionService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var ManifestExtractionService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "depscloud.api.v1beta.ManifestExtractionService",
	HandlerType: (*ManifestExtractionServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Match",
			Handler:    _ManifestExtractionService_Match_Handler,
		},
		{
			MethodName: "Extract",
			Handler:    _ManifestExtractionService_Extract_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "depscloud/api/v1beta/manifest.proto",
}

// ManifestStorageServiceClient is the client API for ManifestStorageService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type ManifestStorageServiceClient interface {
	// Store accepts information about discovered manifest files and persists them.
	Store(ctx context.Context, in *StoreRequest, opts ...grpc.CallOption) (*StoreResponse, error)
}

type manifestStorageServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewManifestStorageServiceClient(cc grpc.ClientConnInterface) ManifestStorageServiceClient {
	return &manifestStorageServiceClient{cc}
}

func (c *manifestStorageServiceClient) Store(ctx context.Context, in *StoreRequest, opts ...grpc.CallOption) (*StoreResponse, error) {
	out := new(StoreResponse)
	err := c.cc.Invoke(ctx, "/depscloud.api.v1beta.ManifestStorageService/Store", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ManifestStorageServiceServer is the server API for ManifestStorageService service.
// All implementations must embed UnimplementedManifestStorageServiceServer
// for forward compatibility
type ManifestStorageServiceServer interface {
	// Store accepts information about discovered manifest files and persists them.
	Store(context.Context, *StoreRequest) (*StoreResponse, error)
	mustEmbedUnimplementedManifestStorageServiceServer()
}

// UnimplementedManifestStorageServiceServer must be embedded to have forward compatible implementations.
type UnimplementedManifestStorageServiceServer struct {
}

func (UnimplementedManifestStorageServiceServer) Store(context.Context, *StoreRequest) (*StoreResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Store not implemented")
}
func (UnimplementedManifestStorageServiceServer) mustEmbedUnimplementedManifestStorageServiceServer() {
}

// UnsafeManifestStorageServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to ManifestStorageServiceServer will
// result in compilation errors.
type UnsafeManifestStorageServiceServer interface {
	mustEmbedUnimplementedManifestStorageServiceServer()
}

func RegisterManifestStorageServiceServer(s grpc.ServiceRegistrar, srv ManifestStorageServiceServer) {
	s.RegisterService(&ManifestStorageService_ServiceDesc, srv)
}

func _ManifestStorageService_Store_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(StoreRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ManifestStorageServiceServer).Store(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/depscloud.api.v1beta.ManifestStorageService/Store",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ManifestStorageServiceServer).Store(ctx, req.(*StoreRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// ManifestStorageService_ServiceDesc is the grpc.ServiceDesc for ManifestStorageService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var ManifestStorageService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "depscloud.api.v1beta.ManifestStorageService",
	HandlerType: (*ManifestStorageServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Store",
			Handler:    _ManifestStorageService_Store_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "depscloud/api/v1beta/manifest.proto",
}
