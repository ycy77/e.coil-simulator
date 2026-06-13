---
entity_id: "protein.P0A6U5"
entity_type: "protein"
name: "rsmG"
source_database: "UniProt"
source_id: "P0A6U5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00074}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rsmG gidB b3740 JW3718"
---

# rsmG

`protein.P0A6U5`

## Static

- Type: `protein`
- Source: `UniProt:P0A6U5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00074}.

## Enriched Summary

FUNCTION: Specifically methylates the N7 position of guanine in position 527 of 16S rRNA. Requires the intact 30S subunit for methylation. {ECO:0000255|HAMAP-Rule:MF_00074, ECO:0000269|PubMed:17238915}. RsmG is the methyltransferase responsible for methylation of 16S rRNA at the N7 position of the G527 nucleotide. In vitro, the enzyme is able to methylate 16S rRNA within the 30S ribosomal subunit, but not naked 16S rRNA . RsmG is highly conserved in Gram-negative as well as Gram-positive bacteria . A crystal structure of RsmG has been solved at 2.4 Å resolution . Amino acids that are important for catalytic activity of RsmG were identified by site-directed mutagenesis of conserved residues . An rsmG mutation has no apparent growth defect and confers low-level resistance to streptomycin. rsmG mutations are found at high frequency in streptomycin-resistant clinical isolates of Mycobacterium tuberculosis . GidB: "glucose-inhibited division" RsmG: "rRNA small subunit methyltransferase G" Review:

## Biological Role

Catalyzes RXN-11578 (reaction.ecocyc.RXN-11578).

## Annotation

FUNCTION: Specifically methylates the N7 position of guanine in position 527 of 16S rRNA. Requires the intact 30S subunit for methylation. {ECO:0000255|HAMAP-Rule:MF_00074, ECO:0000269|PubMed:17238915}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11578|reaction.ecocyc.RXN-11578]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3740|gene.b3740]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6U5`
- `KEGG:ecj:JW3718;eco:b3740;ecoc:C3026_20265;`
- `GeneID:93778227;948250;`
- `GO:GO:0005829; GO:0070043; GO:0070475`
- `EC:2.1.1.170`

## Notes

Ribosomal RNA small subunit methyltransferase G (EC 2.1.1.170) (16S rRNA 7-methylguanosine methyltransferase) (16S rRNA m7G methyltransferase) (Glucose-inhibited division protein B)
