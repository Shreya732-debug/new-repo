# COMET-XAI Lite: preliminary executable baseline

Read `../03_Cursor_Implementation_Playbook.md` for the full research workflow.

Python 3.12. Install `requirements.txt` in a virtual environment, then run:

```bash
python download_data.py
python -m unittest -v test_demo.py
python demo.py --bootstraps 10 --random-partitions 30
```

This is an executed UCI logistic-regression explanation-stability baseline, not
the complete proposed research system. The main script overwrites its own
`results/pilot.json`, `metrics.csv` and `splits.npz` on rerun; copy results first if
you change settings. The staged Cursor plan adds immutable run directories.

Outputs contain data/split counts, group membership, metrics, versions and limits.
`kth_margin` and its tests audit a quantile error in the supplied manual; they are
not used by the pilot and do not constitute a recourse implementation.

Tested in the current cloud environment with versions in `requirements.txt`.
Laptop dependency installation and execution in a personal Colab runtime remain
to be verified. Read data/README.md for attribution, licence and source.

No claim of causal recourse, temporal robustness, legal compliance, general
superiority or publication readiness is made. Preserve preliminary labels.
