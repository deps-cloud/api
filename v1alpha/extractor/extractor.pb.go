// Code generated by protoc-gen-gogo. DO NOT EDIT.
// source: extractor.proto

package api

import (
	context "context"
	fmt "fmt"
	deps "github.com/deps-cloud/api/v1alpha/deps"
	proto "github.com/gogo/protobuf/proto"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.GoGoProtoPackageIsVersion3 // please upgrade the proto package

type ExtractRequest struct {
	Separator            string            `protobuf:"bytes,1,opt,name=separator,proto3" json:"separator,omitempty"`
	FileContents         map[string]string `protobuf:"bytes,2,rep,name=fileContents,proto3" json:"fileContents,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	Url                  string            `protobuf:"bytes,3,opt,name=url,proto3" json:"url,omitempty"`
	XXX_NoUnkeyedLiteral struct{}          `json:"-"`
	XXX_unrecognized     []byte            `json:"-"`
	XXX_sizecache        int32             `json:"-"`
}

func (m *ExtractRequest) Reset()         { *m = ExtractRequest{} }
func (m *ExtractRequest) String() string { return proto.CompactTextString(m) }
func (*ExtractRequest) ProtoMessage()    {}
func (*ExtractRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_39fd19a8b349f81d, []int{0}
}
func (m *ExtractRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ExtractRequest.Unmarshal(m, b)
}
func (m *ExtractRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ExtractRequest.Marshal(b, m, deterministic)
}
func (m *ExtractRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ExtractRequest.Merge(m, src)
}
func (m *ExtractRequest) XXX_Size() int {
	return xxx_messageInfo_ExtractRequest.Size(m)
}
func (m *ExtractRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_ExtractRequest.DiscardUnknown(m)
}

var xxx_messageInfo_ExtractRequest proto.InternalMessageInfo

func (m *ExtractRequest) GetSeparator() string {
	if m != nil {
		return m.Separator
	}
	return ""
}

func (m *ExtractRequest) GetFileContents() map[string]string {
	if m != nil {
		return m.FileContents
	}
	return nil
}

func (m *ExtractRequest) GetUrl() string {
	if m != nil {
		return m.Url
	}
	return ""
}

type ExtractResponse struct {
	ManagementFiles      []*deps.DependencyManagementFile `protobuf:"bytes,1,rep,name=managementFiles,proto3" json:"managementFiles,omitempty"`
	XXX_NoUnkeyedLiteral struct{}                         `json:"-"`
	XXX_unrecognized     []byte                           `json:"-"`
	XXX_sizecache        int32                            `json:"-"`
}

func (m *ExtractResponse) Reset()         { *m = ExtractResponse{} }
func (m *ExtractResponse) String() string { return proto.CompactTextString(m) }
func (*ExtractResponse) ProtoMessage()    {}
func (*ExtractResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_39fd19a8b349f81d, []int{1}
}
func (m *ExtractResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ExtractResponse.Unmarshal(m, b)
}
func (m *ExtractResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ExtractResponse.Marshal(b, m, deterministic)
}
func (m *ExtractResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ExtractResponse.Merge(m, src)
}
func (m *ExtractResponse) XXX_Size() int {
	return xxx_messageInfo_ExtractResponse.Size(m)
}
func (m *ExtractResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_ExtractResponse.DiscardUnknown(m)
}

var xxx_messageInfo_ExtractResponse proto.InternalMessageInfo

func (m *ExtractResponse) GetManagementFiles() []*deps.DependencyManagementFile {
	if m != nil {
		return m.ManagementFiles
	}
	return nil
}

type MatchRequest struct {
	Separator            string   `protobuf:"bytes,1,opt,name=separator,proto3" json:"separator,omitempty"`
	Paths                []string `protobuf:"bytes,2,rep,name=paths,proto3" json:"paths,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *MatchRequest) Reset()         { *m = MatchRequest{} }
func (m *MatchRequest) String() string { return proto.CompactTextString(m) }
func (*MatchRequest) ProtoMessage()    {}
func (*MatchRequest) Descriptor() ([]byte, []int) {
	return fileDescriptor_39fd19a8b349f81d, []int{2}
}
func (m *MatchRequest) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_MatchRequest.Unmarshal(m, b)
}
func (m *MatchRequest) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_MatchRequest.Marshal(b, m, deterministic)
}
func (m *MatchRequest) XXX_Merge(src proto.Message) {
	xxx_messageInfo_MatchRequest.Merge(m, src)
}
func (m *MatchRequest) XXX_Size() int {
	return xxx_messageInfo_MatchRequest.Size(m)
}
func (m *MatchRequest) XXX_DiscardUnknown() {
	xxx_messageInfo_MatchRequest.DiscardUnknown(m)
}

var xxx_messageInfo_MatchRequest proto.InternalMessageInfo

func (m *MatchRequest) GetSeparator() string {
	if m != nil {
		return m.Separator
	}
	return ""
}

func (m *MatchRequest) GetPaths() []string {
	if m != nil {
		return m.Paths
	}
	return nil
}

type MatchResponse struct {
	MatchedPaths         []string `protobuf:"bytes,1,rep,name=matchedPaths,proto3" json:"matchedPaths,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *MatchResponse) Reset()         { *m = MatchResponse{} }
func (m *MatchResponse) String() string { return proto.CompactTextString(m) }
func (*MatchResponse) ProtoMessage()    {}
func (*MatchResponse) Descriptor() ([]byte, []int) {
	return fileDescriptor_39fd19a8b349f81d, []int{3}
}
func (m *MatchResponse) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_MatchResponse.Unmarshal(m, b)
}
func (m *MatchResponse) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_MatchResponse.Marshal(b, m, deterministic)
}
func (m *MatchResponse) XXX_Merge(src proto.Message) {
	xxx_messageInfo_MatchResponse.Merge(m, src)
}
func (m *MatchResponse) XXX_Size() int {
	return xxx_messageInfo_MatchResponse.Size(m)
}
func (m *MatchResponse) XXX_DiscardUnknown() {
	xxx_messageInfo_MatchResponse.DiscardUnknown(m)
}

var xxx_messageInfo_MatchResponse proto.InternalMessageInfo

func (m *MatchResponse) GetMatchedPaths() []string {
	if m != nil {
		return m.MatchedPaths
	}
	return nil
}

func init() {
	proto.RegisterType((*ExtractRequest)(nil), "cloud.deps.api.v1alpha.extractor.ExtractRequest")
	proto.RegisterMapType((map[string]string)(nil), "cloud.deps.api.v1alpha.extractor.ExtractRequest.FileContentsEntry")
	proto.RegisterType((*ExtractResponse)(nil), "cloud.deps.api.v1alpha.extractor.ExtractResponse")
	proto.RegisterType((*MatchRequest)(nil), "cloud.deps.api.v1alpha.extractor.MatchRequest")
	proto.RegisterType((*MatchResponse)(nil), "cloud.deps.api.v1alpha.extractor.MatchResponse")
}

func init() { proto.RegisterFile("extractor.proto", fileDescriptor_39fd19a8b349f81d) }

var fileDescriptor_39fd19a8b349f81d = []byte{
	// 466 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x94, 0x93, 0x4d, 0x6f, 0xd3, 0x30,
	0x1c, 0xc6, 0xe5, 0x54, 0x05, 0xd5, 0x14, 0x0a, 0x66, 0x87, 0x28, 0x80, 0x54, 0xe5, 0x80, 0xaa,
	0x49, 0x73, 0xe8, 0x26, 0x24, 0xd4, 0x0b, 0x52, 0xa1, 0xdc, 0x26, 0xa1, 0x1c, 0x77, 0x99, 0xfe,
	0x4b, 0xfe, 0x4b, 0x22, 0x52, 0xdb, 0xd8, 0xce, 0x20, 0x57, 0x3e, 0x01, 0x12, 0x17, 0xbe, 0x0f,
	0x1f, 0x81, 0xaf, 0xc0, 0x85, 0x6f, 0x81, 0xe2, 0x98, 0xad, 0xe5, 0x45, 0x5b, 0x2f, 0x91, 0xfd,
	0xe8, 0x79, 0x1e, 0xff, 0xfc, 0x12, 0x3a, 0xc1, 0x8f, 0x56, 0x43, 0x66, 0xa5, 0xe6, 0x4a, 0x4b,
	0x2b, 0xd9, 0x34, 0xab, 0x65, 0x93, 0xf3, 0x1c, 0x95, 0xe1, 0xa0, 0x2a, 0x7e, 0x31, 0x87, 0x5a,
	0x95, 0xc0, 0x2f, 0x7d, 0xd1, 0xbc, 0xa8, 0x6c, 0xd9, 0x9c, 0xf1, 0x4c, 0xae, 0x93, 0xce, 0x76,
	0xe0, 0x12, 0x09, 0xa8, 0x2a, 0xf1, 0x66, 0x27, 0xbb, 0x4f, 0x5f, 0x1a, 0x9d, 0x6c, 0x44, 0x0a,
	0xad, 0xb2, 0x03, 0xcc, 0xa4, 0x69, 0x8d, 0x45, 0x3f, 0x2d, 0xc0, 0xe2, 0x07, 0x68, 0x13, 0x5b,
	0x56, 0x3a, 0x3f, 0x55, 0xa0, 0x6d, 0x9b, 0x14, 0x52, 0x16, 0x35, 0x82, 0xaa, 0x8c, 0x1f, 0xba,
	0x15, 0x40, 0x08, 0x69, 0xc1, 0x56, 0x52, 0xf8, 0xee, 0xf8, 0x27, 0xa1, 0xf7, 0x56, 0x3d, 0x5c,
	0x8a, 0xef, 0x1b, 0x34, 0x96, 0x3d, 0xa6, 0x23, 0x83, 0x0a, 0x34, 0x58, 0xa9, 0x43, 0x32, 0x25,
	0xb3, 0x51, 0x7a, 0x25, 0xb0, 0x73, 0x3a, 0x3e, 0xaf, 0x6a, 0x7c, 0x25, 0x85, 0x45, 0x61, 0x4d,
	0x18, 0x4c, 0x07, 0xb3, 0x3b, 0x87, 0x4b, 0x7e, 0xdd, 0xc6, 0xf9, 0xf6, 0x2a, 0xfc, 0xcd, 0x46,
	0xc9, 0x4a, 0x58, 0xdd, 0xa6, 0x5b, 0xbd, 0xec, 0x3e, 0x1d, 0x34, 0xba, 0x0e, 0x07, 0x6e, 0xfd,
	0x6e, 0x18, 0xbd, 0xa4, 0x0f, 0xfe, 0x0a, 0x75, 0xb6, 0x77, 0xd8, 0x7a, 0xcc, 0x6e, 0xc8, 0xf6,
	0xe8, 0xf0, 0x02, 0xea, 0x06, 0xc3, 0xc0, 0x69, 0xfd, 0x64, 0x11, 0xbc, 0x20, 0xb1, 0xa6, 0x93,
	0x4b, 0x08, 0xa3, 0xa4, 0x30, 0xc8, 0x4e, 0xe9, 0x64, 0x0d, 0x02, 0x0a, 0x5c, 0xa3, 0xb0, 0x5d,
	0xbb, 0x09, 0x89, 0xdb, 0xd0, 0xf3, 0xff, 0x6d, 0xc8, 0x09, 0xaf, 0x51, 0xa1, 0xc8, 0x51, 0x64,
	0xed, 0xf1, 0x56, 0x3a, 0xfd, 0xb3, 0x2d, 0x5e, 0xd2, 0xf1, 0x31, 0xd8, 0xac, 0xbc, 0xd9, 0xe1,
	0xee, 0xd1, 0xa1, 0x02, 0x5b, 0xf6, 0xa7, 0x3a, 0x4a, 0xfb, 0x49, 0x7c, 0x44, 0xef, 0xfa, 0x0e,
	0x4f, 0x1d, 0xd3, 0xf1, 0xba, 0x13, 0x30, 0x7f, 0xeb, 0xdc, 0xc4, 0xb9, 0xb7, 0xb4, 0xc3, 0x6f,
	0x01, 0x7d, 0x78, 0x85, 0xb9, 0xfa, 0x7d, 0x0d, 0xec, 0x33, 0xa1, 0x43, 0xd7, 0xc6, 0xf8, 0xf5,
	0x77, 0xb6, 0x89, 0x1e, 0x25, 0x37, 0xf6, 0xf7, 0x98, 0xf1, 0xd3, 0x4f, 0xdf, 0x7f, 0x7c, 0x09,
	0xa6, 0xf1, 0xa3, 0xcd, 0x97, 0xdd, 0x03, 0x55, 0x68, 0x12, 0x87, 0xbb, 0x20, 0xfb, 0xec, 0x2b,
	0xa1, 0xb7, 0x3d, 0x20, 0x7b, 0xb6, 0xeb, 0x43, 0x8a, 0xe6, 0x3b, 0x24, 0x3c, 0xd8, 0xcc, 0x81,
	0xc5, 0xf1, 0x93, 0x7f, 0x83, 0xf9, 0xe0, 0x82, 0xec, 0x2f, 0x87, 0x27, 0x03, 0x50, 0xd5, 0xd9,
	0x2d, 0xf7, 0xb3, 0x1c, 0xfd, 0x0a, 0x00, 0x00, 0xff, 0xff, 0xb2, 0xbc, 0x1f, 0xff, 0xf0, 0x03,
	0x00, 0x00,
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConn

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion4

// DependencyExtractorClient is the client API for DependencyExtractor service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type DependencyExtractorClient interface {
	Match(ctx context.Context, in *MatchRequest, opts ...grpc.CallOption) (*MatchResponse, error)
	Extract(ctx context.Context, in *ExtractRequest, opts ...grpc.CallOption) (*ExtractResponse, error)
}

type dependencyExtractorClient struct {
	cc *grpc.ClientConn
}

func NewDependencyExtractorClient(cc *grpc.ClientConn) DependencyExtractorClient {
	return &dependencyExtractorClient{cc}
}

func (c *dependencyExtractorClient) Match(ctx context.Context, in *MatchRequest, opts ...grpc.CallOption) (*MatchResponse, error) {
	out := new(MatchResponse)
	err := c.cc.Invoke(ctx, "/cloud.deps.api.v1alpha.extractor.DependencyExtractor/Match", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *dependencyExtractorClient) Extract(ctx context.Context, in *ExtractRequest, opts ...grpc.CallOption) (*ExtractResponse, error) {
	out := new(ExtractResponse)
	err := c.cc.Invoke(ctx, "/cloud.deps.api.v1alpha.extractor.DependencyExtractor/Extract", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// DependencyExtractorServer is the server API for DependencyExtractor service.
type DependencyExtractorServer interface {
	Match(context.Context, *MatchRequest) (*MatchResponse, error)
	Extract(context.Context, *ExtractRequest) (*ExtractResponse, error)
}

// UnimplementedDependencyExtractorServer can be embedded to have forward compatible implementations.
type UnimplementedDependencyExtractorServer struct {
}

func (*UnimplementedDependencyExtractorServer) Match(ctx context.Context, req *MatchRequest) (*MatchResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Match not implemented")
}
func (*UnimplementedDependencyExtractorServer) Extract(ctx context.Context, req *ExtractRequest) (*ExtractResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Extract not implemented")
}

func RegisterDependencyExtractorServer(s *grpc.Server, srv DependencyExtractorServer) {
	s.RegisterService(&_DependencyExtractor_serviceDesc, srv)
}

func _DependencyExtractor_Match_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(MatchRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DependencyExtractorServer).Match(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/cloud.deps.api.v1alpha.extractor.DependencyExtractor/Match",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DependencyExtractorServer).Match(ctx, req.(*MatchRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DependencyExtractor_Extract_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ExtractRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DependencyExtractorServer).Extract(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/cloud.deps.api.v1alpha.extractor.DependencyExtractor/Extract",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DependencyExtractorServer).Extract(ctx, req.(*ExtractRequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _DependencyExtractor_serviceDesc = grpc.ServiceDesc{
	ServiceName: "cloud.deps.api.v1alpha.extractor.DependencyExtractor",
	HandlerType: (*DependencyExtractorServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "Match",
			Handler:    _DependencyExtractor_Match_Handler,
		},
		{
			MethodName: "Extract",
			Handler:    _DependencyExtractor_Extract_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "extractor.proto",
}