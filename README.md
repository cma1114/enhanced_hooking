This package implements specialized hooks for decoder-style transformer architectures; it's been tested on GPT2 and LLama-2.

It implements attachment of hooks for inspecting residual stream values at the beginning or end of a layer block, and at specific layers and positions.

It implements attachment of hooks for steering via adding vectors to residual stream activations, as well as zero-ing out vector projections.
