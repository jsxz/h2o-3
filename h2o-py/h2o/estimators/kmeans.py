#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from __future__ import absolute_import, division, print_function, unicode_literals

from h2o.estimators.estimator_base import H2OEstimator
from h2o.exceptions import H2OValueError
from h2o.frame import H2OFrame
from h2o.utils.typechecks import assert_is_type, Enum, numeric


class H2OKMeansEstimator(H2OEstimator):
    """
    K-means

    Performs k-means clustering on an H2O dataset.
    """

    algo = "kmeans"
    param_names = {"model_id", "training_frame", "validation_frame", "nfolds", "keep_cross_validation_models",
                   "keep_cross_validation_predictions", "keep_cross_validation_fold_assignment", "fold_assignment",
                   "fold_column", "ignored_columns", "ignore_const_cols", "score_each_iteration", "k", "estimate_k",
                   "user_points", "max_iterations", "standardize", "seed", "init", "max_runtime_secs",
                   "categorical_encoding", "export_checkpoints_dir"}

    def __init__(self, **kwargs):
        super(H2OKMeansEstimator, self).__init__()
        self._parms = {}
        for pname, pvalue in kwargs.items():
            if pname == 'model_id':
                self._id = pvalue
                self._parms["model_id"] = pvalue
            elif pname in self.param_names:
                # Using setattr(...) will invoke type-checking of the arguments
                setattr(self, pname, pvalue)
            else:
                raise H2OValueError("Unknown parameter %s = %r" % (pname, pvalue))

    @property
    def training_frame(self):
        """
        Id of the training data frame.

        Type: ``H2OFrame``.

        :examples:

        >>> prostate = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/prostate/prostate.csv")
        >>> predictors = ["AGE", "RACE", "DPROS", "DCAPS",
        ...               "PSA", "VOL", "GLEASON"]
        >>> train, valid = prostate.split_frame(ratios = [.8], seed = 1234)
        >>> pros_km = H2OKMeansEstimator(seed = 1234)
        >>> pros_km.train(x = predictors,
        ...               training_frame = train,
        ...               validation_frame = valid)
        >>> pros_km.scoring_history()
        """
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        self._parms["training_frame"] = H2OFrame._validate(training_frame, 'training_frame')


    @property
    def validation_frame(self):
        """
        Id of the validation data frame.

        Type: ``H2OFrame``.

        :examples:

        >>> prostate = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/prostate/prostate.csv")
        >>> predictors = ["AGE", "RACE", "DPROS", "DCAPS",
        ...               "PSA", "VOL", "GLEASON"]
        >>> train, valid = prostate.split_frame(ratios = [.8], seed = 1234)
        >>> pros_km = H2OKMeansEstimator(seed = 1234)
        >>> pros_km.train(x = predictors,
        ...               training_frame = train,
        ...               validation_frame = valid)
        >>> pros_km.scoring_history()
        """
        return self._parms.get("validation_frame")

    @validation_frame.setter
    def validation_frame(self, validation_frame):
        self._parms["validation_frame"] = H2OFrame._validate(validation_frame, 'validation_frame')


    @property
    def nfolds(self):
        """
        Number of folds for K-fold cross-validation (0 to disable or >= 2).

        Type: ``int``  (default: ``0``).

        :examples:

        >>> benign = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/logreg/benign.csv")
        >>> predictors = ["AGMT","FNDX","HIGD","DEG","CHK",
        ...               "AGP1","AGMN","LIV","AGLP"]
        >>> train, valid = benign.split_frame(ratios = [.8], seed = 1234)
        >>> benign_km = H2OKMeansEstimator(nfolds = 5, seed = 1234)
        >>> benign_km.train(x = predictors,
        ...                 training_frame = train,
        ...                 validation_frame = valid)
        >>> benign_km.scoring_history()
        """
        return self._parms.get("nfolds")

    @nfolds.setter
    def nfolds(self, nfolds):
        assert_is_type(nfolds, None, int)
        self._parms["nfolds"] = nfolds


    @property
    def keep_cross_validation_models(self):
        """
        Whether to keep the cross-validation models.

        Type: ``bool``  (default: ``True``).

        :examples:

        >>> ozone = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/glm_test/ozone.csv")
        >>> predictors = ["radiation","temperature","wind"]
        >>> train, valid = ozone.split_frame(ratios = [.8], seed = 1234)
        >>> ozone_km = H2OKMeansEstimator(keep_cross_validation_models = True,
        ...                               nfolds = 5,
        ...                               seed = 1234)
        >>> ozone_km.train(x = predictors,
        ...                training_frame = train,
        ...                validation_frame = valid)
        >>> ozone_km.scoring_history()
        """
        return self._parms.get("keep_cross_validation_models")

    @keep_cross_validation_models.setter
    def keep_cross_validation_models(self, keep_cross_validation_models):
        assert_is_type(keep_cross_validation_models, None, bool)
        self._parms["keep_cross_validation_models"] = keep_cross_validation_models


    @property
    def keep_cross_validation_predictions(self):
        """
        Whether to keep the predictions of the cross-validation models.

        Type: ``bool``  (default: ``False``).

        :examples:

        >>> prostate = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/prostate/prostate.csv")
        >>> predictors = ["AGE", "RACE", "DPROS", "DCAPS",
        ...               "PSA", "VOL", "GLEASON"]
        >>> train, valid = prostate.split_frame(ratios = [.8], seed = 1234)
        >>> pros_km = H2OKMeansEstimator(keep_cross_validation_predictions = True,
        ...                              nfolds = 5,
        ...                              seed = 1234)
        >>> pros_km.train(x = predictors,
        ...               training_frame = train,
        ...               validation_frame = valid)
        >>> pros_km.scoring_history()
        """
        return self._parms.get("keep_cross_validation_predictions")

    @keep_cross_validation_predictions.setter
    def keep_cross_validation_predictions(self, keep_cross_validation_predictions):
        assert_is_type(keep_cross_validation_predictions, None, bool)
        self._parms["keep_cross_validation_predictions"] = keep_cross_validation_predictions


    @property
    def keep_cross_validation_fold_assignment(self):
        """
        Whether to keep the cross-validation fold assignment.

        Type: ``bool``  (default: ``False``).

        :examples:

        >>> ozone = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/glm_test/ozone.csv")
        >>> predictors = ["radiation","temperature","wind"]
        >>> train, valid = ozone.split_frame(ratios = [.8], seed = 1234)
        >>> ozone_km = H2OKMeansEstimator(keep_cross_validation_fold_assignment = True,
        ...                               nfolds = 5,
        ...                               seed = 1234)
        >>> ozone_km.train(x = predictors,
        ...                training_frame = train)
        >>> ozone_km.scoring_history()
        """
        return self._parms.get("keep_cross_validation_fold_assignment")

    @keep_cross_validation_fold_assignment.setter
    def keep_cross_validation_fold_assignment(self, keep_cross_validation_fold_assignment):
        assert_is_type(keep_cross_validation_fold_assignment, None, bool)
        self._parms["keep_cross_validation_fold_assignment"] = keep_cross_validation_fold_assignment


    @property
    def fold_assignment(self):
        """
        Cross-validation fold assignment scheme, if fold_column is not specified. The 'Stratified' option will stratify
        the folds based on the response variable, for classification problems.

        One of: ``"auto"``, ``"random"``, ``"modulo"``, ``"stratified"``  (default: ``"auto"``).

        :examples:

        >>> ozone = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/glm_test/ozone.csv")
        >>> predictors = ["radiation","temperature","wind"]
        >>> train, valid = ozone.split_frame(ratios = [.8], seed = 1234)
        >>> ozone_km = H2OKMeansEstimator(fold_assignment = "Random",
        ...                               nfolds = 5,
        ...                               seed = 1234)
        >>> ozone_km.train(x = predictors,
        ...                training_frame = train,
        ...                validation_frame = valid)
        >>> ozone_km.scoring_history()
        """
        return self._parms.get("fold_assignment")

    @fold_assignment.setter
    def fold_assignment(self, fold_assignment):
        assert_is_type(fold_assignment, None, Enum("auto", "random", "modulo", "stratified"))
        self._parms["fold_assignment"] = fold_assignment


    @property
    def fold_column(self):
        """
        Column with cross-validation fold index assignment per observation.

        Type: ``str``.

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> fold_numbers = cars.kfold_column(n_folds = 5, seed = 1234)
        >>> fold_numbers.set_names(["fold_numbers"])
        >>> cars = cars.cbind(fold_numbers)
        >>> print(cars['fold_numbers'])
        >>> cars_km = H2OKMeansEstimator(seed = 1234)
        >>> cars_km.train(x = predictors,
        ...               training_frame = cars,
        ...               fold_column = "fold_numbers")
        >>> cars_km.scoring_history()
        """
        return self._parms.get("fold_column")

    @fold_column.setter
    def fold_column(self, fold_column):
        assert_is_type(fold_column, None, str)
        self._parms["fold_column"] = fold_column


    @property
    def ignored_columns(self):
        """
        Names of columns to ignore for training.

        Type: ``List[str]``.

        :examples:

        >>> ozone = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/glm_test/ozone.csv")
        >>> train, valid = ozone.split_frame(ratios = [.8], seed = 1234)
        >>> ignore_col = ["wind"]
        >>> ozone_km = H2OKMeansEstimator(ignored_columns = ignore_col,
        ...                               seed = 1234)
        >>> ozone_km.train(training_frame = train,
        ...                validation_frame = valid)
        >>> ozone_km.scoring_history()
        """
        return self._parms.get("ignored_columns")

    @ignored_columns.setter
    def ignored_columns(self, ignored_columns):
        assert_is_type(ignored_columns, None, [str])
        self._parms["ignored_columns"] = ignored_columns


    @property
    def ignore_const_cols(self):
        """
        Ignore constant columns.

        Type: ``bool``  (default: ``True``).

        :examples:

        >>> cars = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/junit/cars_20mpg.csv")
        >>> predictors = ["displacement","power","weight","acceleration","year"]
        >>> cars["const_1"] = 6
        >>> cars["const_2"] = 7
        >>> train, valid = cars.split_frame(ratios = [.8], seed = 1234)
        >>> cars_km = H2OKMeansEstimator(ignore_const_cols = True,
        ...                              seed = 1234)
        >>> cars_km.train(x = predictors,
        ...               training_frame = train,
        ...               validation_frame = valid)
        >>> cars_km.scoring_history()
        """
        return self._parms.get("ignore_const_cols")

    @ignore_const_cols.setter
    def ignore_const_cols(self, ignore_const_cols):
        assert_is_type(ignore_const_cols, None, bool)
        self._parms["ignore_const_cols"] = ignore_const_cols


    @property
    def score_each_iteration(self):
        """
        Whether to score during each iteration of model training.

        Type: ``bool``  (default: ``False``).

        :examples:

        >>> benign = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/logreg/benign.csv")
        >>> predictors = ["AGMT","FNDX","HIGD","DEG","CHK",
        ...               "AGP1","AGMN","LIV","AGLP"]
        >>> train, valid = benign.split_frame(ratios = [.8], seed = 1234)
        >>> benign_km = H2OKMeansEstimator(score_each_iteration = True,
        ...                                seed = 1234)
        >>> benign_km.train(x = predictors,
        ...                 training_frame = train,
        ...                 validation_frame = valid)
        >>> benign_km.scoring_history()
        """
        return self._parms.get("score_each_iteration")

    @score_each_iteration.setter
    def score_each_iteration(self, score_each_iteration):
        assert_is_type(score_each_iteration, None, bool)
        self._parms["score_each_iteration"] = score_each_iteration


    @property
    def k(self):
        """
        The max. number of clusters. If estimate_k is disabled, the model will find k centroids, otherwise it will find
        up to k centroids.

        Type: ``int``  (default: ``1``).

        :examples:

        >>> seeds = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/flow_examples/seeds_dataset.txt")
        >>> predictors = seeds.columns[0:7]
        >>> train, valid = seeds.split_frame(ratios = [.8], seed = 1234)
        >>> seeds_km = H2OKMeansEstimator(k = 3, seed = 1234)
        >>> seeds_km.train(x = predictors,
        ...                training_frame = train,
        ...                validation_frame=valid)
        >>> seeds_km.scoring_history()
        """
        return self._parms.get("k")

    @k.setter
    def k(self, k):
        assert_is_type(k, None, int)
        self._parms["k"] = k


    @property
    def estimate_k(self):
        """
        Whether to estimate the number of clusters (<=k) iteratively and deterministically.

        Type: ``bool``  (default: ``False``).

        :examples:

        >>> iris = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/iris/iris_wheader.csv")
        >>> iris['class'] = iris['class'].asfactor()
        >>> predictors = iris.columns[:-1]
        >>> train, valid = iris.split_frame(ratios = [.8], seed = 1234)
        >>> iris_kmeans = H2OKMeansEstimator(k = 10,
        ...                                  estimate_k = True,
        ...                                  standardize = False,
        ...                                  seed = 1234)
        >>> iris_kmeans.train(x = predictors,
        ...                   training_frame = train,
        ...                   validation_frame=valid)
        >>> isis_kmeans.scoring_history()
        """
        return self._parms.get("estimate_k")

    @estimate_k.setter
    def estimate_k(self, estimate_k):
        assert_is_type(estimate_k, None, bool)
        self._parms["estimate_k"] = estimate_k


    @property
    def user_points(self):
        """
        This option allows you to specify a dataframe, where each row represents an initial cluster center. The user-
        specified points must have the same number of columns as the training observations. The number of rows must
        equal the number of clusters

        Type: ``H2OFrame``.

        :examples:

        >>> iris = h2o.import_file("http://h2o-public-test-data.s3.amazonaws.com/smalldata/iris/iris_wheader.csv")
        >>> iris['class'] = iris['class'].asfactor()
        >>> predictors = iris.columns[:-1]
        >>> train, valid = iris.split_frame(ratios = [.8], seed = 1234)
        >>> point1 = [4.9,3.0,1.4,0.2]
        >>> point2 = [5.6,2.5,3.9,1.1]
        >>> point3 = [6.5,3.0,5.2,2.0]
        >>> points = h2o.H2OFrame([point1, point2, point3])
        >>> iris_km = H2OKMeansEstimator(k = 3,
        ...                              user_points = points,
        ...                              seed = 1234)
        >>> iris_km.train(x=predictors,
        ...               training_frame=iris,
        ...               validation_frame=valid)
        >>> iris_kmeans.tot_withinss(valid = True)
        """
        return self._parms.get("user_points")

    @user_points.setter
    def user_points(self, user_points):
        self._parms["user_points"] = H2OFrame._validate(user_points, 'user_points')


    @property
    def max_iterations(self):
        """
        Maximum training iterations (if estimate_k is enabled, then this is for each inner Lloyds iteration)

        Type: ``int``  (default: ``10``).

        :examples:

        >>> benign = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/logreg/benign.csv")
        >>> predictors = ["AGMT","FNDX","HIGD","DEG","CHK",
        ...               "AGP1","AGMN","LIV","AGLP"]
        >>> train, valid = benign.split_frame(ratios = [.8], seed = 1234)
        >>> benign_km = H2OKMeansEstimator(max_iterations = 50)
        >>> benign_km.train(x = predictors,
        ...                 training_frame = train,
        ...                 validation_frame = valid)
        >>> benign_km.scoring_history()
        """
        return self._parms.get("max_iterations")

    @max_iterations.setter
    def max_iterations(self, max_iterations):
        assert_is_type(max_iterations, None, int)
        self._parms["max_iterations"] = max_iterations


    @property
    def standardize(self):
        """
        Standardize columns before computing distances

        Type: ``bool``  (default: ``True``).

        :examples:

        >>> boston = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/gbm_test/BostonHousing.csv")
        >>> predictors = boston.columns[:-1]
        >>> boston['chas'] = boston['chas'].asfactor()
        >>> train, valid = boston.split_frame(ratios = [.8])
        >>> boston_km = H2OKMeansEstimator(standardize = True)
        >>> boston_km.train(x = predictors,
        ...                 training_frame = train,
        ...                 validation_frame = valid)
        >>> boston_km.scoring_history()
        """
        return self._parms.get("standardize")

    @standardize.setter
    def standardize(self, standardize):
        assert_is_type(standardize, None, bool)
        self._parms["standardize"] = standardize


    @property
    def seed(self):
        """
        RNG Seed

        Type: ``int``  (default: ``-1``).

        :examples:

        >>> prostate = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/prostate/prostate.csv")
        >>> predictors = ["AGE", "RACE", "DPROS", "DCAPS", "PSA", "VOL", "GLEASON"]
        >>> train, valid = prostate.split_frame(ratios = [.8], seed = 1234)
        >>> pros_w_seed = H2OKMeansEstimator(seed = 1234)
        >>> pros_w_seed.train(x = predictors,
        ...                   training_frame = train,
        ...                   validation_frame = valid)
        >>> pros_wo_seed = H2OKMeansEstimator()
        >>> pros_wo_seed.train(x = predictors,
        ...                    training_frame = train,
        ...                    validation_frame = valid)
        >>> pros_w_seed.scoring_history()
        >>> pros_wo_seed.scoring_history()
        """
        return self._parms.get("seed")

    @seed.setter
    def seed(self, seed):
        assert_is_type(seed, None, int)
        self._parms["seed"] = seed


    @property
    def init(self):
        """
        Initialization mode

        One of: ``"random"``, ``"plus_plus"``, ``"furthest"``, ``"user"``  (default: ``"furthest"``).

        :examples:

        >>> seeds = h2o.import_file("https://s3.amazonaws.com/h2o-public-test-data/smalldata/flow_examples/seeds_dataset.txt")
        >>> predictors = seeds.columns[0:7]
        >>> train, valid = seeds.split_frame(ratios = [.8], seed = 1234)
        >>> seeds_km = H2OKMeansEstimator(k = 3,
        ...                                   init='Furthest',
        ...                                   seed = 1234)
        >>> seeds_km.train(x = predictors,
        ...                    training_frame = train,
        ...                    validation_frame= valid)
        >>> seeds_km.scoring_history()
        """
        return self._parms.get("init")

    @init.setter
    def init(self, init):
        assert_is_type(init, None, Enum("random", "plus_plus", "furthest", "user"))
        self._parms["init"] = init


    @property
    def max_runtime_secs(self):
        """
        Maximum allowed runtime in seconds for model training. Use 0 to disable.

        Type: ``float``  (default: ``0``).

        :examples:

        >>> benign = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/logreg/benign.csv")
        >>> predictors = ["AGMT","FNDX","HIGD","DEG","CHK",
        ...               "AGP1","AGMN","LIV","AGLP"]
        >>> train, valid = benign.split_frame(ratios = [.8], seed = 1234)
        >>> benign_km = H2OKMeansEstimator(max_runtime_secs = 10,
        ...                                seed = 1234)
        >>> benign_km.train(x = predictors,
        ...                 training_frame = train,
        ...                 validation_frame = valid)
        >>> benign_km.scoring_history()
        """
        return self._parms.get("max_runtime_secs")

    @max_runtime_secs.setter
    def max_runtime_secs(self, max_runtime_secs):
        assert_is_type(max_runtime_secs, None, numeric)
        self._parms["max_runtime_secs"] = max_runtime_secs


    @property
    def categorical_encoding(self):
        """
        Encoding scheme for categorical features

        One of: ``"auto"``, ``"enum"``, ``"one_hot_internal"``, ``"one_hot_explicit"``, ``"binary"``, ``"eigen"``,
        ``"label_encoder"``, ``"sort_by_response"``, ``"enum_limited"``  (default: ``"auto"``).

        :examples:

        >>> prostate = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/prostate/prostate.csv")
        >>> predictors = ["AGE", "RACE", "DPROS", "DCAPS", "PSA", "VOL", "GLEASON"]
        >>> train, valid = prostate.split_frame(ratios = [.8], seed = 1234)
        >>> encoding = "one_hot_explicit"
        >>> pros_km = H2OKMeansEstimator(categorical_encoding = encoding,
        ...                              seed = 1234)
        >>> pros_km.train(x = predictors,
        ...               training_frame = train,
        ...               validation_frame = valid)
        >>> pros_km.scoring_history()
        """
        return self._parms.get("categorical_encoding")

    @categorical_encoding.setter
    def categorical_encoding(self, categorical_encoding):
        assert_is_type(categorical_encoding, None, Enum("auto", "enum", "one_hot_internal", "one_hot_explicit", "binary", "eigen", "label_encoder", "sort_by_response", "enum_limited"))
        self._parms["categorical_encoding"] = categorical_encoding


    @property
    def export_checkpoints_dir(self):
        """
        Automatically export generated models to this directory.

        Type: ``str``.

        :examples:

        >>> import tempfile
        >>> from os import listdir
        >>> airlines = h2o.import_file("http://s3.amazonaws.com/h2o-public-test-data/smalldata/airlines/allyears2k_headers.zip", destination_frame="air.hex")
        >>> predictors = ["DayofMonth", "DayOfWeek"]
        >>> checkpoints_dir = tempfile.mkdtemp()
        >>> air_km = H2OKMeansEstimator(export_checkpoints_dir = checkpoints_dir,
        ...                             seed = 1234)
        >>> air_km.train(x = predictors, training_frame = airlines)
        >>> len(listdir(checkpoints_dir))
        """
        return self._parms.get("export_checkpoints_dir")

    @export_checkpoints_dir.setter
    def export_checkpoints_dir(self, export_checkpoints_dir):
        assert_is_type(export_checkpoints_dir, None, str)
        self._parms["export_checkpoints_dir"] = export_checkpoints_dir


