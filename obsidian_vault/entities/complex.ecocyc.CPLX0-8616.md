---
entity_id: "complex.ecocyc.CPLX0-8616"
entity_type: "complex"
name: "murein tetrapeptide carboxypeptidase"
source_database: "EcoCyc"
source_id: "CPLX0-8616"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# murein tetrapeptide carboxypeptidase

`complex.ecocyc.CPLX0-8616`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8616`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76008|protein.P76008]]

## Enriched Summary

LdcA is an L,D-carboxypeptidase that has an essential function in murein (peptidoglycan) recycling/turnover . LdcA is a cytoplasmic enzyme which accepts monomeric muropeptides, free tetrapeptide and UDP-activated murein precursors, but not crosslinked muropeptides or murein as substrates . A later report showed that LdcA is able to hydrolyze crosslinked muropeptides to a certain extent . LdcA can discriminate between canonical murotetrapeptide with D-alanine and non-canonical murotetrapeptide with D-methionine, favoring the former . Crystal structures of wild type and the S106A predicted active site mutant of LdcA have been solved . A dithiazoline inhibitor of LdcA has been identified . An ldcA deletion mutant exhibits defects in murein recycling, including decreased peptidoglycan cross-linking. The mutation causes cell lysis at stationary phase . The mutant has decreased levels of UDP-MurNAc-pentapeptide and increased levels of UDP-MurNAc-tetrapeptide (a side product of EG12440-MONOMER Mpl activity) and the tetrapeptide L-Ala-γ-D-Glu-meso-A2pm-D-Ala . The toxicity caused by the ldcA deletion mutant is suppressed by loss of CPLX0-3970 . The Keio collection ldcA mutant is sensitive to lithium (ldcA increases susceptibility to trimethoprim . LdcA was found to be essential for resistance to the β-lactam ceftriaxone...

## Biological Role

Catalyzes RXN0-2061 (reaction.ecocyc.RXN0-2061), RXN0-5227 (reaction.ecocyc.RXN0-5227).

## Annotation

LdcA is an L,D-carboxypeptidase that has an essential function in murein (peptidoglycan) recycling/turnover . LdcA is a cytoplasmic enzyme which accepts monomeric muropeptides, free tetrapeptide and UDP-activated murein precursors, but not crosslinked muropeptides or murein as substrates . A later report showed that LdcA is able to hydrolyze crosslinked muropeptides to a certain extent . LdcA can discriminate between canonical murotetrapeptide with D-alanine and non-canonical murotetrapeptide with D-methionine, favoring the former . Crystal structures of wild type and the S106A predicted active site mutant of LdcA have been solved . A dithiazoline inhibitor of LdcA has been identified . An ldcA deletion mutant exhibits defects in murein recycling, including decreased peptidoglycan cross-linking. The mutation causes cell lysis at stationary phase . The mutant has decreased levels of UDP-MurNAc-pentapeptide and increased levels of UDP-MurNAc-tetrapeptide (a side product of EG12440-MONOMER Mpl activity) and the tetrapeptide L-Ala-γ-D-Glu-meso-A2pm-D-Ala . The toxicity caused by the ldcA deletion mutant is suppressed by loss of CPLX0-3970 . The Keio collection ldcA mutant is sensitive to lithium (ldcA increases susceptibility to trimethoprim . LdcA was found to be essential for resistance to the β-lactam ceftriaxone . ldcA belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 . LdcA: "L,D-carboxypeptidase A" . Review:

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-2061|reaction.ecocyc.RXN0-2061]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5227|reaction.ecocyc.RXN0-5227]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P76008|protein.P76008]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8616`
- `QSPROTEOME:QS00182727`

## Notes

2*protein.P76008
