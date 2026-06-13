---
entity_id: "protein.P0A8R0"
entity_type: "protein"
name: "rraA"
source_database: "UniProt"
source_id: "P0A8R0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rraA menG yiiV b3929 JW3900"
---

# rraA

`protein.P0A8R0`

## Static

- Type: `protein`
- Source: `UniProt:P0A8R0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Globally modulates RNA abundance by binding to RNase E (Rne) and regulating its endonucleolytic activity. Can modulate Rne action in a substrate-dependent manner by altering the composition of the degradosome. Modulates RNA-binding and helicase activities of the degradosome. {ECO:0000269|PubMed:13678585, ECO:0000269|PubMed:16725107, ECO:0000269|PubMed:16771842, ECO:0000269|PubMed:18510556, ECO:0000269|PubMed:20106955}. RraA inhibits CPLX0-3461 activity by binding to and masking the C-terminal RNA binding domain of RNase E. The interaction of RraA with the degradosome is facilitated by protein-RNA remodeling via the ATPase activity of RhlB . RraA physically interacts with RNase E, but does not interact with the RNA substrates . High-affinity binding of RraA to RNase E requires the C-terminal domain (CTD) of RNase E . RraA interacts with both RNA-binding sites of RNase E and interferes with their interaction with RNA . RraA also interacts with the RhlB helicase component of the degradosome, and a ternary complex of RraA, RNase E and RhlB can be observed . Binding of RraA or RraB, a second modulator of RNase E activity, differently affect the composition of the degradosome . RraA also interacts with the DEAD-box protein SrmB and modulates its RNA-dependent ATPase activity...

## Biological Role

Component of ribonuclease E inhibitor protein A (complex.ecocyc.CPLX0-1642).

## Annotation

FUNCTION: Globally modulates RNA abundance by binding to RNase E (Rne) and regulating its endonucleolytic activity. Can modulate Rne action in a substrate-dependent manner by altering the composition of the degradosome. Modulates RNA-binding and helicase activities of the degradosome. {ECO:0000269|PubMed:13678585, ECO:0000269|PubMed:16725107, ECO:0000269|PubMed:16771842, ECO:0000269|PubMed:18510556, ECO:0000269|PubMed:20106955}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1642|complex.ecocyc.CPLX0-1642]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b3929|gene.b3929]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8R0`
- `KEGG:ecj:JW3900;eco:b3929;ecoc:C3026_21235;`
- `GeneID:86944458;93777969;948419;`
- `GO:GO:0005829; GO:0008428; GO:0019899; GO:0032991; GO:0042802; GO:0060698; GO:0070207; GO:1902369`

## Notes

Regulator of ribonuclease activity A
