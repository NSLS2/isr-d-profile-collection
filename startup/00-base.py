print(f"Loading {__file__}...")

import nslsii

nslsii.configure_base(
    user_ns=get_ipython().user_ns,
    redis_url="xf04id1-isr-redis1.nsls2.bnl.gov",
    redis_port=6380,
    redis_ssl=True,
)

