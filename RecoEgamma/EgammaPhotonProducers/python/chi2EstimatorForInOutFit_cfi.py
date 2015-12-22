import FWCore.ParameterSet.Config as cms

import TrackingTools.KalmanUpdators.Chi2MeasurementEstimator_cfi
Chi2MeasurementEstimatorForInOut = TrackingTools.KalmanUpdators.Chi2MeasurementEstimator_cfi.Chi2MeasurementEstimator.clone()
Chi2MeasurementEstimatorForInOut.ComponentName = 'Chi2ForInOut'
Chi2MeasurementEstimatorForInOut.MaxChi2 = 100.
Chi2MeasurementEstimatorForInOut.nSigma = 3.

