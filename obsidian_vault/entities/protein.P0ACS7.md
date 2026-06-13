---
entity_id: "protein.P0ACS7"
entity_type: "protein"
name: "rpiR"
source_database: "UniProt"
source_id: "P0ACS7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpiR alsR yjcY b4089 JW4050"
---

# rpiR

`protein.P0ACS7`

## Static

- Type: `protein`
- Source: `UniProt:P0ACS7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Regulatory protein involved in rpiB gene repression. Also involved in als operon repression. {ECO:0000269|PubMed:9401019}. "Allose utilization regulator," AlsR, negatively controls the expression of genes involved in transport and catabolism of D-allose and low-affinity transport of D-ribose . It is negatively autoregulated and coordinately represses transcription of the divergent gene rpiB, encoding an enzyme in the pentose pathway . Synthesis of alsR and rpiB genes is induced when Escherichia coli is grown on D-allose in the absence of glucose. Gene induction occurs when the physiological inducer, D-allose, binds to AlsR, liberating the repression effect caused by this protein . As a member of the RpiR/YebK/YfhH family of transcriptional regulators, AlsR features an N-terminal domain containing a helix-turn-helix motif . Currently, no DNA-binding sites for this regulator have been reported in the literature.

## Biological Role

Component of AlsR-D-allose (complex.ecocyc.MONOMER0-2482).

## Annotation

FUNCTION: Regulatory protein involved in rpiB gene repression. Also involved in als operon repression. {ECO:0000269|PubMed:9401019}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-2482|complex.ecocyc.MONOMER0-2482]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b4089|gene.b4089]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACS7`
- `KEGG:ecj:JW4050;eco:b4089;ecoc:C3026_22105;`
- `GeneID:948603;`
- `GO:GO:0003677; GO:0003700; GO:0006355; GO:0045892; GO:0097367; GO:1901135`

## Notes

HTH-type transcriptional regulator RpiR (Als operon repressor)
