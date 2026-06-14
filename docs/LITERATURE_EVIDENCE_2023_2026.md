# E. coli mechanism literature 2023–2026 — annotated evidence table

Purpose: ground new graph edges and **real, literature-backed phenotype test
patterns** (to replace the self-authored battery flagged in
`SCORECARD_REPORT_20260613.md`). Scope: *E. coli* K-12 MG1655 (non-K-12 strains
flagged). Window: 2023–2026.

**Verification standard (enforced):** every paper below was confirmed to exist
by fetching its publisher / PMC / Europe PMC / Crossref record — DOI or PMID
recorded from that page. Gray-zone references were dropped, not softened.
Preprints and non-K-12 strains are flagged inline. Direction (activates vs
represses) is stated from the regulator's perspective and is the field that maps
to a graph edge.

Effect-direction confidence tiers: **direct experiment** > **omics-correlation**
> **computational/review synthesis**. b-numbers/UniProt are standard EcoCyc/K-12
annotations — cross-check against the KG's canonical id set before edge insertion.

---

## ★ Priority picks — these directly fix the project's diagnosed gaps

The phenotype battery's problems (see SCORECARD report): only 2 real L2
conflicts, 0 genuine L3, the lac thesis case partly un-discriminating. These
papers supply real replacements:

| Gap to fix | Paper | What it gives |
|---|---|---|
| **lac thesis case** (currently weak) | Lin 2025 (preprint) | CRP **represses** lacI *and* activates lacZYA — a real coherent FFL. Turns glucose+lactose into a genuine, citable L2 with a new `CRP→represses→lacI` edge. |
| **Real L2 conflict (opposing loop)** | Zhao 2024 mBio | CRP **activates** relA/spoT while ppGpp **inhibits** CRP — a true opposing-direction loop. |
| **Real L2 conflict (one regulator, both signs)** | Huang 2024 (Cra) | Cra **represses** glycolysis *and* **activates** gluconeogenesis; F1P releases Cra. Single regulator, opposite directions on two gene sets. |
| **Genuine L3 (multi-input + feedback)** | Cory 2024 + Sass 2024 | SOS with RecA→LexA cleavage + LexA autorepression **plus** a LexA-*independent* SspA arm. A real 3+-input conflict, not parallel derepression. |
| **Genuine L3 (≥6 competing inputs)** | Handler & Kirkpatrick 2024 | RpoS level integrates IraD/M/P (stabilize) + DsrA/RprA/ArcZ (↑) vs CyaR/OxyS/MgrR (↓). A ready-made multi-input conflict scaffold. |
| **Drug perturbation test cases** (matches the NL-intake "ciprofloxacin" example) | Teichmann 2025, Vikedal 2025 | fluoroquinolone → gyrase → RecA* → LexA cleavage → SOS; with ΔrecA as the knockout that abolishes it. End-to-end perturbation→cascade. |
| **New signed KG edges (raise RegulonDB recall)** | Chen 2025 (H-NS), Gorelik 2024 (CsrA) | H-NS⊣porins / H-NS→efflux; CsrA⊣{evgA,gadE,gadA,gadB,ydeO}. Concrete edges to add. |

---

## 1. Gene regulation

| Paper | DOI/PMID | Entities | Condition | Perturbation | Effect & direction | Evidence | Map to simulator |
|---|---|---|---|---|---|---|---|
| Kobayashi 2026, Microorganisms | 10.3390/microorganisms14010134 | HusR/YnfL (b1597); nrdAB, rusA-ylcG, xapA | Stationary phase | husR deletion; hydroxyurea | HusR **activates** targets (DNA-substrate/repair); loss→HU sensitivity, filamentation | Direct (gSELEX+RT-qPCR+KO) | Edges `HusR→activates→{nrdAB,rusA-ylcG,xapA}` gated by stationary phase |
| Anzai 2023, Microb Genomics | 10.1099/mgen.0.001015 / 37219924 | LldR (b3604); lldPRD, glcDEFGBA, gadW, gadY | Lactate / acid | lactate sensing | LldR **activates** all 12 targets | Direct (gSELEX-chip) | `L-/D-lactate→activates→LldR→activates→targets`; acid-resist via gadW/gadY |
| Gao 2023, NAR | 10.1093/nar/gkad253 / 37026477 | Fur (b0683, P0A9E5) | Iron limitation | pan-regulon ChIP | Fur+Fe²⁺ **represses**; only ~36 core targets conserved | Direct (ChIP ×9 strains) | Tag Fur edges core (always) vs accessory (strain-conditional) |
| Bastet 2024, NAR | 10.1093/nar/gkae347 | btuB (b3966); OmrA, OmrB | High AdoCbl / membrane stress | B12 ligand; OmrA/B | Both **repress** btuB (riboswitch termination; sRNA→RNase E decay) | Direct | Two repressing edges onto btuB (distinct mechanisms) |
| Grondin 2024, Commun Biol | 10.1038/s42003-024-07008-5 | thiBPQ (tbpA b0068); TPP riboswitch | High thiamine | TPP ligand | TPP **represses** (OFF) translation + Rho termination | Direct (single-molecule) | `TPP→represses→thiBPQ` ligand-gated OFF |
| Solchaga Flores 2024, NAR | 10.1093/nar/gkae1131 / 39611574 | fepA (b0584); RprA,RybB,OmrA,OmrB,ArrS,RseX,SdsR | Envelope/osmotic/stationary | sRNA expression | 7 sRNAs each **repress** fepA; some need terminator-loop | Direct | 7 `sRNA→represses→fepA` edges |
| Barsheshet Vigoda 2024, NAR | 10.1093/nar/gkae621 | GcvB (b4443); RNase E (b1084); lrp,glpC,sodB,cfa | GcvB-inducing | — | GcvB **represses** via enhanced RNase E cleavage | Direct (cleavage mapping) | `GcvB→represses(via RNase E)→targets` |
| Roca 2025, PNAS | 10.1073/pnas.2503747122 / 40638087 | Hfq (b4172, P0A6X3) | in vitro kinetics | cognate vs noncognate | Hfq **kinetically selects** cognate sRNA targets | Direct (smFRET) | Layer rule: weight sRNA→mRNA edges by duplex stability |
| Małecka & Woodson 2024, Nat Commun | 10.1038/s41467-024-46316-6 / 38453956 | Hfq (b4172) | in vitro | Arg-patch mutants | Hfq compacts + iteratively scans for most-stable duplex | Direct | Layer rule for Hfq target search; Arg-mutant = perturbation node |
| Lin (S-L) 2025, mBio | 10.1128/mbio.03814-24 / 39998215 | stnpA sRNA; YadG (b0146) | Fosfomycin / persistence | fosfomycin | stnpA **activates** YadG efflux → persistence↑ | Direct | `stnpA→activates→YadG`; plasmid-encoded (mobile) |
| Bajpe 2026, NAR (PRECISE-MG1655) | 10.1093/nar/gkag059 | iModulons: RpoS(b2741),ArcA(b4401),Fnr(b1334) | 584 RNA-seq conditions | ICA | RpoS vs Translation **inverse**; ArcA/Fnr co-regulate respiration | Omics (ICA) — moderate | Condition-dependent module activations; TF→target clustering/weighting |

## 2. Drug / antibiotic response

| Paper | DOI/PMID | Entities | Condition | Drug (dose) | Effect & direction | Evidence | Map to simulator |
|---|---|---|---|---|---|---|---|
| Teichmann 2025, BMC Microbiol | 10.1186/s12866-025-03771-5 / 39838279 | RecA (b2699), LexA (b4043) | resistance evolution | CIP/LEV/MOX/ENR (sub-MIC) | SOS **required** for FQ resistance evolution; ΔrecA impaired | Direct (evolution+WGS) | Perturbation: FQ→RecA→derepress SOS; ΔrecA blocks |
| Teichmann 2025, Int J Antimicrob Agents | 10.1016/j.ijantimicag.2024.107420 | RecA (b2699) | adapted lines | CIP vs ENR | SOS proteins **up** (RecA-dep) + a RecA-**independent** arm | Direct (proteomics) | Two parallel response branches from FQ node |
| Vikedal 2025, NAR | 10.1093/nar/gkaf437 | RecN (b2616), RecA (b2699) | CIP DNA damage | ciprofloxacin | DSB→RecA→RecN→nucleoid **supercompaction**; ΔrecN/ΔrecA impair | Direct (imaging) | `RecA→activates→RecN`→reorganization phenotype |
| Kijewski 2024, PLOS ONE | 10.1371/journal.pone.0298746 / 38787890 | RecA, SulA (b0958); stx2, LEE | sub-MIC FQ (EHEC) | CIP 0.06 µg/mL | RecA↑~100×, SulA↑, Shiga-toxin/T3SS **up** | Direct (RNA-seq) — strain=EHEC | omics-pattern validation; flag strain |
| Faraz 2025, AIMS Microbiol | 10.3934/microbiol.2025047 | SeqA (b0688), RpoS (b2741) | low-level FQ resistance | CIP/NOR/LEV | ΔseqA → ~1.5× MIC↑ via supercoiling; **requires RpoS** (AND-gate) | Direct (epistasis) | `SeqA⊣`(loss→tolerance) AND RpoS; ΔseqAΔrpoS reverts |
| Shiraliyev 2024, eLife | 10.7554/eLife.94903 | sucA(b0726),gltA(b0720),mdh(b3236),sdhC(b0721) | TCA/ETC mutants | aminoglycosides | TCA/ETC loss→ribosomal proteins **down**→AG tolerance | Direct+omics | tolerance edge via ribosome-abundance node (not PMF) |
| Chen 2025, Front Vet Sci | 10.3389/fvets.2025.1534498 | H-NS (b1237); ompC/F/G/N; acrA/B/D, emrE | Δhns (ATCC 25922) | gentamicin/amikacin | Δhns→MIC↓8–16×: porins **up**, efflux **down** | Direct — strain=ATCC | Signed edges `H-NS⊣porins`, `H-NS→efflux` |
| Zhang 2024, mSystems | 10.1128/msystems.01295-24 / 39470288 | katG(b3942),sodA(b3908),ahpC(b0605) | persistence/carbon shift | ampicillin 100 µg/mL | drug→ROS→death; detox enzymes ⊣ death; carbon source gates ROS | Direct | bactericidal→ROS→death; metabolic state modulates edge weight |
| Qi 2023, iScience | 10.1016/j.isci.2023.108373 / 38025768 | umuC(b1184),umuD(b1183),mutM(b3635) | sub-lethal drugs | amox/enro/kana + thiourea | drug→ROS→DNA damage→SOS Pol V **up**→mutagenesis; thiourea blocks | Direct | edge chain drug→ROS→SOS→mutagenesis |
| Pal 2024, NAR | 10.1093/nar/gkae719 / 39180403 | narU(b1469), argI(b4117) | early CIP adaptation | CIP (sub-MIC) | regulatory mutations→narU↑/argI↑→ATP/anaerobic shift | Direct (WGS) | metabolic-rewiring perturbation pattern |
| Di Maso 2024, MicrobiologyOpen | 10.1002/mbo3.70006 | TolC (b3035); AcrAB-TolC | efflux/stress | (genetic) | TolC efflux affects motility/fitness beyond drug export | Direct — moderate | TolC as shared OM channel node; efflux loss pleiotropic |

## 3. Stress / starvation

| Paper | DOI/PMID | Entities | Condition | Trigger | Effect & direction | Evidence | Map to simulator |
|---|---|---|---|---|---|---|---|
| Cory 2024, Nat Struct Mol Biol | 10.1038/s41594-024-01317-3 / 38755298 | LexA (b4043), RecA (b2699) | SOS | ssDNA-RecA* filament | RecA* **activates** LexA autoproteolysis → >40 SOS genes derepressed | Direct (cryo-EM) | `RecA*→LexA cleavage`; `LexA⊣SOS`; L3 with feedback |
| Sass 2024, PNAS | 10.1073/pnas.2407832121 / 38935560 | LexA, SspA (b3229), IraD/IraM | replication block | azidothymidine | LexA-SOS **up** + **616 genes LexA-independent** (SspA); IraD/M↑ (RpoS) | Direct (RNA-seq) | L3: LexA arm + SspA arm + RpoS cross-talk |
| Choudhary 2024, Cell Systems | 10.1016/j.cels.2024.10.003 / 39541985 | OxyR (b3961) | oxidative | H₂O₂ | OxyR **activates** in 3 temporal classes (pulsatile vs gradual) | Direct (single-cell) | encode edge "kinetic class" attribute |
| Miwa & Taguchi 2023, PNAS | 10.1073/pnas.2304841120 / 37523569 | IbpA (b3687), σ32/RpoH (b3461) | heat shock | temp upshift | IbpA **represses** rpoH translation (neg feedback) | Direct | `IbpA⊣σ32`; L2 with FtsH⊣σ32 (translation vs degradation) |
| Giuliodori 2023, Front Microbiol | 10.3389/fmicb.2023.1118329 / 36846801 | CspA (b3556) | cold shock | temp downshift | CspA **activates** own translation (pos autoreg) | Direct | `CspA→cspA` + RNA thermometer; L2 |
| Gerken 2024, J Bacteriol | 10.1128/jb.00172-24 / 38809006 | OmpR (b3405), EnvZ (b3404), ompF (b0929) | osmotic/envelope | ompR/envZ alleles | impaired dephospho→OmpR~P↑→ompF **down** | Direct | `EnvZ→OmpR` / `EnvZ⊣OmpR~P` / `OmpR~P⊣ompF`; kinase vs phosphatase L2 |
| Bouillet 2024, PLoS Genet | 10.1371/journal.pgen.1011059 | RpoS (b2741), RssB (b3235), Crl (b0240) | stress recovery | recovery | RpoS→rssB↑ → RssB **promotes** RpoS degradation (neg feedback) | Direct | L3 neg-feedback loop (regulator drives own destruction) |
| Handler & Kirkpatrick 2024, Front Microbiol (review) | 10.3389/fmicb.2024.1363955 | RpoS; IraD/M/P/L; DsrA/RprA/ArcZ vs CyaR/OxyS/MgrR | multi-stress | various starvations | ≥3 stabilizing + ≥3 repressing inputs converge on RpoS | Review — medium | **L3 multi-input conflict scaffold** |
| Hamm 2024, mBio | 10.1128/mbio.03511-24 / 39727417 | polyP, (p)ppGpp (RelA b2784/SpoT b3650), FtsZ (b0095) | starvation/stringent | double loss | polyP+ppGpp **jointly** required for division; double-KO→mislocalized FtsZ | Direct (microscopy) | redundant edges→division; epistasis L2 (only double-KO fails) |
| Qi 2024, iScience | 10.1016/j.isci.2024.109579 / 38617560 | RelA (b2784), RpoS (b2741) | stringent+oxidative | bactericidal drugs | RelA-ppGpp & RpoS **promote** resistance via ROS mutagenesis | Direct (evolution) | cross-domain L3 stress→mutagenesis |
| Qi 2024, Int J Mol Sci | 10.3390/ijms25052582 / 38473832 | RelA, RpoS, ROS genes | fitness cost | ΔrelA, ROS-KOs | stringent/oxidative shape resistance fitness cost | Direct — med/strong | fitness-cost trade-off L2 |

## 4. Metabolism / carbon-source switch

| Paper | DOI/PMID | Entities | Condition | Perturbation | Effect & direction | Evidence | Map to simulator |
|---|---|---|---|---|---|---|---|
| Lin 2025, bioRxiv **(preprint)** | 10.1101/2025.11.14.688166 | CRP (b3357,P0ACJ8), LacI (b0345,P03023), lacZYA (b0344) | glucose→lactose diauxie | add cAMP; Δcrp | cAMP-CRP **represses** lacI (↓5×; ↑15× in Δcrp) AND directly activates lacZYA — coherent FFL | Direct (qPCR+footprint) — **preprint** | **Fix lac L2**: new `CRP→represses→lacI`; real glucose+lactose conflict |
| Wehrens 2023, Cell Reports | 10.1016/j.celrep.2023.113284 / 37864793 | cAMP-CRP (b3357) | single carbon | disable CRP feedback | CRP **buffers** catabolic expression to metabolic flux | Direct (single-cell) | cAMP-CRP as neg-feedback flux sensor |
| Zhao 2024, mBio | 10.1128/mbio.02430-24 | CRP, RelA (b2784,P0AG20), SpoT (b3650,P0AG24), rpsA (b0911), patZ (b3149) | glucose limitation | glucose depletion | CRP **activates** relA/spoT; ppGpp **inhibits** CRP (opposing loop) | Direct | **L2 opposing loop**: `CRP→relA/spoT`(+), `ppGpp⊣CRP`(−) |
| Gorelik 2024, J Bacteriol | 10.1128/jb.00354-23 / 38319100 | CsrA (b2696,P69913); evgA(b2369),gadE(b3512),gadA(b3517),gadB(b1493),ydeO(b1499) | growth vs acid trade-off | Δcsra | CsrA **represses** evgA/gadE/gadA/gadB/ydeO | Direct | New edges `CsrA⊣{acid genes}` |
| Simmons 2024, Nat Commun | 10.1038/s41467-024-52976-1 | CsrA (b2696), CsrB, CsrC | carbon storage | rewiring | CsrA **represses** GGA-motif targets; CsrB/C **sequester** CsrA | Direct (synthetic) | `CsrA⊣targets`, `CsrB/C⊣CsrA`; L2 antagonism |
| Papenfort & Storz 2024, Cell Chem Biol (review) | 10.1016/j.chembiol.2024.07.002 / 39094580 | Spot42 (spf), SpfP, CRP, SgrS, SgrT, ptsG (b1101,P69786) | glucose vs sugar-P stress | — | Spot42⊣TCA/alt-carbon; SpfP⊣CRP; SgrS⊣ptsG; SgrT⊣PtsG | Review — mod/strong | edges + L2 (glucose keeps Spot42 high vs CRP wants alt-carbon on) |
| Luke & Papenfort 2025, microLife | 10.1093/femsml/uqaf034 | Spot42, SpfP, CRP | non-preferred carbon | SpfP overexpression | SpfP **inhibits** CRP → ↓non-preferred catabolic genes | Review — mod | `SpfP⊣CRP` post-translational |
| Huang 2024, Appl Environ Microbiol | 10.1128/aem.01228-24 / 39494897 | Cra/FruR (b0080,P0ACP1); pfkA(b3916),pykF(b1676),ppsA(b1702),aceABK | glycolytic vs gluconeogenic | F1P binding | Cra **represses** glycolysis, **activates** gluconeogenesis; F1P releases Cra | Review — strong | **L2 one-regulator-both-signs**: `Cra⊣glycolysis`,`Cra→gluconeogenesis`,`F1P⊣Cra` |

---

## Caveats (carry into any KG/pattern edit)
- **Preprints** (Lin 2025 metabolism row): flag as not-yet-peer-reviewed; useful but lower evidence weight.
- **Non-K-12 strains**: Kijewski (EHEC), Chen (ATCC 25922) — directions are transferable but fold-changes are not MG1655 ground truth.
- **Omics/review rows** (Bajpe iModulons; Handler & Kirkpatrick; Papenfort; Huang): regulon/module-level, weaker than direct-experiment edges — use for clustering/weighting and pattern scaffolds, not as single hard edges.
- Several ideal mechanisms were **out of window** and dropped (e.g. StxS→rpoS 2020, SrsR/YgfI 2022); revisit if the date range widens.
- b-numbers/UniProt are standard annotations; verify against the KG canonical id set before inserting edges.

Source agents: 4 parallel domain researchers (gene-regulation / drug / stress /
metabolism), each with live web access; every citation fetched and confirmed.
