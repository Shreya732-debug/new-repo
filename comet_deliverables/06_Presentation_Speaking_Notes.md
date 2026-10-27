# Presentation speaking notes

The first four slides form a roughly five-minute proposal presentation. The remaining slides are optional backups. Replace editable placeholders. All pilot numbers are preliminary.

## Slide 1: Stability without concealment

Opening, about 60 seconds. My project asks whether grouping correlated inputs makes model explanations more reliable, or only makes them look more consistent. Imagine six monthly bill amounts: models can distribute importance among these related measurements differently after retraining. I want to distinguish a useful group summary from a summary that hides information. I narrowed the initial COMET proposal because temporal recourse, conformal margins and feature selection would require different evidence. The scope is now feasible in eight weeks on a laptop. The work completed is the proposal audit, literature review and a reproducible logistic-regression pilot; the full experiment is not complete. Name and roll-number fields are editable. Do not call this a finished paper or a new Shapley algorithm.

## Slide 2: What the literature establishes — and what we will test

About 75 seconds. SHAP explains a specified model output using a defined coalition-value game. Krishna and colleagues show that different explanation methods can disagree. groupShapley already explains groups, so grouping is not my invention. I also found a 2025 ITNAC paper on feature grouping for robust SHAP and a 2026 paper on agreement and faithfulness-weighted consensus. Their full methods need to be compared before a novelty claim. Our proposed question is whether correlation grouping beats random partitions with the same group sizes, while preserving fidelity and internal information. We will use synthetic cases with a known explanation game and public credit data. The contribution is an empirical evaluation protocol and findings, not an assertion that combining existing tools creates a new theory. Primary links: https://arxiv.org/abs/2106.12228 ; https://arxiv.org/abs/2202.01602 ; https://doi.org/10.1109/ITNAC66378.2025.11302604 .

## Slide 3: Methodology and controlled evaluation

About 90 seconds. We split data before fitting preprocessing or clusters. We retrain several models and explain the same held-out individuals. Each explanation is a vector of contributions in a stated output scale. We summarize either individual features or groups formed from training correlation. We compare the resulting stability to random groups with exactly the same number and sizes of groups. That controls a major shorter-list artefact. Next, we examine cancellation, synthetic exact group values and perturbation fidelity so a stable summary cannot simply hide opposing components. The initial model is logistic regression, where interventional logit contributions have an exact closed form. A small tree model and TreeSHAP are planned. The primary partition stays fixed across retraining; reclustering uncertainty is a separate analysis. We keep data, explainer and retraining randomness distinct. Removing model features, causal recourse and drift guarantees are outside the minimum project.

## Slide 4: Pilot results and eight-week validation plan

About 90 seconds. The official UCI dataset contains 30,000 rows. Our pilot used 24,000 training and 6,000 test rows; 500 held-out rows were explained for ten bootstrap logistic models. Correlation grouping produced eleven groups from nineteen inputs. Its ranking RBO was .924, compared with .863 for random partitions with the same sizes: an absolute difference of .061. This is not a 6.1 percent improvement in correctness, and it is not a significance claim. Predictive metrics were AP .489, ROC-AUC .713 and Brier .148. Nine mathematical/data-contract checks pass; a repeated run reproduces deterministic outputs. The main limitation is one split and one simple model, including numeric handling of repayment-status codes. The next steps are synthetic ground truth, fidelity/cancellation analysis, a tree model and additional splits/data. I would like approval for this narrowed scope and feedback on whether an empirical evaluation paper meets project requirements. Target a future ICAIF call or a suitable ECML PKDD workshop, with final venue dependent on results.

## Slide 5: The concepts you need before the experiment

Use this if asked to define terms. A feature is an input column, a label is the observed outcome, and a model is a learned mapping. Local attribution concerns one row; global attribution aggregates rows. Stability, fidelity and usefulness are distinct. The full study guide begins before these terms and includes examples.

## Slide 6: The “corrected” manual still needs correction

The manual contains many sensible corrections but is not fully reliable. Lowering rho merges more groups, not fewer. The proposed quantile code can select the wrong order statistic. Alpha=0 is not a no-margin setting. Mean probability is not sigmoid of mean logit. An additive model does not automatically imply the needed additive conditional attribution game. PFI need not always understate correlated features. Historical repayment data do not support feasible causal recourse. These are reasons for a narrower design, not reasons to discard all explainability research.

## Slide 7: A linear attribution you can calculate by hand

For score=3*x1+2*x2, reference means 1 and 2 give base 7. At x=(2,5), the feature differences contribute 3 and 6. They sum to the nine-point score difference, and base plus contributions equals sixteen. In logistic regression this is the logit score, not probability. The actual pilot calculates the background mean after each model’s fitted preprocessor and checks this identity for all 500 audit cases. This verifies implementation of a stated attribution, not that the model is causally correct.

## Slide 8: Stable summaries can conceal different things

Two different issues are shown. Cancellation: +5 and minus 4.8 net to .2, while the unsigned total is 9.8. Net contribution is legitimate but can hide strong opposing components. Game semantics: in a three-player unanimity game every feature gets one third; summing A and B gives two thirds. Treat AB as one group and C as another, and each group gets one half. So the order of grouping and Shapley computation matters. We retain within-group drill-down and use exact small-game values as an oracle.

## Slide 9: Pilot provenance and what its numbers mean

The official dataset was downloaded during this task and hashed. Ten bootstrap models share the same held-out test set. Forty-five pairwise comparisons share models and are not independent experimental units. Feature RBO .776 has nineteen items and group RBO .924 has eleven, so that raw difference is not the main controlled comparison. Random groups preserve the exact group sizes and average .863. This pilot does not implement the full proposed train/development/test protocol; it uses a prespecified 80/20 split without tuning. Numeric repayment-status encoding remains a known limitation.

## Slide 10: Full experiment: isolate one source of change at a time

For the final study, save stratified train/development/test IDs. Train-only transforms and clusters prevent leakage. The primary experiment freezes the correlation partition while retraining models. A separate reclustering analysis measures group discovery uncertainty. A separate explainer-repeat experiment measures sampling variance. Add a synthetic known-game oracle and one tree family. HELOC is conditional on obtaining a verified release and dictionary. The study can succeed as a negative-result evaluation if gains vanish under controls; do not keep expanding modules to force a positive result.

## Slide 11: Evaluation must measure more than consistency

RBO is the primary ranking stability measure. The main effect subtracts the mean of matched random partitions, but this is still a descriptive effect until replicated. Cancellation captures net-versus-unsigned attribution compression. Synthetic oracle error compares against a defined exact game, not assumed causal truth. AP, AUC and Brier validate the predictor; they do not validate explanations. Borrower confidence intervals with fixed models are conditional intervals, not a universal measure of model uncertainty. Report all denominators and failures.

## Slide 12: What would falsify the project hypothesis?

A useful project must be able to fail its hypothesis. If matched random groups are just as stable, there is little evidence that correlation-specific grouping is the cause. If group summaries hide major opposing contributions or fail known-game fidelity checks, stability is insufficient. If benefit exists only in one model/split, generality is weak. If closest prior work already includes the proposed controls, novelty must be revised. These cases can support a careful replication or limitation study, but they do not guarantee publication.

## Slide 13: The code demonstration: two minutes, no hand-waving

Show demo.py, test_demo.py and results/pilot.json. Explain the data exclusions and split, the linear attribution formula, and the matched random partitions. Run the tests; nine should pass. Open the saved result and identify model/data counts and limitations. The quantile helper is only an audit correction and is not used by the main pipeline. The starter includes a downloader and Colab notebook, but no personal Colab account run has been performed. Be candid about AI assistance and your responsibility for validation.

## Slide 14: Eight weeks, with a deliverable gate each fortnight

Week 1 learn and reproduce baseline; week 2 finish data cards and synthetic oracle. Weeks 3 and 4 add the tree explanation and controlled stability experiment. Weeks 5 and 6 assess fidelity, cancellation and replication. Weeks 7 and 8 write and independently replay the work with advisor feedback. Optional features are dropped if core gates fail. Use bounded Cursor tasks; do not ask it to generate a whole paper and system in one pass. Free Colab CPU is sufficient for the scoped experiments.

## Slide 15: Publication plan: target fit, not a promise

ICAIF is the best topical fit among these targets for credit explainability, but the 2026 main submissions are closed and workshop submissions closed October 12. Its 2026 event is November 14 to 17 in Milan. We would target a future call, plausibly 2027, after verifying the actual CFP. An appropriate ECML PKDD workshop may fit an evaluation/reproducibility study, but its archival publication policy must satisfy DTU requirements. PAKDD is a stretch if the methodological contribution becomes strong. EJOR, DSS, ESWA and KBS listed in the old manual are journals, not conferences. There is no guarantee of acceptance and no fee/payment/submission has been made.

## Slide 16: Selected references and the novelty checkpoint

Read the closest sources rather than memorizing citation counts. SHAP defines the attribution framework; Krishna documents disagreement; groupShapley is the central grouping baseline; Chen and colleagues explain model-versus-data semantics. The 2025 feature-grouping robustness paper and 2026 consensus/agreement paper require closest-work comparison before claiming novelty. Do not claim to have reviewed their entire full text if only metadata or abstract was accessible. The research dossier includes more than thirty linked primary sources and distinguishes unresolved references.
