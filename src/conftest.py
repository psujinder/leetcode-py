import pytest
import importlib.util
import sys
import os


@pytest.fixture
def solution(request):
    problem_dir = request.param
    filename = os.path.join(problem_dir, "solution.py")
    spec = importlib.util.spec_from_file_location("Solution", filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules["Solution"] = module
    spec.loader.exec_module(module)
    return module.Solution()
