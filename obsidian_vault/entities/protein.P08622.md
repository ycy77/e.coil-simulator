---
entity_id: "protein.P08622"
entity_type: "protein"
name: "dnaJ"
source_database: "UniProt"
source_id: "P08622"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dnaJ groP b0015 JW0014"
---

# dnaJ

`protein.P08622`

## Static

- Type: `protein`
- Source: `UniProt:P08622`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Interacts with DnaK and GrpE to disassemble a protein complex at the origins of replication of phage lambda and several plasmids. Participates actively in the response to hyperosmotic and heat shock by preventing the aggregation of stress-denatured proteins and by disaggregating proteins, also in an autonomous, DnaK-independent fashion. Unfolded proteins bind initially to DnaJ; upon interaction with the DnaJ-bound protein, DnaK hydrolyzes its bound ATP, resulting in the formation of a stable complex. GrpE releases ADP from DnaK; ATP binding to DnaK triggers the release of the substrate protein, thus completing the reaction cycle. Several rounds of ATP-dependent interactions between DnaJ, DnaK and GrpE are required for fully efficient folding. {ECO:0000269|PubMed:15044009, ECO:0000269|PubMed:15302880, ECO:0000269|PubMed:15485812, ECO:0000269|PubMed:1826368}.

## Biological Role

Component of chaperone protein DnaJ (complex.ecocyc.CPLX0-8191).

## Annotation

FUNCTION: Interacts with DnaK and GrpE to disassemble a protein complex at the origins of replication of phage lambda and several plasmids. Participates actively in the response to hyperosmotic and heat shock by preventing the aggregation of stress-denatured proteins and by disaggregating proteins, also in an autonomous, DnaK-independent fashion. Unfolded proteins bind initially to DnaJ; upon interaction with the DnaJ-bound protein, DnaK hydrolyzes its bound ATP, resulting in the formation of a stable complex. GrpE releases ADP from DnaK; ATP binding to DnaK triggers the release of the substrate protein, thus completing the reaction cycle. Several rounds of ATP-dependent interactions between DnaJ, DnaK and GrpE are required for fully efficient folding. {ECO:0000269|PubMed:15044009, ECO:0000269|PubMed:15302880, ECO:0000269|PubMed:15485812, ECO:0000269|PubMed:1826368}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8191|complex.ecocyc.CPLX0-8191]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0015|gene.b0015]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08622`
- `KEGG:ecj:JW0014;eco:b0015;ecoc:C3026_00075;`
- `GeneID:944753;`
- `GO:GO:0003756; GO:0005524; GO:0005737; GO:0005829; GO:0006260; GO:0006457; GO:0008270; GO:0009408; GO:0015035; GO:0016020; GO:0016032; GO:0016989; GO:0031072; GO:0032991; GO:0042026; GO:0042803; GO:0043335; GO:0051082; GO:0051087; GO:0065003`

## Notes

Chaperone protein DnaJ (HSP40) (Heat shock protein J)
