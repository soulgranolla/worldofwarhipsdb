import sqlite3
import application.data as data

# Connexion à la db
con = sqlite3.connect("world_of_warships.db")
cur = con.cursor()

# Insertion des navires non premium
navires = [
    data.tuple1, data.tuple2, data.tuple3, data.tuple4, data.tuple5, data.tuple6, data.tuple7, data.tuple8, data.tuple9, data.tuple10,
    data.tuple11, data.tuple12, data.tuple13, data.tuple14, data.tuple15, data.tuple16, data.tuple17, data.tuple18, data.tuple19, data.tuple20,
    data.tuple21, data.tuple22, data.tuple23, data.tuple24, data.tuple25, data.tuple26, data.tuple27, data.tuple28, data.tuple29, data.tuple30,
    data.tuple31, data.tuple32, data.tuple33, data.tuple34, data.tuple35, data.tuple36, data.tuple37, data.tuple38, data.tuple39, data.tuple40,
    data.tuple41, data.tuple42, data.tuple43, data.tuple44, data.tuple45, data.tuple46, data.tuple47, data.tuple48, data.tuple49, data.tuple50,
    data.tuple51, data.tuple52, data.tuple53, data.tuple54, data.tuple55, data.tuple56, data.tuple57, data.tuple58, data.tuple59, data.tuple60,
    data.tuple61, data.tuple62, data.tuple63, data.tuple64, data.tuple65, data.tuple66, data.tuple67, data.tuple68, data.tuple69, data.tuple70,
    data.tuple71, data.tuple72, data.tuple73, data.tuple74, data.tuple75, data.tuple76, data.tuple77, data.tuple78, data.tuple79, data.tuple80,
    data.tuple81, data.tuple82, data.tuple83, data.tuple84, data.tuple85, data.tuple86, data.tuple87, data.tuple88, data.tuple89, data.tuple90,
    data.tuple91, data.tuple92, data.tuple93, data.tuple94, data.tuple95, data.tuple96, data.tuple97, data.tuple98, data.tuple99, data.tuple100,
    data.tuple101, data.tuple102, data.tuple103, data.tuple104, data.tuple105, data.tuple106, data.tuple107, data.tuple108, data.tuple109, data.tuple110,
    data.tuple111, data.tuple112, data.tuple113, data.tuple114, data.tuple115, data.tuple116, data.tuple117, data.tuple118, data.tuple119, data.tuple120,
    data.tuple121, data.tuple122, data.tuple123, data.tuple124, data.tuple125, data.tuple126, data.tuple127, data.tuple128, data.tuple129, data.tuple130,
    data.tuple131, data.tuple132, data.tuple133, data.tuple134, data.tuple135, data.tuple136, data.tuple137, data.tuple138, data.tuple139, data.tuple140,
    data.tuple141, data.tuple142, data.tuple143, data.tuple144, data.tuple145, data.tuple146, data.tuple147, data.tuple148, data.tuple149, data.tuple150,
    data.tuple151, data.tuple152, data.tuple153, data.tuple154, data.tuple155, data.tuple156, data.tuple157, data.tuple158, data.tuple159, data.tuple160,
    data.tuple161, data.tuple162, data.tuple163, data.tuple164, data.tuple165, data.tuple166, data.tuple167, data.tuple168, data.tuple169, data.tuple170,
    data.tuple171, data.tuple172, data.tuple173, data.tuple174, data.tuple175, data.tuple176, data.tuple177, data.tuple178, data.tuple179, data.tuple180,
    data.tuple181, data.tuple182, data.tuple183, data.tuple184, data.tuple185, data.tuple186, data.tuple187, data.tuple188, data.tuple189, data.tuple190,
    data.tuple191, data.tuple192, data.tuple193, data.tuple194, data.tuple195, data.tuple196, data.tuple197, data.tuple198, data.tuple199, data.tuple200,
    data.tuple201, data.tuple202, data.tuple203, data.tuple204, data.tuple205, data.tuple206, data.tuple207, data.tuple208, data.tuple209, data.tuple210,
    data.tuple211, data.tuple212, data.tuple213, data.tuple214, data.tuple215, data.tuple216, data.tuple217, data.tuple218, data.tuple219, data.tuple220,
    data.tuple221, data.tuple222, data.tuple223, data.tuple224, data.tuple225, data.tuple226, data.tuple227, data.tuple228, data.tuple229, data.tuple230,
    data.tuple231, data.tuple232, data.tuple233, data.tuple234, data.tuple235, data.tuple236, data.tuple237, data.tuple238, data.tuple239, data.tuple240,
    data.tuple241, data.tuple242, data.tuple243, data.tuple244, data.tuple245, data.tuple246, data.tuple247, data.tuple248, data.tuple249, data.tuple250,
    data.tuple251, data.tuple252, data.tuple253, data.tuple254, data.tuple255, data.tuple256, data.tuple257, data.tuple258, data.tuple259, data.tuple260,
    data.tuple261, data.tuple262, data.tuple263, data.tuple264, data.tuple265, data.tuple266, data.tuple267, data.tuple268, data.tuple269, data.tuple270,
    data.tuple271, data.tuple272, data.tuple273, data.tuple274, data.tuple275, data.tuple276, data.tuple277, data.tuple278, data.tuple279, data.tuple280,
    data.tuple281, data.tuple282, data.tuple283, data.tuple284, data.tuple285, data.tuple286, data.tuple287, data.tuple288, data.tuple289, data.tuple290,
    data.tuple291, data.tuple292, data.tuple293, data.tuple294, data.tuple295, data.tuple296, data.tuple297, data.tuple298, data.tuple299, data.tuple300,
    data.tuple301, data.tuple302, data.tuple303, data.tuple304, data.tuple305, data.tuple306, data.tuple307, data.tuple308, data.tuple309, data.tuple310,
    data.tuple311, data.tuple312, data.tuple313, data.tuple314, data.tuple315, data.tuple316, data.tuple317, data.tuple318, data.tuple319, data.tuple320,
    data.tuple321, data.tuple322, data.tuple323, data.tuple324, data.tuple325, data.tuple326, data.tuple327, data.tuple328, data.tuple329, data.tuple330,
    data.tuple331, data.tuple332, data.tuple333, data.tuple334, data.tuple335, data.tuple336, data.tuple337, data.tuple338, data.tuple339, data.tuple340,
    data.tuple341, data.tuple342, data.tuple343, data.tuple344, data.tuple345, data.tuple346, data.tuple347, data.tuple348, data.tuple349, data.tuple350,
    data.tuple351, data.tuple352, data.tuple353, data.tuple354, data.tuple355, data.tuple356, data.tuple357, data.tuple358, data.tuple359, data.tuple360,
    data.tuple361, data.tuple362, data.tuple363, data.tuple364, data.tuple365, data.tuple366, data.tuple367, data.tuple368, data.tuple369, data.tuple370,
    data.tuple371, data.tuple372, data.tuple373, data.tuple374, data.tuple375, data.tuple376, data.tuple377, data.tuple378, data.tuple379, data.tuple380,
    data.tuple381, data.tuple382, data.tuple383, data.tuple384, data.tuple385, data.tuple386, data.tuple387, data.tuple388, data.tuple389
]

# Insertion des navires premium
navires_premium = [ data.tuple_2_1, data.tuple_2_2, data.tuple_2_3, data.tuple_2_4, data.tuple_2_5, data.tuple_2_6, data.tuple_2_7, data.tuple_2_8, data.tuple_2_9, data.tuple_2_10,
                   data.tuple_2_11, data.tuple_2_12, data.tuple_2_13, data.tuple_2_14, data.tuple_2_15, data.tuple_2_16, data.tuple_2_17, data.tuple_2_18, data.tuple_2_19, data.tuple_2_20,
    data.tuple_2_21, data.tuple_2_22, data.tuple_2_23, data.tuple_2_24, data.tuple_2_25, data.tuple_2_26, data.tuple_2_27, data.tuple_2_28, data.tuple_2_29, data.tuple_2_30,
    data.tuple_2_31, data.tuple_2_32, data.tuple_2_33, data.tuple_2_34, data.tuple_2_35, data.tuple_2_36, data.tuple_2_37, data.tuple_2_38, data.tuple_2_39, data.tuple_2_40,
    data.tuple_2_41, data.tuple_2_42, data.tuple_2_43, data.tuple_2_44, data.tuple_2_45, data.tuple_2_46, data.tuple_2_47, data.tuple_2_48, data.tuple_2_49, data.tuple_2_50,
    data.tuple_2_51, data.tuple_2_52, data.tuple_2_53, data.tuple_2_54, data.tuple_2_55, data.tuple_2_56, data.tuple_2_57, data.tuple_2_58, data.tuple_2_59, data.tuple_2_60,
    data.tuple_2_61, data.tuple_2_62, data.tuple_2_63, data.tuple_2_64, data.tuple_2_65, data.tuple_2_66, data.tuple_2_67, data.tuple_2_68, data.tuple_2_69, data.tuple_2_70,
    data.tuple_2_71, data.tuple_2_72, data.tuple_2_73, data.tuple_2_74, data.tuple_2_75, data.tuple_2_76, data.tuple_2_77, data.tuple_2_78, data.tuple_2_79, data.tuple_2_80,
    data.tuple_2_81, data.tuple_2_82, data.tuple_2_83, data.tuple_2_84, data.tuple_2_85, data.tuple_2_86, data.tuple_2_87, data.tuple_2_88, data.tuple_2_89, data.tuple_2_90,
    data.tuple_2_91, data.tuple_2_92, data.tuple_2_93, data.tuple_2_94, data.tuple_2_95, data.tuple_2_96, data.tuple_2_97, data.tuple_2_98, data.tuple_2_99, data.tuple_2_100,
    data.tuple_2_101, data.tuple_2_102, data.tuple_2_103, data.tuple_2_104, data.tuple_2_105, data.tuple_2_106, data.tuple_2_107, data.tuple_2_108, data.tuple_2_109, data.tuple_2_110,
    data.tuple_2_111, data.tuple_2_112, data.tuple_2_113, data.tuple_2_114, data.tuple_2_115, data.tuple_2_116, data.tuple_2_117, data.tuple_2_118, data.tuple_2_119, data.tuple_2_120,
    data.tuple_2_121, data.tuple_2_122, data.tuple_2_123, data.tuple_2_124, data.tuple_2_125, data.tuple_2_126, data.tuple_2_127, data.tuple_2_128, data.tuple_2_129, data.tuple_2_130,
    data.tuple_2_131, data.tuple_2_132, data.tuple_2_133, data.tuple_2_134, data.tuple_2_135, data.tuple_2_136, data.tuple_2_137, data.tuple_2_138, data.tuple_2_139, data.tuple_2_140,
    data.tuple_2_141, data.tuple_2_142, data.tuple_2_143, data.tuple_2_144, data.tuple_2_145, data.tuple_2_146, data.tuple_2_147, data.tuple_2_148, data.tuple_2_149, data.tuple_2_150,
    data.tuple_2_151, data.tuple_2_152, data.tuple_2_153, data.tuple_2_154, data.tuple_2_155, data.tuple_2_156, data.tuple_2_157, data.tuple_2_158, data.tuple_2_159, data.tuple_2_160,
    data.tuple_2_161, data.tuple_2_162, data.tuple_2_163, data.tuple_2_164, data.tuple_2_165, data.tuple_2_166, data.tuple_2_167, data.tuple_2_168, data.tuple_2_169, data.tuple_2_170,
    data.tuple_2_171, data.tuple_2_172, data.tuple_2_173, data.tuple_2_174, data.tuple_2_175, data.tuple_2_176, data.tuple_2_177, data.tuple_2_178, data.tuple_2_179, data.tuple_2_180,
    data.tuple_2_181, data.tuple_2_182, data.tuple_2_183, data.tuple_2_184, data.tuple_2_185, data.tuple_2_186, data.tuple_2_187, data.tuple_2_188, data.tuple_2_189,
    data.tuple_2_190, data.tuple_2_191, data.tuple_2_192, data.tuple_2_193, data.tuple_2_194, data.tuple_2_195, data.tuple_2_196, data.tuple_2_197, data.tuple_2_198, data.tuple_2_199,
    data.tuple_2_200, data.tuple_2_201, data.tuple_2_202, data.tuple_2_203, data.tuple_2_204, data.tuple_2_205, data.tuple_2_206, data.tuple_2_207, data.tuple_2_208, data.tuple_2_209,
    data.tuple_2_210, data.tuple_2_211, data.tuple_2_212, data.tuple_2_213, data.tuple_2_214, data.tuple_2_215, data.tuple_2_216, data.tuple_2_217, data.tuple_2_218, data.tuple_2_219,
    data.tuple_2_220, data.tuple_2_221, data.tuple_2_222, data.tuple_2_223, data.tuple_2_224, data.tuple_2_225, data.tuple_2_226, data.tuple_2_227, data.tuple_2_228, data.tuple_2_229,
    data.tuple_2_230, data.tuple_2_231, data.tuple_2_232, data.tuple_2_233, data.tuple_2_234, data.tuple_2_235, data.tuple_2_236, data.tuple_2_237, data.tuple_2_238, data.tuple_2_239,
    data.tuple_2_240, data.tuple_2_241, data.tuple_2_242, data.tuple_2_243, data.tuple_2_244, data.tuple_2_245, data.tuple_2_246, data.tuple_2_247, data.tuple_2_248, data.tuple_2_249,
    data.tuple_2_250, data.tuple_2_251, data.tuple_2_252, data.tuple_2_253, data.tuple_2_254, data.tuple_2_255, data.tuple_2_256, data.tuple_2_257, data.tuple_2_258, data.tuple_2_259,
    data.tuple_2_260, data.tuple_2_261, data.tuple_2_262, data.tuple_2_263, data.tuple_2_264, data.tuple_2_265, data.tuple_2_266, data.tuple_2_267, data.tuple_2_268, data.tuple_2_269,
    data.tuple_2_270, data.tuple_2_271, data.tuple_2_272, data.tuple_2_273, data.tuple_2_274, data.tuple_2_275, data.tuple_2_276, data.tuple_2_277, data.tuple_2_278, data.tuple_2_279,
    data.tuple_2_280, data.tuple_2_281, data.tuple_2_282, data.tuple_2_283, data.tuple_2_284, data.tuple_2_285, data.tuple_2_286, data.tuple_2_287, data.tuple_2_288, data.tuple_2_289,
    data.tuple_2_290, data.tuple_2_291, data.tuple_2_292, data.tuple_2_293, data.tuple_2_294, data.tuple_2_295, data.tuple_2_296, data.tuple_2_297, data.tuple_2_298, data.tuple_2_299,
    data.tuple_2_300, data.tuple_2_301, data.tuple_2_302, data.tuple_2_303, data.tuple_2_304, data.tuple_2_305, data.tuple_2_306, data.tuple_2_307, data.tuple_2_308, data.tuple_2_309,
    data.tuple_2_310, data.tuple_2_311, data.tuple_2_312, data.tuple_2_313, data.tuple_2_314, data.tuple_2_315, data.tuple_2_316, data.tuple_2_317, data.tuple_2_318, data.tuple_2_319,
    data.tuple_2_320, data.tuple_2_321, data.tuple_2_322, data.tuple_2_323, data.tuple_2_324, data.tuple_2_325, data.tuple_2_326, data.tuple_2_327, data.tuple_2_328, data.tuple_2_329,
    data.tuple_2_330, data.tuple_2_331, data.tuple_2_332, data.tuple_2_333, data.tuple_2_334, data.tuple_2_335, data.tuple_2_336, data.tuple_2_337, data.tuple_2_338, data.tuple_2_339,
    data.tuple_2_340, data.tuple_2_341, data.tuple_2_342, data.tuple_2_343, data.tuple_2_344, data.tuple_2_345, data.tuple_2_346, data.tuple_2_347, data.tuple_2_348, data.tuple_2_349,
    data.tuple_2_350, data.tuple_2_351, data.tuple_2_352, data.tuple_2_353, data.tuple_2_354, data.tuple_2_355, data.tuple_2_356, data.tuple_2_357, data.tuple_2_358, data.tuple_2_359,
    data.tuple_2_360, data.tuple_2_361, data.tuple_2_362, data.tuple_2_363, data.tuple_2_364, data.tuple_2_365, data.tuple_2_366, data.tuple_2_367, data.tuple_2_368, data.tuple_2_369,
    data.tuple_2_370, data.tuple_2_371, data.tuple_2_372, data.tuple_2_373, data.tuple_2_374, data.tuple_2_375, data.tuple_2_376, data.tuple_2_377, data.tuple_2_378, data.tuple_2_379,
    data.tuple_2_380, data.tuple_2_381, data.tuple_2_382, data.tuple_2_383, data.tuple_2_384, data.tuple_2_385, data.tuple_2_386, data.tuple_2_387, data.tuple_2_388, data.tuple_2_389,
    data.tuple_2_390, data.tuple_2_391, data.tuple_2_392, data.tuple_2_393, data.tuple_2_394, data.tuple_2_395, data.tuple_2_396, data.tuple_2_397, data.tuple_2_398, data.tuple_2_399
    ]

# Insertion des navires test
navires_test = [data.tuple_3_1, data.tuple_3_2, data.tuple_3_3, data.tuple_3_4, data.tuple_3_5, data.tuple_3_6, data.tuple_3_7, data.tuple_3_8, data.tuple_3_9, data.tuple_3_10,
                data.tuple_3_11, data.tuple_3_12, data.tuple_3_13, data.tuple_3_14, data.tuple_3_15, data.tuple_3_16, data.tuple_3_17, data.tuple_3_18, data.tuple_3_19, data.tuple_3_20,
                data.tuple_3_21, data.tuple_3_22, data.tuple_3_23, data.tuple_3_24, data.tuple_3_25, data.tuple_3_26, data.tuple_3_27, data.tuple_3_28, data.tuple_3_29, data.tuple_3_30,
                data.tuple_3_31, data.tuple_3_32, data.tuple_3_33, data.tuple_3_34, data.tuple_3_35, data.tuple_3_36, data.tuple_3_37, data.tuple_3_38, data.tuple_3_39, data.tuple_3_40
]

nvsdp = [data.tuple_4_1, data.tuple_4_2, data.tuple_4_3, data.tuple_4_4, data.tuple_4_5, data.tuple_4_6, data.tuple_4_7, data.tuple_4_8, data.tuple_4_9, data.tuple_4_10,
         data.tuple_4_11, data.tuple_4_12, data.tuple_4_13, data.tuple_4_14, data.tuple_4_15, data.tuple_4_16, data.tuple_4_17, data.tuple_4_18, data.tuple_4_19, data.tuple_4_20,
         data.tuple_4_21
]

mbd = [data.tuple_5_1, data.tuple_5_2, data.tuple_5_3, data.tuple_5_4, data.tuple_5_5, data.tuple_5_6, data.tuple_5_7, data.tuple_5_8, data.tuple_5_9, data.tuple_5_10,
       data.tuple_5_11, data.tuple_5_12, data.tuple_5_13, data.tuple_5_14, data.tuple_5_15, data.tuple_5_16, data.tuple_5_17, data.tuple_5_18, data.tuple_5_19, data.tuple_5_20,
       data.tuple_5_21, data.tuple_5_22, data.tuple_5_23, data.tuple_5_24, data.tuple_5_25, data.tuple_5_26, data.tuple_5_27, data.tuple_5_28, data.tuple_5_29, data.tuple_5_30,
       data.tuple_5_31, data.tuple_5_32, data.tuple_5_33, data.tuple_5_34, data.tuple_5_35, data.tuple_5_36, data.tuple_5_37, data.tuple_5_38, data.tuple_5_39, data.tuple_5_40,
       data.tuple_5_41, data.tuple_5_42, data.tuple_5_43, data.tuple_5_44, data.tuple_5_45, data.tuple_5_46, data.tuple_5_47, data.tuple_5_48, data.tuple_5_49, data.tuple_5_50,
       data.tuple_5_51, data.tuple_5_52, data.tuple_5_53, data.tuple_5_54, data.tuple_5_55, data.tuple_5_56, data.tuple_5_57, data.tuple_5_58, data.tuple_5_59, data.tuple_5_60,
       data.tuple_5_61, data.tuple_5_62, data.tuple_5_63, data.tuple_5_64, data.tuple_5_65, data.tuple_5_66, data.tuple_5_67, data.tuple_5_68, data.tuple_5_69, data.tuple_5_70,
       data.tuple_5_71, data.tuple_5_72, data.tuple_5_73, data.tuple_5_74, data.tuple_5_75, data.tuple_5_76, data.tuple_5_77, data.tuple_5_78, data.tuple_5_79, data.tuple_5_80,
       data.tuple_5_81, data.tuple_5_82, data.tuple_5_83, data.tuple_5_84, data.tuple_5_85, data.tuple_5_86, data.tuple_5_87, data.tuple_5_88, data.tuple_5_89, data.tuple_5_90,
       data.tuple_5_91, data.tuple_5_92, data.tuple_5_93, data.tuple_5_94, data.tuple_5_95, data.tuple_5_96, data.tuple_5_97, data.tuple_5_98, data.tuple_5_99, data.tuple_5_100,
         data.tuple_5_101, data.tuple_5_102, data.tuple_5_103, data.tuple_5_104, data.tuple_5_105, data.tuple_5_106, data.tuple_5_107, data.tuple_5_108, data.tuple_5_109, data.tuple_5_110,
            data.tuple_5_111, data.tuple_5_112, data.tuple_5_113, data.tuple_5_114, data.tuple_5_115, data.tuple_5_116, data.tuple_5_117, data.tuple_5_118, data.tuple_5_119, data.tuple_5_120,
            data.tuple_5_121, data.tuple_5_122, data.tuple_5_123, data.tuple_5_124, data.tuple_5_125, data.tuple_5_126, data.tuple_5_127, data.tuple_5_128, data.tuple_5_129, data.tuple_5_130,
            data.tuple_5_131, data.tuple_5_132, data.tuple_5_133, data.tuple_5_134, data.tuple_5_135, data.tuple_5_136, data.tuple_5_137, data.tuple_5_138, data.tuple_5_139, data.tuple_5_140,
            data.tuple_5_141, data.tuple_5_142, data.tuple_5_143, data.tuple_5_144, data.tuple_5_145, data.tuple_5_146, data.tuple_5_147, data.tuple_5_148, data.tuple_5_149, data.tuple_5_150,
            data.tuple_5_151, data.tuple_5_152, data.tuple_5_153, data.tuple_5_154, data.tuple_5_155, data.tuple_5_156, data.tuple_5_157, data.tuple_5_158, data.tuple_5_159, data.tuple_5_160,
            data.tuple_5_161, data.tuple_5_162, data.tuple_5_163, data.tuple_5_164, data.tuple_5_165, data.tuple_5_166, data.tuple_5_167, data.tuple_5_168, data.tuple_5_169, data.tuple_5_170,
            data.tuple_5_171, data.tuple_5_172, data.tuple_5_173, data.tuple_5_174, data.tuple_5_175, data.tuple_5_176, data.tuple_5_177, data.tuple_5_178, data.tuple_5_179, data.tuple_5_180,
            data.tuple_5_181, data.tuple_5_182, data.tuple_5_183, data.tuple_5_184, data.tuple_5_185, data.tuple_5_186, data.tuple_5_187, data.tuple_5_188, data.tuple_5_189,
            data.tuple_5_190, data.tuple_5_191, data.tuple_5_192, data.tuple_5_193, data.tuple_5_194, data.tuple_5_195, data.tuple_5_196, data.tuple_5_197, data.tuple_5_198, data.tuple_5_199,
            data.tuple_5_200, data.tuple_5_201, data.tuple_5_202, data.tuple_5_203, data.tuple_5_204, data.tuple_5_205, data.tuple_5_206, data.tuple_5_207, data.tuple_5_208, data.tuple_5_209,
            data.tuple_5_210, data.tuple_5_211, data.tuple_5_212, data.tuple_5_213, data.tuple_5_214, data.tuple_5_215, data.tuple_5_216, data.tuple_5_217, data.tuple_5_218, data.tuple_5_219,
            data.tuple_5_220, data.tuple_5_221, data.tuple_5_222, data.tuple_5_223, data.tuple_5_224, data.tuple_5_225, data.tuple_5_226, data.tuple_5_227, data.tuple_5_228, data.tuple_5_229,
            data.tuple_5_230, data.tuple_5_231, data.tuple_5_232, data.tuple_5_233, data.tuple_5_234, data.tuple_5_235, data.tuple_5_236, data.tuple_5_237, data.tuple_5_238, data.tuple_5_239,
            data.tuple_5_240, data.tuple_5_241, data.tuple_5_242, data.tuple_5_243, data.tuple_5_244, data.tuple_5_245, data.tuple_5_246, data.tuple_5_247, data.tuple_5_248, data.tuple_5_249,
            data.tuple_5_250, data.tuple_5_251, data.tuple_5_252, data.tuple_5_253, data.tuple_5_254, data.tuple_5_255, data.tuple_5_256, data.tuple_5_257, data.tuple_5_258, data.tuple_5_259,
            data.tuple_5_260, data.tuple_5_261, data.tuple_5_262, data.tuple_5_263, data.tuple_5_264, data.tuple_5_265, data.tuple_5_266, data.tuple_5_267, data.tuple_5_268, data.tuple_5_269,
            data.tuple_5_270, data.tuple_5_271, data.tuple_5_272, data.tuple_5_273, data.tuple_5_274, data.tuple_5_275, data.tuple_5_276, data.tuple_5_277, data.tuple_5_278, data.tuple_5_279,
            data.tuple_5_280, data.tuple_5_281, data.tuple_5_282, data.tuple_5_283, data.tuple_5_284, data.tuple_5_285, data.tuple_5_286, data.tuple_5_287, data.tuple_5_288, data.tuple_5_289,
            data.tuple_5_290, data.tuple_5_291, data.tuple_5_292, data.tuple_5_293, data.tuple_5_294, data.tuple_5_295, data.tuple_5_296, data.tuple_5_297, data.tuple_5_298, data.tuple_5_299,
            data.tuple_5_300, data.tuple_5_301, data.tuple_5_302, data.tuple_5_303, data.tuple_5_304, data.tuple_5_305, data.tuple_5_306, data.tuple_5_307, data.tuple_5_308, data.tuple_5_309,
            data.tuple_5_310, data.tuple_5_311, data.tuple_5_312, data.tuple_5_313, data.tuple_5_314, data.tuple_5_315, data.tuple_5_316, data.tuple_5_317, data.tuple_5_318, data.tuple_5_319,
            data.tuple_5_320, data.tuple_5_321, data.tuple_5_322, data.tuple_5_323, data.tuple_5_324, data.tuple_5_325, data.tuple_5_326, data.tuple_5_327, data.tuple_5_328, data.tuple_5_329,
            data.tuple_5_330, data.tuple_5_331, data.tuple_5_332, data.tuple_5_333, data.tuple_5_334, data.tuple_5_335, data.tuple_5_336, data.tuple_5_337, data.tuple_5_338, data.tuple_5_339,
            data.tuple_5_340, data.tuple_5_341, data.tuple_5_342, data.tuple_5_343, data.tuple_5_344, data.tuple_5_345, data.tuple_5_346, data.tuple_5_347, data.tuple_5_348, data.tuple_5_349,
            data.tuple_5_350, data.tuple_5_351, data.tuple_5_352, data.tuple_5_353, data.tuple_5_354, data.tuple_5_355, data.tuple_5_356, data.tuple_5_357, data.tuple_5_358, data.tuple_5_359,
            data.tuple_5_360, data.tuple_5_361, data.tuple_5_362, data.tuple_5_363, data.tuple_5_364, data.tuple_5_365, data.tuple_5_366, data.tuple_5_367, data.tuple_5_368, data.tuple_5_369,
            data.tuple_5_370, data.tuple_5_371, data.tuple_5_372, data.tuple_5_373, data.tuple_5_374, data.tuple_5_375, data.tuple_5_376, data.tuple_5_377, data.tuple_5_378, data.tuple_5_379,
            data.tuple_5_380, data.tuple_5_381, data.tuple_5_382, data.tuple_5_383, data.tuple_5_384, data.tuple_5_385, data.tuple_5_386, data.tuple_5_387, data.tuple_5_388, data.tuple_5_389,
            data.tuple_5_390, data.tuple_5_391, data.tuple_5_392, data.tuple_5_393, data.tuple_5_394, data.tuple_5_395, data.tuple_5_396, data.tuple_5_397, data.tuple_5_398, data.tuple_5_399,
            data.tuple_5_400, data.tuple_5_401, data.tuple_5_402, data.tuple_5_403, data.tuple_5_404, data.tuple_5_405, data.tuple_5_406, data.tuple_5_407, data.tuple_5_408, data.tuple_5_409,
            data.tuple_5_410, data.tuple_5_411, data.tuple_5_412, data.tuple_5_413, data.tuple_5_414, data.tuple_5_415, data.tuple_5_416, data.tuple_5_417, data.tuple_5_418, data.tuple_5_419,
            data.tuple_5_420, data.tuple_5_421, data.tuple_5_422, data.tuple_5_423, data.tuple_5_424, data.tuple_5_425, data.tuple_5_426, data.tuple_5_427, data.tuple_5_428, data.tuple_5_429,
            data.tuple_5_430, data.tuple_5_431, data.tuple_5_432, data.tuple_5_433, data.tuple_5_434, data.tuple_5_435, data.tuple_5_436, data.tuple_5_437, data.tuple_5_438, data.tuple_5_439,
            data.tuple_5_440, data.tuple_5_441, data.tuple_5_442, data.tuple_5_443, data.tuple_5_444, data.tuple_5_445, data.tuple_5_446, data.tuple_5_447, data.tuple_5_448, data.tuple_5_449,
            data.tuple_5_450, data.tuple_5_451, data.tuple_5_452, data.tuple_5_453, data.tuple_5_454, data.tuple_5_455, data.tuple_5_456, data.tuple_5_457, data.tuple_5_458, data.tuple_5_459,
            data.tuple_5_460, data.tuple_5_461, data.tuple_5_462, data.tuple_5_463, data.tuple_5_464, data.tuple_5_465, data.tuple_5_466, data.tuple_5_467, data.tuple_5_468, data.tuple_5_469,
            data.tuple_5_470, data.tuple_5_471, data.tuple_5_472, data.tuple_5_473, data.tuple_5_474, data.tuple_5_475, data.tuple_5_476, data.tuple_5_477, data.tuple_5_478, data.tuple_5_479,
            data.tuple_5_480, data.tuple_5_481, data.tuple_5_482, data.tuple_5_483, data.tuple_5_484, data.tuple_5_485, data.tuple_5_486, data.tuple_5_487, data.tuple_5_488, data.tuple_5_489,
            data.tuple_5_490, data.tuple_5_491, data.tuple_5_492, data.tuple_5_493, data.tuple_5_494, data.tuple_5_495, data.tuple_5_496, data.tuple_5_497, data.tuple_5_498, data.tuple_5_499,
            data.tuple_5_500, data.tuple_5_501, data.tuple_5_502, data.tuple_5_503, data.tuple_5_504, data.tuple_5_505, data.tuple_5_506, data.tuple_5_507, data.tuple_5_508, data.tuple_5_509,
            data.tuple_5_510, data.tuple_5_511, data.tuple_5_512, data.tuple_5_513, data.tuple_5_514, data.tuple_5_515, data.tuple_5_516, data.tuple_5_517, data.tuple_5_518, data.tuple_5_519,
            data.tuple_5_520, data.tuple_5_521, data.tuple_5_522, data.tuple_5_523, data.tuple_5_524, data.tuple_5_525, data.tuple_5_526, data.tuple_5_527, data.tuple_5_528, data.tuple_5_529,
            data.tuple_5_530, data.tuple_5_531, data.tuple_5_532, data.tuple_5_533, data.tuple_5_534, data.tuple_5_535, data.tuple_5_536, data.tuple_5_537, data.tuple_5_538, data.tuple_5_539,
            data.tuple_5_540, data.tuple_5_541, data.tuple_5_542, data.tuple_5_543, data.tuple_5_544, data.tuple_5_545, data.tuple_5_546, data.tuple_5_547, data.tuple_5_548, data.tuple_5_549,
            data.tuple_5_550, data.tuple_5_551, data.tuple_5_552, data.tuple_5_553, data.tuple_5_554, data.tuple_5_555, data.tuple_5_556, data.tuple_5_557, data.tuple_5_558, data.tuple_5_559,
            data.tuple_5_560, data.tuple_5_561, data.tuple_5_562, data.tuple_5_563, data.tuple_5_564, data.tuple_5_565, data.tuple_5_566, data.tuple_5_567, data.tuple_5_568, data.tuple_5_569,
            data.tuple_5_570, data.tuple_5_571, data.tuple_5_572, data.tuple_5_573, data.tuple_5_574, data.tuple_5_575, data.tuple_5_576, data.tuple_5_577, data.tuple_5_578, data.tuple_5_579,
            data.tuple_5_580, data.tuple_5_581, data.tuple_5_582, data.tuple_5_583, data.tuple_5_584, data.tuple_5_585, data.tuple_5_586, data.tuple_5_587, data.tuple_5_588, data.tuple_5_589,
            data.tuple_5_590, data.tuple_5_591, data.tuple_5_592, data.tuple_5_593, data.tuple_5_594, data.tuple_5_595, data.tuple_5_596, data.tuple_5_597, data.tuple_5_598, data.tuple_5_599,
            data.tuple_5_600, data.tuple_5_601, data.tuple_5_602, data.tuple_5_603, data.tuple_5_604, data.tuple_5_605, data.tuple_5_606, data.tuple_5_607, data.tuple_5_608, data.tuple_5_609,
            data.tuple_5_610, data.tuple_5_611, data.tuple_5_612, data.tuple_5_613, data.tuple_5_614, data.tuple_5_615, data.tuple_5_616, data.tuple_5_617, data.tuple_5_618, data.tuple_5_619,
            data.tuple_5_620, data.tuple_5_621, data.tuple_5_622, data.tuple_5_623, data.tuple_5_624, data.tuple_5_625, data.tuple_5_626, data.tuple_5_627, data.tuple_5_628, data.tuple_5_629,
            data.tuple_5_630, data.tuple_5_631, data.tuple_5_632, data.tuple_5_633, data.tuple_5_634, data.tuple_5_635, data.tuple_5_636, data.tuple_5_637, data.tuple_5_638, data.tuple_5_639,
            data.tuple_5_640, data.tuple_5_641, data.tuple_5_642, data.tuple_5_643, data.tuple_5_644, data.tuple_5_645, data.tuple_5_646, data.tuple_5_647, data.tuple_5_648, data.tuple_5_649,
            data.tuple_5_650, data.tuple_5_651, data.tuple_5_652, data.tuple_5_653, data.tuple_5_654, data.tuple_5_655, data.tuple_5_656, data.tuple_5_657, data.tuple_5_658, data.tuple_5_659,
            data.tuple_5_660, data.tuple_5_661, data.tuple_5_662, data.tuple_5_663
]

APS = [data.tuple_6_1, data.tuple_6_2, data.tuple_6_3, data.tuple_6_4, data.tuple_6_5, data.tuple_6_6, data.tuple_6_7, data.tuple_6_8, data.tuple_6_9, data.tuple_6_10,
       data.tuple_6_11, data.tuple_6_12, data.tuple_6_13, data.tuple_6_14, data.tuple_6_15, data.tuple_6_16, data.tuple_6_17, data.tuple_6_18, data.tuple_6_19, data.tuple_6_20,
         data.tuple_6_21, data.tuple_6_22, data.tuple_6_23, data.tuple_6_24, data.tuple_6_25, data.tuple_6_26, data.tuple_6_27, data.tuple_6_28, data.tuple_6_29, data.tuple_6_30,
            data.tuple_6_31, data.tuple_6_32, data.tuple_6_33, data.tuple_6_34, data.tuple_6_35, data.tuple_6_36, data.tuple_6_37, data.tuple_6_38, data.tuple_6_39, data.tuple_6_40,
            data.tuple_6_41, data.tuple_6_42, data.tuple_6_43, data.tuple_6_44, data.tuple_6_45, data.tuple_6_46, data.tuple_6_47, data.tuple_6_48, data.tuple_6_49, data.tuple_6_50,
            data.tuple_6_51, data.tuple_6_52, data.tuple_6_53, data.tuple_6_54, data.tuple_6_55, data.tuple_6_56, data.tuple_6_57, data.tuple_6_58, data.tuple_6_59, data.tuple_6_60,
            data.tuple_6_61, data.tuple_6_62, data.tuple_6_63, data.tuple_6_64, data.tuple_6_65, data.tuple_6_66, data.tuple_6_67, data.tuple_6_68, data.tuple_6_69, data.tuple_6_70,
            data.tuple_6_71, data.tuple_6_72, data.tuple_6_73, data.tuple_6_74, data.tuple_6_75, data.tuple_6_76, data.tuple_6_77, data.tuple_6_78, data.tuple_6_79, data.tuple_6_80,
            data.tuple_6_81, data.tuple_6_82, data.tuple_6_83, data.tuple_6_84, data.tuple_6_85, data.tuple_6_86, data.tuple_6_87, data.tuple_6_88, data.tuple_6_89, data.tuple_6_90,
            data.tuple_6_91, data.tuple_6_92, data.tuple_6_93, data.tuple_6_94, data.tuple_6_95, data.tuple_6_96, data.tuple_6_97, data.tuple_6_98, data.tuple_6_99, data.tuple_6_100,
            data.tuple_6_101, data.tuple_6_102, data.tuple_6_103, data.tuple_6_104, data.tuple_6_105, data.tuple_6_106, data.tuple_6_107, data.tuple_6_108, data.tuple_6_109, data.tuple_6_110,
            data.tuple_6_111, data.tuple_6_112, data.tuple_6_113, data.tuple_6_114, data.tuple_6_115, data.tuple_6_116, data.tuple_6_117, data.tuple_6_118, data.tuple_6_119, data.tuple_6_120,
            data.tuple_6_121, data.tuple_6_122, data.tuple_6_123, data.tuple_6_124, data.tuple_6_125, data.tuple_6_126, data.tuple_6_127, data.tuple_6_128, data.tuple_6_129, data.tuple_6_130,
            data.tuple_6_131, data.tuple_6_132, data.tuple_6_133, data.tuple_6_134, data.tuple_6_135, data.tuple_6_136, data.tuple_6_137, data.tuple_6_138, data.tuple_6_139, data.tuple_6_140,
            data.tuple_6_141, data.tuple_6_142, data.tuple_6_143, data.tuple_6_144, data.tuple_6_145, data.tuple_6_146, data.tuple_6_147, data.tuple_6_148, data.tuple_6_149, data.tuple_6_150,
            data.tuple_6_151, data.tuple_6_152, data.tuple_6_153, data.tuple_6_154, data.tuple_6_155, data.tuple_6_156, data.tuple_6_157, data.tuple_6_158, data.tuple_6_159, data.tuple_6_160,
            data.tuple_6_161, data.tuple_6_162, data.tuple_6_163, data.tuple_6_164, data.tuple_6_165, data.tuple_6_166, data.tuple_6_167, data.tuple_6_168, data.tuple_6_169, data.tuple_6_170,
            data.tuple_6_171, data.tuple_6_172, data.tuple_6_173, data.tuple_6_174, data.tuple_6_175, data.tuple_6_176, data.tuple_6_177, data.tuple_6_178, data.tuple_6_179, data.tuple_6_180,
            data.tuple_6_181, data.tuple_6_182, data.tuple_6_183, data.tuple_6_184, data.tuple_6_185, data.tuple_6_186, data.tuple_6_187, data.tuple_6_188, data.tuple_6_189,
            data.tuple_6_190, data.tuple_6_191, data.tuple_6_192, data.tuple_6_193, data.tuple_6_194, data.tuple_6_195, data.tuple_6_196, data.tuple_6_197, data.tuple_6_198, data.tuple_6_199,
            data.tuple_6_200, data.tuple_6_201, data.tuple_6_202, data.tuple_6_203, data.tuple_6_204, data.tuple_6_205, data.tuple_6_206, data.tuple_6_207, data.tuple_6_208, data.tuple_6_209,
            data.tuple_6_210, data.tuple_6_211, data.tuple_6_212, data.tuple_6_213, data.tuple_6_214, data.tuple_6_215, data.tuple_6_216, data.tuple_6_217, data.tuple_6_218, data.tuple_6_219,
            data.tuple_6_220, data.tuple_6_221, data.tuple_6_222, data.tuple_6_223, data.tuple_6_224, data.tuple_6_225, data.tuple_6_226, data.tuple_6_227, data.tuple_6_228, data.tuple_6_229,
            data.tuple_6_230, data.tuple_6_231, data.tuple_6_232, data.tuple_6_233, data.tuple_6_234, data.tuple_6_235, data.tuple_6_236, data.tuple_6_237, data.tuple_6_238, data.tuple_6_239,
            data.tuple_6_240, data.tuple_6_241, data.tuple_6_242, data.tuple_6_243, data.tuple_6_244, data.tuple_6_245, data.tuple_6_246, data.tuple_6_247, data.tuple_6_248, data.tuple_6_249,
            data.tuple_6_250, data.tuple_6_251, data.tuple_6_252, data.tuple_6_253, data.tuple_6_254, data.tuple_6_255, data.tuple_6_256, data.tuple_6_257, data.tuple_6_258, data.tuple_6_259,
            data.tuple_6_260, data.tuple_6_261, data.tuple_6_262, data.tuple_6_263, data.tuple_6_264, data.tuple_6_265, data.tuple_6_266, data.tuple_6_267, data.tuple_6_268, data.tuple_6_269,
            data.tuple_6_270, data.tuple_6_271, data.tuple_6_272, data.tuple_6_273, data.tuple_6_274, data.tuple_6_275, data.tuple_6_276, data.tuple_6_277, data.tuple_6_278, data.tuple_6_279,
            data.tuple_6_280, data.tuple_6_281, data.tuple_6_282, data.tuple_6_283, data.tuple_6_284, data.tuple_6_285, data.tuple_6_286, data.tuple_6_287, data.tuple_6_288, data.tuple_6_289,
            data.tuple_6_290, data.tuple_6_291, data.tuple_6_292, data.tuple_6_293, data.tuple_6_294, data.tuple_6_295, data.tuple_6_296, data.tuple_6_297, data.tuple_6_298, data.tuple_6_299,
            data.tuple_6_300, data.tuple_6_301, data.tuple_6_302, data.tuple_6_303, data.tuple_6_304, data.tuple_6_305, data.tuple_6_306, data.tuple_6_307, data.tuple_6_308, data.tuple_6_309,
            data.tuple_6_310, data.tuple_6_311, data.tuple_6_312, data.tuple_6_313, data.tuple_6_314, data.tuple_6_315, data.tuple_6_316, data.tuple_6_317, data.tuple_6_318, data.tuple_6_319,
            data.tuple_6_320, data.tuple_6_321, data.tuple_6_322, data.tuple_6_323, data.tuple_6_324, data.tuple_6_325, data.tuple_6_326, data.tuple_6_327, data.tuple_6_328, data.tuple_6_329,
            data.tuple_6_330, data.tuple_6_331, data.tuple_6_332, data.tuple_6_333, data.tuple_6_334, data.tuple_6_335, data.tuple_6_336, data.tuple_6_337, data.tuple_6_338, data.tuple_6_339,
            data.tuple_6_340, data.tuple_6_341, data.tuple_6_342, data.tuple_6_343, data.tuple_6_344, data.tuple_6_345, data.tuple_6_346, data.tuple_6_347, data.tuple_6_348, data.tuple_6_349,
            data.tuple_6_350, data.tuple_6_351, data.tuple_6_352, data.tuple_6_353, data.tuple_6_354, data.tuple_6_355, data.tuple_6_356, data.tuple_6_357, data.tuple_6_358, data.tuple_6_359,
            data.tuple_6_360, data.tuple_6_361, data.tuple_6_362, data.tuple_6_363, data.tuple_6_364, data.tuple_6_365, data.tuple_6_366, data.tuple_6_367, data.tuple_6_368, data.tuple_6_369,
            data.tuple_6_370, data.tuple_6_371, data.tuple_6_372, data.tuple_6_373, data.tuple_6_374, data.tuple_6_375, data.tuple_6_376, data.tuple_6_377, data.tuple_6_378, data.tuple_6_379,
            data.tuple_6_380, data.tuple_6_381, data.tuple_6_382, data.tuple_6_383, data.tuple_6_384, data.tuple_6_385, data.tuple_6_386, data.tuple_6_387, data.tuple_6_388, data.tuple_6_389,
            data.tuple_6_390, data.tuple_6_391, data.tuple_6_392, data.tuple_6_393, data.tuple_6_394, data.tuple_6_395, data.tuple_6_396, data.tuple_6_397, data.tuple_6_398, data.tuple_6_399,
            data.tuple_6_400, data.tuple_6_401, data.tuple_6_402, data.tuple_6_403, data.tuple_6_404, data.tuple_6_405, data.tuple_6_406, data.tuple_6_407, data.tuple_6_408, data.tuple_6_409,
            data.tuple_6_410, data.tuple_6_411, data.tuple_6_412, data.tuple_6_413, data.tuple_6_414, data.tuple_6_415, data.tuple_6_416, data.tuple_6_417, data.tuple_6_418, data.tuple_6_419,
            data.tuple_6_420, data.tuple_6_421, data.tuple_6_422, data.tuple_6_423, data.tuple_6_424, data.tuple_6_425, data.tuple_6_426, data.tuple_6_427, data.tuple_6_428, data.tuple_6_429,
            data.tuple_6_430, data.tuple_6_431, data.tuple_6_432, data.tuple_6_433, data.tuple_6_434, data.tuple_6_435, data.tuple_6_436, data.tuple_6_437, data.tuple_6_438, data.tuple_6_439,
            data.tuple_6_440, data.tuple_6_441, data.tuple_6_442, data.tuple_6_443, data.tuple_6_444, data.tuple_6_445, data.tuple_6_446, data.tuple_6_447, data.tuple_6_448, data.tuple_6_449,
            data.tuple_6_450, data.tuple_6_451, data.tuple_6_452, data.tuple_6_453, data.tuple_6_454, data.tuple_6_455, data.tuple_6_456, data.tuple_6_457, data.tuple_6_458, data.tuple_6_459,
            data.tuple_6_460, data.tuple_6_461, data.tuple_6_462, data.tuple_6_463, data.tuple_6_464, data.tuple_6_465, data.tuple_6_466, data.tuple_6_467, data.tuple_6_468, data.tuple_6_469,
            data.tuple_6_470, data.tuple_6_471, data.tuple_6_472, data.tuple_6_473, data.tuple_6_474, data.tuple_6_475, data.tuple_6_476, data.tuple_6_477, data.tuple_6_478, data.tuple_6_479,
            data.tuple_6_480, data.tuple_6_481, data.tuple_6_482, data.tuple_6_483, data.tuple_6_484, data.tuple_6_485, data.tuple_6_486, data.tuple_6_487, data.tuple_6_488, data.tuple_6_489,
            data.tuple_6_490, data.tuple_6_491, data.tuple_6_492, data.tuple_6_493, data.tuple_6_494, data.tuple_6_495, data.tuple_6_496, data.tuple_6_497, data.tuple_6_498, data.tuple_6_499,
            data.tuple_6_500, data.tuple_6_501, data.tuple_6_502, data.tuple_6_503, data.tuple_6_504, data.tuple_6_505, data.tuple_6_506, data.tuple_6_507, data.tuple_6_508, data.tuple_6_509,
            data.tuple_6_510, data.tuple_6_511, data.tuple_6_512, data.tuple_6_513, data.tuple_6_514, data.tuple_6_515, data.tuple_6_516, data.tuple_6_517, data.tuple_6_518, data.tuple_6_519,
            data.tuple_6_520, data.tuple_6_521, data.tuple_6_522, data.tuple_6_523, data.tuple_6_524, data.tuple_6_525, data.tuple_6_526, data.tuple_6_527, data.tuple_6_528, data.tuple_6_529,
            data.tuple_6_530, data.tuple_6_531, data.tuple_6_532, data.tuple_6_533, data.tuple_6_534, data.tuple_6_535, data.tuple_6_536, data.tuple_6_537, data.tuple_6_538, data.tuple_6_539,
            data.tuple_6_540, data.tuple_6_541, data.tuple_6_542, data.tuple_6_543, data.tuple_6_544, data.tuple_6_545, data.tuple_6_546, data.tuple_6_547, data.tuple_6_548, data.tuple_6_549,
            data.tuple_6_550, data.tuple_6_551, data.tuple_6_552, data.tuple_6_553, data.tuple_6_554, data.tuple_6_555, data.tuple_6_556, data.tuple_6_557, data.tuple_6_558, data.tuple_6_559,
            data.tuple_6_560, data.tuple_6_561, data.tuple_6_562, data.tuple_6_563, data.tuple_6_564, data.tuple_6_565, data.tuple_6_566, data.tuple_6_567, data.tuple_6_568, data.tuple_6_569,
            data.tuple_6_570, data.tuple_6_571, data.tuple_6_572, data.tuple_6_573, data.tuple_6_574, data.tuple_6_575, data.tuple_6_576, data.tuple_6_577, data.tuple_6_578, data.tuple_6_579,
            data.tuple_6_580, data.tuple_6_581, data.tuple_6_582, data.tuple_6_583, data.tuple_6_584, data.tuple_6_585, data.tuple_6_586, data.tuple_6_587, data.tuple_6_588, data.tuple_6_589,
            data.tuple_6_590, data.tuple_6_591, data.tuple_6_592, data.tuple_6_593, data.tuple_6_594, data.tuple_6_595, data.tuple_6_596, data.tuple_6_597, data.tuple_6_598, data.tuple_6_599,
            data.tuple_6_600, data.tuple_6_601, data.tuple_6_602, data.tuple_6_603, data.tuple_6_604, data.tuple_6_605, data.tuple_6_606, data.tuple_6_607, data.tuple_6_608, data.tuple_6_609,
            data.tuple_6_610, data.tuple_6_611, data.tuple_6_612, data.tuple_6_613, data.tuple_6_614, data.tuple_6_615, data.tuple_6_616, data.tuple_6_617, data.tuple_6_618, data.tuple_6_619,
            data.tuple_6_620, data.tuple_6_621, data.tuple_6_622, data.tuple_6_623, data.tuple_6_624, data.tuple_6_625, data.tuple_6_626, data.tuple_6_627, data.tuple_6_628, data.tuple_6_629,
            data.tuple_6_630, data.tuple_6_631, data.tuple_6_632, data.tuple_6_633, data.tuple_6_634, data.tuple_6_635, data.tuple_6_636, data.tuple_6_637, data.tuple_6_638, data.tuple_6_639,
            data.tuple_6_640, data.tuple_6_641, data.tuple_6_642, data.tuple_6_643, data.tuple_6_644, data.tuple_6_645, data.tuple_6_646, data.tuple_6_647, data.tuple_6_648, data.tuple_6_649,
            data.tuple_6_650, data.tuple_6_651, data.tuple_6_652, data.tuple_6_653, data.tuple_6_654, data.tuple_6_655, data.tuple_6_656, data.tuple_6_657, data.tuple_6_658, data.tuple_6_659,
            data.tuple_6_660, data.tuple_6_661, data.tuple_6_662, data.tuple_6_663, data.tuple_6_664, data.tuple_6_665, data.tuple_6_666, data.tuple_6_667, data.tuple_6_668, data.tuple_6_669,
            data.tuple_6_670, data.tuple_6_671, data.tuple_6_672, data.tuple_6_673, data.tuple_6_674, data.tuple_6_675, data.tuple_6_676, data.tuple_6_677, data.tuple_6_678, data.tuple_6_679,
            data.tuple_6_680, data.tuple_6_681, data.tuple_6_682, data.tuple_6_683, data.tuple_6_684, data.tuple_6_685, data.tuple_6_686, data.tuple_6_687, data.tuple_6_688, data.tuple_6_689,
            data.tuple_6_690, data.tuple_6_691, data.tuple_6_692, data.tuple_6_693, data.tuple_6_694
]

HESS = [data.tuple_7_1, data.tuple_7_2, data.tuple_7_3, data.tuple_7_4, data.tuple_7_5, data.tuple_7_6, data.tuple_7_7, data.tuple_7_8, data.tuple_7_9, data.tuple_7_10,
        data.tuple_7_11, data.tuple_7_12, data.tuple_7_13, data.tuple_7_14, data.tuple_7_15, data.tuple_7_16, data.tuple_7_17, data.tuple_7_18, data.tuple_7_19, data.tuple_7_20,
        data.tuple_7_21, data.tuple_7_22, data.tuple_7_23, data.tuple_7_24, data.tuple_7_25, data.tuple_7_26, data.tuple_7_27, data.tuple_7_28, data.tuple_7_29, data.tuple_7_30,
        data.tuple_7_31, data.tuple_7_32, data.tuple_7_33, data.tuple_7_34, data.tuple_7_35, data.tuple_7_36, data.tuple_7_37, data.tuple_7_38, data.tuple_7_39, data.tuple_7_40,
        data.tuple_7_41, data.tuple_7_42, data.tuple_7_43, data.tuple_7_44, data.tuple_7_45, data.tuple_7_46, data.tuple_7_47, data.tuple_7_48, data.tuple_7_49, data.tuple_7_50,
        data.tuple_7_51, data.tuple_7_52, data.tuple_7_53, data.tuple_7_54, data.tuple_7_55, data.tuple_7_56, data.tuple_7_57, data.tuple_7_58, data.tuple_7_59, data.tuple_7_60,
        data.tuple_7_61, data.tuple_7_62, data.tuple_7_63, data.tuple_7_64, data.tuple_7_65, data.tuple_7_66, data.tuple_7_67, data.tuple_7_68, data.tuple_7_69, data.tuple_7_70,
        data.tuple_7_71, data.tuple_7_72, data.tuple_7_73, data.tuple_7_74, data.tuple_7_75, data.tuple_7_76, data.tuple_7_77, data.tuple_7_78, data.tuple_7_79, data.tuple_7_80,
        data.tuple_7_81, data.tuple_7_82, data.tuple_7_83, data.tuple_7_84, data.tuple_7_85, data.tuple_7_86, data.tuple_7_87, data.tuple_7_88, data.tuple_7_89, data.tuple_7_90,
        data.tuple_7_91, data.tuple_7_92, data.tuple_7_93, data.tuple_7_94, data.tuple_7_95, data.tuple_7_96, data.tuple_7_97, data.tuple_7_98, data.tuple_7_99, data.tuple_7_100,
        data.tuple_7_101, data.tuple_7_102, data.tuple_7_103, data.tuple_7_104, data.tuple_7_105, data.tuple_7_106, data.tuple_7_107, data.tuple_7_108, data.tuple_7_109, data.tuple_7_110,
        data.tuple_7_111, data.tuple_7_112, data.tuple_7_113, data.tuple_7_114, data.tuple_7_115, data.tuple_7_116, data.tuple_7_117, data.tuple_7_118, data.tuple_7_119, data.tuple_7_120,
        data.tuple_7_121, data.tuple_7_122, data.tuple_7_123, data.tuple_7_124, data.tuple_7_125, data.tuple_7_126, data.tuple_7_127, data.tuple_7_128, data.tuple_7_129, data.tuple_7_130,
        data.tuple_7_131, data.tuple_7_132, data.tuple_7_133, data.tuple_7_134, data.tuple_7_135, data.tuple_7_136, data.tuple_7_137, data.tuple_7_138, data.tuple_7_139, data.tuple_7_140,
        data.tuple_7_141, data.tuple_7_142, data.tuple_7_143, data.tuple_7_144, data.tuple_7_145, data.tuple_7_146, data.tuple_7_147, data.tuple_7_148, data.tuple_7_149, data.tuple_7_150,
        data.tuple_7_151, data.tuple_7_152, data.tuple_7_153, data.tuple_7_154, data.tuple_7_155, data.tuple_7_156, data.tuple_7_157, data.tuple_7_158, data.tuple_7_159, data.tuple_7_160,
        data.tuple_7_161, data.tuple_7_162, data.tuple_7_163, data.tuple_7_164, data.tuple_7_165, data.tuple_7_166, data.tuple_7_167, data.tuple_7_168, data.tuple_7_169, data.tuple_7_170,
        data.tuple_7_171, data.tuple_7_172, data.tuple_7_173, data.tuple_7_174, data.tuple_7_175, data.tuple_7_176, data.tuple_7_177, data.tuple_7_178, data.tuple_7_179, data.tuple_7_180,
        data.tuple_7_181, data.tuple_7_182, data.tuple_7_183, data.tuple_7_184, data.tuple_7_185, data.tuple_7_186, data.tuple_7_187, data.tuple_7_188, data.tuple_7_189,
        data.tuple_7_190, data.tuple_7_191, data.tuple_7_192, data.tuple_7_193, data.tuple_7_194, data.tuple_7_195, data.tuple_7_196, data.tuple_7_197, data.tuple_7_198, data.tuple_7_199,
        data.tuple_7_200, data.tuple_7_201, data.tuple_7_202, data.tuple_7_203, data.tuple_7_204, data.tuple_7_205, data.tuple_7_206, data.tuple_7_207, data.tuple_7_208, data.tuple_7_209,
        data.tuple_7_210, data.tuple_7_211, data.tuple_7_212, data.tuple_7_213, data.tuple_7_214, data.tuple_7_215, data.tuple_7_216, data.tuple_7_217, data.tuple_7_218, data.tuple_7_219,
        data.tuple_7_220, data.tuple_7_221, data.tuple_7_222, data.tuple_7_223, data.tuple_7_224, data.tuple_7_225, data.tuple_7_226, data.tuple_7_227, data.tuple_7_228, data.tuple_7_229,
        data.tuple_7_230, data.tuple_7_231, data.tuple_7_232, data.tuple_7_233, data.tuple_7_234, data.tuple_7_235, data.tuple_7_236, data.tuple_7_237, data.tuple_7_238, data.tuple_7_239,
        data.tuple_7_240, data.tuple_7_241, data.tuple_7_242, data.tuple_7_243, data.tuple_7_244, data.tuple_7_245, data.tuple_7_246, data.tuple_7_247, data.tuple_7_248, data.tuple_7_249,
        data.tuple_7_250, data.tuple_7_251, data.tuple_7_252, data.tuple_7_253, data.tuple_7_254, data.tuple_7_255, data.tuple_7_256, data.tuple_7_257, data.tuple_7_258, data.tuple_7_259,
        data.tuple_7_260, data.tuple_7_261, data.tuple_7_262, data.tuple_7_263, data.tuple_7_264, data.tuple_7_265, data.tuple_7_266, data.tuple_7_267, data.tuple_7_268, data.tuple_7_269,
        data.tuple_7_270, data.tuple_7_271, data.tuple_7_272, data.tuple_7_273, data.tuple_7_274, data.tuple_7_275, data.tuple_7_276, data.tuple_7_277, data.tuple_7_278, data.tuple_7_279,
        data.tuple_7_280, data.tuple_7_281, data.tuple_7_282, data.tuple_7_283, data.tuple_7_284, data.tuple_7_285, data.tuple_7_286, data.tuple_7_287, data.tuple_7_288, data.tuple_7_289,
        data.tuple_7_290, data.tuple_7_291, data.tuple_7_292, data.tuple_7_293, data.tuple_7_294, data.tuple_7_295, data.tuple_7_296, data.tuple_7_297, data.tuple_7_298, data.tuple_7_299,
        data.tuple_7_300, data.tuple_7_301, data.tuple_7_302, data.tuple_7_303, data.tuple_7_304, data.tuple_7_305, data.tuple_7_306, data.tuple_7_307, data.tuple_7_308, data.tuple_7_309,
        data.tuple_7_310, data.tuple_7_311, data.tuple_7_312, data.tuple_7_313, data.tuple_7_314, data.tuple_7_315, data.tuple_7_316, data.tuple_7_317, data.tuple_7_318, data.tuple_7_319,
        data.tuple_7_320, data.tuple_7_321, data.tuple_7_322, data.tuple_7_323, data.tuple_7_324, data.tuple_7_325, data.tuple_7_326, data.tuple_7_327, data.tuple_7_328, data.tuple_7_329,
        data.tuple_7_330, data.tuple_7_331, data.tuple_7_332, data.tuple_7_333, data.tuple_7_334, data.tuple_7_335, data.tuple_7_336, data.tuple_7_337, data.tuple_7_338, data.tuple_7_339,
        data.tuple_7_340, data.tuple_7_341, data.tuple_7_342, data.tuple_7_343, data.tuple_7_344, data.tuple_7_345, data.tuple_7_346, data.tuple_7_347, data.tuple_7_348, data.tuple_7_349,
        data.tuple_7_350, data.tuple_7_351, data.tuple_7_352, data.tuple_7_353, data.tuple_7_354, data.tuple_7_355, data.tuple_7_356, data.tuple_7_357, data.tuple_7_358, data.tuple_7_359,
        data.tuple_7_360, data.tuple_7_361, data.tuple_7_362, data.tuple_7_363, data.tuple_7_364, data.tuple_7_365, data.tuple_7_366, data.tuple_7_367, data.tuple_7_368, data.tuple_7_369,
        data.tuple_7_370, data.tuple_7_371, data.tuple_7_372, data.tuple_7_373, data.tuple_7_374, data.tuple_7_375, data.tuple_7_376, data.tuple_7_377, data.tuple_7_378, data.tuple_7_379,
        data.tuple_7_380, data.tuple_7_381, data.tuple_7_382, data.tuple_7_383, data.tuple_7_384, data.tuple_7_385, data.tuple_7_386, data.tuple_7_387, data.tuple_7_388, data.tuple_7_389,
        data.tuple_7_390, data.tuple_7_391, data.tuple_7_392, data.tuple_7_393, data.tuple_7_394, data.tuple_7_395, data.tuple_7_396, data.tuple_7_397, data.tuple_7_398, data.tuple_7_399,
        data.tuple_7_400, data.tuple_7_401, data.tuple_7_402, data.tuple_7_403, data.tuple_7_404, data.tuple_7_405, data.tuple_7_406, data.tuple_7_407, data.tuple_7_408, data.tuple_7_409,
        data.tuple_7_410, data.tuple_7_411, data.tuple_7_412, data.tuple_7_413, data.tuple_7_414, data.tuple_7_415, data.tuple_7_416, data.tuple_7_417, data.tuple_7_418, data.tuple_7_419,
        data.tuple_7_420, data.tuple_7_421, data.tuple_7_422, data.tuple_7_423, data.tuple_7_424, data.tuple_7_425, data.tuple_7_426, data.tuple_7_427, data.tuple_7_428, data.tuple_7_429,
        data.tuple_7_430, data.tuple_7_431, data.tuple_7_432, data.tuple_7_433, data.tuple_7_434, data.tuple_7_435, data.tuple_7_436, data.tuple_7_437, data.tuple_7_438, data.tuple_7_439,
        data.tuple_7_440, data.tuple_7_441, data.tuple_7_442, data.tuple_7_443, data.tuple_7_444, data.tuple_7_445, data.tuple_7_446, data.tuple_7_447, data.tuple_7_448, data.tuple_7_449,
        data.tuple_7_450, data.tuple_7_451, data.tuple_7_452, data.tuple_7_453, data.tuple_7_454, data.tuple_7_455, data.tuple_7_456, data.tuple_7_457, data.tuple_7_458, data.tuple_7_459,
        data.tuple_7_460, data.tuple_7_461, data.tuple_7_462, data.tuple_7_463, data.tuple_7_464, data.tuple_7_465, data.tuple_7_466, data.tuple_7_467, data.tuple_7_468, data.tuple_7_469,
        data.tuple_7_470, data.tuple_7_471, data.tuple_7_472, data.tuple_7_473, data.tuple_7_474, data.tuple_7_475, data.tuple_7_476, data.tuple_7_477, data.tuple_7_478, data.tuple_7_479,
        data.tuple_7_480, data.tuple_7_481, data.tuple_7_482, data.tuple_7_483, data.tuple_7_484, data.tuple_7_485, data.tuple_7_486, data.tuple_7_487, data.tuple_7_488, data.tuple_7_489,
        data.tuple_7_490, data.tuple_7_491, data.tuple_7_492, data.tuple_7_493, data.tuple_7_494, data.tuple_7_495, data.tuple_7_496, data.tuple_7_497, data.tuple_7_498, data.tuple_7_499,
        data.tuple_7_500, data.tuple_7_501, data.tuple_7_502, data.tuple_7_503, data.tuple_7_504, data.tuple_7_505, data.tuple_7_506, data.tuple_7_507, data.tuple_7_508, data.tuple_7_509,
        data.tuple_7_510, data.tuple_7_511, data.tuple_7_512, data.tuple_7_513, data.tuple_7_514, data.tuple_7_515, data.tuple_7_516, data.tuple_7_517, data.tuple_7_518, data.tuple_7_519,
        data.tuple_7_520, data.tuple_7_521, data.tuple_7_522, data.tuple_7_523, data.tuple_7_524, data.tuple_7_525, data.tuple_7_526, data.tuple_7_527, data.tuple_7_528, data.tuple_7_529,
        data.tuple_7_530, data.tuple_7_531, data.tuple_7_532, data.tuple_7_533, data.tuple_7_534, data.tuple_7_535, data.tuple_7_536, data.tuple_7_537, data.tuple_7_538, data.tuple_7_539,
        data.tuple_7_540, data.tuple_7_541, data.tuple_7_542, data.tuple_7_543, data.tuple_7_544, data.tuple_7_545, data.tuple_7_546, data.tuple_7_547, data.tuple_7_548, data.tuple_7_549,
        data.tuple_7_550, data.tuple_7_551, data.tuple_7_552, data.tuple_7_553, data.tuple_7_554, data.tuple_7_555, data.tuple_7_556, data.tuple_7_557, data.tuple_7_558, data.tuple_7_559,
        data.tuple_7_560, data.tuple_7_561, data.tuple_7_562, data.tuple_7_563, data.tuple_7_564, data.tuple_7_565, data.tuple_7_566, data.tuple_7_567, data.tuple_7_568, data.tuple_7_569,
        data.tuple_7_570, data.tuple_7_571, data.tuple_7_572, data.tuple_7_573, data.tuple_7_574, data.tuple_7_575, data.tuple_7_576, data.tuple_7_577, data.tuple_7_578, data.tuple_7_579,
        data.tuple_7_580, data.tuple_7_581, data.tuple_7_582, data.tuple_7_583, data.tuple_7_584, data.tuple_7_585, data.tuple_7_586, data.tuple_7_587, data.tuple_7_588, data.tuple_7_589,
        data.tuple_7_590, data.tuple_7_591, data.tuple_7_592, data.tuple_7_593, data.tuple_7_594, data.tuple_7_595, data.tuple_7_596, data.tuple_7_597, data.tuple_7_598, data.tuple_7_599,
        data.tuple_7_600, data.tuple_7_601, data.tuple_7_602, data.tuple_7_603, data.tuple_7_604, data.tuple_7_605, data.tuple_7_606, data.tuple_7_607, data.tuple_7_608, data.tuple_7_609,
        data.tuple_7_610, data.tuple_7_611, data.tuple_7_612, data.tuple_7_613, data.tuple_7_614, data.tuple_7_615, data.tuple_7_616, data.tuple_7_617, data.tuple_7_618, data.tuple_7_619,
        data.tuple_7_620, data.tuple_7_621, data.tuple_7_622, data.tuple_7_623, data.tuple_7_624, data.tuple_7_625, data.tuple_7_626, data.tuple_7_627, data.tuple_7_628, data.tuple_7_629,
        data.tuple_7_630, data.tuple_7_631, data.tuple_7_632, data.tuple_7_633, data.tuple_7_634, data.tuple_7_635, data.tuple_7_636, data.tuple_7_637, data.tuple_7_638, data.tuple_7_639,
        data.tuple_7_640, data.tuple_7_641, data.tuple_7_642, data.tuple_7_643, data.tuple_7_644, data.tuple_7_645, data.tuple_7_646, data.tuple_7_647, data.tuple_7_648, data.tuple_7_649,
        data.tuple_7_650, data.tuple_7_651, data.tuple_7_652, data.tuple_7_653, data.tuple_7_654, data.tuple_7_655, data.tuple_7_656, data.tuple_7_657, data.tuple_7_658, data.tuple_7_659,
        data.tuple_7_660, data.tuple_7_661, data.tuple_7_662, data.tuple_7_663, data.tuple_7_664, data.tuple_7_665, data.tuple_7_666, data.tuple_7_667, data.tuple_7_668, data.tuple_7_669,
        data.tuple_7_670, data.tuple_7_671, data.tuple_7_672, data.tuple_7_673, data.tuple_7_674, data.tuple_7_675, data.tuple_7_676, data.tuple_7_677, data.tuple_7_678, data.tuple_7_679,
        data.tuple_7_680, data.tuple_7_681, data.tuple_7_682, data.tuple_7_683, data.tuple_7_684, data.tuple_7_685, data.tuple_7_686, data.tuple_7_687, data.tuple_7_688, data.tuple_7_689,
        data.tuple_7_690, data.tuple_7_691, data.tuple_7_692, data.tuple_7_693
]

SAPS = [data.tuple_8_1, data.tuple_8_2, data.tuple_8_3, data.tuple_8_4, data.tuple_8_5, data.tuple_8_6, data.tuple_8_7, data.tuple_8_8, data.tuple_8_9, data.tuple_8_10,
        data.tuple_8_11, data.tuple_8_12, data.tuple_8_13, data.tuple_8_14, data.tuple_8_15, data.tuple_8_16, data.tuple_8_17, data.tuple_8_18, data.tuple_8_19, data.tuple_8_20,
        data.tuple_8_21, data.tuple_8_22, data.tuple_8_23, data.tuple_8_24, data.tuple_8_25, data.tuple_8_26, data.tuple_8_27, data.tuple_8_28, data.tuple_8_29, data.tuple_8_30,
        data.tuple_8_31, data.tuple_8_32, data.tuple_8_33, data.tuple_8_34, data.tuple_8_35, data.tuple_8_36, data.tuple_8_37, data.tuple_8_38, data.tuple_8_39, data.tuple_8_40,
        data.tuple_8_41, data.tuple_8_42, data.tuple_8_43, data.tuple_8_44, data.tuple_8_45, data.tuple_8_46, data.tuple_8_47, data.tuple_8_48, data.tuple_8_49, data.tuple_8_50,
        data.tuple_8_51, data.tuple_8_52
]

Secondaire = [data.tuple_9_1, data.tuple_9_2, data.tuple_9_3, data.tuple_9_4, data.tuple_9_5, data.tuple_9_6, data.tuple_9_7, data.tuple_9_8, data.tuple_9_9, data.tuple_9_10,
              data.tuple_9_11, data.tuple_9_12, data.tuple_9_13, data.tuple_9_14, data.tuple_9_15, data.tuple_9_16, data.tuple_9_17, data.tuple_9_18, data.tuple_9_19, data.tuple_9_20,
              data.tuple_9_21, data.tuple_9_22, data.tuple_9_23, data.tuple_9_24, data.tuple_9_25, data.tuple_9_26, data.tuple_9_27, data.tuple_9_28, data.tuple_9_29, data.tuple_9_30,
              data.tuple_9_31, data.tuple_9_32, data.tuple_9_33, data.tuple_9_34, data.tuple_9_35, data.tuple_9_36, data.tuple_9_37, data.tuple_9_38, data.tuple_9_39, data.tuple_9_40,
              data.tuple_9_41, data.tuple_9_42, data.tuple_9_43, data.tuple_9_44, data.tuple_9_45, data.tuple_9_46, data.tuple_9_47, data.tuple_9_48, data.tuple_9_49, data.tuple_9_50,
              data.tuple_9_51, data.tuple_9_52, data.tuple_9_53, data.tuple_9_54, data.tuple_9_55, data.tuple_9_56, data.tuple_9_57, data.tuple_9_58, data.tuple_9_59, data.tuple_9_60,
              data.tuple_9_61, data.tuple_9_62, data.tuple_9_63, data.tuple_9_64, data.tuple_9_65, data.tuple_9_66, data.tuple_9_67, data.tuple_9_68, data.tuple_9_69, data.tuple_9_70,
              data.tuple_9_71, data.tuple_9_72, data.tuple_9_73, data.tuple_9_74, data.tuple_9_75, data.tuple_9_76, data.tuple_9_77, data.tuple_9_78, data.tuple_9_79, data.tuple_9_80,
                data.tuple_9_81, data.tuple_9_82, data.tuple_9_83, data.tuple_9_84, data.tuple_9_85, data.tuple_9_86, data.tuple_9_87, data.tuple_9_88, data.tuple_9_89, data.tuple_9_90,
                data.tuple_9_91, data.tuple_9_92, data.tuple_9_93, data.tuple_9_94, data.tuple_9_95, data.tuple_9_96, data.tuple_9_97, data.tuple_9_98, data.tuple_9_99, data.tuple_9_100,
                data.tuple_9_101, data.tuple_9_102, data.tuple_9_103, data.tuple_9_104, data.tuple_9_105, data.tuple_9_106, data.tuple_9_107, data.tuple_9_108, data.tuple_9_109, data.tuple_9_110,
                data.tuple_9_111, data.tuple_9_112, data.tuple_9_113, data.tuple_9_114, data.tuple_9_115, data.tuple_9_116, data.tuple_9_117, data.tuple_9_118, data.tuple_9_119, data.tuple_9_120,
                data.tuple_9_121, data.tuple_9_122, data.tuple_9_123, data.tuple_9_124, data.tuple_9_125, data.tuple_9_126, data.tuple_9_127, data.tuple_9_128, data.tuple_9_129, data.tuple_9_130,
                data.tuple_9_131, data.tuple_9_132, data.tuple_9_133, data.tuple_9_134, data.tuple_9_135, data.tuple_9_136, data.tuple_9_137, data.tuple_9_138, data.tuple_9_139, data.tuple_9_140,
                data.tuple_9_141, data.tuple_9_142, data.tuple_9_143, data.tuple_9_144, data.tuple_9_145, data.tuple_9_146, data.tuple_9_147, data.tuple_9_148, data.tuple_9_149, data.tuple_9_150,
                data.tuple_9_151, data.tuple_9_152, data.tuple_9_153, data.tuple_9_154, data.tuple_9_155, data.tuple_9_156, data.tuple_9_157, data.tuple_9_158, data.tuple_9_159, data.tuple_9_160,
                data.tuple_9_161, data.tuple_9_162, data.tuple_9_163, data.tuple_9_164, data.tuple_9_165, data.tuple_9_166, data.tuple_9_167, data.tuple_9_168, data.tuple_9_169, data.tuple_9_170,
                data.tuple_9_171, data.tuple_9_172, data.tuple_9_173, data.tuple_9_174, data.tuple_9_175, data.tuple_9_176, data.tuple_9_177, data.tuple_9_178, data.tuple_9_179, data.tuple_9_180,
                data.tuple_9_181, data.tuple_9_182, data.tuple_9_183, data.tuple_9_184, data.tuple_9_185, data.tuple_9_186, data.tuple_9_187, data.tuple_9_188, data.tuple_9_189,
                data.tuple_9_190, data.tuple_9_191, data.tuple_9_192, data.tuple_9_193, data.tuple_9_194, data.tuple_9_195, data.tuple_9_196, data.tuple_9_197, data.tuple_9_198, data.tuple_9_199,
                data.tuple_9_200, data.tuple_9_201, data.tuple_9_202, data.tuple_9_203, data.tuple_9_204, data.tuple_9_205, data.tuple_9_206, data.tuple_9_207, data.tuple_9_208, data.tuple_9_209,
                data.tuple_9_210, data.tuple_9_211, data.tuple_9_212, data.tuple_9_213, data.tuple_9_214, data.tuple_9_215, data.tuple_9_216, data.tuple_9_217, data.tuple_9_218, data.tuple_9_219,
                data.tuple_9_220, data.tuple_9_221, data.tuple_9_222, data.tuple_9_223, data.tuple_9_224, data.tuple_9_225, data.tuple_9_226, data.tuple_9_227, data.tuple_9_228, data.tuple_9_229,
                data.tuple_9_230, data.tuple_9_231, data.tuple_9_232, data.tuple_9_233, data.tuple_9_234, data.tuple_9_235, data.tuple_9_236, data.tuple_9_237, data.tuple_9_238, data.tuple_9_239,
                data.tuple_9_240, data.tuple_9_241, data.tuple_9_242, data.tuple_9_243, data.tuple_9_244, data.tuple_9_245, data.tuple_9_246, data.tuple_9_247, data.tuple_9_248, data.tuple_9_249,
                data.tuple_9_250, data.tuple_9_251, data.tuple_9_252, data.tuple_9_253, data.tuple_9_254, data.tuple_9_255, data.tuple_9_256, data.tuple_9_257, data.tuple_9_258, data.tuple_9_259,
                data.tuple_9_260, data.tuple_9_261, data.tuple_9_262, data.tuple_9_263, data.tuple_9_264, data.tuple_9_265, data.tuple_9_266, data.tuple_9_267, data.tuple_9_268, data.tuple_9_269,
                data.tuple_9_270, data.tuple_9_271, data.tuple_9_272, data.tuple_9_273, data.tuple_9_274, data.tuple_9_275, data.tuple_9_276, data.tuple_9_277, data.tuple_9_278, data.tuple_9_279,
                data.tuple_9_280, data.tuple_9_281, data.tuple_9_282, data.tuple_9_283, data.tuple_9_284, data.tuple_9_285, data.tuple_9_286, data.tuple_9_287, data.tuple_9_288, data.tuple_9_289,
                data.tuple_9_290, data.tuple_9_291, data.tuple_9_292, data.tuple_9_293, data.tuple_9_294, data.tuple_9_295, data.tuple_9_296, data.tuple_9_297, data.tuple_9_298, data.tuple_9_299,
                data.tuple_9_300, data.tuple_9_301, data.tuple_9_302, data.tuple_9_303, data.tuple_9_304, data.tuple_9_305, data.tuple_9_306, data.tuple_9_307, data.tuple_9_308, data.tuple_9_309,
                data.tuple_9_310, data.tuple_9_311, data.tuple_9_312, data.tuple_9_313, data.tuple_9_314, data.tuple_9_315, data.tuple_9_316, data.tuple_9_317, data.tuple_9_318, data.tuple_9_319,
                data.tuple_9_320, data.tuple_9_321, data.tuple_9_322, data.tuple_9_323, data.tuple_9_324, data.tuple_9_325, data.tuple_9_326, data.tuple_9_327, data.tuple_9_328, data.tuple_9_329,
                data.tuple_9_330, data.tuple_9_331, data.tuple_9_332, data.tuple_9_333, data.tuple_9_334, data.tuple_9_335, data.tuple_9_336, data.tuple_9_337, data.tuple_9_338, data.tuple_9_339,
                data.tuple_9_340, data.tuple_9_341, data.tuple_9_342, data.tuple_9_343, data.tuple_9_344, data.tuple_9_345, data.tuple_9_346, data.tuple_9_347, data.tuple_9_348, data.tuple_9_349,
                data.tuple_9_350, data.tuple_9_351, data.tuple_9_352, data.tuple_9_353, data.tuple_9_354, data.tuple_9_355, data.tuple_9_356, data.tuple_9_357, data.tuple_9_358, data.tuple_9_359,
                data.tuple_9_360, data.tuple_9_361, data.tuple_9_362, data.tuple_9_363, data.tuple_9_364, data.tuple_9_365, data.tuple_9_366, data.tuple_9_367, data.tuple_9_368, data.tuple_9_369,
                data.tuple_9_370, data.tuple_9_371, data.tuple_9_372, data.tuple_9_373, data.tuple_9_374, data.tuple_9_375, data.tuple_9_376, data.tuple_9_377, data.tuple_9_378, data.tuple_9_379,
                data.tuple_9_380, data.tuple_9_381, data.tuple_9_382, data.tuple_9_383, data.tuple_9_384, data.tuple_9_385, data.tuple_9_386, data.tuple_9_387, data.tuple_9_388, data.tuple_9_389,
                data.tuple_9_390, data.tuple_9_391, data.tuple_9_392, data.tuple_9_393, data.tuple_9_394, data.tuple_9_395, data.tuple_9_396, data.tuple_9_397, data.tuple_9_398, data.tuple_9_399,
                data.tuple_9_400, data.tuple_9_401, data.tuple_9_402, data.tuple_9_403, data.tuple_9_404, data.tuple_9_405, data.tuple_9_406, data.tuple_9_407, data.tuple_9_408, data.tuple_9_409,
                data.tuple_9_410, data.tuple_9_411, data.tuple_9_412, data.tuple_9_413, data.tuple_9_414, data.tuple_9_415, data.tuple_9_416, data.tuple_9_417, data.tuple_9_418, data.tuple_9_419,
                data.tuple_9_420, data.tuple_9_421, data.tuple_9_422, data.tuple_9_423, data.tuple_9_424, data.tuple_9_425, data.tuple_9_426, data.tuple_9_427, data.tuple_9_428, data.tuple_9_429,
                data.tuple_9_430, data.tuple_9_431, data.tuple_9_432, data.tuple_9_433, data.tuple_9_434, data.tuple_9_435, data.tuple_9_436, data.tuple_9_437, data.tuple_9_438, data.tuple_9_439,
                data.tuple_9_440, data.tuple_9_441, data.tuple_9_442, data.tuple_9_443, data.tuple_9_444, data.tuple_9_445, data.tuple_9_446, data.tuple_9_447, data.tuple_9_448, data.tuple_9_449,
                data.tuple_9_450, data.tuple_9_451, data.tuple_9_452, data.tuple_9_453, data.tuple_9_454, data.tuple_9_455, data.tuple_9_456, data.tuple_9_457, data.tuple_9_458, data.tuple_9_459,
                data.tuple_9_460, data.tuple_9_461, data.tuple_9_462, data.tuple_9_463, data.tuple_9_464, data.tuple_9_465, data.tuple_9_466, data.tuple_9_467, data.tuple_9_468, data.tuple_9_469,
                data.tuple_9_470, data.tuple_9_471, data.tuple_9_472, data.tuple_9_473, data.tuple_9_474, data.tuple_9_475, data.tuple_9_476, data.tuple_9_477, data.tuple_9_478, data.tuple_9_479,
                data.tuple_9_480, data.tuple_9_481, data.tuple_9_482, data.tuple_9_483, data.tuple_9_484, data.tuple_9_485, data.tuple_9_486, data.tuple_9_487, data.tuple_9_488, data.tuple_9_489,
                data.tuple_9_490, data.tuple_9_491, data.tuple_9_492, data.tuple_9_493, data.tuple_9_494, data.tuple_9_495, data.tuple_9_496, data.tuple_9_497, data.tuple_9_498, data.tuple_9_499,
                data.tuple_9_500, data.tuple_9_501, data.tuple_9_502, data.tuple_9_503, data.tuple_9_504, data.tuple_9_505, data.tuple_9_506, data.tuple_9_507, data.tuple_9_508, data.tuple_9_509,
                data.tuple_9_510, data.tuple_9_511, data.tuple_9_512, data.tuple_9_513
]

Sonar = [data.tuple_10_1, data.tuple_10_2, data.tuple_10_3, data.tuple_10_4, data.tuple_10_5, data.tuple_10_6, data.tuple_10_7, data.tuple_10_8, data.tuple_10_9, data.tuple_10_10,
         data.tuple_10_11, data.tuple_10_12, data.tuple_10_13, data.tuple_10_14, data.tuple_10_15, data.tuple_10_16, data.tuple_10_17, data.tuple_10_18, data.tuple_10_19, data.tuple_10_20,
         data.tuple_10_21
]

Torp = [data.tuple_11_1, data.tuple_11_2, data.tuple_11_3, data.tuple_11_4, data.tuple_11_5, data.tuple_11_6, data.tuple_11_7, data.tuple_11_8, data.tuple_11_9, data.tuple_11_10,
        data.tuple_11_11, data.tuple_11_12, data.tuple_11_13, data.tuple_11_14, data.tuple_11_15, data.tuple_11_16, data.tuple_11_17, data.tuple_11_18, data.tuple_11_19, data.tuple_11_20,
        data.tuple_11_21, data.tuple_11_22, data.tuple_11_23, data.tuple_11_24, data.tuple_11_25, data.tuple_11_26, data.tuple_11_27, data.tuple_11_28, data.tuple_11_29, data.tuple_11_30,
        data.tuple_11_31, data.tuple_11_32, data.tuple_11_33, data.tuple_11_34, data.tuple_11_35, data.tuple_11_36, data.tuple_11_37, data.tuple_11_38, data.tuple_11_39, data.tuple_11_40,
        data.tuple_11_41, data.tuple_11_42, data.tuple_11_43, data.tuple_11_44, data.tuple_11_45, data.tuple_11_46, data.tuple_11_47, data.tuple_11_48, data.tuple_11_49, data.tuple_11_50,
        data.tuple_11_51, data.tuple_11_52, data.tuple_11_53, data.tuple_11_54, data.tuple_11_55, data.tuple_11_56, data.tuple_11_57, data.tuple_11_58, data.tuple_11_59, data.tuple_11_60,
        data.tuple_11_61, data.tuple_11_62, data.tuple_11_63, data.tuple_11_64, data.tuple_11_65, data.tuple_11_66, data.tuple_11_67, data.tuple_11_68, data.tuple_11_69, data.tuple_11_70,
        data.tuple_11_71, data.tuple_11_72, data.tuple_11_73, data.tuple_11_74, data.tuple_11_75, data.tuple_11_76, data.tuple_11_77, data.tuple_11_78, data.tuple_11_79, data.tuple_11_80,
        data.tuple_11_81, data.tuple_11_82, data.tuple_11_83, data.tuple_11_84, data.tuple_11_85, data.tuple_11_86, data.tuple_11_87, data.tuple_11_88, data.tuple_11_89, data.tuple_11_90,
        data.tuple_11_91, data.tuple_11_92, data.tuple_11_93, data.tuple_11_94, data.tuple_11_95, data.tuple_11_96, data.tuple_11_97, data.tuple_11_98, data.tuple_11_99, data.tuple_11_100,
        data.tuple_11_101, data.tuple_11_102, data.tuple_11_103, data.tuple_11_104, data.tuple_11_105, data.tuple_11_106, data.tuple_11_107, data.tuple_11_108, data.tuple_11_109, data.tuple_11_110,
        data.tuple_11_111, data.tuple_11_112, data.tuple_11_113, data.tuple_11_114, data.tuple_11_115, data.tuple_11_116, data.tuple_11_117, data.tuple_11_118, data.tuple_11_119, data.tuple_11_120,
        data.tuple_11_121, data.tuple_11_122, data.tuple_11_123, data.tuple_11_124, data.tuple_11_125, data.tuple_11_126, data.tuple_11_127, data.tuple_11_128, data.tuple_11_129, data.tuple_11_130,
        data.tuple_11_131, data.tuple_11_132, data.tuple_11_133, data.tuple_11_134, data.tuple_11_135, data.tuple_11_136, data.tuple_11_137, data.tuple_11_138, data.tuple_11_139, data.tuple_11_140,
        data.tuple_11_141, data.tuple_11_142, data.tuple_11_143, data.tuple_11_144, data.tuple_11_145, data.tuple_11_146, data.tuple_11_147, data.tuple_11_148, data.tuple_11_149, data.tuple_11_150,
        data.tuple_11_151, data.tuple_11_152, data.tuple_11_153, data.tuple_11_154, data.tuple_11_155, data.tuple_11_156, data.tuple_11_157, data.tuple_11_158, data.tuple_11_159, data.tuple_11_160,
        data.tuple_11_161, data.tuple_11_162, data.tuple_11_163, data.tuple_11_164, data.tuple_11_165, data.tuple_11_166, data.tuple_11_167, data.tuple_11_168, data.tuple_11_169, data.tuple_11_170,
        data.tuple_11_171, data.tuple_11_172, data.tuple_11_173, data.tuple_11_174, data.tuple_11_175, data.tuple_11_176, data.tuple_11_177, data.tuple_11_178, data.tuple_11_179, data.tuple_11_180,
        data.tuple_11_181, data.tuple_11_182, data.tuple_11_183, data.tuple_11_184, data.tuple_11_185, data.tuple_11_186, data.tuple_11_187, data.tuple_11_188, data.tuple_11_189,
        data.tuple_11_190, data.tuple_11_191, data.tuple_11_192, data.tuple_11_193, data.tuple_11_194, data.tuple_11_195, data.tuple_11_196, data.tuple_11_197, data.tuple_11_198, data.tuple_11_199,
        data.tuple_11_200, data.tuple_11_201, data.tuple_11_202, data.tuple_11_203, data.tuple_11_204, data.tuple_11_205, data.tuple_11_206, data.tuple_11_207, data.tuple_11_208, data.tuple_11_209,
        data.tuple_11_210, data.tuple_11_211, data.tuple_11_212, data.tuple_11_213, data.tuple_11_214, data.tuple_11_215, data.tuple_11_216, data.tuple_11_217, data.tuple_11_218, data.tuple_11_219,
        data.tuple_11_220, data.tuple_11_221, data.tuple_11_222, data.tuple_11_223, data.tuple_11_224, data.tuple_11_225, data.tuple_11_226, data.tuple_11_227, data.tuple_11_228, data.tuple_11_229,
        data.tuple_11_230, data.tuple_11_231, data.tuple_11_232, data.tuple_11_233, data.tuple_11_234, data.tuple_11_235, data.tuple_11_236, data.tuple_11_237, data.tuple_11_238, data.tuple_11_239,
        data.tuple_11_240, data.tuple_11_241, data.tuple_11_242, data.tuple_11_243, data.tuple_11_244, data.tuple_11_245, data.tuple_11_246, data.tuple_11_247, data.tuple_11_248, data.tuple_11_249,
        data.tuple_11_250, data.tuple_11_251, data.tuple_11_252, data.tuple_11_253, data.tuple_11_254, data.tuple_11_255, data.tuple_11_256, data.tuple_11_257, data.tuple_11_258, data.tuple_11_259,
        data.tuple_11_260, data.tuple_11_261, data.tuple_11_262, data.tuple_11_263, data.tuple_11_264, data.tuple_11_265, data.tuple_11_266, data.tuple_11_267, data.tuple_11_268, data.tuple_11_269,
        data.tuple_11_270, data.tuple_11_271, data.tuple_11_272, data.tuple_11_273, data.tuple_11_274, data.tuple_11_275, data.tuple_11_276, data.tuple_11_277, data.tuple_11_278, data.tuple_11_279,
        data.tuple_11_280, data.tuple_11_281, data.tuple_11_282, data.tuple_11_283, data.tuple_11_284, data.tuple_11_285, data.tuple_11_286, data.tuple_11_287, data.tuple_11_288, data.tuple_11_289,
        data.tuple_11_290, data.tuple_11_291, data.tuple_11_292, data.tuple_11_293, data.tuple_11_294, data.tuple_11_295, data.tuple_11_296, data.tuple_11_297, data.tuple_11_298, data.tuple_11_299,
        data.tuple_11_300, data.tuple_11_301, data.tuple_11_302, data.tuple_11_303, data.tuple_11_304, data.tuple_11_305, data.tuple_11_306, data.tuple_11_307, data.tuple_11_308, data.tuple_11_309,
        data.tuple_11_310, data.tuple_11_311, data.tuple_11_312, data.tuple_11_313, data.tuple_11_314, data.tuple_11_315, data.tuple_11_316, data.tuple_11_317, data.tuple_11_318, data.tuple_11_319,
        data.tuple_11_320, data.tuple_11_321, data.tuple_11_322, data.tuple_11_323, data.tuple_11_324, data.tuple_11_325, data.tuple_11_326, data.tuple_11_327, data.tuple_11_328, data.tuple_11_329,
        data.tuple_11_330, data.tuple_11_331, data.tuple_11_332, data.tuple_11_333, data.tuple_11_334, data.tuple_11_335, data.tuple_11_336, data.tuple_11_337, data.tuple_11_338, data.tuple_11_339,
        data.tuple_11_340, data.tuple_11_341, data.tuple_11_342, data.tuple_11_343, data.tuple_11_344, data.tuple_11_345, data.tuple_11_346, data.tuple_11_347, data.tuple_11_348, data.tuple_11_349,
        data.tuple_11_350, data.tuple_11_351, data.tuple_11_352, data.tuple_11_353, data.tuple_11_354, data.tuple_11_355, data.tuple_11_356, data.tuple_11_357, data.tuple_11_358, data.tuple_11_359,
        data.tuple_11_360, data.tuple_11_361, data.tuple_11_362, data.tuple_11_363, data.tuple_11_364, data.tuple_11_365, data.tuple_11_366, data.tuple_11_367, data.tuple_11_368, data.tuple_11_369,
        data.tuple_11_370, data.tuple_11_371, data.tuple_11_372, data.tuple_11_373, data.tuple_11_374, data.tuple_11_375, data.tuple_11_376, data.tuple_11_377, data.tuple_11_378, data.tuple_11_379,
        data.tuple_11_380, data.tuple_11_381, data.tuple_11_382, data.tuple_11_383, data.tuple_11_384, data.tuple_11_385, data.tuple_11_386, data.tuple_11_387, data.tuple_11_388, data.tuple_11_389,
        data.tuple_11_390, data.tuple_11_391, data.tuple_11_392, data.tuple_11_393, data.tuple_11_394, data.tuple_11_395, data.tuple_11_396, data.tuple_11_397, data.tuple_11_398, data.tuple_11_399,
        data.tuple_11_400, data.tuple_11_401, data.tuple_11_402, data.tuple_11_403, data.tuple_11_404, data.tuple_11_405, data.tuple_11_406, data.tuple_11_407, data.tuple_11_408, data.tuple_11_409,
        data.tuple_11_410, data.tuple_11_411, data.tuple_11_412, data.tuple_11_413, data.tuple_11_414, data.tuple_11_415, data.tuple_11_416, data.tuple_11_417, data.tuple_11_418, data.tuple_11_419,
        data.tuple_11_420, data.tuple_11_421, data.tuple_11_422, data.tuple_11_423, data.tuple_11_424, data.tuple_11_425, data.tuple_11_426, data.tuple_11_427, data.tuple_11_428, data.tuple_11_429,
        data.tuple_11_430, data.tuple_11_431, data.tuple_11_432, data.tuple_11_433, data.tuple_11_434, data.tuple_11_435, data.tuple_11_436, data.tuple_11_437, data.tuple_11_438, data.tuple_11_439,
        data.tuple_11_440, data.tuple_11_441, data.tuple_11_442, data.tuple_11_443, data.tuple_11_444, data.tuple_11_445, data.tuple_11_446, data.tuple_11_447, data.tuple_11_448, data.tuple_11_449,
        data.tuple_11_450, data.tuple_11_451, data.tuple_11_452, data.tuple_11_453, data.tuple_11_454, data.tuple_11_455, data.tuple_11_456, data.tuple_11_457, data.tuple_11_458, data.tuple_11_459,
        data.tuple_11_460, data.tuple_11_461, data.tuple_11_462, data.tuple_11_463, data.tuple_11_464, data.tuple_11_465, data.tuple_11_466, data.tuple_11_467, data.tuple_11_468, data.tuple_11_469,
        data.tuple_11_470, data.tuple_11_471, data.tuple_11_472, data.tuple_11_473, data.tuple_11_474, data.tuple_11_475, data.tuple_11_476, data.tuple_11_477, data.tuple_11_478, data.tuple_11_479,
        data.tuple_11_480, data.tuple_11_481, data.tuple_11_482, data.tuple_11_483, data.tuple_11_484, data.tuple_11_485, data.tuple_11_486, data.tuple_11_487, data.tuple_11_488, data.tuple_11_489,
        data.tuple_11_490, data.tuple_11_491
]

AA = [data.tuple_12_1, data.tuple_12_2, data.tuple_12_3, data.tuple_12_4, data.tuple_12_5, data.tuple_12_6, data.tuple_12_7, data.tuple_12_8, data.tuple_12_9, data.tuple_12_10,
      data.tuple_12_11, data.tuple_12_12, data.tuple_12_13, data.tuple_12_14, data.tuple_12_15, data.tuple_12_16, data.tuple_12_17, data.tuple_12_18, data.tuple_12_19, data.tuple_12_20,
      data.tuple_12_21, data.tuple_12_22, data.tuple_12_23, data.tuple_12_24, data.tuple_12_25, data.tuple_12_26, data.tuple_12_27, data.tuple_12_28, data.tuple_12_29, data.tuple_12_30,
      data.tuple_12_31, data.tuple_12_32, data.tuple_12_33, data.tuple_12_34, data.tuple_12_35, data.tuple_12_36, data.tuple_12_37, data.tuple_12_38, data.tuple_12_39, data.tuple_12_40,
      data.tuple_12_41, data.tuple_12_42, data.tuple_12_43, data.tuple_12_44, data.tuple_12_45, data.tuple_12_46, data.tuple_12_47, data.tuple_12_48, data.tuple_12_49, data.tuple_12_50,
      data.tuple_12_51, data.tuple_12_52, data.tuple_12_53, data.tuple_12_54, data.tuple_12_55, data.tuple_12_56, data.tuple_12_57, data.tuple_12_58, data.tuple_12_59, data.tuple_12_60,
      data.tuple_12_61, data.tuple_12_62, data.tuple_12_63, data.tuple_12_64, data.tuple_12_65, data.tuple_12_66, data.tuple_12_67, data.tuple_12_68, data.tuple_12_69, data.tuple_12_70,
      data.tuple_12_71, data.tuple_12_72, data.tuple_12_73, data.tuple_12_74, data.tuple_12_75, data.tuple_12_76, data.tuple_12_77, data.tuple_12_78, data.tuple_12_79, data.tuple_12_80,
      data.tuple_12_81, data.tuple_12_82, data.tuple_12_83, data.tuple_12_84, data.tuple_12_85, data.tuple_12_86, data.tuple_12_87, data.tuple_12_88, data.tuple_12_89, data.tuple_12_90,
        data.tuple_12_91, data.tuple_12_92, data.tuple_12_93, data.tuple_12_94, data.tuple_12_95, data.tuple_12_96, data.tuple_12_97, data.tuple_12_98, data.tuple_12_99, data.tuple_12_100,
        data.tuple_12_101, data.tuple_12_102, data.tuple_12_103, data.tuple_12_104, data.tuple_12_105, data.tuple_12_106, data.tuple_12_107, data.tuple_12_108, data.tuple_12_109, data.tuple_12_110,
        data.tuple_12_111, data.tuple_12_112, data.tuple_12_113, data.tuple_12_114, data.tuple_12_115, data.tuple_12_116, data.tuple_12_117, data.tuple_12_118, data.tuple_12_119, data.tuple_12_120,
        data.tuple_12_121, data.tuple_12_122, data.tuple_12_123, data.tuple_12_124, data.tuple_12_125, data.tuple_12_126, data.tuple_12_127, data.tuple_12_128, data.tuple_12_129, data.tuple_12_130,
        data.tuple_12_131, data.tuple_12_132, data.tuple_12_133, data.tuple_12_134, data.tuple_12_135, data.tuple_12_136, data.tuple_12_137, data.tuple_12_138, data.tuple_12_139, data.tuple_12_140,
        data.tuple_12_141, data.tuple_12_142, data.tuple_12_143, data.tuple_12_144, data.tuple_12_145, data.tuple_12_146, data.tuple_12_147, data.tuple_12_148, data.tuple_12_149, data.tuple_12_150,
        data.tuple_12_151, data.tuple_12_152, data.tuple_12_153, data.tuple_12_154, data.tuple_12_155, data.tuple_12_156, data.tuple_12_157, data.tuple_12_158, data.tuple_12_159, data.tuple_12_160,
        data.tuple_12_161, data.tuple_12_162, data.tuple_12_163, data.tuple_12_164, data.tuple_12_165, data.tuple_12_166, data.tuple_12_167, data.tuple_12_168, data.tuple_12_169, data.tuple_12_170,
        data.tuple_12_171, data.tuple_12_172, data.tuple_12_173, data.tuple_12_174, data.tuple_12_175, data.tuple_12_176, data.tuple_12_177, data.tuple_12_178, data.tuple_12_179, data.tuple_12_180,
        data.tuple_12_181, data.tuple_12_182, data.tuple_12_183, data.tuple_12_184, data.tuple_12_185, data.tuple_12_186, data.tuple_12_187, data.tuple_12_188, data.tuple_12_189,
        data.tuple_12_190, data.tuple_12_191, data.tuple_12_192, data.tuple_12_193, data.tuple_12_194, data.tuple_12_195, data.tuple_12_196, data.tuple_12_197, data.tuple_12_198, data.tuple_12_199,
        data.tuple_12_200, data.tuple_12_201, data.tuple_12_202, data.tuple_12_203, data.tuple_12_204, data.tuple_12_205, data.tuple_12_206, data.tuple_12_207, data.tuple_12_208, data.tuple_12_209,
        data.tuple_12_210, data.tuple_12_211, data.tuple_12_212, data.tuple_12_213, data.tuple_12_214, data.tuple_12_215, data.tuple_12_216, data.tuple_12_217, data.tuple_12_218, data.tuple_12_219,
        data.tuple_12_220, data.tuple_12_221, data.tuple_12_222, data.tuple_12_223, data.tuple_12_224, data.tuple_12_225, data.tuple_12_226, data.tuple_12_227, data.tuple_12_228, data.tuple_12_229,
        data.tuple_12_230, data.tuple_12_231, data.tuple_12_232, data.tuple_12_233, data.tuple_12_234, data.tuple_12_235, data.tuple_12_236, data.tuple_12_237, data.tuple_12_238, data.tuple_12_239,
        data.tuple_12_240, data.tuple_12_241, data.tuple_12_242, data.tuple_12_243, data.tuple_12_244, data.tuple_12_245, data.tuple_12_246, data.tuple_12_247, data.tuple_12_248, data.tuple_12_249,
        data.tuple_12_250, data.tuple_12_251, data.tuple_12_252, data.tuple_12_253, data.tuple_12_254, data.tuple_12_255, data.tuple_12_256, data.tuple_12_257, data.tuple_12_258, data.tuple_12_259,
        data.tuple_12_260, data.tuple_12_261, data.tuple_12_262, data.tuple_12_263, data.tuple_12_264, data.tuple_12_265, data.tuple_12_266, data.tuple_12_267, data.tuple_12_268, data.tuple_12_269,
        data.tuple_12_270, data.tuple_12_271, data.tuple_12_272, data.tuple_12_273, data.tuple_12_274, data.tuple_12_275, data.tuple_12_276, data.tuple_12_277, data.tuple_12_278, data.tuple_12_279,
        data.tuple_12_280, data.tuple_12_281, data.tuple_12_282, data.tuple_12_283, data.tuple_12_284, data.tuple_12_285, data.tuple_12_286, data.tuple_12_287, data.tuple_12_288, data.tuple_12_289,
        data.tuple_12_290, data.tuple_12_291, data.tuple_12_292, data.tuple_12_293, data.tuple_12_294, data.tuple_12_295, data.tuple_12_296, data.tuple_12_297, data.tuple_12_298, data.tuple_12_299,
        data.tuple_12_300, data.tuple_12_301, data.tuple_12_302, data.tuple_12_303, data.tuple_12_304, data.tuple_12_305, data.tuple_12_306, data.tuple_12_307, data.tuple_12_308, data.tuple_12_309,
        data.tuple_12_310, data.tuple_12_311, data.tuple_12_312, data.tuple_12_313, data.tuple_12_314, data.tuple_12_315, data.tuple_12_316, data.tuple_12_317, data.tuple_12_318, data.tuple_12_319,
        data.tuple_12_320, data.tuple_12_321, data.tuple_12_322, data.tuple_12_323, data.tuple_12_324, data.tuple_12_325, data.tuple_12_326, data.tuple_12_327, data.tuple_12_328, data.tuple_12_329,
        data.tuple_12_330, data.tuple_12_331, data.tuple_12_332, data.tuple_12_333, data.tuple_12_334, data.tuple_12_335, data.tuple_12_336, data.tuple_12_337, data.tuple_12_338, data.tuple_12_339,
        data.tuple_12_340, data.tuple_12_341, data.tuple_12_342, data.tuple_12_343, data.tuple_12_344, data.tuple_12_345, data.tuple_12_346, data.tuple_12_347, data.tuple_12_348, data.tuple_12_349,
        data.tuple_12_350, data.tuple_12_351, data.tuple_12_352, data.tuple_12_353, data.tuple_12_354, data.tuple_12_355, data.tuple_12_356, data.tuple_12_357, data.tuple_12_358, data.tuple_12_359,
        data.tuple_12_360, data.tuple_12_361, data.tuple_12_362, data.tuple_12_363, data.tuple_12_364, data.tuple_12_365, data.tuple_12_366, data.tuple_12_367, data.tuple_12_368, data.tuple_12_369,
        data.tuple_12_370, data.tuple_12_371, data.tuple_12_372, data.tuple_12_373, data.tuple_12_374, data.tuple_12_375, data.tuple_12_376, data.tuple_12_377, data.tuple_12_378, data.tuple_12_379,
        data.tuple_12_380, data.tuple_12_381, data.tuple_12_382, data.tuple_12_383, data.tuple_12_384, data.tuple_12_385, data.tuple_12_386, data.tuple_12_387, data.tuple_12_388, data.tuple_12_389,
        data.tuple_12_390, data.tuple_12_391, data.tuple_12_392, data.tuple_12_393, data.tuple_12_394, data.tuple_12_395, data.tuple_12_396, data.tuple_12_397, data.tuple_12_398, data.tuple_12_399,
        data.tuple_12_400, data.tuple_12_401, data.tuple_12_402, data.tuple_12_403, data.tuple_12_404, data.tuple_12_405, data.tuple_12_406, data.tuple_12_407, data.tuple_12_408, data.tuple_12_409,
        data.tuple_12_410, data.tuple_12_411, data.tuple_12_412, data.tuple_12_413, data.tuple_12_414, data.tuple_12_415, data.tuple_12_416, data.tuple_12_417, data.tuple_12_418, data.tuple_12_419,
        data.tuple_12_420, data.tuple_12_421, data.tuple_12_422, data.tuple_12_423, data.tuple_12_424, data.tuple_12_425, data.tuple_12_426, data.tuple_12_427, data.tuple_12_428, data.tuple_12_429,
        data.tuple_12_430, data.tuple_12_431, data.tuple_12_432, data.tuple_12_433, data.tuple_12_434, data.tuple_12_435, data.tuple_12_436, data.tuple_12_437, data.tuple_12_438, data.tuple_12_439,
        data.tuple_12_440, data.tuple_12_441, data.tuple_12_442, data.tuple_12_443, data.tuple_12_444, data.tuple_12_445, data.tuple_12_446, data.tuple_12_447, data.tuple_12_448, data.tuple_12_449,
        data.tuple_12_450, data.tuple_12_451, data.tuple_12_452, data.tuple_12_453, data.tuple_12_454, data.tuple_12_455, data.tuple_12_456, data.tuple_12_457, data.tuple_12_458, data.tuple_12_459,
        data.tuple_12_460, data.tuple_12_461, data.tuple_12_462, data.tuple_12_463, data.tuple_12_464, data.tuple_12_465, data.tuple_12_466, data.tuple_12_467, data.tuple_12_468, data.tuple_12_469,
        data.tuple_12_470, data.tuple_12_471, data.tuple_12_472, data.tuple_12_473, data.tuple_12_474, data.tuple_12_475, data.tuple_12_476, data.tuple_12_477, data.tuple_12_478, data.tuple_12_479,
        data.tuple_12_480, data.tuple_12_481, data.tuple_12_482, data.tuple_12_483, data.tuple_12_484, data.tuple_12_485, data.tuple_12_486, data.tuple_12_487, data.tuple_12_488, data.tuple_12_489,
        data.tuple_12_490, data.tuple_12_491, data.tuple_12_492, data.tuple_12_493, data.tuple_12_494, data.tuple_12_495, data.tuple_12_496, data.tuple_12_497, data.tuple_12_498, data.tuple_12_499,
        data.tuple_12_500, data.tuple_12_501, data.tuple_12_502, data.tuple_12_503, data.tuple_12_504, data.tuple_12_505, data.tuple_12_506, data.tuple_12_507, data.tuple_12_508, data.tuple_12_509,
        data.tuple_12_510, data.tuple_12_511, data.tuple_12_512, data.tuple_12_513, data.tuple_12_514, data.tuple_12_515, data.tuple_12_516, data.tuple_12_517, data.tuple_12_518, data.tuple_12_519,
        data.tuple_12_520, data.tuple_12_521, data.tuple_12_522, data.tuple_12_523, data.tuple_12_524, data.tuple_12_525, data.tuple_12_526, data.tuple_12_527, data.tuple_12_528, data.tuple_12_529,
        data.tuple_12_530, data.tuple_12_531, data.tuple_12_532, data.tuple_12_533, data.tuple_12_534, data.tuple_12_535, data.tuple_12_536, data.tuple_12_537, data.tuple_12_538, data.tuple_12_539,
        data.tuple_12_540, data.tuple_12_541, data.tuple_12_542, data.tuple_12_543, data.tuple_12_544, data.tuple_12_545, data.tuple_12_546, data.tuple_12_547, data.tuple_12_548, data.tuple_12_549,
        data.tuple_12_550, data.tuple_12_551, data.tuple_12_552, data.tuple_12_553, data.tuple_12_554, data.tuple_12_555, data.tuple_12_556, data.tuple_12_557, data.tuple_12_558, data.tuple_12_559,
        data.tuple_12_560, data.tuple_12_561, data.tuple_12_562, data.tuple_12_563, data.tuple_12_564, data.tuple_12_565, data.tuple_12_566, data.tuple_12_567, data.tuple_12_568, data.tuple_12_569,
        data.tuple_12_570, data.tuple_12_571, data.tuple_12_572, data.tuple_12_573, data.tuple_12_574, data.tuple_12_575, data.tuple_12_576, data.tuple_12_577, data.tuple_12_578, data.tuple_12_579,
        data.tuple_12_580, data.tuple_12_581, data.tuple_12_582, data.tuple_12_583, data.tuple_12_584, data.tuple_12_585, data.tuple_12_586, data.tuple_12_587, data.tuple_12_588, data.tuple_12_589,
        data.tuple_12_590, data.tuple_12_591, data.tuple_12_592, data.tuple_12_593, data.tuple_12_594, data.tuple_12_595, data.tuple_12_596, data.tuple_12_597, data.tuple_12_598, data.tuple_12_599,
        data.tuple_12_600, data.tuple_12_601, data.tuple_12_602, data.tuple_12_603, data.tuple_12_604, data.tuple_12_605, data.tuple_12_606, data.tuple_12_607, data.tuple_12_608, data.tuple_12_609,
        data.tuple_12_610, data.tuple_12_611, data.tuple_12_612, data.tuple_12_613, data.tuple_12_614, data.tuple_12_615, data.tuple_12_616, data.tuple_12_617, data.tuple_12_618, data.tuple_12_619,
        data.tuple_12_620, data.tuple_12_621, data.tuple_12_622, data.tuple_12_623, data.tuple_12_624, data.tuple_12_625, data.tuple_12_626, data.tuple_12_627, data.tuple_12_628, data.tuple_12_629,
        data.tuple_12_630, data.tuple_12_631, data.tuple_12_632, data.tuple_12_633, data.tuple_12_634, data.tuple_12_635, data.tuple_12_636, data.tuple_12_637, data.tuple_12_638, data.tuple_12_639,
        data.tuple_12_640, data.tuple_12_641, data.tuple_12_642, data.tuple_12_643, data.tuple_12_644, data.tuple_12_645, data.tuple_12_646, data.tuple_12_647, data.tuple_12_648, data.tuple_12_649,
        data.tuple_12_650, data.tuple_12_651, data.tuple_12_652, data.tuple_12_653, data.tuple_12_654, data.tuple_12_655, data.tuple_12_656, data.tuple_12_657, data.tuple_12_658, data.tuple_12_659,
        data.tuple_12_660, data.tuple_12_661, data.tuple_12_662, data.tuple_12_663, data.tuple_12_664, data.tuple_12_665, data.tuple_12_666, data.tuple_12_667, data.tuple_12_668, data.tuple_12_669,
        data.tuple_12_670, data.tuple_12_671, data.tuple_12_672, data.tuple_12_673, data.tuple_12_674, data.tuple_12_675, data.tuple_12_676, data.tuple_12_677, data.tuple_12_678, data.tuple_12_679,
        data.tuple_12_680, data.tuple_12_681, data.tuple_12_682, data.tuple_12_683, data.tuple_12_684, data.tuple_12_685, data.tuple_12_686, data.tuple_12_687, data.tuple_12_688, data.tuple_12_689,
        data.tuple_12_690, data.tuple_12_691, data.tuple_12_692, data.tuple_12_693, data.tuple_12_694, data.tuple_12_695, data.tuple_12_696, data.tuple_12_697, data.tuple_12_698, data.tuple_12_699,
        data.tuple_12_700, data.tuple_12_701, data.tuple_12_702, data.tuple_12_703, data.tuple_12_704, data.tuple_12_705, data.tuple_12_706, data.tuple_12_707, data.tuple_12_708, data.tuple_12_709,
        data.tuple_12_710, data.tuple_12_711, data.tuple_12_712, data.tuple_12_713, data.tuple_12_714, data.tuple_12_715, data.tuple_12_716, data.tuple_12_717, data.tuple_12_718, data.tuple_12_719,
        data.tuple_12_720, data.tuple_12_721, data.tuple_12_722, data.tuple_12_723, data.tuple_12_724, data.tuple_12_725, data.tuple_12_726, data.tuple_12_727, data.tuple_12_728, data.tuple_12_729,
        data.tuple_12_730, data.tuple_12_731, data.tuple_12_732, data.tuple_12_733, data.tuple_12_734, data.tuple_12_735, data.tuple_12_736, data.tuple_12_737, data.tuple_12_738, data.tuple_12_739,
        data.tuple_12_740, data.tuple_12_741, data.tuple_12_742, data.tuple_12_743, data.tuple_12_744, data.tuple_12_745, data.tuple_12_746, data.tuple_12_747, data.tuple_12_748, data.tuple_12_749,
        data.tuple_12_750, data.tuple_12_751, data.tuple_12_752, data.tuple_12_753, data.tuple_12_754, data.tuple_12_755, data.tuple_12_756, data.tuple_12_757, data.tuple_12_758, data.tuple_12_759,
        data.tuple_12_760, data.tuple_12_761, data.tuple_12_762, data.tuple_12_763, data.tuple_12_764, data.tuple_12_765, data.tuple_12_766, data.tuple_12_767, data.tuple_12_768, data.tuple_12_769,
        data.tuple_12_770, data.tuple_12_771, data.tuple_12_772, data.tuple_12_773, data.tuple_12_774, data.tuple_12_775
]

DC = [data.tuple_13_1, data.tuple_13_2, data.tuple_13_3, data.tuple_13_4, data.tuple_13_5, data.tuple_13_6, data.tuple_13_7, data.tuple_13_8, data.tuple_13_9, data.tuple_13_10,
      data.tuple_13_11, data.tuple_13_12, data.tuple_13_13, data.tuple_13_14, data.tuple_13_15, data.tuple_13_16, data.tuple_13_17, data.tuple_13_18, data.tuple_13_19, data.tuple_13_20,
      data.tuple_13_21, data.tuple_13_22, data.tuple_13_23, data.tuple_13_24, data.tuple_13_25, data.tuple_13_26, data.tuple_13_27, data.tuple_13_28, data.tuple_13_29, data.tuple_13_30,
      data.tuple_13_31, data.tuple_13_32, data.tuple_13_33, data.tuple_13_34, data.tuple_13_35, data.tuple_13_36, data.tuple_13_37, data.tuple_13_38, data.tuple_13_39, data.tuple_13_40,
      data.tuple_13_41, data.tuple_13_42, data.tuple_13_43, data.tuple_13_44, data.tuple_13_45, data.tuple_13_46, data.tuple_13_47, data.tuple_13_48, data.tuple_13_49, data.tuple_13_50,
      data.tuple_13_51, data.tuple_13_52, data.tuple_13_53, data.tuple_13_54, data.tuple_13_55, data.tuple_13_56, data.tuple_13_57, data.tuple_13_58, data.tuple_13_59, data.tuple_13_60,
      data.tuple_13_61, data.tuple_13_62, data.tuple_13_63, data.tuple_13_64, data.tuple_13_65, data.tuple_13_66, data.tuple_13_67, data.tuple_13_68, data.tuple_13_69, data.tuple_13_70,
      data.tuple_13_71, data.tuple_13_72, data.tuple_13_73, data.tuple_13_74, data.tuple_13_75, data.tuple_13_76, data.tuple_13_77, data.tuple_13_78, data.tuple_13_79, data.tuple_13_80,
      data.tuple_13_81, data.tuple_13_82, data.tuple_13_83, data.tuple_13_84, data.tuple_13_85, data.tuple_13_86, data.tuple_13_87, data.tuple_13_88, data.tuple_13_89, data.tuple_13_90,
        data.tuple_13_91, data.tuple_13_92, data.tuple_13_93, data.tuple_13_94, data.tuple_13_95, data.tuple_13_96, data.tuple_13_97, data.tuple_13_98, data.tuple_13_99, data.tuple_13_100,
        data.tuple_13_101, data.tuple_13_102, data.tuple_13_103, data.tuple_13_104, data.tuple_13_105, data.tuple_13_106, data.tuple_13_107, data.tuple_13_108, data.tuple_13_109, data.tuple_13_110,
        data.tuple_13_111, data.tuple_13_112, data.tuple_13_113, data.tuple_13_114, data.tuple_13_115, data.tuple_13_116, data.tuple_13_117, data.tuple_13_118, data.tuple_13_119, data.tuple_13_120,
        data.tuple_13_121, data.tuple_13_122, data.tuple_13_123, data.tuple_13_124, data.tuple_13_125, data.tuple_13_126, data.tuple_13_127, data.tuple_13_128, data.tuple_13_129, data.tuple_13_130,
        data.tuple_13_131, data.tuple_13_132, data.tuple_13_133, data.tuple_13_134, data.tuple_13_135, data.tuple_13_136, data.tuple_13_137, data.tuple_13_138, data.tuple_13_139, data.tuple_13_140,
        data.tuple_13_141, data.tuple_13_142, data.tuple_13_143, data.tuple_13_144, data.tuple_13_145, data.tuple_13_146, data.tuple_13_147, data.tuple_13_148, data.tuple_13_149, data.tuple_13_150,
        data.tuple_13_151, data.tuple_13_152, data.tuple_13_153, data.tuple_13_154, data.tuple_13_155, data.tuple_13_156, data.tuple_13_157, data.tuple_13_158, data.tuple_13_159, data.tuple_13_160,
        data.tuple_13_161, data.tuple_13_162, data.tuple_13_163, data.tuple_13_164, data.tuple_13_165, data.tuple_13_166, data.tuple_13_167, data.tuple_13_168, data.tuple_13_169, data.tuple_13_170,
        data.tuple_13_171, data.tuple_13_172, data.tuple_13_173, data.tuple_13_174, data.tuple_13_175, data.tuple_13_176, data.tuple_13_177, data.tuple_13_178, data.tuple_13_179, data.tuple_13_180,
        data.tuple_13_181, data.tuple_13_182, data.tuple_13_183, data.tuple_13_184, data.tuple_13_185, data.tuple_13_186, data.tuple_13_187, data.tuple_13_188, data.tuple_13_189,
        data.tuple_13_190, data.tuple_13_191, data.tuple_13_192, data.tuple_13_193, data.tuple_13_194, data.tuple_13_195, data.tuple_13_196, data.tuple_13_197, data.tuple_13_198, data.tuple_13_199,
        data.tuple_13_200, data.tuple_13_201, data.tuple_13_202, data.tuple_13_203, data.tuple_13_204, data.tuple_13_205, data.tuple_13_206, data.tuple_13_207, data.tuple_13_208, data.tuple_13_209,
        data.tuple_13_210, data.tuple_13_211, data.tuple_13_212, data.tuple_13_213, data.tuple_13_214, data.tuple_13_215, data.tuple_13_216, data.tuple_13_217, data.tuple_13_218, data.tuple_13_219,
        data.tuple_13_220, data.tuple_13_221, data.tuple_13_222, data.tuple_13_223, data.tuple_13_224, data.tuple_13_225, data.tuple_13_226, data.tuple_13_227, data.tuple_13_228, data.tuple_13_229,
        data.tuple_13_230, data.tuple_13_231, data.tuple_13_232, data.tuple_13_233, data.tuple_13_234, data.tuple_13_235, data.tuple_13_236, data.tuple_13_237, data.tuple_13_238, data.tuple_13_239,
        data.tuple_13_240, data.tuple_13_241, data.tuple_13_242, data.tuple_13_243, data.tuple_13_244, data.tuple_13_245, data.tuple_13_246, data.tuple_13_247, data.tuple_13_248, data.tuple_13_249,
        data.tuple_13_250, data.tuple_13_251, data.tuple_13_252, data.tuple_13_253, data.tuple_13_254, data.tuple_13_255, data.tuple_13_256
]

airstrike = [data.tuple_14_1, data.tuple_14_2, data.tuple_14_3, data.tuple_14_4, data.tuple_14_5, data.tuple_14_6, data.tuple_14_7, data.tuple_14_8, data.tuple_14_9, data.tuple_14_10,
                data.tuple_14_11, data.tuple_14_12, data.tuple_14_13, data.tuple_14_14, data.tuple_14_15, data.tuple_14_16, data.tuple_14_17, data.tuple_14_18, data.tuple_14_19, data.tuple_14_20,
                data.tuple_14_21, data.tuple_14_22, data.tuple_14_23, data.tuple_14_24, data.tuple_14_25, data.tuple_14_26, data.tuple_14_27, data.tuple_14_28, data.tuple_14_29, data.tuple_14_30,
                data.tuple_14_31, data.tuple_14_32, data.tuple_14_33, data.tuple_14_34, data.tuple_14_35, data.tuple_14_36, data.tuple_14_37, data.tuple_14_38, data.tuple_14_39, data.tuple_14_40,
                data.tuple_14_41, data.tuple_14_42, data.tuple_14_43, data.tuple_14_44, data.tuple_14_45, data.tuple_14_46, data.tuple_14_47, data.tuple_14_48, data.tuple_14_49, data.tuple_14_50,
                data.tuple_14_51, data.tuple_14_52, data.tuple_14_53, data.tuple_14_54, data.tuple_14_55, data.tuple_14_56, data.tuple_14_57, data.tuple_14_58, data.tuple_14_59, data.tuple_14_60,
                data.tuple_14_61, data.tuple_14_62, data.tuple_14_63, data.tuple_14_64, data.tuple_14_65, data.tuple_14_66, data.tuple_14_67, data.tuple_14_68, data.tuple_14_69, data.tuple_14_70,
                data.tuple_14_71, data.tuple_14_72, data.tuple_14_73, data.tuple_14_74, data.tuple_14_75, data.tuple_14_76, data.tuple_14_77, data.tuple_14_78, data.tuple_14_79, data.tuple_14_80,
                data.tuple_14_81, data.tuple_14_82, data.tuple_14_83, data.tuple_14_84, data.tuple_14_85, data.tuple_14_86, data.tuple_14_87, data.tuple_14_88, data.tuple_14_89, data.tuple_14_90,
                data.tuple_14_91, data.tuple_14_92, data.tuple_14_93, data.tuple_14_94, data.tuple_14_95, data.tuple_14_96, data.tuple_14_97, data.tuple_14_98, data.tuple_14_99, data.tuple_14_100,
                data.tuple_14_101, data.tuple_14_102, data.tuple_14_103, data.tuple_14_104, data.tuple_14_105, data.tuple_14_106, data.tuple_14_107, data.tuple_14_108, data.tuple_14_109, data.tuple_14_110,
                data.tuple_14_111, data.tuple_14_112, data.tuple_14_113, data.tuple_14_114, data.tuple_14_115, data.tuple_14_116, data.tuple_14_117, data.tuple_14_118, data.tuple_14_119, data.tuple_14_120,
                data.tuple_14_121, data.tuple_14_122, data.tuple_14_123, data.tuple_14_124, data.tuple_14_125, data.tuple_14_126, data.tuple_14_127, data.tuple_14_128, data.tuple_14_129, data.tuple_14_130,
                data.tuple_14_131, data.tuple_14_132, data.tuple_14_133, data.tuple_14_134, data.tuple_14_135, data.tuple_14_136, data.tuple_14_137, data.tuple_14_138, data.tuple_14_139, data.tuple_14_140,
                data.tuple_14_141, data.tuple_14_142, data.tuple_14_143, data.tuple_14_144, data.tuple_14_145, data.tuple_14_146, data.tuple_14_147, data.tuple_14_148, data.tuple_14_149, data.tuple_14_150,
                data.tuple_14_151, data.tuple_14_152, data.tuple_14_153, data.tuple_14_154, data.tuple_14_155, data.tuple_14_156, data.tuple_14_157, data.tuple_14_158, data.tuple_14_159, data.tuple_14_160,
                data.tuple_14_161, data.tuple_14_162, data.tuple_14_163, data.tuple_14_164, data.tuple_14_165, data.tuple_14_166, data.tuple_14_167, data.tuple_14_168, data.tuple_14_169, data.tuple_14_170,
                data.tuple_14_171, data.tuple_14_172, data.tuple_14_173, data.tuple_14_174, data.tuple_14_175, data.tuple_14_176, data.tuple_14_177, data.tuple_14_178, data.tuple_14_179, data.tuple_14_180,
                data.tuple_14_181, data.tuple_14_182, data.tuple_14_183, data.tuple_14_184, data.tuple_14_185, data.tuple_14_186, data.tuple_14_187, data.tuple_14_188, data.tuple_14_189,
                data.tuple_14_190, data.tuple_14_191, data.tuple_14_192, data.tuple_14_193, data.tuple_14_194, data.tuple_14_195, data.tuple_14_196, data.tuple_14_197, data.tuple_14_198, data.tuple_14_199,
                data.tuple_14_200, data.tuple_14_201, data.tuple_14_202, data.tuple_14_203, data.tuple_14_204, data.tuple_14_205, data.tuple_14_206, data.tuple_14_207, data.tuple_14_208, data.tuple_14_209,
                data.tuple_14_210, data.tuple_14_211, data.tuple_14_212, data.tuple_14_213, data.tuple_14_214, data.tuple_14_215, data.tuple_14_216, data.tuple_14_217, data.tuple_14_218, data.tuple_14_219,
                data.tuple_14_220, data.tuple_14_221, data.tuple_14_222, data.tuple_14_223, data.tuple_14_224, data.tuple_14_225, data.tuple_14_226, data.tuple_14_227, data.tuple_14_228, data.tuple_14_229,
                data.tuple_14_230, data.tuple_14_231, data.tuple_14_232, data.tuple_14_233, data.tuple_14_234, data.tuple_14_235, data.tuple_14_236, data.tuple_14_237, data.tuple_14_238, data.tuple_14_239,
                data.tuple_14_240, data.tuple_14_241, data.tuple_14_242, data.tuple_14_243, data.tuple_14_244, data.tuple_14_245, data.tuple_14_246, data.tuple_14_247, data.tuple_14_248, data.tuple_14_249,
                data.tuple_14_250, data.tuple_14_251, data.tuple_14_252, data.tuple_14_253, data.tuple_14_254, data.tuple_14_255, data.tuple_14_256, data.tuple_14_257, data.tuple_14_258, data.tuple_14_259,
                data.tuple_14_260, data.tuple_14_261, data.tuple_14_262, data.tuple_14_263, data.tuple_14_264, data.tuple_14_265, data.tuple_14_266, data.tuple_14_267, data.tuple_14_268, data.tuple_14_269,
                data.tuple_14_270, data.tuple_14_271, data.tuple_14_272, data.tuple_14_273, data.tuple_14_274, data.tuple_14_275, data.tuple_14_276, data.tuple_14_277, data.tuple_14_278, data.tuple_14_279,
                data.tuple_14_280, data.tuple_14_281, data.tuple_14_282, data.tuple_14_283, data.tuple_14_284, data.tuple_14_285, data.tuple_14_286, data.tuple_14_287, data.tuple_14_288, data.tuple_14_289,
                data.tuple_14_290, data.tuple_14_291, data.tuple_14_292, data.tuple_14_293, data.tuple_14_294, data.tuple_14_295, data.tuple_14_296, data.tuple_14_297, data.tuple_14_298, data.tuple_14_299,
                data.tuple_14_300, data.tuple_14_301, data.tuple_14_302, data.tuple_14_303, data.tuple_14_304, data.tuple_14_305, data.tuple_14_306, data.tuple_14_307, data.tuple_14_308, data.tuple_14_309,
                data.tuple_14_310, data.tuple_14_311, data.tuple_14_312, data.tuple_14_313, data.tuple_14_314, data.tuple_14_315, data.tuple_14_316, data.tuple_14_317, data.tuple_14_318, data.tuple_14_319,
                data.tuple_14_320, data.tuple_14_321, data.tuple_14_322, data.tuple_14_323, data.tuple_14_324, data.tuple_14_325, data.tuple_14_326, data.tuple_14_327, data.tuple_14_328, data.tuple_14_329,
                data.tuple_14_330, data.tuple_14_331, data.tuple_14_332, data.tuple_14_333, data.tuple_14_334, data.tuple_14_335, data.tuple_14_336, data.tuple_14_337, data.tuple_14_338, data.tuple_14_339,
                data.tuple_14_340, data.tuple_14_341, data.tuple_14_342, data.tuple_14_343, data.tuple_14_344, data.tuple_14_345, data.tuple_14_346, data.tuple_14_347, data.tuple_14_348, data.tuple_14_349,
                data.tuple_14_350, data.tuple_14_351, data.tuple_14_352, data.tuple_14_353, data.tuple_14_354, data.tuple_14_355, data.tuple_14_356, data.tuple_14_357, data.tuple_14_358, data.tuple_14_359,
                data.tuple_14_360, data.tuple_14_361, data.tuple_14_362, data.tuple_14_363, data.tuple_14_364, data.tuple_14_365, data.tuple_14_366, data.tuple_14_367, data.tuple_14_368, data.tuple_14_369,
                data.tuple_14_370, data.tuple_14_371, data.tuple_14_372, data.tuple_14_373, data.tuple_14_374, data.tuple_14_375, data.tuple_14_376, data.tuple_14_377, data.tuple_14_378, data.tuple_14_379,
                data.tuple_14_380, data.tuple_14_381, data.tuple_14_382, data.tuple_14_383, data.tuple_14_384, data.tuple_14_385, data.tuple_14_386, data.tuple_14_387, data.tuple_14_388, data.tuple_14_389,
                data.tuple_14_390, data.tuple_14_391, data.tuple_14_392, data.tuple_14_393, data.tuple_14_394, data.tuple_14_395, data.tuple_14_396, data.tuple_14_397, data.tuple_14_398, data.tuple_14_399,
                data.tuple_14_400, data.tuple_14_401, data.tuple_14_402, data.tuple_14_403, data.tuple_14_404, data.tuple_14_405, data.tuple_14_406, data.tuple_14_407, data.tuple_14_408, data.tuple_14_409,
                data.tuple_14_410, data.tuple_14_411, data.tuple_14_412, data.tuple_14_413, data.tuple_14_414, data.tuple_14_415, data.tuple_14_416, data.tuple_14_417, data.tuple_14_418, data.tuple_14_419,
                data.tuple_14_420, data.tuple_14_421, data.tuple_14_422, data.tuple_14_423, data.tuple_14_424, data.tuple_14_425, data.tuple_14_426, data.tuple_14_427, data.tuple_14_428, data.tuple_14_429,
                data.tuple_14_430, data.tuple_14_431, data.tuple_14_432, data.tuple_14_433, data.tuple_14_434, data.tuple_14_435, data.tuple_14_436, data.tuple_14_437, data.tuple_14_438, data.tuple_14_439,
                data.tuple_14_440, data.tuple_14_441, data.tuple_14_442, data.tuple_14_443, data.tuple_14_444, data.tuple_14_445, data.tuple_14_446, data.tuple_14_447, data.tuple_14_448, data.tuple_14_449,
                data.tuple_14_450, data.tuple_14_451
]

Attk_aircraft = [data.tuple_15_1, data.tuple_15_2, data.tuple_15_3, data.tuple_15_4, data.tuple_15_5, data.tuple_15_6, data.tuple_15_7, data.tuple_15_8, data.tuple_15_9, data.tuple_15_10,
                    data.tuple_15_11, data.tuple_15_12, data.tuple_15_13, data.tuple_15_14, data.tuple_15_15, data.tuple_15_16, data.tuple_15_17, data.tuple_15_18, data.tuple_15_19, data.tuple_15_20,
                    data.tuple_15_21, data.tuple_15_22, data.tuple_15_23, data.tuple_15_24, data.tuple_15_25, data.tuple_15_26, data.tuple_15_27, data.tuple_15_28, data.tuple_15_29, data.tuple_15_30,
                    data.tuple_15_31, data.tuple_15_32, data.tuple_15_33, data.tuple_15_34, data.tuple_15_35, data.tuple_15_36, data.tuple_15_37, data.tuple_15_38, data.tuple_15_39, data.tuple_15_40,
                    data.tuple_15_41, data.tuple_15_42, data.tuple_15_43, data.tuple_15_44, data.tuple_15_45, data.tuple_15_46, data.tuple_15_47, data.tuple_15_48, data.tuple_15_49, data.tuple_15_50,
]

Torp_bombers = [data.tuple_16_1, data.tuple_16_2, data.tuple_16_3, data.tuple_16_4, data.tuple_16_5, data.tuple_16_6, data.tuple_16_7, data.tuple_16_8, data.tuple_16_9, data.tuple_16_10,
                    data.tuple_16_11, data.tuple_16_12, data.tuple_16_13, data.tuple_16_14, data.tuple_16_15, data.tuple_16_16, data.tuple_16_17, data.tuple_16_18, data.tuple_16_19, data.tuple_16_20,
                    data.tuple_16_21, data.tuple_16_22, data.tuple_16_23, data.tuple_16_24, data.tuple_16_25, data.tuple_16_26, data.tuple_16_27, data.tuple_16_28, data.tuple_16_29, data.tuple_16_30,
                    data.tuple_16_31, data.tuple_16_32, data.tuple_16_33, data.tuple_16_34, data.tuple_16_35, data.tuple_16_36, data.tuple_16_37, data.tuple_16_38, data.tuple_16_39, data.tuple_16_40,
                    data.tuple_16_41, data.tuple_16_42, data.tuple_16_43, data.tuple_16_44, data.tuple_16_45, data.tuple_16_46, data.tuple_16_47, data.tuple_16_48, data.tuple_16_49, data.tuple_16_50,
                    data.tuple_16_51, data.tuple_16_52, data.tuple_16_53, data.tuple_16_54, data.tuple_16_55, data.tuple_16_56, data.tuple_16_57
]

Bombers = [data.tuple_17_1, data.tuple_17_2, data.tuple_17_3, data.tuple_17_4, data.tuple_17_5, data.tuple_17_6, data.tuple_17_7, data.tuple_17_8, data.tuple_17_9, data.tuple_17_10,
            data.tuple_17_11, data.tuple_17_12, data.tuple_17_13, data.tuple_17_14, data.tuple_17_15, data.tuple_17_16, data.tuple_17_17, data.tuple_17_18, data.tuple_17_19, data.tuple_17_20,
            data.tuple_17_21, data.tuple_17_22, data.tuple_17_23, data.tuple_17_24, data.tuple_17_25, data.tuple_17_26, data.tuple_17_27, data.tuple_17_28, data.tuple_17_29, data.tuple_17_30,
            data.tuple_17_31, data.tuple_17_32, data.tuple_17_33, data.tuple_17_34, data.tuple_17_35, data.tuple_17_36, data.tuple_17_37, data.tuple_17_38, data.tuple_17_39, data.tuple_17_40,
            data.tuple_17_41, data.tuple_17_42, data.tuple_17_43, data.tuple_17_44, data.tuple_17_45, data.tuple_17_46, data.tuple_17_47, data.tuple_17_48, data.tuple_17_49, data.tuple_17_50,
            data.tuple_17_51
]

Skip_Bombers = [data.tuple_18_1, data.tuple_18_2, data.tuple_18_3, data.tuple_18_4, data.tuple_18_5, data.tuple_18_6, data.tuple_18_7, data.tuple_18_8, data.tuple_18_9, data.tuple_18_10,
                data.tuple_18_11, data.tuple_18_12
]

# Regarder la taille des tuples
print("Voulez vous verifier la taille des tuples?")
print("1. Oui")
print("2. Non")
choix = input("Votre choix: ")
if choix == "1":
                print("Length of first tuple in navires:", len(navires[0]))
                print("Length of first tuple in navires_premium:", len(navires_premium[0]))
                print("Length of first tuple in navires_test:", len(navires_test[0]))
                print("Length of first tuple in NVSD:", len(nvsdp[0]))
                print("Length of first tuple in mbd:", len(mbd[0]))
                print("Length of first tuple in APS:", len(APS[0]))
                print("Length of first tuple in HESS:", len(HESS[0]))
                print("Length of first tuple in SAPS:", len(SAPS[0]))
                print("Length of first tuple in Secondaire:", len(Secondaire[0]))
                print("Length of first tuple in Sonar:", len(Sonar[0]))
                print("Length of first tuple in Torp:", len(Torp[0]))
                print("Length of first tuple in AA:", len(AA[0]))
                print("Length of first tuple in DC:", len(DC[0]))
                print("Length of first tuple in airstrike:", len(airstrike[0]))
                print("Length of first tuple in Attk_aircraft:", len(Attk_aircraft[0]))
                print("Length of first tuple in Torp_bombers:", len(Torp_bombers[0]))
                print("Length of first tuple in Bombers:", len(Bombers[0]))
                print("Length of first tuple in Skip_Bombers:", len(Skip_Bombers[0]))
else:
    pass


# Insertion des infos
cur.execute("""
Insert into Tier (valeur) values (1), (2), (3), (4), (5), (6), (7), (8), (9), (10), (11)
""")

cur.execute("""
Insert into Class (name) values ("Destroyer"), ("Cruiser"), ("Battleship"), ("Aircraft Carrier"), ("Submarine")
""")

cur.execute("""
Insert into Nation (name) values ("Commonwealth"), ("Europe"), ("France"), ("Germany"), ("Italy"), ("Japan"), ("Netherlands"), ("Pan_Asia"), ("Pan_America"), ("U.S.S.R"), ("U.K."), ("U.S.A"), ("Spain")""")

cur.executemany("""
INSERT INTO Navires (
    Ship, Tier_id, Class_id, Nation_id, Length, Beam, Tonnage, Health, Detect_by_sea, Detect_by_air, Max_speed, Acceleration, Rudder_shift, Turning_circle, Repair_percentage, Gun_range_percentage, Torpedo_protection_percentage, Fire_resistance_percentage
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", navires)

cur.executemany("""
INSERT INTO Navires_premium (
    Ship, Tier_id, Class_id, Nation_id, Length, Beam, Tonnage, Health, Detect_by_sea, Detect_by_air, Max_speed, Acceleration, Rudder_shift, Turning_circle, Repair_percentage, Gun_range_percentage, Torpedo_protection_percentage, Fire_resistance_percentage
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", navires_premium)

cur.executemany("""
INSERT INTO Navires_test (
    Ship, Tier_id, Class_id, Nation_id, Length, Beam, Tonnage, Health, Detect_by_sea, Detect_by_air, Max_speed, Acceleration, Rudder_shift, Turning_circle, Repair_percentage, Gun_range_percentage, Torpedo_protection_percentage, Fire_resistance_percentage
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", navires_test)

cur.executemany("""
INSERT INTO Capa_de_polonger (
    Ship, Tier_id, Class_id, Nation_id, Detectability, Submerged_speed, Diving_plane_shift, Diving_speed, Dive_capacity, Depletion_rate, Recharge_rate
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", nvsdp)

cur.executemany("""
INSERT INTO Main_Battery (
    Ship, Tier_id, Class_id, Nation_id, Description, AP_DPM, HE_DPM, SAP_DPM, AP_Salvo, HE_Salvo, SAP_Salvo, Range, Reload, Turn_180, Horizontal_dispetion, Vertical_dispertion, Sigma, Flight_time, Shells_per_minute
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", mbd)

cur.executemany("""
INSERT INTO AP_Shells (
    Ship, Tier_id, Class_id, Nation_id, Description, Weight, Damage, Initial_speed, Drag_coeff, Flight_time, Impact_speed, Impact_angle, Krupp, Penetration, Overwatch, Ricochet, Thershold, Fuse_time
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", APS)

cur.executemany("""
INSERT INTO HE_Shells (
    Ship, Tier_id, Class_id, Nation_id, Description, Weight, Damage, Initial_speed, Drag_coeff, Flight_time, impact_speed, Impact_angle, Penetration, Fire_chance, Fires_per_minute
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", HESS)

cur.executemany("""
INSERT INTO SAP_Shells (
    Ship, Tier_id, Class_id, Nation_id, Description, Weight, Damage, Initial_speed, Drag_coeff, Flight_time, Impact_speed, Impact_angle, Pernetration, Ricochet
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", SAPS)

cur.executemany("""
INSERT INTO Secondaries (
    Ship, Tier_id, Class_id, Nation_id, Description, Secondary_DPM, Hitting_DPM, Range, Reload, Flight_time, Horizontal_Dispertion, Sigma, Penetration, Fire_chance, Fire_per_minutes, Shells_per_minutes
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", Secondaire)

cur.executemany("""
INSERT INTO Sonar (
    Ship, Tier_id, Class_id, Nation_id, Range, Reload, Turn_180, First_life_time, Seconde_life_time, Wave_width, Wave_speed
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", Sonar)

cur.executemany("""
INSERT INTO Torpedoes (
    Ship, Tier_id, Class_id, Nation_id, Description, Type, Loaders, Torpedo_DPM, Range, Damage, Spread, Flood_chance, Reload, Speed, Detectability, Reaction_time, Torpedoes_per_minutes, Homming_rate
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", Torp)

cur.executemany("""
INSERT INTO Anti_Aircraft (
    Ship, Tier_id, Class_id, Nation_id, AA_strength, Long_range, Long_DPS, Medium_range, Medium_DPS, Short_range, Short_DPS, Flak_Strength, Flak_count, Flak_DPS, Sector_time, Sector_pourcentage, DFAA_pourcentage
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", AA)

cur.executemany("""
INSERT INTO Deep_Charges (
    Ship, Tier_id, Class_id, Nation_id, Attacks, Reload, Bombs, Interval, Detonation_timer, Detonation_depth, Damage, Radius, Flood_chance, Fire_chance
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", DC)

cur.executemany("""
INSERT INTO Airstrike (
    Ship, Tier_id, Class_id, Nation_id, Type, Attacks, Reload, Min_distance, Max_distance, Bombs, Retide_size, Deto_timer, Deto_Depth, Damage, Radius, Flood_chance, Fire_chance, Penetration
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", airstrike)

cur.executemany("""
INSERT INTO Attack_aircraft (
    Ship, Tier_id, Class_id, Nation_id, Description, Healt, Max_speed, Detectability, On_Deck, Regeneration, Squadron, Rockets, Recticle_size, Firing_dealy, Type, Damage, Fire_chance, Penetration, Threshold, Fuse_time
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", Attk_aircraft)

cur.executemany("""
INSERT INTO Torpedo_Bombers (
    Ship, Tier_id, Class_id, Nation_id, Description, Health, Max_speed, Detectability, On_Deck, Regeneration, Squadron, Torpedoes, Tropedoes_speed, Arming_time, Arming_distance, Range, Damage, Flood_chance
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", Torp_bombers)

cur.executemany("""
INSERT INTO Bombers (
    Ship, Tier_id, Class_id, Nation_id, Description, Health, Max_speed, Detectability, On_Deck, Regeneration, Squadron, Bombs, Reticl_size, Type, Damage, Fire_chance, Penetration, Threshold, Fuse_time
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", Bombers)

cur.executemany("""
INSERT INTO Skip_Bombers (
    Ship, Tier_id, Class_id, Nation_id, Description, Health, Max_speed, Detectability, On_Deck, Regeneration, Squadron, Bombs, Type, Damage, Fire_chance, Penetration, Threshold, Fuse_time
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", Skip_Bombers)

con.commit()
con.close()