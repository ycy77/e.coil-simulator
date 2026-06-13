---
entity_id: "complex.ecocyc.CPLX0-8545"
entity_type: "complex"
name: "peptidoglycan DD endopeptidase DacB"
source_database: "EcoCyc"
source_id: "CPLX0-8545"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# peptidoglycan DD endopeptidase DacB

`complex.ecocyc.CPLX0-8545`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8545`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P24228|protein.P24228]]

## Enriched Summary

dacB encodes penicillin binding protein 4 (PBP4), a bifunctional, penicillin-sensitive protein with peptidoglycan DD-endopeptidase and DD-carboxypeptidase activity. Early studies characterizing dacB mutants and PBP4 include: . PBP4 is synthesized as a pre-protein; a signal peptide of 20 amino acids is cleaved . The majority of overexpressed PBP4 is found in the soluble fraction of a cell free extract but it can also be detected in, and isolated from, the membrane fraction ; PBP4 (from both fractions) binds penicillin G (see also ). Purified PBP4 has DD-endopeptidase activity, catalysing the hydrolysis of D-Ala-meso-A2pm peptide bonds in the cross-bridge of isolated dimeric muropeptides in vitro . Analysis of the murein from a PBP4 overexpressing strain suggests that PBP4 has DD-endopeptidase and DD-carboxypeptidase activity in vivo but does not catalyse a DD-transpeptidation reaction . X-ray crystal structures of the apoprotein and of PDP4 complexed to 5 different antibiotics have been reported - in these latter structures Ser-62 is covalently linked to the antibiotic by an ester linkage ; purified PDP4 is dimeric in solution . PBP4 contains two putative disulphide cross-links (see also ). dacB mutants are viable as are dacA dacB double mutants and dacA dacB dacC dacD quadruple mutants (see also )...

## Biological Role

Catalyzes RXN-16649 (reaction.ecocyc.RXN-16649), RXN0-3461 (reaction.ecocyc.RXN0-3461).

## Annotation

dacB encodes penicillin binding protein 4 (PBP4), a bifunctional, penicillin-sensitive protein with peptidoglycan DD-endopeptidase and DD-carboxypeptidase activity. Early studies characterizing dacB mutants and PBP4 include: . PBP4 is synthesized as a pre-protein; a signal peptide of 20 amino acids is cleaved . The majority of overexpressed PBP4 is found in the soluble fraction of a cell free extract but it can also be detected in, and isolated from, the membrane fraction ; PBP4 (from both fractions) binds penicillin G (see also ). Purified PBP4 has DD-endopeptidase activity, catalysing the hydrolysis of D-Ala-meso-A2pm peptide bonds in the cross-bridge of isolated dimeric muropeptides in vitro . Analysis of the murein from a PBP4 overexpressing strain suggests that PBP4 has DD-endopeptidase and DD-carboxypeptidase activity in vivo but does not catalyse a DD-transpeptidation reaction . X-ray crystal structures of the apoprotein and of PDP4 complexed to 5 different antibiotics have been reported - in these latter structures Ser-62 is covalently linked to the antibiotic by an ester linkage ; purified PDP4 is dimeric in solution . PBP4 contains two putative disulphide cross-links (see also ). dacB mutants are viable as are dacA dacB double mutants and dacA dacB dacC dacD quadruple mutants (see also ). PBP4 is lytic when overexpressed early in the growth phase but has less effect as cells approach stationary phase; expression of cloned PBP4 does not complement the morphological defects associated with loss of the major DD-carboxypeptidase, CPLX0-8252 PBP5 (see also ). PBP4 activity has been implicated in cell separation; deletion of PBP4 is associated with an increase in the chaining phenotype of amiC deletion mutants (see also ). PBP4 is a class C low molecular mass penici

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-16649|reaction.ecocyc.RXN-16649]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-3461|reaction.ecocyc.RXN0-3461]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P24228|protein.P24228]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8545`
- `QSPROTEOME:QS00196471`

## Notes

2*protein.P24228
