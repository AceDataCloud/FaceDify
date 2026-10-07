"""Published API contracts; source revisions are recorded in tests/parity-audit.json."""

TASK_PATH = None

ENDPOINTS = {
    "face_transform": {
        "method": "POST",
        "path": "/face/analyze",
        "operation": "face",
        "schema": {
            "type": "object",
            "required": ["image_url"],
            "properties": {
                "mode": {"type": "number"},
                "image_url": {"type": "string"},
                "face_model_version": {"type": "string"},
                "need_rotate_detection": {"type": "number"},
            },
        },
        "properties": {
            "mode": {"type": "number"},
            "image_url": {"type": "string"},
            "face_model_version": {"type": "string"},
            "need_rotate_detection": {"type": "number"},
        },
        "parameters": [],
        "defaults": {"action": "keypoints"},
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
        "media_response": False,
        "selector": {
            "keypoints": "face:keypoints",
            "beautify": "face:beautify",
            "age": "face:age",
            "gender": "face:gender",
            "swap": "face:swap",
            "cartoon": "face:cartoon",
            "liveness": "face:liveness",
        },
        "selector_default": "keypoints",
    },
    "face:keypoints": {
        "method": "POST",
        "path": "/face/analyze",
        "schema": {
            "type": "object",
            "required": ["image_url"],
            "properties": {
                "mode": {"type": "number"},
                "image_url": {"type": "string"},
                "face_model_version": {"type": "string"},
                "need_rotate_detection": {"type": "number"},
            },
        },
        "parameters": [],
        "properties": {
            "mode": {"type": "number"},
            "image_url": {"type": "string"},
            "face_model_version": {"type": "string"},
            "need_rotate_detection": {"type": "number"},
        },
        "operation": "face",
        "defaults": {},
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
    },
    "face:beautify": {
        "method": "POST",
        "path": "/face/beautify",
        "schema": {
            "type": "object",
            "required": ["image_url"],
            "properties": {
                "image_url": {"type": "string"},
                "smoothing": {"type": "number"},
                "whitening": {"type": "number"},
                "face_lifting": {"type": "number"},
                "eye_enlarging": {"type": "number"},
            },
        },
        "parameters": [],
        "properties": {
            "image_url": {"type": "string"},
            "smoothing": {"type": "number"},
            "whitening": {"type": "number"},
            "face_lifting": {"type": "number"},
            "eye_enlarging": {"type": "number"},
        },
        "operation": "face",
        "defaults": {},
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
    },
    "face:age": {
        "method": "POST",
        "path": "/face/change-age",
        "schema": {
            "type": "object",
            "required": ["image_url", "age_infos"],
            "properties": {
                "age_infos": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "required": ["age"],
                        "properties": {"age": {"type": "number"}},
                    },
                },
                "image_url": {"type": "string"},
            },
        },
        "parameters": [],
        "properties": {
            "age_infos": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["age"],
                    "properties": {"age": {"type": "number"}},
                },
            },
            "image_url": {"type": "string"},
        },
        "operation": "face",
        "defaults": {},
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
    },
    "face:gender": {
        "method": "POST",
        "path": "/face/change-gender",
        "schema": {
            "type": "object",
            "required": ["image_url", "gender_infos"],
            "properties": {
                "image_url": {"type": "string"},
                "gender_infos": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "gender": {"type": "number"},
                            "face_rect": {
                                "type": "object",
                                "properties": {
                                    "x": {"type": "number"},
                                    "y": {"type": "number"},
                                    "width": {"type": "number"},
                                    "height": {"type": "number"},
                                },
                            },
                        },
                    },
                },
            },
        },
        "parameters": [],
        "properties": {
            "image_url": {"type": "string"},
            "gender_infos": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "gender": {"type": "number"},
                        "face_rect": {
                            "type": "object",
                            "properties": {
                                "x": {"type": "number"},
                                "y": {"type": "number"},
                                "width": {"type": "number"},
                                "height": {"type": "number"},
                            },
                        },
                    },
                },
            },
        },
        "operation": "face",
        "defaults": {},
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
    },
    "face:swap": {
        "method": "POST",
        "path": "/face/swap",
        "schema": {
            "type": "object",
            "properties": {
                "timeout": {"type": "number"},
                "callback_url": {"type": "string"},
                "async": {"type": "boolean"},
                "source_image_url": {"type": "string"},
                "target_image_url": {"type": "string"},
            },
        },
        "parameters": [],
        "properties": {
            "timeout": {"type": "number"},
            "callback_url": {"type": "string"},
            "async": {"type": "boolean"},
            "source_image_url": {"type": "string"},
            "target_image_url": {"type": "string"},
        },
        "operation": "face",
        "defaults": {},
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
    },
    "face:cartoon": {
        "method": "POST",
        "path": "/face/cartoon",
        "schema": {
            "type": "object",
            "required": ["image_url"],
            "properties": {"image_url": {"type": "string"}},
        },
        "parameters": [],
        "properties": {"image_url": {"type": "string"}},
        "operation": "face",
        "defaults": {},
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
    },
    "face:liveness": {
        "method": "POST",
        "path": "/face/detect-live",
        "schema": {
            "type": "object",
            "required": ["image_url"],
            "properties": {
                "image_url": {"type": "string"},
                "face_model_version": {"type": "number"},
            },
        },
        "parameters": [],
        "properties": {"image_url": {"type": "string"}, "face_model_version": {"type": "number"}},
        "operation": "face",
        "defaults": {},
        "fixed": {},
        "allow_empty": [],
        "query_actions": [],
    },
}
