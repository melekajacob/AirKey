#include <node.h>
#include <uv.h>

#include "arduino.cpp"

namespace letterPredictorModule {
	using v8::Context;
	using v8::Function;
	using v8::FunctionCallbackInfo;
	using v8::Isolate;
	using v8::Local;
	using v8::Persistent;
	using v8::Null;
	using v8::NumberObject;
	using v8::Object;
	using v8::Value;

	uv_async_t asyncCallback;
	uv_loop_t *loop;
	uv_work_t request;

	mutex callbackLock;	
	Persistent<Function> connectionReadyCallback;

	void connectionReady() {
		 Isolate* isolate = args.GetIsolate();

  		Local<Context> context = isolate->GetCurrentContext();
  		Local<FunctionTemplate> tpl = FunctionTemplate::New(isolate, MyFunction);
  		Local<Function> fn = tpl->GetFunction(context).ToLocalChecked();

  // omit this to make it anonymous
  		fn->SetName(String::NewFromUtf8(isolate, "theFunction", NewStringType::kNormal).ToLocalChecked());

	}

	void openConnection(const FunctionCallbackInfo<Value>& args) {
		// Create the connection to the arduino (takes in a callback for arduino ready, callback should take in a fucntion)
		// Creates a worker that opens a thread that intiates the connection and 
		Isolate* isolate = args.GetIsolate();

		Local<Function> connectionReadyCallback = Local<Function>::Cast(args[0]);
  		const unsigned argc = 1;
  		Local<Value> argv[argc] = {String::NewFromUtf8(isolate, "hello world", NewStringType::kNormal).ToLocalChecked() };
  		cb->Call(context, Null(isolate), argc, argv).ToLocalChecked();
		args.GetReturnValue().Set(fn);
	}


	void Initialize(Local<Object> exports) {
		stopped = true;

		NODE_SET_METHOD(exports, "openConnection", openConnection);
		NODE_SET_METHOD(exports, "openConnection", openConnection);
	}

	NODE_MODULE(NODE_GYP_MODULE_NAME, Initialize);
}