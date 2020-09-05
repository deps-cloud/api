// Code generated by protoc-gen-dts. DO NOT EDIT.
// source: graphstore/api/v1beta/graphstore.proto

import {
  ChannelCredentials, 
  Client, 
  ClientUnaryCall,
  ClientReadableStream,
  ClientWritableStream,
  ClientDuplexStream,
  Metadata,
  ServerUnaryCall,
  ServerReadableStream,
  ServerWritableStream,
  ServerDuplexStream,
  ServiceDefinition,
} from "@grpc/grpc-js";

import {
  Any,
} from "@grpc/grpc-js/src/generated/google/protobuf/any";

import {
  Timestamp,
} from "@grpc/grpc-js/src/generated/google/protobuf/timestamp";

export enum Encoding {
  UNSPECIFIED = 0,
  JSON = 1,
  PROTOCOL_BUFFERS = 2,
}

export interface GraphItem {
  k1: Buffer;
  k2: Buffer;
  k3: Buffer;
  kind: string;
  encoding: Encoding;
  data: Buffer;
  dateDeleted: Timestamp;
  lastModified: Timestamp;
}

export interface Node {
  key: Buffer;
  body: Any;
}

export interface Edge {
  fromKey: Buffer;
  toKey: Buffer;
  key: Buffer;
  body: Any;
}

export interface PutRequest {
  nodes: Array<Node>;
  edges: Array<Edge>;
}

export interface PutResponse {
}

export interface DeleteRequest {
  nodes: Array<Node>;
  edges: Array<Edge>;
}

export interface DeleteResponse {
}

export interface ListRequest {
  parent: string;
  pageSize: number;
  pageToken: string;
  kind: string;
}

export interface ListResponse {
  nextPageToken: string;
  nodes: Array<Node>;
  edges: Array<Edge>;
}

export interface Neighbor {
  node: Node;
  edges: Array<Edge>;
}

export interface EdgeFilter {
  body: Any;
}

export interface NeighborsRequest {
  node: Node;
  from: Node;
  to: Node;
  filter: Array<EdgeFilter>;
}

export interface NeighborsResponse {
  neighbors: Array<Neighbor>;
}

export interface TraverseRequest {
  cancel: boolean;
  request: NeighborsRequest;
}

export interface TraverseResponse {
  request: NeighborsRequest;
  response: NeighborsResponse;
}

export interface IGraphStore { 
  put(call: ServerUnaryCall<PutRequest, PutResponse>, callback: (error: Error, response: PutResponse) => void): void; 
  delete(call: ServerUnaryCall<DeleteRequest, DeleteResponse>, callback: (error: Error, response: DeleteResponse) => void): void; 
  list(call: ServerUnaryCall<ListRequest, ListResponse>, callback: (error: Error, response: ListResponse) => void): void; 
  neighbors(call: ServerUnaryCall<NeighborsRequest, NeighborsResponse>, callback: (error: Error, response: NeighborsResponse) => void): void;
  traverse(call: ServerDuplexStream<TraverseRequest, TraverseResponse>): void;
}

export class GraphStore extends Client {
  public static service: ServiceDefinition<IGraphStore>;

  constructor(address: string, credentials: ChannelCredentials, options?: object); 
  public put(request: PutRequest, callback: (error: Error, response: PutResponse) => void): void;
  public put(request: PutRequest, metadata: Metadata, callback: (error: Error, response: PutResponse) => void): void; 
  public delete(request: DeleteRequest, callback: (error: Error, response: DeleteResponse) => void): void;
  public delete(request: DeleteRequest, metadata: Metadata, callback: (error: Error, response: DeleteResponse) => void): void; 
  public list(request: ListRequest, callback: (error: Error, response: ListResponse) => void): void;
  public list(request: ListRequest, metadata: Metadata, callback: (error: Error, response: ListResponse) => void): void; 
  public neighbors(request: NeighborsRequest, callback: (error: Error, response: NeighborsResponse) => void): void;
  public neighbors(request: NeighborsRequest, metadata: Metadata, callback: (error: Error, response: NeighborsResponse) => void): void;
  public traverse(): ClientDuplexStream<TraverseRequest, TraverseResponse>
  public traverse(metadata: Metadata): ClientDuplexStream<TraverseRequest, TraverseResponse>
}

