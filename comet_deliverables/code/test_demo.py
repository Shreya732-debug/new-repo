import unittest
import numpy as np
import pandas as pd
from demo import rbo, groups_from_training, kth_margin

class Contracts(unittest.TestCase):
    def test_identical_rbo(self):
        for n in [1,3,5,19]:
            self.assertAlmostEqual(rbo(list(range(n)),list(range(n))),1)
    def test_hand_computed_rbo(self):
        self.assertAlmostEqual(rbo(list('abc'),list('acb')),0.93625)
    def test_rbo_rejects_unequal_or_empty(self):
        for a,b in [([],[]),([1],[1,2]),([1,1],[1,1])]:
            with self.assertRaises(ValueError):rbo(a,b)
    def test_complete_linkage_within_group(self):
        rng=np.random.default_rng(8);a=rng.normal(size=1000)
        X=pd.DataFrame({'a':a,'b':a+.02*rng.normal(size=1000),'c':rng.normal(size=1000)})
        groups,corr=groups_from_training(X)
        self.assertIn([0,1],groups)
        for g in groups:self.assertGreaterEqual(np.abs(corr[np.ix_(g,g)]).min(),.7)
    def test_quantile_off_by_one_regression(self):
        self.assertEqual(kth_margin(np.arange(20),.2),16)
    def test_small_sample_margin_is_infinite(self):
        self.assertTrue(np.isinf(kth_margin([.1,.2],.1)))
    def test_negative_shift_clipped(self):
        self.assertEqual(kth_margin([-2,-1,0,1],.5),0)
    def test_owen_not_feature_sum(self):
        # Enumerate all orders independently for a unanimity game.
        import itertools
        values=[]
        for order in itertools.permutations('abc'):
            present=set();credits={x:0 for x in 'abc'}
            for player in order:
                before=int(len(present)==3);present.add(player)
                credits[player]=int(len(present)==3)-before
            values.append(credits['a']+credits['b'])
        grouped=[]
        for order in itertools.permutations(['ab','c']):
            present=set();credits={x:0 for x in ['ab','c']}
            for player in order:
                before=int(len(present)==3);present.update(player)
                credits[player]=int(len(present)==3)-before
            grouped.append(credits['ab'])
        self.assertAlmostEqual(np.mean(values),2/3)
        self.assertAlmostEqual(np.mean(grouped),1/2)
    def test_linear_shap_additivity(self):
        beta=np.array([3.,2.]);x=np.array([2.,5.]);base=np.array([1.,2.])
        phi=beta*(x-base)
        np.testing.assert_allclose(phi,[3,6])
        self.assertAlmostEqual(float(beta@base+phi.sum()),float(beta@x))

if __name__=='__main__':unittest.main(verbosity=2)
