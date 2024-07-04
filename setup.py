from setuptools import Extension, setup
from Cython.Build import build_ext, cythonize
import numpy

extensions = [
    Extension(
        "src/FMNM/cython/*",
        ["src/FMNM/cython/*.pyx"],
        include_dirs=[numpy.get_include()],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
    )
]


setup(
    name="fmnm_cython",
    cmdclass={"build_ext": build_ext},
    ext_modules=cythonize(extensions, language_level="3"),
)
