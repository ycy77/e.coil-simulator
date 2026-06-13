---
entity_id: "protein.P09372"
entity_type: "protein"
name: "grpE"
source_database: "UniProt"
source_id: "P09372"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "grpE b2614 JW2594"
---

# grpE

`protein.P09372`

## Static

- Type: `protein`
- Source: `UniProt:P09372`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Participates actively in the response to hyperosmotic and heat shock by preventing the aggregation of stress-denatured proteins, in association with DnaK and GrpE. It is the nucleotide exchange factor for DnaK and may function as a thermosensor. Unfolded proteins bind initially to DnaJ; upon interaction with the DnaJ-bound protein, DnaK hydrolyzes its bound ATP, resulting in the formation of a stable complex. GrpE releases ADP from DnaK; ATP binding to DnaK triggers the release of the substrate protein, thus completing the reaction cycle. Several rounds of ATP-dependent interactions between DnaJ, DnaK and GrpE are required for fully efficient folding. {ECO:0000269|PubMed:15102842, ECO:0000269|PubMed:8890154}.

## Biological Role

Component of nucleotide exchange factor GrpE (complex.ecocyc.CPLX0-8192).

## Annotation

FUNCTION: Participates actively in the response to hyperosmotic and heat shock by preventing the aggregation of stress-denatured proteins, in association with DnaK and GrpE. It is the nucleotide exchange factor for DnaK and may function as a thermosensor. Unfolded proteins bind initially to DnaJ; upon interaction with the DnaJ-bound protein, DnaK hydrolyzes its bound ATP, resulting in the formation of a stable complex. GrpE releases ADP from DnaK; ATP binding to DnaK triggers the release of the substrate protein, thus completing the reaction cycle. Several rounds of ATP-dependent interactions between DnaJ, DnaK and GrpE are required for fully efficient folding. {ECO:0000269|PubMed:15102842, ECO:0000269|PubMed:8890154}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8192|complex.ecocyc.CPLX0-8192]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2614|gene.b2614]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09372`
- `KEGG:ecj:JW2594;eco:b2614;ecoc:C3026_14465;`
- `GeneID:947097;`
- `GO:GO:0000774; GO:0005737; GO:0005829; GO:0006457; GO:0009408; GO:0019904; GO:0032991; GO:0042803; GO:0043335; GO:0051082; GO:0051087; GO:0065003`

## Notes

Protein GrpE (HSP-70 cofactor) (HSP24) (Heat shock protein B25.3)
