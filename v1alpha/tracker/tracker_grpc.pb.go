// Code generated by protoc-gen-go-grpc. DO NOT EDIT.

package tracker

import (
	context "context"
	schema "github.com/depscloud/api/v1alpha/schema"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// SourceServiceClient is the client API for SourceService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type SourceServiceClient interface {
	List(ctx context.Context, in *ListRequest, opts ...grpc.CallOption) (*ListSourceResponse, error)
	Track(ctx context.Context, in *SourceRequest, opts ...grpc.CallOption) (*TrackResponse, error)
}

type sourceServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewSourceServiceClient(cc grpc.ClientConnInterface) SourceServiceClient {
	return &sourceServiceClient{cc}
}

func (c *sourceServiceClient) List(ctx context.Context, in *ListRequest, opts ...grpc.CallOption) (*ListSourceResponse, error) {
	out := new(ListSourceResponse)
	err := c.cc.Invoke(ctx, "/cloud.deps.api.v1alpha.tracker.SourceService/List", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *sourceServiceClient) Track(ctx context.Context, in *SourceRequest, opts ...grpc.CallOption) (*TrackResponse, error) {
	out := new(TrackResponse)
	err := c.cc.Invoke(ctx, "/cloud.deps.api.v1alpha.tracker.SourceService/Track", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// SourceServiceServer is the server API for SourceService service.
// All implementations must embed UnimplementedSourceServiceServer
// for forward compatibility
type SourceServiceServer interface {
	List(context.Context, *ListRequest) (*ListSourceResponse, error)
	Track(context.Context, *SourceRequest) (*TrackResponse, error)
	mustEmbedUnimplementedSourceServiceServer()
}

// UnimplementedSourceServiceServer must be embedded to have forward compatible implementations.
type UnimplementedSourceServiceServer struct {
}

func (UnimplementedSourceServiceServer) List(context.Context, *ListRequest) (*ListSourceResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method List not implemented")
}
func (UnimplementedSourceServiceServer) Track(context.Context, *SourceRequest) (*TrackResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Track not implemented")
}
func (UnimplementedSourceServiceServer) mustEmbedUnimplementedSourceServiceServer() {}

// UnsafeSourceServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to SourceServiceServer will
// result in compilation errors.
type UnsafeSourceServiceServer interface {
	mustEmbedUnimplementedSourceServiceServer()
}

func RegisterSourceServiceServer(s grpc.ServiceRegistrar, srv SourceServiceServer) {
	s.RegisterService(&SourceService_ServiceDesc, srv)
}

func _SourceService_List_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SourceServiceServer).List(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/cloud.deps.api.v1alpha.tracker.SourceService/List",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SourceServiceServer).List(ctx, req.(*ListRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _SourceService_Track_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SourceRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(SourceServiceServer).Track(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/cloud.deps.api.v1alpha.tracker.SourceService/Track",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(SourceServiceServer).Track(ctx, req.(*SourceRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// SourceService_ServiceDesc is the grpc.ServiceDesc for SourceService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var SourceService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "cloud.deps.api.v1alpha.tracker.SourceService",
	HandlerType: (*SourceServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "List",
			Handler:    _SourceService_List_Handler,
		},
		{
			MethodName: "Track",
			Handler:    _SourceService_Track_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "depscloud_api/v1alpha/tracker/tracker.proto",
}

// ModuleServiceClient is the client API for ModuleService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type ModuleServiceClient interface {
	List(ctx context.Context, in *ListRequest, opts ...grpc.CallOption) (*ListModuleResponse, error)
	ListSources(ctx context.Context, in *schema.Module, opts ...grpc.CallOption) (*ListSourcesResponse, error)
	ListManaged(ctx context.Context, in *schema.Source, opts ...grpc.CallOption) (*ListManagedResponse, error)
}

type moduleServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewModuleServiceClient(cc grpc.ClientConnInterface) ModuleServiceClient {
	return &moduleServiceClient{cc}
}

func (c *moduleServiceClient) List(ctx context.Context, in *ListRequest, opts ...grpc.CallOption) (*ListModuleResponse, error) {
	out := new(ListModuleResponse)
	err := c.cc.Invoke(ctx, "/cloud.deps.api.v1alpha.tracker.ModuleService/List", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *moduleServiceClient) ListSources(ctx context.Context, in *schema.Module, opts ...grpc.CallOption) (*ListSourcesResponse, error) {
	out := new(ListSourcesResponse)
	err := c.cc.Invoke(ctx, "/cloud.deps.api.v1alpha.tracker.ModuleService/ListSources", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *moduleServiceClient) ListManaged(ctx context.Context, in *schema.Source, opts ...grpc.CallOption) (*ListManagedResponse, error) {
	out := new(ListManagedResponse)
	err := c.cc.Invoke(ctx, "/cloud.deps.api.v1alpha.tracker.ModuleService/ListManaged", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// ModuleServiceServer is the server API for ModuleService service.
// All implementations must embed UnimplementedModuleServiceServer
// for forward compatibility
type ModuleServiceServer interface {
	List(context.Context, *ListRequest) (*ListModuleResponse, error)
	ListSources(context.Context, *schema.Module) (*ListSourcesResponse, error)
	ListManaged(context.Context, *schema.Source) (*ListManagedResponse, error)
	mustEmbedUnimplementedModuleServiceServer()
}

// UnimplementedModuleServiceServer must be embedded to have forward compatible implementations.
type UnimplementedModuleServiceServer struct {
}

func (UnimplementedModuleServiceServer) List(context.Context, *ListRequest) (*ListModuleResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method List not implemented")
}
func (UnimplementedModuleServiceServer) ListSources(context.Context, *schema.Module) (*ListSourcesResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListSources not implemented")
}
func (UnimplementedModuleServiceServer) ListManaged(context.Context, *schema.Source) (*ListManagedResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListManaged not implemented")
}
func (UnimplementedModuleServiceServer) mustEmbedUnimplementedModuleServiceServer() {}

// UnsafeModuleServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to ModuleServiceServer will
// result in compilation errors.
type UnsafeModuleServiceServer interface {
	mustEmbedUnimplementedModuleServiceServer()
}

func RegisterModuleServiceServer(s grpc.ServiceRegistrar, srv ModuleServiceServer) {
	s.RegisterService(&ModuleService_ServiceDesc, srv)
}

func _ModuleService_List_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ModuleServiceServer).List(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/cloud.deps.api.v1alpha.tracker.ModuleService/List",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ModuleServiceServer).List(ctx, req.(*ListRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _ModuleService_ListSources_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(schema.Module)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ModuleServiceServer).ListSources(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/cloud.deps.api.v1alpha.tracker.ModuleService/ListSources",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ModuleServiceServer).ListSources(ctx, req.(*schema.Module))
	}
	return interceptor(ctx, in, info, handler)
}

func _ModuleService_ListManaged_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(schema.Source)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(ModuleServiceServer).ListManaged(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/cloud.deps.api.v1alpha.tracker.ModuleService/ListManaged",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(ModuleServiceServer).ListManaged(ctx, req.(*schema.Source))
	}
	return interceptor(ctx, in, info, handler)
}

// ModuleService_ServiceDesc is the grpc.ServiceDesc for ModuleService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var ModuleService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "cloud.deps.api.v1alpha.tracker.ModuleService",
	HandlerType: (*ModuleServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "List",
			Handler:    _ModuleService_List_Handler,
		},
		{
			MethodName: "ListSources",
			Handler:    _ModuleService_ListSources_Handler,
		},
		{
			MethodName: "ListManaged",
			Handler:    _ModuleService_ListManaged_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "depscloud_api/v1alpha/tracker/tracker.proto",
}

// DependencyServiceClient is the client API for DependencyService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type DependencyServiceClient interface {
	ListDependents(ctx context.Context, in *DependencyRequest, opts ...grpc.CallOption) (*ListDependentsResponse, error)
	ListDependencies(ctx context.Context, in *DependencyRequest, opts ...grpc.CallOption) (*ListDependenciesResponse, error)
}

type dependencyServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewDependencyServiceClient(cc grpc.ClientConnInterface) DependencyServiceClient {
	return &dependencyServiceClient{cc}
}

func (c *dependencyServiceClient) ListDependents(ctx context.Context, in *DependencyRequest, opts ...grpc.CallOption) (*ListDependentsResponse, error) {
	out := new(ListDependentsResponse)
	err := c.cc.Invoke(ctx, "/cloud.deps.api.v1alpha.tracker.DependencyService/ListDependents", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *dependencyServiceClient) ListDependencies(ctx context.Context, in *DependencyRequest, opts ...grpc.CallOption) (*ListDependenciesResponse, error) {
	out := new(ListDependenciesResponse)
	err := c.cc.Invoke(ctx, "/cloud.deps.api.v1alpha.tracker.DependencyService/ListDependencies", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// DependencyServiceServer is the server API for DependencyService service.
// All implementations must embed UnimplementedDependencyServiceServer
// for forward compatibility
type DependencyServiceServer interface {
	ListDependents(context.Context, *DependencyRequest) (*ListDependentsResponse, error)
	ListDependencies(context.Context, *DependencyRequest) (*ListDependenciesResponse, error)
	mustEmbedUnimplementedDependencyServiceServer()
}

// UnimplementedDependencyServiceServer must be embedded to have forward compatible implementations.
type UnimplementedDependencyServiceServer struct {
}

func (UnimplementedDependencyServiceServer) ListDependents(context.Context, *DependencyRequest) (*ListDependentsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListDependents not implemented")
}
func (UnimplementedDependencyServiceServer) ListDependencies(context.Context, *DependencyRequest) (*ListDependenciesResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListDependencies not implemented")
}
func (UnimplementedDependencyServiceServer) mustEmbedUnimplementedDependencyServiceServer() {}

// UnsafeDependencyServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to DependencyServiceServer will
// result in compilation errors.
type UnsafeDependencyServiceServer interface {
	mustEmbedUnimplementedDependencyServiceServer()
}

func RegisterDependencyServiceServer(s grpc.ServiceRegistrar, srv DependencyServiceServer) {
	s.RegisterService(&DependencyService_ServiceDesc, srv)
}

func _DependencyService_ListDependents_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DependencyRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DependencyServiceServer).ListDependents(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/cloud.deps.api.v1alpha.tracker.DependencyService/ListDependents",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DependencyServiceServer).ListDependents(ctx, req.(*DependencyRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DependencyService_ListDependencies_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DependencyRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DependencyServiceServer).ListDependencies(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/cloud.deps.api.v1alpha.tracker.DependencyService/ListDependencies",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DependencyServiceServer).ListDependencies(ctx, req.(*DependencyRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// DependencyService_ServiceDesc is the grpc.ServiceDesc for DependencyService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var DependencyService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "cloud.deps.api.v1alpha.tracker.DependencyService",
	HandlerType: (*DependencyServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "ListDependents",
			Handler:    _DependencyService_ListDependents_Handler,
		},
		{
			MethodName: "ListDependencies",
			Handler:    _DependencyService_ListDependencies_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "depscloud_api/v1alpha/tracker/tracker.proto",
}

// SearchServiceClient is the client API for SearchService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type SearchServiceClient interface {
	Search(ctx context.Context, opts ...grpc.CallOption) (SearchService_SearchClient, error)
	BreadthFirstSearch(ctx context.Context, opts ...grpc.CallOption) (SearchService_BreadthFirstSearchClient, error)
	DepthFirstSearch(ctx context.Context, opts ...grpc.CallOption) (SearchService_DepthFirstSearchClient, error)
}

type searchServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewSearchServiceClient(cc grpc.ClientConnInterface) SearchServiceClient {
	return &searchServiceClient{cc}
}

func (c *searchServiceClient) Search(ctx context.Context, opts ...grpc.CallOption) (SearchService_SearchClient, error) {
	stream, err := c.cc.NewStream(ctx, &SearchService_ServiceDesc.Streams[0], "/cloud.deps.api.v1alpha.tracker.SearchService/Search", opts...)
	if err != nil {
		return nil, err
	}
	x := &searchServiceSearchClient{stream}
	return x, nil
}

type SearchService_SearchClient interface {
	Send(*SearchRequest) error
	Recv() (*SearchResponse, error)
	grpc.ClientStream
}

type searchServiceSearchClient struct {
	grpc.ClientStream
}

func (x *searchServiceSearchClient) Send(m *SearchRequest) error {
	return x.ClientStream.SendMsg(m)
}

func (x *searchServiceSearchClient) Recv() (*SearchResponse, error) {
	m := new(SearchResponse)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *searchServiceClient) BreadthFirstSearch(ctx context.Context, opts ...grpc.CallOption) (SearchService_BreadthFirstSearchClient, error) {
	stream, err := c.cc.NewStream(ctx, &SearchService_ServiceDesc.Streams[1], "/cloud.deps.api.v1alpha.tracker.SearchService/BreadthFirstSearch", opts...)
	if err != nil {
		return nil, err
	}
	x := &searchServiceBreadthFirstSearchClient{stream}
	return x, nil
}

type SearchService_BreadthFirstSearchClient interface {
	Send(*SearchRequest) error
	Recv() (*SearchResponse, error)
	grpc.ClientStream
}

type searchServiceBreadthFirstSearchClient struct {
	grpc.ClientStream
}

func (x *searchServiceBreadthFirstSearchClient) Send(m *SearchRequest) error {
	return x.ClientStream.SendMsg(m)
}

func (x *searchServiceBreadthFirstSearchClient) Recv() (*SearchResponse, error) {
	m := new(SearchResponse)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *searchServiceClient) DepthFirstSearch(ctx context.Context, opts ...grpc.CallOption) (SearchService_DepthFirstSearchClient, error) {
	stream, err := c.cc.NewStream(ctx, &SearchService_ServiceDesc.Streams[2], "/cloud.deps.api.v1alpha.tracker.SearchService/DepthFirstSearch", opts...)
	if err != nil {
		return nil, err
	}
	x := &searchServiceDepthFirstSearchClient{stream}
	return x, nil
}

type SearchService_DepthFirstSearchClient interface {
	Send(*SearchRequest) error
	Recv() (*SearchResponse, error)
	grpc.ClientStream
}

type searchServiceDepthFirstSearchClient struct {
	grpc.ClientStream
}

func (x *searchServiceDepthFirstSearchClient) Send(m *SearchRequest) error {
	return x.ClientStream.SendMsg(m)
}

func (x *searchServiceDepthFirstSearchClient) Recv() (*SearchResponse, error) {
	m := new(SearchResponse)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

// SearchServiceServer is the server API for SearchService service.
// All implementations must embed UnimplementedSearchServiceServer
// for forward compatibility
type SearchServiceServer interface {
	Search(SearchService_SearchServer) error
	BreadthFirstSearch(SearchService_BreadthFirstSearchServer) error
	DepthFirstSearch(SearchService_DepthFirstSearchServer) error
	mustEmbedUnimplementedSearchServiceServer()
}

// UnimplementedSearchServiceServer must be embedded to have forward compatible implementations.
type UnimplementedSearchServiceServer struct {
}

func (UnimplementedSearchServiceServer) Search(SearchService_SearchServer) error {
	return status.Errorf(codes.Unimplemented, "method Search not implemented")
}
func (UnimplementedSearchServiceServer) BreadthFirstSearch(SearchService_BreadthFirstSearchServer) error {
	return status.Errorf(codes.Unimplemented, "method BreadthFirstSearch not implemented")
}
func (UnimplementedSearchServiceServer) DepthFirstSearch(SearchService_DepthFirstSearchServer) error {
	return status.Errorf(codes.Unimplemented, "method DepthFirstSearch not implemented")
}
func (UnimplementedSearchServiceServer) mustEmbedUnimplementedSearchServiceServer() {}

// UnsafeSearchServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to SearchServiceServer will
// result in compilation errors.
type UnsafeSearchServiceServer interface {
	mustEmbedUnimplementedSearchServiceServer()
}

func RegisterSearchServiceServer(s grpc.ServiceRegistrar, srv SearchServiceServer) {
	s.RegisterService(&SearchService_ServiceDesc, srv)
}

func _SearchService_Search_Handler(srv interface{}, stream grpc.ServerStream) error {
	return srv.(SearchServiceServer).Search(&searchServiceSearchServer{stream})
}

type SearchService_SearchServer interface {
	Send(*SearchResponse) error
	Recv() (*SearchRequest, error)
	grpc.ServerStream
}

type searchServiceSearchServer struct {
	grpc.ServerStream
}

func (x *searchServiceSearchServer) Send(m *SearchResponse) error {
	return x.ServerStream.SendMsg(m)
}

func (x *searchServiceSearchServer) Recv() (*SearchRequest, error) {
	m := new(SearchRequest)
	if err := x.ServerStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func _SearchService_BreadthFirstSearch_Handler(srv interface{}, stream grpc.ServerStream) error {
	return srv.(SearchServiceServer).BreadthFirstSearch(&searchServiceBreadthFirstSearchServer{stream})
}

type SearchService_BreadthFirstSearchServer interface {
	Send(*SearchResponse) error
	Recv() (*SearchRequest, error)
	grpc.ServerStream
}

type searchServiceBreadthFirstSearchServer struct {
	grpc.ServerStream
}

func (x *searchServiceBreadthFirstSearchServer) Send(m *SearchResponse) error {
	return x.ServerStream.SendMsg(m)
}

func (x *searchServiceBreadthFirstSearchServer) Recv() (*SearchRequest, error) {
	m := new(SearchRequest)
	if err := x.ServerStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func _SearchService_DepthFirstSearch_Handler(srv interface{}, stream grpc.ServerStream) error {
	return srv.(SearchServiceServer).DepthFirstSearch(&searchServiceDepthFirstSearchServer{stream})
}

type SearchService_DepthFirstSearchServer interface {
	Send(*SearchResponse) error
	Recv() (*SearchRequest, error)
	grpc.ServerStream
}

type searchServiceDepthFirstSearchServer struct {
	grpc.ServerStream
}

func (x *searchServiceDepthFirstSearchServer) Send(m *SearchResponse) error {
	return x.ServerStream.SendMsg(m)
}

func (x *searchServiceDepthFirstSearchServer) Recv() (*SearchRequest, error) {
	m := new(SearchRequest)
	if err := x.ServerStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

// SearchService_ServiceDesc is the grpc.ServiceDesc for SearchService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var SearchService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "cloud.deps.api.v1alpha.tracker.SearchService",
	HandlerType: (*SearchServiceServer)(nil),
	Methods:     []grpc.MethodDesc{},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "Search",
			Handler:       _SearchService_Search_Handler,
			ServerStreams: true,
			ClientStreams: true,
		},
		{
			StreamName:    "BreadthFirstSearch",
			Handler:       _SearchService_BreadthFirstSearch_Handler,
			ServerStreams: true,
			ClientStreams: true,
		},
		{
			StreamName:    "DepthFirstSearch",
			Handler:       _SearchService_DepthFirstSearch_Handler,
			ServerStreams: true,
			ClientStreams: true,
		},
	},
	Metadata: "depscloud_api/v1alpha/tracker/tracker.proto",
}