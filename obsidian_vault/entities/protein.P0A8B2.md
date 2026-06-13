---
entity_id: "protein.P0A8B2"
entity_type: "protein"
name: "smrB"
source_database: "UniProt"
source_id: "P0A8B2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "smrB yfcN b2331 JW2328"
---

# smrB

`protein.P0A8B2`

## Static

- Type: `protein`
- Source: `UniProt:P0A8B2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Acts as a ribosome collision sensor (PubMed:35264790). Detects stalled/collided disomes (pairs of ribosomes where the leading ribosome is stalled and a second ribosome has collided with it) and endonucleolytically cleaves mRNA at the 5' boundary of the stalled ribosome (PubMed:35264790). Stalled/collided disomes form a new interface (primarily via the 30S subunits) that binds SmrB (PubMed:35264790). Cleaved mRNA becomes available for tmRNA ligation, leading to ribosomal subunit dissociation and rescue of stalled ribosomes (PubMed:35264790). {ECO:0000255|HAMAP-Rule:MF_01042, ECO:0000269|PubMed:35264790}. Ribosome rescue factor SmrB recognizes and acts on collided ribosomes; SmrB cleaves mRNAs upstream of stalled ribosomes and triggers SSRA-RNA-mediated ribosome rescue . smrB insertion mutations allow ribosomes to translate through a strong stalling motif; ΔsmrB cells are hypersensitive to erythromycin, an antibiotic that stalls elongating ribosomes at specific sequences . SmrB contains a small mutS-related (SMR) domain with motifs implicated in catalysis and RNA binding . Cryo-EM structures of nuclease-deficient SmrB on collided disomes are available; SmrB binds at the interface of the two ribosomes and its precise positioning likely activates catalytic activity . smr: small mutS-related (see )

## Annotation

FUNCTION: Acts as a ribosome collision sensor (PubMed:35264790). Detects stalled/collided disomes (pairs of ribosomes where the leading ribosome is stalled and a second ribosome has collided with it) and endonucleolytically cleaves mRNA at the 5' boundary of the stalled ribosome (PubMed:35264790). Stalled/collided disomes form a new interface (primarily via the 30S subunits) that binds SmrB (PubMed:35264790). Cleaved mRNA becomes available for tmRNA ligation, leading to ribosomal subunit dissociation and rescue of stalled ribosomes (PubMed:35264790). {ECO:0000255|HAMAP-Rule:MF_01042, ECO:0000269|PubMed:35264790}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b2331|gene.b2331]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8B2`
- `KEGG:ecj:JW2328;eco:b2331;ecoc:C3026_12985;`
- `GeneID:93774844;944847;`
- `GO:GO:0004521; GO:0016787; GO:0019843; GO:0072344`
- `EC:3.1.-.-`

## Notes

Ribosome rescue factor SmrB (EC 3.1.-.-)
