---
entity_id: "protein.P76938"
entity_type: "protein"
name: "epmC"
source_database: "UniProt"
source_id: "P76938"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "epmC yfcM b2326 JW5381"
---

# epmC

`protein.P76938`

## Static

- Type: `protein`
- Source: `UniProt:P76938`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Is involved in the final hydroxylation step of the post-translational modification of translation elongation factor P (EF-P) on 'Lys-34'. Acts after beta-lysylation of 'Lys-34' by EpmA and EpmB. EpmC adds an oxygen atom to the C5 position of 'Lys-34' and does not modify the added beta-lysine. {ECO:0000269|PubMed:22706199}. EpmC catalyzes the hydroxylation of the γ (C4) or δ (C5) position of Lys34 in EG12099-MONOMER. The 5-hydroxyllysine form of EF-P appears to be present in vivo. EpmC is the final enzyme in the pathway generating the fully modified Lys34 residue . A crystal structure of EpmC has been solved at 1.45Å resolution . A metal-coordinating 2-His-1-carboxylate motif similar to that of non-heme iron enzymes forms the catalytic site . A catalytic mechanism has been proposed . EpmC: "EF-P post-translational modification C"

## Biological Role

Catalyzes RXN0-7000 (reaction.ecocyc.RXN0-7000).

## Annotation

FUNCTION: Is involved in the final hydroxylation step of the post-translational modification of translation elongation factor P (EF-P) on 'Lys-34'. Acts after beta-lysylation of 'Lys-34' by EpmA and EpmB. EpmC adds an oxygen atom to the C5 position of 'Lys-34' and does not modify the added beta-lysine. {ECO:0000269|PubMed:22706199}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7000|reaction.ecocyc.RXN0-7000]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2326|gene.b2326]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76938`
- `KEGG:ecj:JW5381;eco:b2326;ecoc:C3026_12960;`
- `GeneID:946807;`
- `GO:GO:0004497; GO:0016709; GO:0043687; GO:0046872`
- `EC:1.14.13.-`

## Notes

Elongation factor P lysine hydroxylase (EF-P lysine hydroxylase) (EC 1.14.13.-) (EF-P post-translational modification enzyme C)
