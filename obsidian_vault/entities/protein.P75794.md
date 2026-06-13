---
entity_id: "protein.P75794"
entity_type: "protein"
name: "ybiY"
source_database: "UniProt"
source_id: "P75794"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybiY b0824 JW0808"
---

# ybiY

`protein.P75794`

## Static

- Type: `protein`
- Source: `UniProt:P75794`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Activation of pyruvate formate-lyase 2 under anaerobic conditions by generation of an organic free radical, using S-adenosylmethionine and reduced flavodoxin as cosubstrates to produce 5'-deoxy-adenosine. {ECO:0000250}. No information about this protein was found by a literature search conducted on August 23, 2018. However, based on its similarity to PFLACTENZ-MONOMER (EG10028) it has been annotated as a putative pyruvate formate-lyase activating enzyme.

## Biological Role

Catalyzes protein-glycine,dihydroflavodoxin:S-adenosyl-L-methionine oxidoreductase (S-adenosyl-L-methionine cleaving) (reaction.R04710).

## Annotation

FUNCTION: Activation of pyruvate formate-lyase 2 under anaerobic conditions by generation of an organic free radical, using S-adenosylmethionine and reduced flavodoxin as cosubstrates to produce 5'-deoxy-adenosine. {ECO:0000250}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.R04710|reaction.R04710]] `KEGG` `database` - via EC:1.97.1.4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0824|gene.b0824]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75794`
- `KEGG:ecj:JW0808;eco:b0824;ecoc:C3026_05175;`
- `GeneID:93776600;945445;`
- `GO:GO:0005737; GO:0043365; GO:0046872; GO:0051539`
- `EC:1.97.1.4`

## Notes

Putative pyruvate formate-lyase 3-activating enzyme (EC 1.97.1.4) (Formate-C-acetyltransferase-activating enzyme 3) (PFL-activating enzyme 3)
