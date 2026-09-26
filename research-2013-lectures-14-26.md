# MIT 18.S096, Fall 2013: lectures 14–26

Research date: September 25, 2026. This guide uses official MIT OCW PDFs and recording descriptions. Lecture headings reproduce the lecture-notes index; the recording title differs slightly for lectures 19 and 26. The PDFs were read beyond their titles, with page references below. Each PDF contributes fewer than 200 words of summary. Mathematical notation is normalized for legibility. Supplemental study prompts are interpretation, not a claim that the lecturer assigned them.

Coverage: eleven lecture-notes PDFs are available. Lecture 16's notes are only an outline; lecture 20 has no notes. Both gaps were substantially closed by reading official downloadable transcript PDFs discovered in the resource-page HTML. Lecture 22 has neither notes nor a recording in the published video gallery. Other recording descriptions were checked, but their complete transcripts were not reviewed. Source discovery used public MIT HTML, with no video downloads. [Notes index](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/pages/lecture-notes/), [video gallery](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/video_galleries/video-lectures/).

## 14 — Portfolio Theory

The lecture builds single-period Markowitz optimization from asset return means and covariance. It derives minimum-variance weights with Lagrange multipliers, compares equivalent return-maximization and risk-aversion formulations, and identifies the efficient frontier. Adding a constant-return asset leads to the common risky portfolio and Tobin separation. Later material connects preferences to von Neumann–Morgenstern utility, including quadratic, exponential, power, and logarithmic utility; introduces long-only, holding, turnover, benchmark, and tracking-error constraints; and considers estimation and alternative risk measures.

The core quantities are

\[
E[R_w]=w^\top\alpha,\qquad \operatorname{Var}(R_w)=w^\top\Sigma w.
\]

For a target mean, minimize the second expression subject to \(w^\top\alpha=\alpha_0\) and \(w^\top1=1\). The unconstrained derivation uses an invertible covariance matrix; real portfolios may require additional constraints. Expected return and variance are model inputs, not automatically reliable estimates. The application is allocation across correlated assets, including allocation relative to a benchmark. [PDF, pp. 3–14, 16–33](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/bba02164ba6642f7d516df35347aec01_MIT18_S096F13_lecnote14.pdf).

Supplemental study prompt: explain how a holding constraint can alter the unconstrained frontier before implementing an optimizer.

## 15 — Factor Modeling

This lecture separates asset observations into common factors and asset-specific noise:

\[
x_t=\alpha+Bf_t+\epsilon_t,\qquad
\Sigma_x=B\Omega_fB^\top+\Psi.
\]

The model holds intercepts and loadings constant through time, assumes covariance-stationary factors, diagonal specific-risk covariance, white-noise residuals, and zero factor–residual cross-covariances. It contrasts macroeconomic factors, fundamental characteristics, and statistically inferred factors. Fundamental examples include industry, size, dividend yield, and valuation style. BARRA treats attributes as observed loadings; the Fama–French approach constructs characteristic-sorted long–short portfolios and estimates exposures through time-series regression. Statistical sections cover factor-analysis identification, Gaussian maximum likelihood, principal components, and the principal-factor method.

The application is a parsimonious model of joint stock, futures, currency, or Treasury-yield variation. The covariance decomposition explains which portfolio risks are shared and which are specific. Gaussian assumptions belong to the presented likelihood formulation; they are stronger than the general covariance decomposition. [PDF, pp. 3–6, 13–16, 20–38](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/3c8e688538b350a73a8c1cd46056fc5a_MIT18_S096F13_lecnote15.pdf).

Supplemental study prompt: distinguish a statistically convenient component from an economically interpretable factor.

## 16 — Portfolio Management

Jake Xia's posted PDF supplies an outline covering construction, special-case portfolio theory, risk parity, and limitations. [Outline PDF, p. 1](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/d36136adb6ab4d3d841df5e31824bf81_MIT18_S096F13_lecnote16.pdf).

The transcript begins with students constructing portfolios, then relates objectives to personal cashflows, endowments, pensions, and capital allocated across traders. Two-asset examples vary volatility and correlation; later discussion reviews beta, Sharpe ratio, Kelly sizing, and the equity/bond 60/40 benchmark. Risk parity balances risk weights rather than market-value weights; leverage scales exposure, while the illustrated cash/risky-asset Sharpe ratio stays unchanged. A two-year example demonstrates gains from restoring equal weights between assets with alternating returns. Limitations include historically estimated volatility, bond exposure during rising yields, crowding, and market participants changing the system. Bridge and metronome analogies illustrate synchronization. The practical application is constructing and adapting allocations to investor objectives, rather than treating an estimated frontier as permanently optimal. [Transcript, pp. 2–21](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/2aa2fec3d040b7d3746ca7ba5c192041_8TJQhQ2GZ0Y.pdf).

Supplemental caution: the lecture's special-case discussion does not establish universal Sharpe-ratio optimality for risk parity.

## 17 — Stochastic Processes II

The notes move from discrete-time processes to distributions over continuous paths. Standard Brownian motion starts at zero, has continuous paths, independent nonoverlapping increments, and normal increments:

\[
B_t-B_s\sim N(0,t-s),\qquad [B]_T=T.
\]

A scaled random walk motivates the continuous limit. The lecture studies maxima through the reflection principle, the distribution of a modeled stock's daily range, almost-sure nondifferentiability, quadratic variation, and Brownian motion with drift. It explicitly leaves rigorous construction of the probability measure outside the course's scope.

The financial application is a continuous-time approximation supporting stock-path and range calculations. Continuous paths do not have ordinary derivatives; nonzero quadratic variation is the reason a separate calculus becomes necessary. The model's Gaussian independent increments are assumptions, rather than a conclusion that actual market returns have these properties. [PDF, pp. 1–6](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/3b97c6b0c282dd9dc024c4c7ffe3fba8_MIT18_S096F13_lecnote17.pdf).

Supplemental study prompt: contrast a continuous differentiable price curve with a Brownian path by computing sums of squared increments on finer partitions.

## 18 — Itō Calculus

The lecture develops the second-order correction required by Brownian quadratic variation. For \(dX_t=\mu_tdt+\sigma_tdB_t\), normalized notation gives

\[
df(t,X_t)=\left(f_t+\mu_tf_x+\tfrac12\sigma_t^2f_{xx}\right)dt
+\sigma_tf_xdB_t.
\]

Examples include integrating \(B_t\), exponential Brownian functions, and drifted Brownian motion. The second part treats adaptedness, stochastic integrals as martingales under integrability conditions, deterministic-integrand normality, and Itō isometry. The final part introduces changes of probability measure and a drift-removal theorem.

The intended financial bridge is transforming stochastic prices, calculating integral variances, and understanding risk-neutral modeling. Smoothness and square-integrability conditions matter: a random integrand does not automatically produce a normal integral. Adaptedness expresses dependence on information available at the current time. [PDF, pp. 1–7](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/ef2c66c8079ba656210ad1fd4a5e2fa8_MIT18_S096F13_lecnote18.pdf).

Editorial correction, visually verified against rendered PDF p. 2: the stated general theorem omits \(\sigma_t\) in the diffusion term, although its proof includes it. The equation above uses the proof's coefficient. This is a correction, not a quotation.

## 19 — Black-Scholes Formula & Risk-neutral Valuation

The lecture begins with a bookmaker example, then prices forwards and European calls and puts through replication. A one-step binomial model distinguishes actual transition probability from the pricing probability that makes discounted stock value a martingale. Its continuous analogue is

\[
V_t=e^{-r(T-t)}E^Q[V_T\mid\mathcal F_t].
\]

Assuming lognormal stock dynamics, a stock-and-money-market replicating strategy and Itō's formula yield

\[
V_t+rSV_S+\tfrac12\sigma^2S^2V_{SS}-rV=0.
\]

Payoffs determine terminal and boundary conditions; a transformation connects this PDE with the heat equation. The key result is elimination of the stock's actual drift from the pricing equation. Applications are derivative valuation and delta replication under the stipulated continuous model, interest-rate and volatility assumptions. [PDF, pp. 2–18](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/d19208c017ada04f9261cfb41ab8d702_MIT18_S096F13_lecnote19.pdf).

Supplemental clarification: \(P\) describes physical outcomes; \(Q\) is a pricing measure. A derivative price is not generally its discounted physical expected payoff. The formula above assumes constant \(r\) and the model's replicability conditions.

## 20 — Option Price and Probability Duality

No lecture notes are posted, but the official transcript provides substantive coverage. Blythe defines calls, zero-coupon bonds, and digitals; narrowing call spreads replicate digitals, and differentiating call prices with respect to strike produces the conditional distribution and density. With discount bond price \(Z(t,T)\), normalized notation gives

\[
-C_K=Z\,\Pr^{\mathrm{pricing}}(S_T>K\mid\mathcal F_t),\qquad
f^{\mathrm{pricing}}(K)=C_{KK}/Z.
\]

Butterflies approximate density exposure and support trading views about particular terminal-price regions. The relationship does not require choosing Black–Scholes; inserting its call formula produces a lognormal density. The other direction prices terminal payoffs from the distribution and statically replicates sufficiently smooth European payoffs with bonds, stock, and a continuum of calls. Assumptions include appropriate pricing probabilities, no-arbitrage valuation, and smoothness/continuous-strike limits; the lecturer discusses discrete quoted strikes and deviations between long-dated replicas and contracts when risk capital is constrained. Path-dependent claims lie outside this terminal-payoff spanning argument. [Transcript, pp. 6–15, 20–26](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/681ecdd52c5813a283f4a4065fd768fc_eG_aRPy1KVE.pdf).

Supplemental clarification: these are pricing probabilities, not automatically physical forecasts. For stochastic rates, the bond-normalized expression naturally uses the maturity-forward pricing measure; with deterministic rates this coincides with the relevant money-market pricing distribution.

## 21 — Stochastic Differential Equations

The notes define an SDE through its integral form and state existence and pathwise uniqueness under spatial Lipschitz and growth conditions. Coefficient matching gives geometric Brownian motion; an integrating-factor construction solves a mean-reverting Ornstein–Uhlenbeck process. For constant coefficients,

\[
dX_t=\mu X_tdt+\sigma X_tdB_t,
\quad X_t=x_0e^{(\mu-\sigma^2/2)t+\sigma B_t}.
\]

The lecture then surveys finite differences, Monte Carlo sampling, and trees built from random-walk approximations. Its final topic is the heat equation and the change-of-variables relationship with Black–Scholes. Financial applications include simulating stochastic models and approximating derivative-pricing equations when closed forms are unavailable. The existence theorem's technical proof is omitted. [PDF, pp. 1–6](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/a671d0d2abe626c371fd5850ad670397_MIT18_S096F13_lecnote21.pdf).

Supplemental clarification: path simulation requires stochastic increments of the correct distribution and scale. A simulated Brownian path does not become differentiable. Treat the notes' informal finite-difference description as intuition, then distinguish time-discretization error from Monte Carlo sampling error.

## 22 — Calculus of Variations and its Application in FX Execution

The official notes index supplies this title and explicitly states that no notes are available. The video gallery omits lecture 22. There is therefore no verified subtopic list, equation, execution-cost model, or worked financial example in the accessed OCW materials. [Official notes index](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/pages/lecture-notes/).

Supplemental study direction: calculus of variations optimizes a functional over paths, whereas ordinary finite-dimensional optimization chooses a vector. In an execution setting, a trading schedule can be the path being chosen. However, the precise functional, boundary constraints, market-impact assumptions, and FX objective used by this lecturer remain unknown. Do not present a standard execution model as the actual lecture. This section is a documented coverage gap rather than a reconstructed lesson.

## 23 — Quanto Credit Hedging

Andreev combines FX interest-rate parity, risk-neutral expectations, sovereign default, and currency jumps. Currency-denominated payoff examples show why comparing nominal payouts can be misleading. The basic credit model takes default as the first Poisson arrival with constant hazard \(h\). A minimal FX model imposes a fixed multiplicative jump:

\[
Q(\tau>T\mid\tau>t)=e^{-h(T-t)},\qquad S_{\tau+}=e^JS_{\tau-}.
\]

The lecture prices zero-coupon bonds in different currencies, derives hedge notionals, and checks continuous rebalancing in default and survival states. Zero recovery supports the presented exact-replication example; introducing positive recovery defeats that exact replication. Adding diffusive FX risk creates a second risk source and motivates additional hedge instruments, including forwards. Applications include sovereign currency-default links and quanto CDS, whose protection denomination differs from the underlying bond. [PDF, pp. 3–7, 17–30](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/c6a3c15db672e2bd462f3002da1e2262_MIT18_S096F13_lecnote23.pdf).

Supplemental study prompt: identify which model assumptions make the proposed hedge replicating, and which extra risks appear after adding diffusion or recovery.

## 24 — HJM Model for Interest Rates and Credit

Gorokhov motivates a reusable simulation framework through dynamic option hedging and risk-neutral Monte Carlo. Interest-rate material connects discount factors, forwards, and short-rate models, including Ho–Lee, Hull–White, and CIR. HJM models the whole forward curve. In the illustrated one-factor formulation,

\[
df(t,T)=\sigma(t,T)\left[\int_t^T\sigma(t,u)du\right]dt
+\sigma(t,T)dW_t^Q.
\]

No-arbitrage fixes the drift once volatility is selected. The practical sequence is to bootstrap swap quotes, initialize forwards, calibrate volatility to swaptions, simulate, and discount averaged payoffs. Credit material covers CDS, recovery, survival probabilities, hazard rates, risky discount factors, callable bonds, and forward-hazard dynamics. The simplified CDS illustration assumes zero interest; the credit HJM derivation uses a zero-recovery bond. Applications are interest-rate and credit derivative pricing and exercise decisions. [PDF, pp. 3–24, 25–30](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/e4c52338bad489162192dd0cc44375ab_MIT18_S096F13_lecnote24.pdf).

Supplemental study prompt: explain why fitting today's curve does not determine its volatility or future physical evolution.

## 25 — Ross Recovery Theorem

The PDF is titled *Can We Recover?*, by Carr and Yu. It examines extracting representative beliefs from Arrow–Debreu prices, finite-state Markov recovery, change of numeraire, the numeraire portfolio, bounded diffusion states, and successes or failures on unbounded states. The distinction is explicit: \(P\) is physical probability, \(Q\) the no-arbitrage pricing measure, and \(R\) recovered representative beliefs. Only if market beliefs match reality does \(R=P\).

The bounded-diffusion discussion assumes time-homogeneous dynamics, a positive diffusion coefficient, known pricing drift and short-rate functions, and suitable numeraire-portfolio structure. Separation of variables and spectral reasoning identify beliefs under additional restrictions. The authors state that their technical assumptions do not recover stock dynamics from Black–Scholes option prices. Applications are forward-looking market-implied beliefs, including means and rare-move probabilities, conditional on the theorem's assumptions. [PDF, pp. 4–8, 34–45](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/65ff25bf0160cee676bbc5540cdf951f_MIT18_S096F13_lecnote25.pdf).

Supplemental study prompt: articulate why knowing option prices at one current state does not automatically reveal an entire state-transition system or objective future probabilities.

## 26 — Introduction to Counterparty Credit Risk Conclusions

Tang introduces counterparty default and mark-to-market credit risk in OTC portfolios. CVA adjusts default-free derivative value for credit exposure; collateral and offsets make this an enterprise portfolio problem. Its positive-exposure structure is, with \(\beta_0=1\),

\[
\mathrm{CVA}=-E^Q\!\left[1_{\{\tau\le T\}}\beta_\tau^{-1}
(1-R_\tau)(V_{\tau-}-C_{\tau-})^+\right].
\]

The slides distinguish receivable and payable adjustments, discuss funding and wrong-way risk, and develop money-market, forward, annuity, and survival-annuity measures. They introduce martingale tests, resampling, and interpolation for numerical consistency. Exposure spans interest rates, FX, credit, equities, commodities, and mortgages; trade-level models alone cannot generally capture nonlinear netting effects. The recording description also identifies institutional economic objectives and the course conclusion. [PDF, pp. 2–8, 12–19](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/6a88ece1d51780a6a719cc620abc7c2f_MIT18_S096F13_lecnote26.pdf), [recording description](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/resources/lecture-26-introduction-to-counterparty-credit-risk/).

Supplemental clarification: the symbol \(P^T\) here denotes a forward pricing measure, not the physical \(P\). The negative sign makes CVA a value deduction; positive reported CVA loss uses the opposite sign convention.
