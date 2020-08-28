expected_output = {
    "five_min_cpu": 6,
    "five_sec_cpu_interrupts": 1,
    "one_min_cpu": 6,
    "nonzero_cpu_processes": ["PLFM-MGR IPC pro", "Spanning Tree"],
    "zero_cpu_processes": ["IPC Seat TX Cont"],
    "five_sec_cpu_total": 5,
    "sort": {
        1: {
            "five_min_cpu": 0.54,
            "invoked": 6437005,
            "usecs": 1236,
            "one_min_cpu": 0.53,
            "tty": 0,
            "process": "PLFM-MGR IPC pro",
            "five_sec_cpu": 0.31,
            "runtime": 7962054,
            "pid": 152,
        },
        2: {
            "five_min_cpu": 0.31,
            "invoked": 14602032,
            "usecs": 336,
            "one_min_cpu": 0.31,
            "tty": 0,
            "process": "Spanning Tree",
            "five_sec_cpu": 0.23,
            "runtime": 4915791,
            "pid": 242,
        },
        3: {
            "five_min_cpu": 0.0,
            "invoked": 1,
            "usecs": 0,
            "one_min_cpu": 0.0,
            "tty": 0,
            "process": "IPC Seat TX Cont",
            "five_sec_cpu": 0.0,
            "runtime": 0,
            "pid": 32,
        },
    },
}
