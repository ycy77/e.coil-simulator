---
entity_id: "protein.P75876"
entity_type: "protein"
name: "rlmI"
source_database: "UniProt"
source_id: "P75876"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rlmI yccW b0967 JW5898"
---

# rlmI

`protein.P75876`

## Static

- Type: `protein`
- Source: `UniProt:P75876`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Specifically methylates the cytosine at position 1962 (m5C1962) of 23S rRNA. Methylation occurs before assembly of 23S rRNA into 50S subunits. {ECO:0000269|PubMed:18786544}. RlmI is the methyltransferase responsible for methylation of 23S rRNA at the C5 position of the C1962 nucleotide. The enzyme can methylate naked 23S rRNA, but not assembled 50S ribosomal subunits or 70S ribosomes . A crystal structure of RlmI has been solved at 2 Å resolution; domain organization and possible evolutionary relationships of the enzyme are discussed . A mutant with a deletion of rlmI shows a significant decrease in biofilm formation . However, an rlmI mutant shows only a slight growth defect compared to wild-type cells during competitive growth experiments in rich or minimal medium . Expression of rlmI increases 17-fold upon deletion of tqsA, which increases biofilm formation . RlmI: "rRNA large subunit methyltransferase I" Review:

## Biological Role

Component of 23S rRNA m5C1962 methyltransferase (complex.ecocyc.CPLX0-7726).

## Annotation

FUNCTION: Specifically methylates the cytosine at position 1962 (m5C1962) of 23S rRNA. Methylation occurs before assembly of 23S rRNA into 50S subunits. {ECO:0000269|PubMed:18786544}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7726|complex.ecocyc.CPLX0-7726]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0967|gene.b0967]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75876`
- `KEGG:ecj:JW5898;eco:b0967;ecoc:C3026_05910;`
- `GeneID:946691;`
- `GO:GO:0003723; GO:0005737; GO:0005829; GO:0009383; GO:0016434; GO:0031167; GO:0042803; GO:0044010; GO:0070475`
- `EC:2.1.1.191`

## Notes

Ribosomal RNA large subunit methyltransferase I (EC 2.1.1.191) (23S rRNA m5C1962 methyltransferase) (rRNA (cytosine-C(5)-)-methyltransferase RlmI)
