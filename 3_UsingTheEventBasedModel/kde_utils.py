import itertools
def extract_pvd(ml_order,samples):
    if type(ml_order) is list:
        #* List of PVDs from cross-validation/bootstrapping
        n_ = len(ml_order[0])
        pvd = np.zeros((n_,n_))
        #all_orders = np.array(ml_order)
        if type(samples[0]) is list:
            #* 10-fold CV returns MCMC samples for each fold separately in a list - concatenate them here
            all_samples = list(itertools.chain.from_iterable(samples))
        else:
            #* Bootstrapping returns MCMC samples pre-concatenated
            all_samples = samples
        all_orders = np.array([x.ordering for x in all_samples])
        for i in range(n_):
            pvd[i, :] = np.sum(all_orders == ml_order[0][i], axis=0)
        #pvd_cv, cv_rank = reorder_PVD_average_ranking(PVD=pvd)
        pvd, rank = reorder_PVD(pvd)
        seq = [ml_order[0][i] for i in rank]
    else:
        #* Single PVD (ML results)
        n_ = len(ml_order)
        pvd = np.zeros((n_,n_))
        samples_ = np.array([x.ordering for x in samples])
        seq = ml_order
        for i in range(n_):
            pvd[i, :] = np.sum(samples_ == seq[i], axis=0)
    return pvd, seq

def reorder_PVD(PVD,mean_bool=False,edf_threshold=0.5):
    """
    Reorders a PVD by scoring the frequencies in each row, then ranking in increasing order.

    Score: integral of complementary empirical distribution (1-EDF) up to a threshold.
    Rationale: the sooner the EDF gets to the threshold, the earlier it should be in the ranking.

    """

    if mean_bool:
        n_ = PVD.shape[0]
        ranking = np.linspace(1,n_,n_) # weights
        weights = PVD
        mean_rank = []
        for i in range(n_):
            mean_rank.append( sum( weights[i,:] * ranking ) / sum(weights[i,:]) )
        new_order = np.argsort(mean_rank)
    else:
        #* Find where the empirical distribution first exceeds the threshold
        edf = np.cumsum(PVD,axis=1)
        edf = edf / np.tile(np.max(edf,axis=1).reshape(-1,1),(1,edf.shape[1]))
        edf_above_threshold = []
        for k in range(edf.shape[0]):
            edf_above_threshold.append(np.where(edf[k,:]>=edf_threshold)[0][0])
        #* Ties implicitly split by original ordering in the PVD (likely the ML ordering)
        edf_rank = np.argsort(edf_above_threshold)
        new_order = edf_rank

    PVD_new = PVD[new_order,:]
    # PVD_new = np.zeros((n_,n_))
    # for i in range(n_):
    #     PVD_new[i, :] = PVD[new_order[i],:]

    return PVD_new, new_order

# Frontiers default is pdf with 300dpi
# And run it all through imagemagick after to convert
def save_plot(fig, fname, fig_format="png", dpi=150, **kwargs):
    fig.savefig(
        f"{fname}.{fig_format}",
        dpi=300,
        bbox_inches="tight",
        **kwargs
    )