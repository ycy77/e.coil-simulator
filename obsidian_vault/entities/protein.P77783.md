---
entity_id: "protein.P77783"
entity_type: "protein"
name: "ynfF"
source_database: "UniProt"
source_id: "P77783"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000250}; Peripheral membrane protein {ECO:0000250}; Cytoplasmic side {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ynfF b1588 JW5260"
---

# ynfF

`protein.P77783`

## Static

- Type: `protein`
- Source: `UniProt:P77783`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000250}; Peripheral membrane protein {ECO:0000250}; Cytoplasmic side {ECO:0000250}.

## Enriched Summary

FUNCTION: Terminal reductase during anaerobic growth on various sulfoxide and N-oxide compounds. {ECO:0000250}. YnfF has been implicated as a Tat-dependent selenate reductase enzyme in E.coli. A ynfEF double null mutant is unable to reduce selenate to elemental selenium . The disruption is specific to the initial selenate reduction process since selenium production is restored when selenite is added to the growth medium . Production of either YnfE or YnfF from a plasmid restored the ability of the E. coli ynfEF double mutant to reduce selenate to selenium in vivo . YnfF is highly similar to DmsA, the catalytic subunit of the dimethyl sulfoxide reductase heterotrimer, and cross-reacts with an anti-DmsA antibody. The protein is poorly expressed. When expressed together with DmsB and DmsC in a plasmid expression system, YnfF can form a complex with DmsB and DmsC, but the chimeric enzyme does not support growth on DMSO . The YnfF signal peptide can direct export through the twin arginine translocation (Tat) pathway and the general secretory pathway (Sec) pathway . YnfF is a predicted molybdoenzyme; deletion of ynfF does not confer a 6-N-hydroxylaminopurine (HAP)-sensitive phenotype .

## Biological Role

Component of selenate reductase (complex.ecocyc.CPLX0-1601).

## Enriched Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Annotation

FUNCTION: Terminal reductase during anaerobic growth on various sulfoxide and N-oxide compounds. {ECO:0000250}.

## Pathways

- `eco00450` Selenocompound metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1601|complex.ecocyc.CPLX0-1601]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1588|gene.b1588]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77783`
- `KEGG:ecj:JW5260;eco:b1588;`
- `GeneID:75171646;945268;`
- `GO:GO:0005886; GO:0009055; GO:0009061; GO:0009389; GO:0030151; GO:0030288; GO:0033797; GO:0043546; GO:0051539; GO:1990204`
- `EC:1.8.99.-`

## Notes

Probable dimethyl sulfoxide reductase chain YnfF (DMSO reductase) (EC 1.8.99.-)
