
# Troubleshooting

### Issue with pydantic 2.5.3

error: 
pydantic.errors.PydanticUserError: If you use `@root_validator` with pre=False (the default) you MUST specify `skip_on_failure=True`. Note that `@root_validator` is deprecated and should be replaced with `@model_validator`.

python - 3.7.6

pydantic - 2.5.3

langchain - 0.0.27

**Solution**
Go to this file D:\MARS Program Files\miniconda\lib\site-packages\pydantic\deprecated\class_validators.py", line 240 and change default value of skip_on_failure to True. 


def root_validator(
    *__args,
    pre: bool = False,
    skip_on_failure: bool = True,
    allow_reuse: bool = False,
) -> Any:

[Reference](https://docs.pydantic.dev/2.5/errors/usage_errors/#root-validator-pre-skip)


After resolving this error, I am getting following error

File "D:\MARS Program Files\miniconda\lib\site-packages\pydantic\_internal\_model_construction.py", line 376, in inspect_namespace
    code='model-field-missing-annotation',
pydantic.errors.PydanticUserError: A non-annotated attribute was detected: `lookup_index = 0`. All model fields require a type annotation; if `lookup_index` is not meant to be a field, you may be able to resolve this error by annotating it as a `ClassVar` or updating `model_config['ignored_types']`.

Could not find a way to resolve the above error. So, decided to ditch hub only and downgrade pydantic.

### Issue with pydantic 1.10

pip install "pydantic==1.*"

cannot import name 'hub' from 'langchain'

*ImportError: cannot import name 'hub' from 'langchain'*
To resolve this error use latest version of langchain and pydantic.

**Solution**

`pip install --upgrade langchain pydantic`

