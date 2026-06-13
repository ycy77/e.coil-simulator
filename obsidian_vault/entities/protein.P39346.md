---
entity_id: "protein.P39346"
entity_type: "protein"
name: "idnD"
source_database: "UniProt"
source_id: "P39346"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "idnD yjgV b4267 JW4224"
---

# idnD

`protein.P39346`

## Static

- Type: `protein`
- Source: `UniProt:P39346`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the NADH/NADPH-dependent oxidation of L-idonate to 5-ketogluconate (5KG). {ECO:0000269|PubMed:9658018}. L-idonate 5-dehydrogenase catalyzes the reversible oxidation of L-idonate to 5-ketogluconate. This is the first reaction of the L-idonate catabolic pathway after uptake of L-idonate into the cell. The enzyme specifically oxidizes L-idonate using NAD and catalyzes the specific reduction of 5-ketogluconate using NADH or NADPH . A strain containing a deletion of idnD can not grow on L-idonate as the sole source of carbon and energy . Expression of the idnDOTR operon is catabolite repressed and induced by L-idonate or 5-ketogluconate . IdnD: "idonate" Review:

## Biological Role

Catalyzes 1.1.1.264-RXN (reaction.ecocyc.1.1.1.264-RXN).

## Annotation

FUNCTION: Catalyzes the NADH/NADPH-dependent oxidation of L-idonate to 5-ketogluconate (5KG). {ECO:0000269|PubMed:9658018}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.1.1.1.264-RXN|reaction.ecocyc.1.1.1.264-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4267|gene.b4267]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39346`
- `KEGG:ecj:JW4224;eco:b4267;ecoc:C3026_23015;`
- `GeneID:944769;`
- `GO:GO:0019521; GO:0046183; GO:0046872; GO:0050572; GO:0102198`
- `EC:1.1.1.264`

## Notes

L-idonate 5-dehydrogenase (NAD(P)(+)) (EC 1.1.1.264)
