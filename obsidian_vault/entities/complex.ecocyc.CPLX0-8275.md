---
entity_id: "complex.ecocyc.CPLX0-8275"
entity_type: "complex"
name: "histidine kinase GlrK"
source_database: "EcoCyc"
source_id: "CPLX0-8275"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# histidine kinase GlrK

`complex.ecocyc.CPLX0-8275`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8275`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P52101|protein.P52101]]

## Enriched Summary

GlrK is the histidine kinase of the GlrKR signal transduction system which, together with the multifunctional RNA binding protein CPLX0-7998 "RapZ" and the small RNAs TKE1-RNA "GlmY" and SRAJ-RNA "GlmZ" (see ), forms a regulatory circuit that ensures glucosamine-6-phosphate homeostasis and envelope integrity . GlrK is an 'orthodox' histidine kinase; it consists of a periplasmic input domain located between two transmembrane domains and a cytoplasmic 'transmitter' region which contains a dimerization and histidine phosphotransfer (DHp) domain containing the histidine site of phosphorylation (His-259) and a catalytic and ATP binding (CA) domain (see ). Purified, soluble GlrK self-phosphorylates in the presence of ATP; phosphorylated GlrK transphosphorylates its cognate response regulator, GlrR, in vitro . The outer membrane lipoprotein EG12139-MONOMER "QseG" interacts physically with dimeric GlrK in vivo; GlrK and QseG are both required for efficient phosphorylation of aspartate-56 in the GlrR response regulator; a single substitution mutation (S58N) in GlrK impairs the physical interaction between QseG and GlrK and results in a 3-fold decrease in glmY expression...

## Biological Role

Catalyzes 2.7.13.3-RXN (reaction.ecocyc.2.7.13.3-RXN).

## Annotation

GlrK is the histidine kinase of the GlrKR signal transduction system which, together with the multifunctional RNA binding protein CPLX0-7998 "RapZ" and the small RNAs TKE1-RNA "GlmY" and SRAJ-RNA "GlmZ" (see ), forms a regulatory circuit that ensures glucosamine-6-phosphate homeostasis and envelope integrity . GlrK is an 'orthodox' histidine kinase; it consists of a periplasmic input domain located between two transmembrane domains and a cytoplasmic 'transmitter' region which contains a dimerization and histidine phosphotransfer (DHp) domain containing the histidine site of phosphorylation (His-259) and a catalytic and ATP binding (CA) domain (see ). Purified, soluble GlrK self-phosphorylates in the presence of ATP; phosphorylated GlrK transphosphorylates its cognate response regulator, GlrR, in vitro . The outer membrane lipoprotein EG12139-MONOMER "QseG" interacts physically with dimeric GlrK in vivo; GlrK and QseG are both required for efficient phosphorylation of aspartate-56 in the GlrR response regulator; a single substitution mutation (S58N) in GlrK impairs the physical interaction between QseG and GlrK and results in a 3-fold decrease in glmY expression . L-EPINEPHRINE "Epinephrine" induces moderate stimulation of GlrR phosphorylation and increased glmY expression in the stationary growth phase; GlrK and QseG are required for this effect suggesting that epinephrine may stimulate GlrK autophosphorylation in a QseG-dependent manner . The RNA binding protein RapZ interacts transiently and independently, with both GlrK and GlrR; when glucosamine-6-phosphate is depleted, RapZ stimulates autophosphorylation of GlrK and subsequent activation of the response regulator, GlrR . GlrK: "glmY-regulating kinase"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.3-RXN|reaction.ecocyc.2.7.13.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P52101|protein.P52101]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8275`
- `QSPROTEOME:QS00199585`

## Notes

2*protein.P52101
