import pytest
import pytest
import os

import {{cookiecutter.wireload_package_name}}
from merceedge.util.yaml import load_yaml
from merceedge.util.mock import MockEdge, gen_test_loop

mock_edge = MockEdge(my_wireload.__config__)

@pytest.mark.run(order=1)
@gen_test_loop(mock_edge)
async def test_{{cookiecutter.wireload_package_name}}():
    tests_path = os.path.dirname(os.path.realpath(__file__))
    model_template_yml = load_yaml(os.path.join(tests_path, '../templates', '{{cookiecutter.wireload_class_name}}_template.yml'))
    new_wireload_obj = MyWireload(edge=mock_edge,
                                  model_template_config=model_template_yml)

    def get_ouput(output_name, output_payload):
        # Get output
        assert output_payload is not None

    # mock output
    new_wireload_obj.emit_output_call = get_output
    # input
    input_payload = {"test": "test_value"}
    # process
    await new_wireload_obj.process(input_payload)
    
   

    
    

        
