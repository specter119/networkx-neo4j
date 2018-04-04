def closeness_centrality(G, u=None, distance=None,
                         wf_improved=True, reverse=False):
    # doesn't currently supported `distance` or `reverse`
    centralities = G.closeness_centrality(wf_improved)

    if u:
        return centralities[u]

    return centralities


def betweenness_centrality(G, k=None, normalized=True, weight=None,
                           endpoints=False, seed=None):
    # doesn't currently support `weight`, `k`, `endpoints`, `seed`
    return G.betweenness_centrality()

def harmonic_centrality(G, nbunch=None, distance=None):
    # doesn't currently support `distance`
    centralities = G.harmonic_centrality()

    if nbunch:
        return {k: v for k, v in centralities.items() if k in nbunch}

    return centralities