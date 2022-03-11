#ifndef analyzers_ONNXRuntime_h
#define analyzers_ONNXRuntime_h

//#include <vector>
//#include "Math/Vector4D.h"
#include "ROOT/RVec.hxx"
//#include "TObject.h"
//#include "edm4hep/MCParticleData.h"
#include "core/session/onnxruntime_cxx_api.h"

class ONNXRuntime {
public:
  ONNXRuntime() = default;
  explicit ONNXRuntime(const std::string& model_path, const std::string& preprocess_json="");
  ONNXRuntime(const ONNXRuntime&) = delete;
  ~ONNXRuntime();

  ONNXRuntime& operator=(const ONNXRuntime&) = delete;

  ROOT::VecOps::RVec<float> operator()(ROOT::VecOps::RVec<int> in);

private:
  ROOT::VecOps::RVec<ROOT::VecOps::RVec<float> > run() const;
};


#endif
