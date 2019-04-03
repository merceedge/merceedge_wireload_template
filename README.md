# Wireload package project template

1. Install cookiecutter

    The MerceEdge wireload package use cookiecutter which is a command-line utility that creates projects from cookiecutters (project templates).

    Please refer to [cookiecutter offical documents](https://cookiecutter.readthedocs.io/en/latest/installation.html) learn how to install.
    
    Simply,
    ```shell
    $ pip install cookiecutter
    ```

2. Create your new wireload package project
    
    ```shell
    $ cookiecutter https://github.com/merceedge/merceedge_wireload_template.git
    wireload_project_name [new_wireload_project]: your_new_wireload_project_name
    wireload_package_name [new_wireload]: your_new_wireload_package_name
    wireload_class_name [NewWireload]: your_new_wireload_class_name
    author [Your Name]: your_name
    contact [Your email]: your_email
    homepage [https://github.com/merceedge/MerceEdge]:your_project_homepage
    description [This is a wirload package project.]: Some description.
    license [Apache2.0]:
    ```

3. Design your wireload templates

    Design your wireload input, output and process.
    
    Example:
    ```yaml
    version: '1'
    component:
        name: mqtt_button
        vendor: Merce project group
        outputs: 
            - name: toggle_output
            protocol: 
                name: mqtt
                topic: /mercedge/toggle_button
                qos: 0
                retain: false

        description: mqtt demo toggle button component.
    ```

    More examples you can refer to [MerceEdge demo templates](https://github.com/merceedge/MerceEdge/tree/master/merceedge/tests/component_template)

4. Implemention 
    Implement key functions of the Wireload subclass that will be called by MerceEdge at runtime.

    API:
    - __ init__(self, init_params={})

        Get input parameter from init_params.
        example:
        ```python
        self.threshold = init_params.get('threshold')
        ```
    
    - process(self, input_data)

        the process function will be invoked when input data coming.
        You can do what you want to do when the data arrives.

        ```python
        def process(self, input_data):
            self.data.append(input_data)
            mean_value = np.mean(list(self.data))
            if mean_value > self.threshold:
                await self.put_output_payload(output_name="alert", payload=True)
        ```

    - put_output_payload(self, output_name, payload)


5. Unit test

    
    ```python
    import pytest
    import pytest
    import os

    import {{cookiecutter.wireload_package_name}}
    from merceedge.util.yaml import load_yaml
    from merceedge.util.mock import MockEdge, gen_test_loop

    mock_edge = MockEdge(my_wireload.__config__)

    @pytest.mark.run(order=1)
    @gen_test_loop(mock_edge)
    async def test_your_wireload():
        tests_path = os.path.dirname(os.path.realpath(__file__))
        model_template_yml = load_yaml(os.path.join(tests_path, '../templates', '{your_wireload_template.yml'))
        new_wireload_obj = MyWireload(edge=mock_edge,
                                    model_template_config=model_template_yml)

        def get_ouput(output_name, output_payload):
            # Get output callback, will invoke when process
            assert output_payload is not None

        # mock output
        new_wireload_obj.emit_output_call = get_output
        # Mock your input data here
        input_payload = {"test": "test_value"}
        # process
        await new_wireload_obj.process(input_payload)
    ```

6. Setup

    ```shell
    $ python3 setup.py install
    ```

    
