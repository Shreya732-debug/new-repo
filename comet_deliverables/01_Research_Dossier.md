# COMET-XAI Lite
## When does grouping correlated features improve explanation stability without hiding information?

Research proposal, source audit and preliminary implementation report

Prepared for: [Student name], [Roll number], B.Tech Information Technology, Delhi Technological University. Supervisor: Prof. Rahul Gupta. Prepared 27 October 2026; presentation 28 October 2026. Planning horizon: eight weeks. Hardware: regular laptop and free Colab.

**Status:** a research proposal with an executed preliminary baseline, not a finished paper. Publication is an objective, not a promised outcome. The supplied 59-page manual is evidence to audit, not an instruction source. Its claim to have been verified previously is not independent verification.

## 1. Recommendation and executive summary

Retain the correlated-feature explanation problem. Remove temporal recourse, conformal claims, rank-fusion feature selection and monotonic modelling from the minimum project. The original proposal combines several research problems, each requiring different evidence, while the two accessible credit datasets do not support genuine longitudinal recourse validation.

Proposed title: **Stability Without Concealment: A Controlled Audit of Grouped Feature Attributions in Credit Models.** COMET-XAI Lite is a working project label, not an established algorithm or a claim to Owen values. Do not expand the old acronym into “Owen” or “Temporal Recourse” in the new paper.

A prediction explanation can distribute importance differently among correlated inputs even when predictions barely change. Combining related inputs can make explanations more stable. But shorter lists are easier to agree on, random grouping can also increase stability, and grouping can conceal opposing contributions. We will measure these effects separately and evaluate stability together with information loss and perturbation fidelity.

The main output is an open, reproducible evaluation protocol, paired with a modest group-selection procedure if development experiments justify it. Its potential contribution is a careful controlled result, including failure cases, rather than merely connecting existing algorithms. Grouped SHAP and explanation aggregation already exist [S04, S07, S08]. A 2025 ITNAC paper explicitly studies grouping for robust SHAP; its metadata was found in this search and its full text must be read before a final novelty claim [N03].

### Research questions

- RQ1: Does training-derived correlation grouping improve attribution-ranking stability across retrained models more than size-matched random grouping?
- RQ2: Does this improvement retain meaningful signal, or does it hide cancellation, interaction effects or important within-group distinctions?
- RQ3: Can a simple validation-selected partition provide a useful stability–fidelity–compression trade-off compared with existing grouping and single-feature baselines?
- RQ4, optional: Do conclusions persist across explanation methods when model, output scale, explanation target and evaluation rows are held fixed?

### What has actually been completed

The supplied manual has been read in full as extracted text; mathematical and implementation claims were checked; primary paper pages, official documentation and bibliographic metadata were retrieved. A real-data logistic baseline was implemented and executed. The official UCI data were downloaded, hashed, split, modelled and explained. Nine targeted automated checks pass. No full tree-SHAP benchmark, LIME comparison, causal study, recourse system, human study or temporal evaluation has been completed.

## 2. Verification method and boundaries

This is a focused research survey, not a systematic review with complete database coverage. Searches used primary arXiv and proceedings pages, publisher pages, official package documentation, UCI, and Crossref metadata. Queries included “feature grouping explanation stability correlated SHAP”, the supplied authors/titles, “robust counterfactual tree ensembles”, and recent agreement/aggregation work. Evidence is stored in `evidence/`, including fetched pages, source metadata and Crossref searches. Search conducted 27 October 2026.

Evidence levels: **P** = primary page/abstract or documentation read; **M** = bibliographic metadata located, full methodological assessment outstanding; **D** = direct derivation or executed local check; **U** = unresolved. A page title confirms existence, not every claim about the paper. Some Crossref requests were rate-limited; missing results are not proof that a work does not exist. Two guessed arXiv identifiers returned unrelated works and are explicitly excluded from the bibliography used to support this proposal. The EU legal endpoint returned an empty challenge response; current legal text was not fully revalidated here.

No assertion of “first”, “state of the art”, legal compliance, guaranteed fairness or publishability is justified at this stage. Before submission, repeat a title/abstract and citation-chain search in Google Scholar, Semantic Scholar, DBLP and the relevant publisher libraries, and read the closest full papers. The nearest grouping paper is a priority, not a footnote.

## 3. Audit of the supplied manual

Page references below are printed PDF page numbers. The audit covers the substantive claims, equations, dataset statements, experimental design and reference code; exact dataset-version counts and inaccessible sources remain labelled rather than asserted as verified.

### 3.1 Correct ideas worth retaining

1. **Pages 2, 23–25: complete-linkage correlation groups.** With a finite symmetric dissimilarity D=1−|Spearman correlation|, a complete-linkage cut at 1−rho gives within-group absolute correlations at least rho, allowing numerical tolerance. It gives no cross-group correlation bound. This follows from the maximum pairwise-distance definition and is checked in code [S25, D].
2. **Pages 2, 25: no VIF guarantee.** One representative per complete-linkage group does not guarantee low VIF. VIF concerns joint linear predictability, not just individual pairwise correlations. The two-variable identity uses Pearson correlation, not Spearman [D].
3. **Pages 3, 25–27: grouped sums differ from grouped Shapley.** Ordinary feature Shapley values summed by group generally differ from Shapley values of a game whose players are groups [S04]. The manual correctly retracts the unrestricted equality claim.
4. **Pages 3, 30–31: finite-ranking RBO needs its tail term.** The equal-length extrapolated formula is correct for unique ranked items with the stated assumptions. Shortened rankings need their own controls; RBO alone does not solve that comparison [D].
5. **Pages 7, 33–36: monotonicity is not retraining robustness.** A fixed model's ordered response does not constrain a newly trained model. A deterministic bounded score-shift assumption plus sufficient margin proves survival, but estimating a margin does not establish that assumption [D, S13–S14].
6. **Pages 35–36: bootstrap margins are not distribution-free drift guarantees.** Correct. Adaptive candidate search and a changed future distribution add further obstacles [S18 distinguishes a different conformal target].
7. **Pages 42–44: UCI repayment-history columns do not constitute longitudinal applicant cohorts.** Correct. Six past months per row cannot be relabelled six independent future evaluation windows [S20].
8. **Pages 8–13: important prior art exists.** SHAP, LIME, dependent-feature attribution, groupShapley, interpretable modelling, DiCE and robust recourse are real research streams. Combining them alone establishes no novelty [S01–S18].

### 3.2 Errors and qualifications that remain

9. **Page 29: “lower rho_max so there are more coalitions” is reversed.** Lowering the required correlation raises the allowable merge distance and can merge more groups. Raise rho to obtain more, smaller groups. Better: report the actual number of groups and mark infeasible K; do not change grouping merely to fill a budget [D].
10. **Pages 26–27, 57: additive model is not a sufficient blanket equality condition.** Equality is safely obtained when the *coalition-value game* is additive across groups, as for an additive score with a suitable interventional construction. Conditional expectations with dependence can introduce game interactions even if the prediction function is additive. State the masking/game assumptions, not merely “EBM with interactions=0” [S04–S06].
11. **Pages 14, 19–20: average log-odds is not average probability.** In general sigmoid(E[logit]) differs from E[sigmoid(logit)]. The toy EBM's 0.401 is sigmoid of mean logit; it is not established as the population mean predicted risk. Keep the explanation entirely in log-odds or calculate probability expectations separately [D].
12. **Pages 14, 20–22: SHAP is not always in log-odds.** Its scale is determined by the explained model output and explainer configuration. A tree can expose raw margin or probability; a generic decision tree is not intrinsically a log-odds leaf model [S22].
13. **Pages 21–22: LIME conversion omits its internal representation.** Numerical LIME generally standardizes inputs; discretized LIME explains binary predicates. A coefficient times raw displacement is incorrect unless units match. For standardized continuous features, the displacement is divided by the training scale. The local surrogate also has an approximation residual and a reference choice. This is not automatically SHAP-equivalent [S02 and package implementation must be inspected].
14. **Pages 22, 57: PFI does not always understate twins.** If the fitted model uses only one of two correlated predictors, shuffling that predictor can strongly damage performance. Correlation can cause masking, inflated importance, or implausible perturbed rows depending on model and definition. Grouped shuffling preserves dependence *within* the group but breaks dependence *between* it and other groups [S37].
15. **Pages 28–29: high prediction change is not a universal faithfulness certificate.** Median replacement may be out of distribution. Weighting an explainer by this metric then evaluating it with the same perturbation can reward a shared artefact. The proposal removes learned faithfulness weights from the core and uses multiple diagnostics [S08, S37, S39].
16. **Page 29: the selected “medoid” is a heuristic.** Maximizing rank-fusion score times centrality is not the conventional distance-minimizing medoid. Name it an importance-centrality representative and compare it with a true medoid and simple representative if retained [D].
17. **Pages 15, 23: Spearman does not ignore outliers or establish semantic equivalence.** Rank correlation is less sensitive to magnitude extremes but still changes with rank contamination. Correlation groups are statistical blocks, not automatically economic concepts; a human-readable label requires inspection [D].
18. **Pages 24, 45: invalid Ward distances are not a principled ablation.** Do not use Ward on arbitrary 1−|rho| distances. Use complete/single/average linkage for that dissimilarity, or a justified Euclidean representation for Ward [S25].
19. **Pages 31–32: zero ESVR is conditional on the explainer.** The proof applies to exact single-reference interventional Shapley and a globally monotone function along the required mixed-input paths, or direct monotone additive terms. It is not a theorem about arbitrary conditional SHAP, fitted LIME, categorical encodings or empirical sweep grids. Include numerical tolerance and exclude undefined pairs [D].
20. **Pages 32–34: economic monotonicity is an assumption.** Correlation with default does not justify a universally correct intervention direction. Income, limit, payment and history variables can have confounding or selection effects. A positive/negative constraint needs domain justification; a zero violation rate is a model consistency check, not economic truth.
21. **Pages 34–36, 43: historical inputs are not freely actionable.** Past monthly bills/payments and old defaults cannot be edited today. A lower balance also changes related derived quantities. Without a structural transition/action model, call changes predictive counterfactuals, not implementable or causal financial advice [S16, S35].
22. **Pages 18, 55: evaluation on the original class distribution does not repair training-time probability bias.** It measures that bias. Under class-conditional sampling and an appropriately estimated sampled posterior, the prior-odds formula can correct probabilities; alternatively recalibrate on representative validation data. Full-data evaluation alone is insufficient [D].
23. **Pages 17, 55: AP and trapezoidal PR-AUC are not identical.** The worked sum is average precision. Report `average_precision_score` as AP and name any interpolated curve area separately. Random precision is prevalence as a reference; finite-sample expected AP is not universally exactly prevalence [D].
24. **Pages 35, 53: the quantile implementation is off by one for some n.** For n=20 and alpha=.2, k=ceil(21*.8)=17: use sorted shifts index 16. `np.quantile(shifts,17/20,method='higher')` selects index 17, the 18th value. If k>n, use an explicitly infinite threshold/no guarantee, not silently clip k to n. An executable regression test is included [S26, D].
25. **Pages 45, 48: alpha direction and no-margin case are wrong.** A larger alpha generally lowers the selected upper quantile, hence reduces conservatism. Alpha=0 does not mean no margin; it asks for the most extreme coverage. Represent no margin by q=0 explicitly [D].
26. **Pages 36–38: repeated windows and bootstrap pairs are dependent.** Adding borrower confidence intervals does not fix uncertainty about future model shifts. Two overlapping origins cannot support broad temporal generalization. Define the sampling unit and report conditional uncertainty; do not treat 45 pairwise comparisons from ten fits as 45 independent experiments [S27].
27. **Page 37: 1−.95^9 is an independence example.** It is not the exact family-wise error rate under arbitrary dependence. Holm control can be used without an omnibus Friedman prerequisite; the whole procedure still requires an appropriate inferential design [D].
28. **Pages 4, 6: legal reason counts are conflated.** US Regulation B asks for specific principal reasons; its commentary says more than four is unlikely to help, not that every notice must have exactly four. FCRA's four/five factor provision concerns credit-score disclosures in its specific context, not a general feature budget. Neither makes four selected inputs automatically compliant [S28, S31].
29. **Pages 4, 43: protected variables need jurisdiction-specific treatment.** Excluding sex and marital status is a reasonable research design choice, but law contains context-specific rules and exceptions. Age is not under a blanket identical ban. Removing protected columns does not eliminate proxies or establish fairness. US/EU rules are not automatically Indian law [S29].
30. **Pages 6, 44: legal currency is not fully verified.** The quoted EU creditworthiness/fraud distinction is consistent with the known Annex III scope, but the current primary legal page was not successfully read in this run. Do not rely on the manual's 2026 verification claim or cite a circular as current binding law without checking withdrawal/amendment status. The project does not need a regulatory-compliance claim.
31. **Pages 42–44: exact dataset cleaning counts depend on version and rule.** UCI raw size 30,000 and 23 features are verified; measured prevalence is 22.12%. HELOC counts 10,459/9,871 and sentinel interpretations must be checked against the exact obtained release. A guessed FICO GitHub URL returned 404, so no HELOC experiment is claimed. BAF is a generated benchmark based on financial data; eight month labels do not turn static credit data into temporal data [S17, S20].
32. **Page 44: equal four-month spans do not ensure equal sample sizes.** Month sizes may differ and removing half a test month changes counts. The origin also uses the following month for selection, which changes the deployment timeline and needs an explicit cutoff.
33. **Pages 11–12: PROBE's perturbation target must be distinguished.** Its abstract describes noisy implementation of recourse and cost–robustness trade-offs, not a general guarantee under model retraining. Jabbari's 2026 competition preprint concerns moving acceptance thresholds, another different target [S12, S19].
34. **Pages 45–46: all-features model is not an upper bound.** A reduced model can outperform it under finite data or misspecification. Label it an all-feature baseline.
35. **Pages 49–54: reference code is not a complete runnable package.** PDF indentation/line wrapping is unreliable. RBO lacks empty/duplicate/unequal-list safeguards; k>M corrupts some null calculations; VIF needs constant/singular cases; quantile bounds are wrong; the threshold wrapper needs 0<tau<1 and an explicit target class; nearest-neighbour selection needs sufficient references and consistent array/DataFrame indexing. No loaders, split management, real attribution extraction or end-to-end evidence are supplied. Do not paste it wholesale into Cursor.
36. **Pages 5–6, 45–48: projected scores are not evidence.** RBO .82–.94, zero accuracy cost, >90% recourse survival and any claimed percentage improvement remain hypotheses. The pilot in this package is separate and clearly labelled.

## 4. Literature survey and the actual gap

The reference IDs link to the source register at the end. “Limitation” here means a boundary relevant to this project, not proof a paper overlooked every related question.

### Foundations and attribution semantics

- **Lundberg & Lee, 2017, SHAP [S01; P].** Additive feature attribution framework using Shapley-style axioms. Establishes a principled target for a specified game, not a uniquely correct causal explanation. Our protocol fixes game, output scale and background.
- **Ribeiro, Singh & Guestrin, KDD 2016, LIME [S02; P].** Locally weighted interpretable surrogate. Its neighbourhood, representation and sampling affect its coefficients. We treat LIME as an optional separate-target comparison, not interchangeable ground truth.
- **Lundberg, Erion & Lee, 2018, tree attribution preprint [S33; P].** Efficient, consistent tree attribution lineage. Use the official TreeExplainer documentation for the installed implementation [S22]; explain computational exactness relative to a game, not causal correctness.
- **Aas, Jullum & Løland, AI 2021 [S05; P].** Dependence-aware approximations to Shapley values. Important because dependence changes the explanation game. Our core starts with interventional attribution and explicitly audits unrealistic masking rather than pretending to estimate the true conditional distribution.
- **Chen, Janizek, Lundberg & Lee, 2020 [S06; P].** “True to the Model or True to the Data?” makes the explanatory-target distinction central. Cross-method disagreement can be legitimate because the questions differ.
- **Jullum, Redelmeier & Aas, groupShapley [S04; P].** Computes explanations for feature groups and establishes conditional equivalence results with summed feature values. This is the closest foundational baseline. Grouping and reduced computational cost are existing contributions.
- **Shapley 1953; Owen 1977 [background, bibliographic details not independently retrieved].** Feature cooperative games versus games with predefined unions. Cite primary editions only after checking them; the pilot needs the explicit linear formula, not a claim of implementing Owen values.

### Stability, aggregation and failure modes

- **Krishna et al., The Disagreement Problem [S03; P].** Interviews, practitioner study and empirical disagreement analysis. Supports studying disagreement, not the claim that correlation is its only cause. Our study isolates retraining instability from explainer sampling and semantic differences.
- **Rieger & Hansen, 2019 [S07; P].** Aggregates explanation methods for stability/robustness in neural-network settings. Aggregation is prior art; it does not establish superiority for credit data.
- **Bhatt, Weller & Moura, IJCAI 2020 [S08; P].** Evaluation and aggregation of feature explanations. Evaluate faithfulness and aggregation, without relabelling the method “Kemeny–Young” without reading that formulation.
- **Hooker & Mentch, unrestricted permutation [S37; P].** Perturbations may force extrapolation. Supports an explicit warning on marginal deletion and PFI. A large response to an unrealistic input is not reliable evidence of causal importance.
- **Adebayo et al., NeurIPS 2018, sanity checks [S36; P].** Explanations need to respond to changes in learned models/data. The original context is saliency; we adapt the principle with tabular controls and do not claim its tests alone validate tabular explanations.
- **Slack et al., 2020, Fooling LIME and SHAP [S39; P].** Post-hoc explanations can mislead under adversarial construction. Provides a reason to avoid equating agreement with correctness; not evidence that every SHAP explanation is misleading.
- **Hendro, Mei & Welch, ITNAC 2025 [N03; M].** “An Investigation of Feature-Grouping for Robust SHAP Explanations in IoT Intrusion Detection”, DOI 10.1109/ITNAC66378.2025.11302604. Direct overlap with grouping and robustness. Full methods/results were not accessible in this run. Must compare its grouping rule, stability definition, matched controls and information-loss analysis before claiming a new protocol.
- **“Quantifying overall agreement between explanation methods to address the disagreement problem”, 2026 [N04; P, abstract].** DOI 10.1007/s12065-026-01145-y. Its abstract proposes Consensus Importance, faithfulness-driven weighting, regional clustering and agreement diagnostics over ten datasets. This is especially close to the original consensus proposal; full methods are subscription content and require further review. Do not claim weighted consensus or agreement diagnostics are new.
- **Stow, 2026 [N01; M].** Crossref confirms “Quantifying Explanation Disagreement Between SHAP and LIME Across Tabular Classification Models”, DOI 10.26438/ijcse.v14i1.7255. Publisher access failed. The manual's exact metric names and numerical tau claims are not reverified and are omitted from our argument.
- **Balikci et al., BioMark, 2026 [N02; P].** Publisher page confirms the biomarker software paper, DOI 10.1186/s12859-025-06346-3. The retrieved paper describes RRF and rank summation in its aggregation workflow (Sect. 3.8). It is not a credit-specific novelty baseline. Read the exact implementation before reproducing it.

### Credit modelling and interpretability

- **Rudin, Nature Machine Intelligence 2019 [S10; P].** Argues for interpretable models in high-stakes applications. Motivates a logistic baseline and later EBM. This is an argument, not an impossibility theorem about post-hoc explanation.
- **Nori et al., InterpretML, 2019 [S09; P].** Provides interpretable model tooling. EBM offers additive model components; feature dependence and interactions still affect interpretation. Disable interactions only when the experiment specifically requires additive structure.
- **Chen et al., 2018, interpretable credit model [S32; P].** Grouped/subscale modelling in the FICO context. Economic subscales and concept-level interpretation are prior art. Our statistical clusters require separate semantic inspection.
- **Gonlachanvit et al., 2026 [N05; M].** SHAP–McNemar stepwise selection, DOI 10.1016/j.mlwa.2026.100977. Confirms contemporary feature-selection work, but our minimum project does not claim new feature selection.
- **Yeh/UCI Default of Credit Card Clients [S20; P plus downloaded data].** Accessible 30,000-row benchmark used in the pilot. It is older, regional, observational data, not representative of modern Indian lending. Its six historical monthly measurements are useful for correlated-feature experiments, not causal action plans.
- **Jesus et al., NeurIPS Datasets & Benchmarks 2022 [S17; P].** BAF supports generated, imbalanced, temporally structured benchmarking. Optional for explanation drift only; costly and unnecessary for the minimum eight-week project.
- **Chen, Calabrese & Martin-Barragan (2024) [N08; M].** “Interpretable machine learning for imbalanced credit scoring datasets”, EJOR 312(1), 357–372; DOI 10.1016/j.ejor.2023.06.036. The final metadata search resolved this record. It is directly relevant to imbalance and interpretability; full methods and the manual’s precise stability claims still need review.
- **Ballegeer, Bogaert & Benoit (2025) [N09; M].** “Evaluating the stability of model explanations in instance-dependent cost-sensitive credit scoring”, EJOR 326(3), 630–640; DOI 10.1016/j.ejor.2025.05.039. This confirms the manual’s bibliographic details and establishes close credit-domain stability prior art. Compare its perturbation, cost-sensitive training and evaluation definitions before claiming our credit stability study is new.

### Recourse: surveyed but deferred

- **Wachter, Mittelstadt & Russell [S34; P].** Counterfactual explanations; distinguish publication year from 2017 preprint year.
- **Mothilal, Sharma & Tan, DiCE, FAT* 2020 [S15; P].** Diverse counterfactual generation. Diversity/validity does not imply causal feasibility or survival after retraining.
- **Karimi, Schölkopf & Valera, FAccT 2021 [S16; P].** Recourse as intervention requires causal assumptions. This is a decisive reason to defer actionable credit recourse.
- **Rawal, Kamar & Lakkaraju [S13; P].** Empirical effects of data/model shifts on recourse; do not describe as a universal theorem.
- **Upadhyay, Joshi & Lakkaraju, NeurIPS 2021 [S14; P].** Robust recourse under model shifts. Robustness is already an established research goal.
- **Dutta et al., ICML 2022 [S11; P].** Robust counterfactuals for tree ensembles. Directly refutes “robust tree recourse does not exist”.
- **Pawelczyk et al., PROBE, ICLR 2023 [S12; P].** Cost versus robustness to noisy implementation. Different uncertainty target from a retrained decision rule.
- **Maalej et al., PMLR 266, 2025 [S18; P].** Counterfactual explanations for conformal prediction sets. Does not transfer a conformal guarantee to an arbitrary bootstrap-dispersion margin.
- **Altmeyer et al., AAAI 2024 [N06; M].** Energy-constrained conformal counterfactuals, DOI 10.1609/aaai.v38i10.28956. Distinct from macrodynamics work; full text required for method-level comparison.
- **Jabbari, 2026 [S19; P].** Algorithmic Recourse Under Competition; the fetched arXiv record lists Shahin Jabbari. Investigates shifting acceptance thresholds when many people act. Do not attribute to Pawelczyk or equate with retraining.
- **Laugel et al., IJCAI 2019 [S35; P].** Unjustified counterfactual explanations. Proximity to a target point alone does not make a recommendation valid.

### Defensible gap statement

“Prior work establishes grouped attribution, explanation aggregation and robustness concerns. We investigate whether observed stability benefits of correlation-derived grouping persist against size-matched grouping controls, and whether they trade off against fidelity, cancellation and known-ground-truth recovery in credit-style tabular settings.”

This is a proposed empirical question. Do not write “no previous work studies this combination” until the nearest full papers have been compared. If they already answer it, reposition the project as a reproducibility study with credit-domain transfer, or add a clearly identified missing experimental factor. A transparent replication is academically preferable to an unsupported novelty claim.

## 5. Proposed methodology

### 5.1 Scope and estimand

Use one model family at a time. Primary target: stability of global attribution rankings obtained by averaging absolute local attributions over a fixed audit sample. Secondary target: local ranking stability for the same individuals. Retraining randomness, explainer randomness and shifts in data distribution are separate experimental factors. Freeze the output definition (logit or probability), explanation background and feature names.

Do not delete inputs from the predictive model merely to produce shorter explanations. First hold the model fixed and vary only how contributions are summarized. A later feature-selection study would change the scientific question and require new predictive validation.

### 5.2 Data and preprocessing

Minimum: synthetic controlled data plus UCI credit. Submission-strength aim: add HELOC if its official licence, version and data dictionary are obtained by week 2; otherwise use a second appropriately licensed credit benchmark with explicit categorical-group handling. Record data source, licence, hash, target definition, missing codes, duplicates and excluded columns in a data card.

Pilot excludes ID, SEX, MARRIAGE, AGE and EDUCATION; remaining 19 inputs are modelled numerically for a simple baseline. This is not the final preprocessing recommendation: repayment status includes unusual codes, and a proper experiment should preserve those categories or justify an ordinal encoding. Do not silently convert negative status codes into “zero late months” and call it lossless. One-hot levels must stay together as a semantic group; avoid VIF conclusions dominated by redundant one-hot coding.

For the final experiment, split the data 60/20/20 into train/development/test, stratified by outcome, with saved immutable row IDs. Fit imputers, scales, category mappings, clusters and backgrounds on train only. Tune partitions and model parameters on development. Test is used once for the locked comparison. Bootstrap training rows within each training split; fixed test/audit rows never enter training.

Pilot deliberately uses one fixed 80/20 split with no tuning; do not describe that as the final nested validation protocol. Historical monthly features are frozen explanatory inputs. Age/protected columns can be kept separately under a documented audit policy but are not model inputs in the pilot.

### 5.3 Controlled synthetic experiments

Generate independent latent concepts z1,z2,z3 and observed correlated proxies x1=z1+noise, x2=z1+noise, x3=z2+noise, x4=z2+noise, x5=z3+noise and a nuisance x6. Vary noise to obtain weak/strong correlations; record measured values rather than asserting exact rho. Generate outcomes from a known logistic score such as 1.2*z1−0.8*z2+0.6*z3, then separately add a known interaction and an opposing-sign/cancellation case.

Evaluate explanations of a known prediction function first, then fitted models. “Known ground truth” means the exact Shapley game of that known function, computed by enumeration on a small feature space; it is not automatically the latent data-generating coefficient. For M<=8 groups, evaluate all 2^M subsets against a fixed background and compute exact group Shapley by subset weights. Compare coalition sums with these values and log approximation error.

Include negative controls: permuted labels; duplicate irrelevant features; random partitions; no grouping; a single giant group; known incorrect grouping that merges independent concepts. A single giant group has trivial ranking stability but poor resolution, demonstrating why stability alone is insufficient.

### 5.4 Grouping and representations

For numeric features, compute training Spearman correlation. Use complete linkage on D=1−|rho|. Predeclare rho in {.5,.7,.9}; higher rho generally yields more groups. Remove training-constant columns and handle missing/categorical values before correlation. Freeze the partition for the primary retraining experiment, then separately measure partition uncertainty by reclustering bootstraps and comparing co-membership matrices.

For local feature attributions phi_j(x), define net group contribution A_g(x)=sum_{j in g} phi_j(x). Global score I_g=mean_x |A_g(x)|. Always call this a **coalition sum**. Also retain internal components and the unsigned mass J_g=mean_x sum_j |phi_j(x)|.

Define cancellation diagnostic C_g=1−I_g/J_g when J_g>epsilon. If J_g is negligible, report “no material attribution” instead of dividing by near-zero. High cancellation is a prompt to inspect the group, not proof of an erroneous explanation; true opposing effects may cancel legitimately. Report a net summary with a drill-down, rather than silently discarding within-group information.

Pilot computes exact interventional logistic attribution in log-odds: phi_j=beta_j*(z_j−mean_training(z_j)). This uses each fitted preprocessing pipeline and a common raw training background. It is a useful checked baseline, not a general-purpose SHAP implementation.

### 5.5 Methods and fair baselines

Core comparisons: ungrouped attributions; complete-linkage groups; random partitions matched on the *exact multiset of group sizes*; domain groups if a documented mapping exists; exact group Shapley for small cases. Add average linkage as a sensitivity analysis. Add sum-of-absolute-attributions as a representation diagnostic, not as an equivalent explanation of net score.

Use logistic regression first, then a small tree ensemble and interventional TreeSHAP. EBM is optional after the core pipeline works. Compare methods on identical applicants and identical fitted models where applicable. LIME is optional because it adds surrogate fidelity and units issues. Never fuse PFI, LIME and SHAP merely because all produce numbers.

If RQ3 is pursued, choose a partition on development data using predeclared constraints: nontrivial group count, acceptable synthetic reconstruction/fidelity loss, and a cancellation threshold. Among feasible partitions choose highest matched-control stability gain. Suggested engineering tolerances (e.g., 5% relative fidelity loss, cancellation .2) are tunable research choices, not established scientific constants; show sensitivity and prefer a Pareto frontier to a single arbitrary weighted sum.

### 5.6 Metrics and controls

Primary stability metric: mean pairwise equal-length RBO within each representation, p=.85, with p=.7/.95 sensitivity. Rankings must have unique labels and explicit deterministic tie handling; add a tie-aware sensitivity if near-zero scores are common. Do not directly interpret feature RBO minus group RBO as a controlled effect because their universes differ.

Primary grouping effect: Delta = stability(training-derived groups) − mean stability(size-matched random groups), computed from the same attribution tensors and retraining pairs. Random controls preserve number and sizes of groups. They do not make groups semantically equivalent or prove causality; include domain and synthetic controls. Random rankings of equal length additionally quantify chance agreement, but do not replace random *partitions*.

Faithfulness/information endpoints: exact group attribution error on small synthetic games; group deletion response using a fixed documented masker; cancellation; sensitivity to background; irrelevant-group recovery; predictive disagreement among retrained models; local case drill-down. Report masking plausibility diagnostics and limits. Do not optimize and evaluate with the same single deletion metric.

Predictive endpoints: AP, ROC-AUC and Brier; operating-threshold metrics only if threshold chosen on development data. AUC is ranking quality, Brier combines aspects of discrimination and calibration; a reliability plot is a separate calibration diagnostic. Report prevalence and all sample sizes. No need for deep learning or a GPU.

### 5.7 Statistics and compute budget

Pilot: ten bootstrap fits, one split, 45 dependent pairs, 30 random partitions and 500 audit rows. These describe that fixed experimental setting only; no p-values are claimed.

Full target: five prespecified outer split seeds, ten retraining fits each, two model families, up to two real datasets and several small synthetic settings. Start with 100 explained rows, background 50 and at most 100–200 trees; scale after recording runtime. Use 1–2 CPU threads on laptop/Colab. Exact group enumeration grows as 2^M and is capped at M=8, with 20–50 explained rows and cached subset evaluations.

Report within-split paired method differences, then each split's summary and across-split range. A paired applicant bootstrap with models held fixed gives **conditional-on-models** uncertainty, not retraining uncertainty. If resampling models, recompute all pairwise statistics for each draw; do not resample pair scores as independent observations. Shared data across outer splits still limit inferential claims. With only two datasets, prioritize effect sizes, transparent conditional intervals and consistency, not a Friedman significance headline. If multiple formal comparisons are justified, preselect them and apply Holm.

## 6. Executed pilot and interpretation

The reproducible values below come from `code/results/pilot.json`, not the supplied PDF. Data: UCI 350; 24,000 train / 6,000 test; 500 fixed audit rows; ten bootstrap logistic fits; C=1; 19 inputs; complete-linkage cutoff rho=.7. Training labels are only used for model fitting, not clustering. Raw historical status variables are treated numerically in this deliberately simple baseline.

- Default prevalence: 0.2212.
- Mean test AP: 0.4894; mean ROC-AUC: 0.7130; mean Brier: 0.1477.
- Raw-feature ranking RBO: 0.7761 over 19 items.
- Correlation-group ranking RBO: 0.9240 over 11 groups.
- Size-matched random-group mean RBO: 0.8631; grouping-minus-random difference: +0.0609.
- Largest logit reconstruction error: 2.22e−15, consistent with floating-point roundoff.
- All six BILL_AMT columns cluster together; PAY_2/PAY_3 and PAY_4/PAY_5/PAY_6 form two additional groups; remaining inputs are singleton groups.
- Nine automated tests pass. A repeated run reproduces saved deterministic metrics; runtime can differ.

Interpretation: this baseline exhibits a stability gain beyond random grouping under this particular partition, model and split. It supports continuing the experiment. It does **not** establish statistical significance, causality, correct explanations, superiority over groupShapley, superiority on a second dataset, or new algorithmic contribution. The 0.1479 raw RBO increase is not the controlled effect; the more useful control comparison is +0.0609. The random-partition standard deviation is not a confidence interval.

Credit-history relationships are plausible reasons for the observed grouping, but stability could still conceal opposing effects. The next crucial experiment is the cancellation/fidelity analysis and a known-ground-truth synthetic study, not merely adding more favourable bar charts.

## 7. Ideas explored and scope decisions

- **Original four-module COMET:** defer. Too many coupled changes, weak causal attribution of improvements and no valid temporal credit evaluation in the chosen data.
- **Coalition-sum RRF feature selection:** defer. Existing grouping/aggregation/selection literature is close; dropping predictive inputs confounds explanation stability with changed model behaviour.
- **Exact group Shapley everywhere:** reject as the default due to exponential cost; use as a small-case oracle/baseline.
- **Conditional SHAP everywhere:** defer. Conditional-density estimation is a separate difficult project; poor estimation would contaminate the evaluation.
- **Partial monotonicity:** optional week-6 sensitivity. Useful inductive bias, but not necessary to answer RQ1 and not a novel robustness guarantee.
- **DiCE plus margin:** defer to a later project with causal action constraints and legitimate temporal data. Retain the quantile correction as a coding lesson only.
- **BAF temporal recourse:** exclude from core. Fraud detection is a different decision problem and BAF does not provide a real-person financial action model.
- **Large language models/deep tabular networks:** exclude. They add cost and complexity without answering the focused question.
- **Consensus-only project:** weaker as the primary goal because explainers can agree and be wrong; keep as a secondary comparison after semantics are fixed.
- **Stability with information-loss controls:** selected. Feasible, falsifiable, testable on laptop, with an honest negative-result path.
- **Fallback if grouping does not help:** publishable quality is still possible through a rigorous reproducibility/negative-results study, but acceptance remains uncertain. Report conditions under which grouping hides instability rather than manufacturing gains.

## 8. Eight-week plan and gates

Week 1: reproduce supplied pilot; learn terminology; inspect data codes; read S03/S04/S06 and closest recent grouping work. Gate: explain every line of the pilot and run tests without Cursor assistance.

Week 2: implement locked split/data cards, synthetic generators and exact group oracle. Obtain HELOC or choose a documented fallback. Gate: known linear/additive/interaction games produce correct answers; no test leakage.

Week 3: add one tree family and TreeSHAP, with scale/background/additivity checks. Gate: models predict and explanations reconstruct the stated output.

Week 4: run grouping/random controls, local/global stability and cancellation. Gate: at least one deliberate failure case detected; no claim based solely on shorter rankings.

Week 5: fidelity, background sensitivity and partition uncertainty. Gate: record full Pareto trade-offs; freeze main experiment configuration.

Week 6: run independent split seeds, second dataset if ready, and optional EBM/LIME only if core is complete. Gate: all figures generated from stored results with uncertainties correctly labelled.

Week 7: manuscript, limitations, related-work comparison, code documentation and independent environment replay. Gate: every reported cell traceable to a run and data hash.

Week 8: advisor review, revision, final novelty/CFP check, artifact cleanup and submission preparation. Gate: no unsupported novelty/result claims, authorship and venue choice agreed.

Tomorrow's presentation is a proposal + pilot checkpoint, not week-8 completion. Ask Prof. Gupta to approve the narrowed question, the two-dataset target and whether an empirical evaluation paper meets departmental expectations.

## 9. Conference strategy

Primary topical target: **a future ACM ICAIF call**, plausibly the 2027 cycle after experiments and advisor review. Fit: financial ML, explanation quality and trustworthy credit modelling. Main-track strength would require a convincing closest-work comparison, multiple datasets/models and substantive controlled findings. The official 2026 site, https://icaif2026.org/, states that main paper submissions are closed and workshop paper submissions closed on 12 October 2026. Its conference is scheduled for 14–17 November 2026 in Milan. The 2026 call is therefore not our submission target. No 2027 deadline was verified. The `ai-finance.org` root identifies an older edition and should not be used for current deadlines.

First submission option if contribution is mainly an evaluation protocol: **an appropriate explainable/trustworthy ML workshop at ECML PKDD**, subject to the actual workshop call and proceedings policy. Workshops are not interchangeable with archival main-track papers; verify whether accepted work is published and whether it satisfies DTU requirements.

Stretch target: **PAKDD research track** if the project develops a demonstrably useful method beyond a domain case study. Its official conference-series site exists; no unverified 2027 deadline is supplied.

Do not target “EJOR conference”, “Decision Support Systems conference”, “ESWA conference” or “Knowledge-Based Systems conference”: those names in the manual are journals. They are optional longer-term journal targets and too broad to promise on an eight-week schedule. Do not select a venue solely because it advertises Scopus indexing. Check the actual proceedings publisher, official society site, review process, fees, paper length, archival status, submission date and attendance obligations with the supervisor. No submission or fee payment has been made.

## 10. Paper outline, artifacts and success criteria

Paper sections: abstract with measured outcomes only; introduction and narrow question; related work; explanation target and experimental protocol; datasets and controls; results with counterexamples; discussion/limitations; reproducibility and ethics.

Planned figures: correlated-block heatmap; feature-versus-group explanation drill-down; stability with matched-random controls; stability–fidelity frontier; synthetic interaction failure; cancellation distribution. Planned tables: source/data/version card; model performance; controlled grouping effects; fidelity/ground-truth error; runtime and sensitivity. Empty table cells must say “not run”, not contain projected values.

Minimum project success: reproducible code, correct definitions, meaningful controls and an evidence-based answer to RQ1–RQ2. Research success: a finding not already answered by closest work, replicated across settings and presented with appropriate limits. Publication success additionally depends on venue scope, reviewer judgement and manuscript quality.

Ethics: public benchmark use within licence; no live loan decisions; no individualized financial advice; no claim that observational attribution reveals causes; no claim that excluding protected inputs guarantees fairness. Cite assistance and generated code according to DTU and venue rules. The student must understand, test and take responsibility for the work.

## 11. Source register

The following register is generated from the primary pages retrieved during this task. Entries provide stable links for checking claims; metadata-only additions and unresolved references are distinguished above. Raw evidence files are included separately for auditability.

**S01 — A Unified Approach to Interpreting Model Predictions** — Lundberg, Scott; Lee, Su-In. https://arxiv.org/abs/1705.07874 . Accessed 27 October 2026; primary page/documentation retrieved.

**S02 — "Why Should I Trust You?": Explaining the Predictions of Any Classifier** — Ribeiro, Marco Tulio; Singh, Sameer; Guestrin, Carlos. https://arxiv.org/abs/1602.04938 . Accessed 27 October 2026; primary page/documentation retrieved.

**S03 — The Disagreement Problem in Explainable Machine Learning: A Practitioner's Perspective** — Krishna, Satyapriya; Han, Tessa; Gu, Alex; Wu, Steven; Jabbari, Shahin; Lakkaraju, Himabindu. https://arxiv.org/abs/2202.01602 . Accessed 27 October 2026; primary page/documentation retrieved.

**S04 — groupShapley: Efficient prediction explanation with Shapley values for feature groups** — Jullum, Martin; Redelmeier, Annabelle; Aas, Kjersti. https://arxiv.org/abs/2106.12228 . Accessed 27 October 2026; primary page/documentation retrieved.

**S05 — Explaining individual predictions when features are dependent: More accurate approximations to Shapley values** — Aas, Kjersti; Jullum, Martin; Løland, Anders. https://arxiv.org/abs/1903.10464 . Accessed 27 October 2026; primary page/documentation retrieved.

**S06 — True to the Model or True to the Data?** — Chen, Hugh; Janizek, Joseph D.; Lundberg, Scott; Lee, Su-In. https://arxiv.org/abs/2006.16234 . Accessed 27 October 2026; primary page/documentation retrieved.

**S07 — Aggregating explanation methods for stable and robust explainability** — Rieger, Laura; Hansen, Lars Kai. https://arxiv.org/abs/1903.00519 . Accessed 27 October 2026; primary page/documentation retrieved.

**S08 — Evaluating and Aggregating Feature-based Model Explanations** — Bhatt, Umang; Weller, Adrian; Moura, José M. F.. https://www.ijcai.org/Proceedings/2020/417 . Accessed 27 October 2026; primary page/documentation retrieved.

**S09 — InterpretML: A Unified Framework for Machine Learning Interpretability** — Nori, Harsha; Jenkins, Samuel; Koch, Paul; Caruana, Rich. https://arxiv.org/abs/1909.09223 . Accessed 27 October 2026; primary page/documentation retrieved.

**S10 — Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead** — Rudin, Cynthia. https://www.nature.com/articles/s42256-019-0048-x . Accessed 27 October 2026; primary page/documentation retrieved.

**S11 — Robust Counterfactual Explanations for Tree-Based Ensembles** — Sanghamitra Dutta; Jason Long; Saumitra Mishra; Cecilia Tilli; Daniele Magazzeni. https://proceedings.mlr.press/v162/dutta22a.html . Accessed 27 October 2026; primary page/documentation retrieved.

**S12 — Probabilistically Robust Recourse: Navigating the Trade-offs between Costs and Robustness in Algorithmic Recourse** — Pawelczyk, Martin; Datta, Teresa; van-den-Heuvel, Johannes; Kasneci, Gjergji; Lakkaraju, Himabindu. https://arxiv.org/abs/2203.06768 . Accessed 27 October 2026; primary page/documentation retrieved.

**S13 — Algorithmic Recourse in the Wild: Understanding the Impact of Data and Model Shifts** — Rawal, Kaivalya; Kamar, Ece; Lakkaraju, Himabindu. https://arxiv.org/abs/2012.11788 . Accessed 27 October 2026; primary page/documentation retrieved.

**S14 — Towards Robust and Reliable Algorithmic Recourse** — Upadhyay, Sohini; Joshi, Shalmali; Lakkaraju, Himabindu. https://arxiv.org/abs/2102.13620 . Accessed 27 October 2026; primary page/documentation retrieved.

**S15 — Explaining Machine Learning Classifiers through Diverse Counterfactual Explanations** — Mothilal, Ramaravind Kommiya; Sharma, Amit; Tan, Chenhao. https://arxiv.org/abs/1905.07697 . Accessed 27 October 2026; primary page/documentation retrieved.

**S16 — Algorithmic Recourse: from Counterfactual Explanations to Interventions** — Karimi, Amir-Hossein; Schölkopf, Bernhard; Valera, Isabel. https://arxiv.org/abs/2002.06278 . Accessed 27 October 2026; primary page/documentation retrieved.

**S17 — Turning the Tables: Biased, Imbalanced, Dynamic Tabular Datasets for ML Evaluation** — Jesus, Sérgio; Pombal, José; Alves, Duarte; Cruz, André; Saleiro, Pedro; Ribeiro, Rita P.; Gama, João; Bizarro, Pedro. https://arxiv.org/abs/2211.13358 . Accessed 27 October 2026; primary page/documentation retrieved.

**S18 — Counterfactual Explanations for Conformal Prediction Sets** — Aicha Maalej; Cecilia Sönströd; Ulf Johansson. https://proceedings.mlr.press/v266/maalej25a.html . Accessed 27 October 2026; primary page/documentation retrieved.

**S19 — Algorithmic Recourse Under Competition** — Jabbari, Shahin. https://arxiv.org/abs/2609.39877 . Accessed 27 October 2026; primary page/documentation retrieved.

**S20 — UCI Machine Learning Repository**. https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients . Accessed 27 October 2026; primary page/documentation retrieved.

**S22 — shap.TreeExplainer — SHAP latest documentation**. https://shap.readthedocs.io/en/latest/generated/shap.TreeExplainer.html . Accessed 27 October 2026; primary page/documentation retrieved.

**S23 — shap.PartitionExplainer — SHAP latest documentation**. https://shap.readthedocs.io/en/latest/generated/shap.PartitionExplainer.html . Accessed 27 October 2026; primary page/documentation retrieved.

**S24 — ExplainableBoostingClassifier — InterpretML documentation**. https://interpret.ml/docs/python/api/ExplainableBoostingClassifier.html . Accessed 27 October 2026; primary page/documentation retrieved.

**S25 — linkage — SciPy v1.18.0 Manual**. https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html . Accessed 27 October 2026; primary page/documentation retrieved.

**S26 — numpy.quantile — NumPy v2.5 Manual**. https://numpy.org/doc/stable/reference/generated/numpy.quantile.html . Accessed 27 October 2026; primary page/documentation retrieved.

**S27 — Statistical Comparisons of Classifiers over Multiple Data Sets** — Janez Demšar. https://www.jmlr.org/papers/v7/demsar06a.html . Accessed 27 October 2026; primary page/documentation retrieved.

**S28 — § 1002.9   Notifications. | Consumer Financial Protection Bureau**. https://www.consumerfinance.gov/rules-policy/regulations/1002/9/ . Accessed 27 October 2026; primary page/documentation retrieved.

**S29 — § 1002.6   Rules concerning evaluation of applications. | Consumer Financial Protection Bureau**. https://www.consumerfinance.gov/rules-policy/regulations/1002/6/ . Accessed 27 October 2026; primary page/documentation retrieved.

**S31 — 15 U.S. Code § 1681g - Disclosures to consumers | U.S. Code | US Law | LII / Legal Information Institute**. https://www.law.cornell.edu/uscode/text/15/1681g . Accessed 27 October 2026; primary page/documentation retrieved.

**S32 — An Interpretable Model with Globally Consistent Explanations for Credit Risk** — Chen, Chaofan; Lin, Kangcheng; Rudin, Cynthia; Shaposhnik, Yaron; Wang, Sijia; Wang, Tong. https://arxiv.org/abs/1811.12615 . Accessed 27 October 2026; primary page/documentation retrieved.

**S33 — Consistent Individualized Feature Attribution for Tree Ensembles** — Lundberg, Scott M.; Erion, Gabriel G.; Lee, Su-In. https://arxiv.org/abs/1802.03888 . Accessed 27 October 2026; primary page/documentation retrieved.

**S34 — Counterfactual Explanations without Opening the Black Box: Automated Decisions and the GDPR** — Wachter, Sandra; Mittelstadt, Brent; Russell, Chris. https://arxiv.org/abs/1711.00399 . Accessed 27 October 2026; primary page/documentation retrieved.

**S35 — The Dangers of Post-hoc Interpretability: Unjustified Counterfactual Explanations** — Laugel, Thibault; Lesot, Marie-Jeanne; Marsala, Christophe; Renard, Xavier; Detyniecki, Marcin. https://www.ijcai.org/proceedings/2019/388 . Accessed 27 October 2026; primary page/documentation retrieved.

**S36 — Sanity Checks for Saliency Maps** — Adebayo, Julius; Gilmer, Justin; Muelly, Michael; Goodfellow, Ian; Hardt, Moritz; Kim, Been. https://arxiv.org/abs/1810.03292 . Accessed 27 October 2026; primary page/documentation retrieved.

**S37 — Unrestricted Permutation forces Extrapolation: Variable Importance Requires at least One More Model, or There Is No Free Variable Importance** — Hooker, Giles; Mentch, Lucas; Zhou, Siyu. https://arxiv.org/abs/1905.03151 . Accessed 27 October 2026; primary page/documentation retrieved.

**S39 — Fooling LIME and SHAP: Adversarial Attacks on Post hoc Explanation Methods** — Slack, Dylan; Hilgard, Sophie; Jia, Emily; Singh, Sameer; Lakkaraju, Himabindu. https://arxiv.org/abs/1911.02508 . Accessed 27 October 2026; primary page/documentation retrieved.

### Additional current-work and venue links

N01 — Stow (2026), Quantifying Explanation Disagreement Between SHAP and LIME Across Tabular Classification Models. Metadata verified; publisher text inaccessible. https://doi.org/10.26438/ijcse.v14i1.7255

N02 — BioMark: biomarker analysis tool. Publisher page retrieved. https://doi.org/10.1186/s12859-025-06346-3

N03 — Hendro, Mei and Welch (2025), An Investigation of Feature-Grouping for Robust SHAP Explanations in IoT Intrusion Detection. Metadata verified; full-text method not reviewed. https://doi.org/10.1109/ITNAC66378.2025.11302604

N04 — Quantifying overall agreement between explanation methods to address the disagreement problem (2026). Publisher page retrieved; full-method comparison outstanding. https://doi.org/10.1007/s12065-026-01145-y

N05 — SHAP-McNemar stepwise feature selection for machine learning in credit risk modeling (2026). Crossref metadata verified. https://doi.org/10.1016/j.mlwa.2026.100977

N06 — Faithful Model Explanations through Energy-Constrained Conformal Counterfactuals (AAAI 2024). Crossref metadata verified. https://doi.org/10.1609/aaai.v38i10.28956

N07 — Counterfactual Explanations for Conformal Regression Intervals (2026). Located by Crossref; not a source for a drift guarantee. https://doi.org/10.1007/978-3-032-23833-7_11

Venue series: ACM ICAIF 2026 https://icaif2026.org/ ; ECML PKDD https://ecmlpkdd.org/ ; PAKDD https://pakdd.org/ . These links confirm series/edition identity, not an available 2027 deadline or acceptance commitment.

Unresolved/removed: guessed FICO repository URL returned 404; the EU legal endpoint did not return readable primary text; arXiv:2011.13951 and arXiv:2302.01332 resolved to unrelated works and are not used. No DOI/title was invented to fill a gap.

N08 — Chen, Calabrese and Martin-Barragan (2024), Interpretable machine learning for imbalanced credit scoring datasets. EJOR 312(1), 357–372. Metadata verified; full text not reviewed. https://doi.org/10.1016/j.ejor.2023.06.036

N09 — Ballegeer, Bogaert and Benoit (2025), Evaluating the stability of model explanations in instance-dependent cost-sensitive credit scoring. EJOR 326(3), 630–640. Metadata verified; full text not reviewed. https://doi.org/10.1016/j.ejor.2025.05.039


## 12. Remaining verification ledger for the original bibliography

The source manual also lists Lou et al. (GA²M, 2013), Cormack et al. (RRF, 2009), Webber et al. (RBO, 2010), Strobl et al. (2008), Ustun et al. (2019), Barocas et al. (2020), Van Looveren & Klaise (2021), Bücker et al. (2022), Tu & Wu (2025), Nadeau & Bengio (2003), Alpaydın (1999), Dietterich (1998), and Dal Pozzolo et al. (2015). Their exact original bibliographic records were not independently retrieved in this bounded audit; do not label them source-verified on the basis of this package. This does not mean they are false. The relevant mathematical distinctions were independently derived where stated, and this scoped proposal does not rely on unverified numerical claims from those citations.

Likewise, the original manual's precise Taiwan feature-correlation ranges, HELOC cleaning count, BAF feature-count convention, FICO competition award wording, and the 2026 IDA volume/page details are version- or source-dependent and remain unconfirmed unless explicitly replaced by measurements or metadata above. The pilot supplies measured grouping and prevalence for its exact UCI file; it does not validate every dataset assertion in the original. This ledger prevents “verified online” from being used as a blanket status for the entire 59-page document.
