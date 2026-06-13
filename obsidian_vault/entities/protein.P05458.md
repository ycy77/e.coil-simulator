---
entity_id: "protein.P05458"
entity_type: "protein"
name: "ptrA"
source_database: "UniProt"
source_id: "P05458"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ptrA ptr b2821 JW2789"
---

# ptrA

`protein.P05458`

## Static

- Type: `protein`
- Source: `UniProt:P05458`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: Endopeptidase that degrades small peptides of less than 7 kDa, such as glucagon and insulin. Protease III is a periplasmic protein that rapidly degrades small proteins and peptides in vitro . Protease III is partially responsible for degrading A-β-lactamase as well as misfolded MalE31 . Protease III is a zinc metalloendopeptidase with a nontraditional zinc-binding motif, featuring the consensus sequence HXXEH rather than the more traditional HEXXH . In addition to the two histidines in the zinc-binding motif, glutamate162 is also required for zinc coordination . A 50 kDa polypeptide with no apparent protease function derived from the N-terminal end of protease III can be found in the periplasm under some circumstances .

## Biological Role

Catalyzes 3.4.24.55-RXN (reaction.ecocyc.3.4.24.55-RXN).

## Annotation

FUNCTION: Endopeptidase that degrades small peptides of less than 7 kDa, such as glucagon and insulin.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.4.24.55-RXN|reaction.ecocyc.3.4.24.55-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2821|gene.b2821]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P05458`
- `KEGG:ecj:JW2789;eco:b2821;ecoc:C3026_15490;`
- `GeneID:947284;`
- `GO:GO:0004222; GO:0005737; GO:0006508; GO:0008270; GO:0030288`
- `EC:3.4.24.55`

## Notes

Protease 3 (EC 3.4.24.55) (Pitrilysin) (Protease III) (Protease pi)
