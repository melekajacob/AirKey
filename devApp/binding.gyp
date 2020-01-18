{
    "targets": [{
        "target_name": "arduinoInterface",
        'include_dirs': [
            '.',
            '/user/local/lib',
        ],
        'cflags': [
            '-std=c++11',
        ],
        'cflags!': [ '-fno-exceptions'],
        'cflags_cc!': [ '-fno-exceptions'],
        'conditions': [
            ['OS=="mac"', {
                'xcode_settings': {
                    'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                    "GCC_ENABLE_CPP_RTTI": 'YES'
                }
            }]
        ],
        "sources": [
            "./interface/module.cpp"
        ]
    }]
}
