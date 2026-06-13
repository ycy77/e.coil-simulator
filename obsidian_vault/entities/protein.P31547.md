---
entity_id: "protein.P31547"
entity_type: "protein"
name: "metI"
source_database: "UniProt"
source_id: "P31547"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000305|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "metI yaeE b0198 JW0194"
---

# metI

`protein.P31547`

## Static

- Type: `protein`
- Source: `UniProt:P31547`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000305|PubMed:15919996}.

## Enriched Summary

FUNCTION: Part of the binding-protein-dependent transport system for D-methionine and the toxic methionine analog alpha-methyl-methionine. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:12169620}.; FUNCTION: (Microbial infection) Probably transports the toxic C-terminal region of CdiA from E.coli strain MHI813 across the inner membrane to the cytoplasm, where CdiA has a toxic effect. Toxin transport is strain-specific, mutations in this gene do not confer resistance to several other tested CdiA toxins. {ECO:0000269|PubMed:26305955}. MetI is the integral membrane subunit of a high affinity methionine ABC transporter. Purified, crystallized MetNI contains two copies of MetI; the MetI monomer contains 5 transmembrane regions with its N-terminus located in the periplasm and the C-terminus located in the cytoplasm MetI has been implicated in the import of specific toxins of contact-dependent growth inhibition (CDI) systems in gram-negative bacteria; metI transposon insertion mutants and metI in-frame deletion mutants are resistant to the CdiA-CTMHI813 toxin; inner membrane proteins such as MetI are thought to act as receptors which bring the nuclease domain of CDI toxins into close proximity with the inner membrane of target cells .

## Biological Role

Component of L-methionine/D-methionine ABC transporter (complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the binding-protein-dependent transport system for D-methionine and the toxic methionine analog alpha-methyl-methionine. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:12169620}.; FUNCTION: (Microbial infection) Probably transports the toxic C-terminal region of CdiA from E.coli strain MHI813 across the inner membrane to the cytoplasm, where CdiA has a toxic effect. Toxin transport is strain-specific, mutations in this gene do not confer resistance to several other tested CdiA toxins. {ECO:0000269|PubMed:26305955}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX|complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0198|gene.b0198]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31547`
- `KEGG:ecj:JW0194;eco:b0198;ecoc:C3026_00920;`
- `GeneID:86862709;944894;`
- `GO:GO:0005886; GO:0015191; GO:0015821; GO:0016020; GO:0033232; GO:0048473; GO:0055052; GO:1903692; GO:1990197`

## Notes

D-methionine transport system permease protein MetI
