# COMET-XAI Lite: study guide from first principles

For [Student name], final-year B.Tech IT, Delhi Technological University. Presentation to Prof. Rahul Gupta, 28 October 2026.

## 1. The project in three sentences

Machine-learning models can make almost the same prediction but give different-looking explanations when several inputs contain similar information. We study whether combining those inputs into groups makes explanations more stable, while checking that the improvement is not just an effect of shorter lists or concealed information. We have completed a small logistic-regression pilot on public credit data; the broader research study is planned for eight weeks.

**Thirty-second answer:** “My project evaluates the reliability of feature-attribution explanations. I compare correlation-based feature groups against random groups with exactly the same sizes, and assess both stability and information loss. The preliminary credit-data baseline shows a positive controlled stability difference, but I have not yet established generality or novelty.”

**What to say about your progress:** “I audited the initial proposal, reviewed the relevant literature, narrowed the question, and prepared and ran a reproducible baseline with automated checks. I am now proposing the full validation study.” Do not say you invented SHAP, completed temporal recourse, or proved a new theorem.

## 2. A dataset is a spreadsheet

A row describes one example, such as one credit-card customer. A column describes one measured property, such as credit limit or last month's bill. An input column is a **feature**. The outcome we want to predict is the **label**, here whether default occurred in the next period. We use y=1 for default and y=0 for no default.

An input vector x is simply the list of values for one person. A model f is a function that takes x and produces a score. A probability score of .3 means the model estimates a 30% chance of the outcome, not that 30% of this person will default. Whether that probability is trustworthy is a separate calibration question.

The UCI dataset has 30,000 rows and 23 input features excluding ID and target. The pilot omits ID plus sex, marriage, age and education, leaving 19 inputs. Excluding these fields is a modelling choice; it does not remove all demographic proxies or prove fairness.

There are six months of previous bills and payments in each row. These are historical measurements of the same person. They are not six separate future cohorts. This is why our current study does not claim temporal recourse validation.

## 3. Learning, training and testing

Training chooses the parameters of f using examples whose outcomes are known. A parameter is a number learned from data, such as a regression weight. A hyperparameter is a setting we choose, such as regularization strength or tree depth.

The model should work on new examples. Therefore, some rows are withheld as a test set. If we choose settings after observing test performance, the test has indirectly influenced the model and its estimate becomes optimistic. This is **leakage**. Even seemingly harmless preprocessing, such as computing imputation medians or clusters on all rows, can leak information about the test distribution.

In the pilot, 24,000 rows are training data and 6,000 are test data. There is no tuning. In the full project we will use train/development/test roles: fit on train, choose settings on development, report locked comparisons on test. Every saved split has row IDs so we can prove that training and test do not overlap.

**Overfitting** means fitting idiosyncrasies of the training data rather than patterns that generalize. A memorized answer sheet is a useful analogy. Regularization discourages unnecessarily extreme model parameters, but does not guarantee generalization.

## 4. Logistic regression without mystery

A linear score adds weighted input values: z=b+beta1*x1+beta2*x2+... . The sigmoid converts any real score into a number between zero and one: p=1/(1+exp(−z)). A larger z means a larger probability of default.

The inverse scale is log-odds: z=log(p/(1−p)). For p=.5, z=0; for p approximately .731, z=1. A change of one logit is not a one-percentage-point change. Always name the units of an explanation.

Logistic regression learns b and the beta weights. Standardizing features means subtracting their training mean and dividing by their training standard deviation, so a rupee-valued feature does not dominate simply because of its units. The pipeline stores the imputer and scaler together with the fitted classifier so new rows receive the same transformation.

Why start here? It is quick on a laptop, easier to understand, and has an exact attribution formula. It gives us a reliable reference before more complex trees. It is not assumed to be the best credit predictor.

## 5. Trees, ensembles and EBM

A decision tree is a sequence of questions: “Is the bill above this amount?”, then “Is repayment delayed?” A leaf stores a prediction or score depending on the implementation. A random forest averages many trees. Gradient boosting builds trees sequentially to improve a loss function. These approaches can represent nonlinearities and interactions.

An **interaction** means that the effect of one feature depends on another. For instance, the effect of a balance can depend on the credit limit. A purely additive score has one separate contribution function per feature. An EBM is an interpretable boosting model that can use such additive functions, optionally with interactions.

A model is not automatically trustworthy because it is interpretable; nor is every complex model impossible to inspect. We need to state what is being evaluated. The core project evaluates the stability and retained information of explanations, not the philosophical distinction between black boxes and glass boxes.

## 6. Prediction, explanation and causation are different

Prediction: “What score does this model assign?” Explanation: “Which inputs account for this score under a chosen explanation definition?” Causation: “What would actually happen if we intervened in the world?”

An umbrella predicts rain but does not cause rain. Likewise, a past payment may predict default without being something a person can change today. Removing a feature in software is not equivalent to intervening on a real economic system.

**Local explanation** describes one person. **Global explanation** summarizes many people. Our main global score averages the magnitudes of local contributions across a fixed set of 500 people in the pilot. A global top feature is not necessarily the top reason for every individual.

## 7. What SHAP is trying to do

Imagine a team earns a score and you want to divide credit among its members. A Shapley value averages each member's marginal contribution over the different orders in which members could join. In a model explanation, the members are features, and the “team score” requires a rule for filling in features that have not joined.

Two-feature example: v(empty)=0, v(A)=10, v(B)=20, v(A,B)=50. If A joins first, A gets 10 and B gets 40. If B joins first, B gets 20 and A gets 30. Average: A gets 20 and B gets 30. Total credit is 50.

The important phrase is **under a specified game**. Missing inputs might be drawn from a background dataset independently of the fixed inputs (interventional masking), or from a conditional distribution given the fixed inputs. These answer different questions. “Exact SHAP” means exact for the selected game, not a uniquely correct account of real causes.

For our linear logit model, interventional attribution is simple: contribution_j = beta_j * (standardized value_j − mean standardized background_j). Base logit plus all contributions must equal the model's logit prediction. The code verifies this to floating-point precision. We do not claim to have implemented TreeSHAP in the pilot.

**Hand calculation:** model score=3*x1+2*x2. Background means=(1,2), person=(2,5). Base score=7. Contributions are 3*(2−1)=3 and 2*(5−2)=6. Full score=7+3+6=16. This is an exact linear explanation.

## 8. Why correlated inputs create a problem

Correlation describes how two measured quantities vary together. Pearson measures linear association; Spearman measures association between ranks. Strong rank correlation does not prove that features mean the same thing or cause one another.

Suppose x1 and x2 are identical measurements. Model A uses score 2*x1+2*x2. Model B uses 4*x1. On data where x1=x2, both models make identical predictions. Their interventional feature explanations differ: A divides credit; B attributes all credit to x1. This is partly a property of model underidentification, not necessarily an explainer mistake.

If both inputs measure the same concept, summing them may provide a stable concept-level explanation. But we must test this. If we merge everything into one group, every ranking has one item and is trivially stable. That explanation has almost no resolution.

In the pilot, all six monthly bill amounts cluster together. Calling the group “bill history” is reasonable after inspecting column definitions. It does not establish that every member is interchangeable or that earlier months are irrelevant.

## 9. Clustering from first principles

Set distance between two numeric features to D=1−|Spearman correlation|. Highly correlated features have small distance. Start with each feature as its own group. Complete-linkage clustering merges groups using their largest cross-feature distance. Thus, a group must be internally close at the cut threshold.

If rho=.7, cut at distance .3. All feature pairs inside each resulting group have absolute correlation at least .7, subject to numerical precision. Features in different groups can still be strongly correlated. The method is not a guarantee of independent concepts.

Raising rho makes the grouping stricter and generally yields more smaller groups. Lowering rho allows more merging. This direction was reversed in the uploaded manual.

A constant column has undefined correlation. Missing values, special codes and categorical representations need explicit handling. In the current UCI pilot there are no missing cells, but repayment-status coding remains a limitation of the simple numeric baseline.

## 10. Grouped sums, exact group Shapley and cancellation

For one person, sum the contributions inside a group. Then take the magnitude of this net contribution. Average those magnitudes over people for a global importance score.

Example: contributions +5 and −4.8 give a net group contribution of .2. The sum of magnitudes is 9.8. These measure different things. Net contribution explains the net score effect; the magnitude sum reveals large opposing components. Both can be useful, and reporting only .2 can conceal important internal behaviour.

Our cancellation diagnostic is 1−net-magnitude-total/unsigned-magnitude-total, aggregated over the audit sample. Near zero means little cancellation. Near one means substantial cancellation. When both quantities are negligible, the ratio is undefined and should be reported as uninformative. High cancellation is not automatically a bug.

**Exact group Shapley** makes whole groups the players before calculating values. **Coalition-sum attribution** computes ordinary feature values first and sums them afterwards. They need not match. In a three-feature game where the value is one only when A, B and C are all present, each ordinary Shapley value is 1/3. Summing A+B gives 2/3. If {A,B} and {C} are the two players, each group gets 1/2. This is why we must not casually call a coalition sum an Owen value.

Our linear interventional example has a suitably additive game, so aggregation is straightforward. The final synthetic interaction experiment will show where that simplification fails.

## 11. What LIME and permutation importance do

LIME fits a simple surrogate near the input being explained. Its coefficients depend on neighbourhood sampling, kernel width, feature representation and scaling. A coefficient is not automatically a contribution in the same units as SHAP. We need the standardized displacement and surrogate residual if making a careful comparison.

Permutation importance shuffles inputs and measures how a chosen prediction-performance metric changes. It is generally a global performance-dependence measure, not a local contribution matrix. Correlation can make its behaviour unintuitive. Shuffling a whole group together preserves relationships among that group's members but can still break relationships with other groups.

Our initial project does not fuse these outputs. First compare the same explanation target across retrained models. Add cross-explainer comparisons only after controlling output scale, model and input sample.

## 12. Stability and its controls

A stable explanation changes little when reasonable aspects of the modelling process change. “Reasonable” must be specified. Different seeds, bootstrap training samples, new datasets and input perturbations are different changes.

Bootstrapping samples training rows with replacement. Some original rows appear several times; others are omitted. We train ten logistic models on ten such samples, then explain the same 500 held-out people using a common raw training background. This probes sensitivity to the available training sample.

We rank features or groups using their mean absolute contributions. RBO compares two ranked lists and emphasizes the top. With p=.85, early ranks get more weight. Identical lists score one. It is a descriptive agreement score, not a probability that explanations are correct.

Ten fits create 45 unordered pairs. Those 45 pairs share models, so they are dependent. Treating them as 45 independent studies exaggerates certainty.

Two controls are different: random rankings of M items measure chance agreement among rankings; random partitions of d features into groups of the same sizes measure the effect of grouping itself. We use the latter in the pilot. Every random partition has the same number and sizes of groups as the correlation partition, so a shorter list alone cannot explain its advantage over that control.

Still, one positive difference is not proof of broad superiority. The random groups can differ in semantic meaning or score distribution. Synthetic ground truth, domain groups, multiple datasets and fidelity checks address further concerns.

## 13. Accuracy metrics you should be able to explain

Accuracy is the fraction of correct class decisions. If only 1% of cases are positive, predicting negative always gives 99% accuracy while missing every positive.

Precision=correct positive predictions/all positive predictions. Recall=correct positive predictions/all actual positives. Example: a model flags 100 cases, 30 are truly positive, and the dataset has 50 positives. Precision=.30 and recall=.60.

ROC-AUC measures ranking discrimination across thresholds. AP summarizes precision along the recall progression when cases are ranked by score. It is not the same numerical definition as trapezoidal PR-AUC. Default prevalence provides useful context; the pilot prevalence is .2212.

Brier score averages (predicted probability−actual outcome)^2. For predictions .9,.2,.7 and labels 1,0,1, the score is (.01+.04+.09)/3=.0467. Lower is better. It is not a pure calibration measure; use calibration plots when discussing calibration itself.

Our pilot averages these metrics over ten fitted models on the same held-out test set: AP .4894, ROC-AUC .7130 and Brier .1477. These are baseline measurements, not scores of the full proposed method.

## 14. Faithfulness, stability, plausibility and usefulness

**Faithfulness** asks whether an explanation reflects the specified model's behaviour. **Stability** asks whether it changes under specified perturbations/retraining. **Plausibility** asks whether a human finds it sensible. **Usefulness** asks whether it helps a person perform a task. They are different.

A constant explanation can be perfectly stable but unfaithful. A faithful explanation can describe an undesirable model. A plausible financial story can be unsupported by the model. A human-usefulness claim requires an appropriate user study, which is outside our minimum scope.

We evaluate known-game attribution error on synthetic examples and perturbation behaviour with explicit limits. We keep internal group details so stable summaries do not hide all individual differences. This is the “without concealment” part of the title.

## 15. Recourse, monotonicity and why they were deferred

A counterfactual is an alternative input that changes a model decision. Recourse is a feasible course of action a person can actually take. Changing a historical payment in a CSV is a counterfactual edit, not an action today.

Monotonicity means changing a constrained input in a given direction cannot move the current model's output in the opposite direction while others are fixed. It can make a model's shape more consistent with stated assumptions. It does not ensure that another model trained next month will preserve a recommendation.

A margin can help if future scores cannot move by more than the margin. But a sample quantile of past or bootstrapped shifts does not establish a universal future bound. Conformal coverage requires a defined prediction target and assumptions such as exchangeability; arbitrary drift and adaptive optimization do not inherit its guarantee.

Because the chosen credit datasets do not provide valid future action trajectories, adding all these topics would weaken the study. Deferring them is a scope decision grounded in evidence, not a lack of ambition.

## 16. The actual code, in order

1. `demo.py` reads the official Excel file using pandas and checks the expected 30,000 rows.
2. It separates the target and drops the documented excluded columns.
3. It saves a deterministic stratified train/test split and chooses fixed audit rows without using their labels.
4. `groups_from_training` calculates the training correlation matrix and complete-linkage groups.
5. A loop draws ten bootstrap samples and fits imputation → standardization → logistic regression pipelines.
6. For each pipeline it calculates held-out probability metrics and exact interventional logit contributions.
7. It asserts that base logit plus contributions reconstructs each prediction.
8. `mean_stability` computes rankings and pairwise RBO for either singleton or grouped contributions.
9. It repeats the grouping calculation using 30 random partitions with matching sizes.
10. It writes JSON, CSV and split IDs. `test_demo.py` checks key mathematical contracts independently.

`kth_margin` is an isolated, tested correction to the uploaded manual's order-statistic bug. It is not called by the main pilot and does not imply recourse was implemented. If asked why it is included, say it is an audit regression test, not part of the proposed core pipeline.

## 17. Explain the pilot without overstating it

Say: “The correlation groups achieved RBO .924, while random groups with the same sizes averaged .863. The controlled difference is approximately .061 in this particular logistic baseline. Next I need to test fidelity, interactions and other models.”

Do not say: “Our method improves explainability by 6.1%.” RBO is not an explainability percentage, .061 is an absolute score difference, and the outcome is only stability under the specified experiment.

Do not compare AP .489 with RBO .924; they measure different objects. Do not use one result to claim 92.4% accurate explanations. Do not call the 45 model pairs independent repeats.

## 18. Likely viva questions and concise answers

**1. What is new?** Grouping itself is not new. The intended contribution is a controlled audit of stability against matched grouping controls together with information-loss checks. Final novelty depends on comparison with the closest full papers.

**2. Why not simply use SHAP?** SHAP supplies an attribution for a specified model/game. It does not automatically tell us how stable a summary is after retraining or whether grouping conceals distinctions.

**3. Why credit data?** It contains naturally correlated monthly financial measurements and is publicly accessible. Results on old Taiwanese data do not establish deployment suitability in India.

**4. Is this causal?** No. It explains predictive model outputs under stated masking assumptions.

**5. Why no deep learning?** The scientific question is about explanation representation and controls, not model scale. Tabular baselines are sufficient and feasible on our hardware.

**6. Why complete linkage?** It gives an interpretable within-group correlation criterion. It does not ensure independent groups or low VIF.

**7. Why not one big group?** It gives trivial stability and loses resolution. We include it as a failure control.

**8. What if random grouping performs equally well?** Then evidence for correlation-specific benefit is weak. That is an important negative finding.

**9. What if grouping is stable but unfaithful?** We report the trade-off and reject a claim of improved explanation quality.

**10. Why take absolute value after summing?** We measure the group's net contribution to the score. We separately retain unsigned magnitude to detect cancellation.

**11. Can all explainers agree and be wrong?** Yes. Agreement is not correctness.

**12. Why is bootstrap not temporal drift?** Resampling the same training distribution does not model actual passage of time or structural economic change.

**13. What has been coded?** The UCI logistic baseline, grouping, exact linear attribution, matched random controls, RBO, result export and tests. Trees, LIME, synthetic oracle and full study are future work.

**14. How do you know the code works?** Tests check hand-computed cases and failure conditions; the data/split checks and reconstruction identity pass; a deterministic rerun reproduces saved metrics. These checks do not prove the research hypothesis.

**15. Could the model use proxies for sex?** Yes. Dropping a protected variable is not a fairness guarantee.

**16. Why not use accuracy?** It can hide poor minority-class performance. We report AP, ROC-AUC and Brier with prevalence.

**17. Is the baseline score competitive?** We have not performed a competitive benchmark. It is an interpretable starting point.

**18. Why are exact group values expensive?** Enumerating subsets costs 2^M coalition evaluations before accounting for backgrounds and explained rows. We cap exact experiments at small M.

**19. What is the difference between SHAP and Owen?** Ordinary Shapley averages unrestricted feature orders; Owen accounts for predefined coalition structure. A post-hoc sum is not generally either an exact grouped game or Owen computation.

**20. What if the cluster changes across seeds?** The primary experiment freezes training-derived groups to isolate attribution instability. A separate analysis reclusters and evaluates partition uncertainty.

**21. What is the unit of explanation?** Log-odds in the pilot. We must explicitly choose the unit for future tree experiments.

**22. Why use the same audit rows?** So differences are not due to explaining different people.

**23. Why use a fixed raw background?** To reduce baseline-distribution changes as a source of attribution differences. Each model transforms it through its own fitted preprocessing.

**24. Why not test on the training data?** Held-out rows better assess behaviour beyond memorized examples. Training data are used for fitting and background construction, not final performance claims.

**25. Can missing-value imputation change explanations?** Yes. It is part of the fitted pipeline and must be documented and included in interpretation.

**26. Does stability imply fairness?** No. A discriminatory explanation could be stable.

**27. What is a confidence interval here?** An interval for a specified sampling procedure and estimand. Applicant resampling with models fixed describes applicant-sampling uncertainty, not all model retraining uncertainty.

**28. Why no p-value on the slide?** The pilot has a single split and dependent model pairs. A bare significance claim would overstate its evidence.

**29. Which conference?** We will assess a future ACM ICAIF call; an appropriate ECML PKDD workshop may fit an evaluation study. Deadlines and publication policy are not yet committed.

**30. Is publication guaranteed?** No. It depends on novel, valid results, writing quality and peer review.

**31. What if recent work already does this?** Read and reproduce it, then identify a real missing factor or reposition as a transparent replication. Do not manufacture novelty.

**32. What is your next experiment?** Synthetic known-game tests and cancellation/fidelity checks, followed by a tree model.

**33. Can you explain the code without Cursor?** Demonstrate data loading, splitting, grouping, training, the linear attribution equation and JSON outputs. If a line is unclear, say so and learn it before claiming ownership of its design.

**34. What are the main risks?** Existing similar work; unstable or misleading grouping; weak dataset coverage; masking artefacts; and limited time. The scoped protocol and failure controls address these directly.

**35. How will the project finish in eight weeks?** Keep two model families, one or two real datasets and controlled synthetic cases. Defer the original recourse system and optional explainers unless core gates pass.

## 19. Tonight's preparation plan

First 30 minutes: read sections 1–6 and rehearse the project in plain words. Next 45 minutes: learn the SHAP example, correlation problem, grouping controls and the precise pilot interpretation. Next 30 minutes: run the tests and demo once and inspect the JSON. Next 30 minutes: rehearse the four slides with the speaker notes. Last 30 minutes: practise the viva answers and remove anything from the slides you cannot explain.

If time is short, prioritize the four-slide deck, sections 1/8/10/12/16/17 and the first fifteen viva questions. Do not try to master every advanced concept tonight. Have the PDF deck and screenshots of the actual saved output available as an offline backup; label the screenshot as output from the recorded run.

## 20. Quick self-test

1. If a model outputs .8, are SHAP values necessarily probabilities? No; check the explained output scale.
2. If rho is raised from .7 to .9, do groups usually become larger? No; the merge requirement becomes stricter.
3. What is |5−4.8| versus |5|+|−4.8|? .2 versus 9.8.
4. Do ten fits give 45 independent experiments? No; pair comparisons share fitted models.
5. What is the fairer pilot comparison: .924−.776 or .924−.863? The second controls the number and sizes of groups through random partitions.
6. Can the six historic monthly bill columns validate future recourse? No.
7. What result would weaken your idea? No advantage over matched random grouping, or stability improvement accompanied by unacceptable information loss.
8. What have you not yet done? Full synthetic/oracle validation, tree/LIME evaluation, second dataset, inferential study and publication.

For source citations, formulas, qualifications and the detailed audit, use the accompanying Research Dossier. For exact commands and Cursor prompts, use the Implementation Playbook.
