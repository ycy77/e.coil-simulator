---
entity_id: "protein.P0AGI1"
entity_type: "protein"
name: "rbsC"
source_database: "UniProt"
source_id: "P0AGI1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:9922273}; Multi-pass membrane protein {ECO:0000305|PubMed:9922273}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rbsC b3750 JW3729"
---

# rbsC

`protein.P0AGI1`

## Static

- Type: `protein`
- Source: `UniProt:P0AGI1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:9922273}; Multi-pass membrane protein {ECO:0000305|PubMed:9922273}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex RbsABC involved in ribose import. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:25533465, ECO:0000269|PubMed:6327617}.; FUNCTION: (Microbial infection) Probably transports the toxic C-terminal region of CdiA from D.dadantii strain 3937 across the inner membrane to the cytoplasm, where CdiA has a toxic effect. Toxin transport is strain-specific, mutations in this gene do not confer resistance to several other tested CdiA toxins. {ECO:0000269|PubMed:26305955}. RbsC is predicted to be the inner membrane subunit of an ATP-dependent ribose uptake system . Topology analysis suggests that it contains 6 transmembrane regions with the N and C-termini located in the cytoplasm . RbsC has been implicated in the import of specific toxins of contact-dependent growth inhibition (CDI) systems in gram-negative bacteria; rbsC transposon insertion mutants and rbsC in-frame deletion mutants are resistant to the CdiA-CT1Dd3937 toxin; inner membrane proteins such as RbsC are thought to act as receptors which bring the nuclease domain of CDI toxins into close proximity with the inner membrane of target cells .

## Biological Role

Component of ribose ABC transporter (complex.ecocyc.ABC-28-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex RbsABC involved in ribose import. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:25533465, ECO:0000269|PubMed:6327617}.; FUNCTION: (Microbial infection) Probably transports the toxic C-terminal region of CdiA from D.dadantii strain 3937 across the inner membrane to the cytoplasm, where CdiA has a toxic effect. Toxin transport is strain-specific, mutations in this gene do not confer resistance to several other tested CdiA toxins. {ECO:0000269|PubMed:26305955}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-28-CPLX|complex.ecocyc.ABC-28-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3750|gene.b3750]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGI1`
- `KEGG:ecj:JW3729;eco:b3750;ecoc:C3026_20315;`
- `GeneID:86861858;93778199;948262;`
- `GO:GO:0005886; GO:0015591; GO:0015752; GO:0016020; GO:0043190; GO:0055052`

## Notes

Ribose import permease protein RbsC
