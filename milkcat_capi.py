# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_milkcat_capi', [dirname(__file__)])
        except ImportError:
            import _milkcat_capi
            return _milkcat_capi
        if fp is not None:
            try:
                _mod = imp.load_module('_milkcat_capi', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _milkcat_capi = swig_import_helper()
    del swig_import_helper
else:
    import _milkcat_capi
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class milkcat_parseriterator_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, milkcat_parseriterator_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, milkcat_parseriterator_t, name)
    __repr__ = _swig_repr
    __swig_getmethods__["word"] = _milkcat_capi.milkcat_parseriterator_t_word_get
    if _newclass:word = _swig_property(_milkcat_capi.milkcat_parseriterator_t_word_get)
    __swig_getmethods__["part_of_speech_tag"] = _milkcat_capi.milkcat_parseriterator_t_part_of_speech_tag_get
    if _newclass:part_of_speech_tag = _swig_property(_milkcat_capi.milkcat_parseriterator_t_part_of_speech_tag_get)
    __swig_getmethods__["head"] = _milkcat_capi.milkcat_parseriterator_t_head_get
    if _newclass:head = _swig_property(_milkcat_capi.milkcat_parseriterator_t_head_get)
    __swig_getmethods__["dependency_label"] = _milkcat_capi.milkcat_parseriterator_t_dependency_label_get
    if _newclass:dependency_label = _swig_property(_milkcat_capi.milkcat_parseriterator_t_dependency_label_get)
    __swig_getmethods__["is_begin_of_sentence"] = _milkcat_capi.milkcat_parseriterator_t_is_begin_of_sentence_get
    if _newclass:is_begin_of_sentence = _swig_property(_milkcat_capi.milkcat_parseriterator_t_is_begin_of_sentence_get)
    __swig_getmethods__["it"] = _milkcat_capi.milkcat_parseriterator_t_it_get
    if _newclass:it = _swig_property(_milkcat_capi.milkcat_parseriterator_t_it_get)
    def __init__(self): 
        this = _milkcat_capi.new_milkcat_parseriterator_t()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _milkcat_capi.delete_milkcat_parseriterator_t
    __del__ = lambda self : None;
milkcat_parseriterator_t_swigregister = _milkcat_capi.milkcat_parseriterator_t_swigregister
milkcat_parseriterator_t_swigregister(milkcat_parseriterator_t)

MC_SEGMENTER_BIGRAM = _milkcat_capi.MC_SEGMENTER_BIGRAM
MC_SEGMENTER_CRF = _milkcat_capi.MC_SEGMENTER_CRF
MC_SEGMENTER_MIXED = _milkcat_capi.MC_SEGMENTER_MIXED
MC_POSTAGGER_MIXED = _milkcat_capi.MC_POSTAGGER_MIXED
MC_POSTAGGER_CRF = _milkcat_capi.MC_POSTAGGER_CRF
MC_POSTAGGER_HMM = _milkcat_capi.MC_POSTAGGER_HMM
MC_POSTAGGER_NONE = _milkcat_capi.MC_POSTAGGER_NONE
MC_DEPPARSER_YAMADA = _milkcat_capi.MC_DEPPARSER_YAMADA
MC_DEPPARSER_BEAMYAMADA = _milkcat_capi.MC_DEPPARSER_BEAMYAMADA
MC_DEPPARSER_NONE = _milkcat_capi.MC_DEPPARSER_NONE
class milkcat_parseroptions_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, milkcat_parseroptions_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, milkcat_parseroptions_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["word_segmenter"] = _milkcat_capi.milkcat_parseroptions_t_word_segmenter_set
    __swig_getmethods__["word_segmenter"] = _milkcat_capi.milkcat_parseroptions_t_word_segmenter_get
    if _newclass:word_segmenter = _swig_property(_milkcat_capi.milkcat_parseroptions_t_word_segmenter_get, _milkcat_capi.milkcat_parseroptions_t_word_segmenter_set)
    __swig_setmethods__["part_of_speech_tagger"] = _milkcat_capi.milkcat_parseroptions_t_part_of_speech_tagger_set
    __swig_getmethods__["part_of_speech_tagger"] = _milkcat_capi.milkcat_parseroptions_t_part_of_speech_tagger_get
    if _newclass:part_of_speech_tagger = _swig_property(_milkcat_capi.milkcat_parseroptions_t_part_of_speech_tagger_get, _milkcat_capi.milkcat_parseroptions_t_part_of_speech_tagger_set)
    __swig_setmethods__["dependency_parser"] = _milkcat_capi.milkcat_parseroptions_t_dependency_parser_set
    __swig_getmethods__["dependency_parser"] = _milkcat_capi.milkcat_parseroptions_t_dependency_parser_get
    if _newclass:dependency_parser = _swig_property(_milkcat_capi.milkcat_parseroptions_t_dependency_parser_get, _milkcat_capi.milkcat_parseroptions_t_dependency_parser_set)
    __swig_setmethods__["user_dictionary_path"] = _milkcat_capi.milkcat_parseroptions_t_user_dictionary_path_set
    __swig_getmethods__["user_dictionary_path"] = _milkcat_capi.milkcat_parseroptions_t_user_dictionary_path_get
    if _newclass:user_dictionary_path = _swig_property(_milkcat_capi.milkcat_parseroptions_t_user_dictionary_path_get, _milkcat_capi.milkcat_parseroptions_t_user_dictionary_path_set)
    __swig_setmethods__["model_path"] = _milkcat_capi.milkcat_parseroptions_t_model_path_set
    __swig_getmethods__["model_path"] = _milkcat_capi.milkcat_parseroptions_t_model_path_get
    if _newclass:model_path = _swig_property(_milkcat_capi.milkcat_parseroptions_t_model_path_get, _milkcat_capi.milkcat_parseroptions_t_model_path_set)
    def __init__(self): 
        this = _milkcat_capi.new_milkcat_parseroptions_t()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _milkcat_capi.delete_milkcat_parseroptions_t
    __del__ = lambda self : None;
milkcat_parseroptions_t_swigregister = _milkcat_capi.milkcat_parseroptions_t_swigregister
milkcat_parseroptions_t_swigregister(milkcat_parseroptions_t)


def milkcat_parseroptions_init(*args):
  return _milkcat_capi.milkcat_parseroptions_init(*args)
milkcat_parseroptions_init = _milkcat_capi.milkcat_parseroptions_init

def milkcat_parser_new(*args):
  return _milkcat_capi.milkcat_parser_new(*args)
milkcat_parser_new = _milkcat_capi.milkcat_parser_new

def milkcat_parser_destroy(*args):
  return _milkcat_capi.milkcat_parser_destroy(*args)
milkcat_parser_destroy = _milkcat_capi.milkcat_parser_destroy

def milkcat_parser_predict(*args):
  return _milkcat_capi.milkcat_parser_predict(*args)
milkcat_parser_predict = _milkcat_capi.milkcat_parser_predict

def milkcat_parseriterator_new():
  return _milkcat_capi.milkcat_parseriterator_new()
milkcat_parseriterator_new = _milkcat_capi.milkcat_parseriterator_new

def milkcat_parseriterator_destroy(*args):
  return _milkcat_capi.milkcat_parseriterator_destroy(*args)
milkcat_parseriterator_destroy = _milkcat_capi.milkcat_parseriterator_destroy

def milkcat_parseriterator_next(*args):
  return _milkcat_capi.milkcat_parseriterator_next(*args)
milkcat_parseriterator_next = _milkcat_capi.milkcat_parseriterator_next

def milkcat_last_error():
  return _milkcat_capi.milkcat_last_error()
milkcat_last_error = _milkcat_capi.milkcat_last_error
# This file is compatible with both classic and new-style classes.


