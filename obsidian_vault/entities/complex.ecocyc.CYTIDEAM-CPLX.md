---
entity_id: "complex.ecocyc.CYTIDEAM-CPLX"
entity_type: "complex"
name: "cytidine/deoxycytidine deaminase"
source_database: "EcoCyc"
source_id: "CYTIDEAM-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# cytidine/deoxycytidine deaminase

`complex.ecocyc.CYTIDEAM-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:CYTIDEAM-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0ABF6|protein.P0ABF6]]

## Enriched Summary

Cytidine deaminase catalyzes the hydrolytic deamination of CYTIDINE and DEOXYCYTIDINE to URIDINE and DEOXYURIDINE, respectively, in a thermodynamically favorable reaction. 2-deoxycytidine is a better substrate than cytidine . The products can undergo phosphorolysis to yield pentose derivatives. This allows cytidine to serve as a sole carbon source . Crystal structures of the enzyme have been solved, contributing to the understanding of the catalytic mechanism . Kinetic analysis showed a rapid-equilibrium random uni-bi mechanism . The catalytic mechanism of cytidine deaminase has been studied . The enzyme binds one atom of zinc per subunit ; the zinc-binding motif has been identified . Site-directed mutagenesis of the zinc-liganding cysteine residues results in loss of zinc and dramatic reduction in enzymatic activity . Expression of cdd is induced by cytosine and oleic acid . Expression is downregulated in an iscS mutant . In order to understand the role of natural selection in bacterial regulation, the cdd gene, among other genes, has undergone an analysis that compared the level of expression, plasticity, and noise of random versus segregating variants of many environmental isolates of E. coli, including E. coli MG1655...

## Biological Role

Catalyzes CYTIDEAM-RXN (reaction.ecocyc.CYTIDEAM-RXN), CYTIDEAM2-RXN (reaction.ecocyc.CYTIDEAM2-RXN). Bound by Zinc cation (molecule.C00038).

## Annotation

Cytidine deaminase catalyzes the hydrolytic deamination of CYTIDINE and DEOXYCYTIDINE to URIDINE and DEOXYURIDINE, respectively, in a thermodynamically favorable reaction. 2-deoxycytidine is a better substrate than cytidine . The products can undergo phosphorolysis to yield pentose derivatives. This allows cytidine to serve as a sole carbon source . Crystal structures of the enzyme have been solved, contributing to the understanding of the catalytic mechanism . Kinetic analysis showed a rapid-equilibrium random uni-bi mechanism . The catalytic mechanism of cytidine deaminase has been studied . The enzyme binds one atom of zinc per subunit ; the zinc-binding motif has been identified . Site-directed mutagenesis of the zinc-liganding cysteine residues results in loss of zinc and dramatic reduction in enzymatic activity . Expression of cdd is induced by cytosine and oleic acid . Expression is downregulated in an iscS mutant . In order to understand the role of natural selection in bacterial regulation, the cdd gene, among other genes, has undergone an analysis that compared the level of expression, plasticity, and noise of random versus segregating variants of many environmental isolates of E. coli, including E. coli MG1655 . Review:

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.CYTIDEAM-RXN|reaction.ecocyc.CYTIDEAM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.CYTIDEAM2-RXN|reaction.ecocyc.CYTIDEAM2-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0ABF6|protein.P0ABF6]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CYTIDEAM-CPLX`
- `QSPROTEOME:QS00207019`

## Notes

2*protein.P0ABF6
