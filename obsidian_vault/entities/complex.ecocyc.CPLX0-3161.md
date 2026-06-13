---
entity_id: "complex.ecocyc.CPLX0-3161"
entity_type: "complex"
name: "succinyl-diaminopimelate desuccinylase"
source_database: "EcoCyc"
source_id: "CPLX0-3161"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# succinyl-diaminopimelate desuccinylase

`complex.ecocyc.CPLX0-3161`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3161`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AED7|protein.P0AED7]]

## Enriched Summary

The E. coli N-succinyl-L-diaminopimelate desuccinylase (DapE) catalyzes the deacylation of succinyl-diaminopimelate, forming the diaminopimelate intermediate in the DAPLYSINESYN-PWY pathway. The enzyme is highly specific for its natural substrate . DapE is also a component of the divisome; by interacting with ZapB, it localizes to midcell and may enhance the Ter signal, thereby promoting functional Z ring formation . The enzyme exists as a mixture of homodimers and homotetramers in solution and requires either Co(II) or Zn(II) for activity . The dapE gene bears similarity to argE, acetylornithine deacetylase . dapE is a multicopy suppressor of ftsP and ftsEX mutant phenotypes and is a multicopy suppressor of the cell division defect at 30°C of a Δmin ΔslmA double mutant . Expression of a DapE E134A mutant can not substitute for wild-type DapE, but can function as a multicopy suppressor for the Δmin ΔslmA and ΔftsEX mutants, indicating that DapE's enzymatic activity is not required for its function in cell division . A ΔdapE mutation exacerbates the growth defect of the temperature-sensitive ftsZ84 and ftsA12 alleles . MsgB: "multicopy suppressor of grpE280" The E. coli N-succinyl-L-diaminopimelate desuccinylase (DapE) catalyzes the deacylation of succinyl-diaminopimelate, forming the diaminopimelate intermediate in the DAPLYSINESYN-PWY pathway...

## Biological Role

Catalyzes SUCCDIAMINOPIMDESUCC-RXN (reaction.ecocyc.SUCCDIAMINOPIMDESUCC-RXN). Bound by Zinc cation (molecule.C00038), Cobalt ion (molecule.C00175).

## Annotation

The E. coli N-succinyl-L-diaminopimelate desuccinylase (DapE) catalyzes the deacylation of succinyl-diaminopimelate, forming the diaminopimelate intermediate in the DAPLYSINESYN-PWY pathway. The enzyme is highly specific for its natural substrate . DapE is also a component of the divisome; by interacting with ZapB, it localizes to midcell and may enhance the Ter signal, thereby promoting functional Z ring formation . The enzyme exists as a mixture of homodimers and homotetramers in solution and requires either Co(II) or Zn(II) for activity . The dapE gene bears similarity to argE, acetylornithine deacetylase . dapE is a multicopy suppressor of ftsP and ftsEX mutant phenotypes and is a multicopy suppressor of the cell division defect at 30°C of a Δmin ΔslmA double mutant . Expression of a DapE E134A mutant can not substitute for wild-type DapE, but can function as a multicopy suppressor for the Δmin ΔslmA and ΔftsEX mutants, indicating that DapE's enzymatic activity is not required for its function in cell division . A ΔdapE mutation exacerbates the growth defect of the temperature-sensitive ftsZ84 and ftsA12 alleles . MsgB: "multicopy suppressor of grpE280"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.SUCCDIAMINOPIMDESUCC-RXN|reaction.ecocyc.SUCCDIAMINOPIMDESUCC-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AED7|protein.P0AED7]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3161`
- `QSPROTEOME:QS00200443`

## Notes

2*protein.P0AED7
