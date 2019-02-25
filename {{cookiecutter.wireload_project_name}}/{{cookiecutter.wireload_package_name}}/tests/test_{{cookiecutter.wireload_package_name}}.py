import pytest
from MyWireload_wireload import MyWireload, 
import my_wireload


class MockEdge:
    def __init__(self, package_config):
        self.user_config = package_config

    def wireload_emit_output_payload(output_name, 
                                    mock_output_call, 
                                    output_payload):
        mock_output_call(output_name, output_payload)        
    


@pytest.mark.run(order=1)
def test_{{cookiecutter.wireload_package_name}}():
    mock_edge = MockEdge(my_wireload.__config__)
    new_wireload_obj = {{cookiecutter.wireload_class_name}}(edge=mock_edge,
                                  model_template_config=)
    def get_ouput(output_payload):
        # Get output
        assert output_payload is not None
        
    # mock output
    new_wireload_obj.emit_output_call = get_output
    # input
    input_payload = {"test": "test_value"}
    # process
    new_wireload_obj.process(input_payload)
    
   

    
    

        
