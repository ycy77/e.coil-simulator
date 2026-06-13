---
entity_id: "protein.P75782"
entity_type: "protein"
name: "rlmF"
source_database: "UniProt"
source_id: "P75782"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:18021804}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rlmF ybiN b0807 JW5107"
---

# rlmF

`protein.P75782`

## Static

- Type: `protein`
- Source: `UniProt:P75782`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:18021804}.

## Enriched Summary

FUNCTION: Specifically methylates the adenine in position 1618 of 23S rRNA. {ECO:0000269|PubMed:18021804}. RlmF is the methyltransferase responsible for methylation of 23S rRNA at the N6 position of the A1618 nucleotide . In vitro, RlmF can methylate A1618 in LiCl ribosomal core particles (a model for early ribosomal assembly intermediates), but not in protein-free 23S rRNA or more fully assembled ribosomal particles . RlmF is most similar to several m2G methyltransferases and was thus expected to confer m2G1516 methyltransferase activity . Predicted catalytic residues and a predicted reaction mechanism are discussed . Both an rlmF null mutant and a strain overexpressing rlmF show a growth defect . RlmF: "rRNA large subunit methyltransferase F"

## Biological Role

Catalyzes RXN-11596 (reaction.ecocyc.RXN-11596).

## Annotation

FUNCTION: Specifically methylates the adenine in position 1618 of 23S rRNA. {ECO:0000269|PubMed:18021804}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11596|reaction.ecocyc.RXN-11596]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0807|gene.b0807]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75782`
- `KEGG:ecj:JW5107;eco:b0807;ecoc:C3026_05085;`
- `GeneID:944938;`
- `GO:GO:0005737; GO:0052907; GO:0070475`
- `EC:2.1.1.181`

## Notes

Ribosomal RNA large subunit methyltransferase F (EC 2.1.1.181) (23S rRNA mA1618 methyltransferase) (rRNA adenine N-6-methyltransferase)
