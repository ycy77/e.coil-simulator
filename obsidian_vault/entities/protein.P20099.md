---
entity_id: "protein.P20099"
entity_type: "protein"
name: "bisC"
source_database: "UniProt"
source_id: "P20099"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bisC b3551 JW5940"
---

# bisC

`protein.P20099`

## Static

- Type: `protein`
- Source: `UniProt:P20099`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: This enzyme may serve as a scavenger, allowing the cell to utilize biotin sulfoxide as a biotin source. It reduces a spontaneous oxidation product of biotin, D-biotin D-sulfoxide (BSO or BDS), back to biotin. Also exhibits methionine-(S)-sulfoxide (Met-S-SO) reductase activity, acting specifically on the (S) enantiomer in the free, but not the protein-bound form. It thus plays a role in assimilation of oxidized methionines. {ECO:0000269|PubMed:15601707, ECO:0000269|PubMed:2180922}. BisC was first identified as a biotin sulfoxide reductase that reduces a spontaneous oxidation product of biotin, biotin-d-sulfoxide (BDS), back to biotin. The enzyme allows scavenging of BDS as a biotin source and may also protect the cell from oxidation damage . The other genes which were originally identified to be required for biotin sulfoxide reductase activity are likely involved in the biosynthesis and insertion of the molybdenum cofactor . A small, heat-stable, thioredoxin-like protein functions as a source for reducing equivalents and is required for biotin sulfoxide reductase activity . BisC also exhibits methionine-S-sulfoxide reductase activity, acting specifically on the S enantiomer in the free, but not the protein-bound form. It thus plays a role in assimilation of oxidized methionines...

## Biological Role

Catalyzes 1.8.4.13-RXN (reaction.ecocyc.1.8.4.13-RXN), RXN0-6277 (reaction.ecocyc.RXN0-6277). Bound by bis(guanylyl molybdopterin) cofactor (molecule.ecocyc.CPD-15873).

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: This enzyme may serve as a scavenger, allowing the cell to utilize biotin sulfoxide as a biotin source. It reduces a spontaneous oxidation product of biotin, D-biotin D-sulfoxide (BSO or BDS), back to biotin. Also exhibits methionine-(S)-sulfoxide (Met-S-SO) reductase activity, acting specifically on the (S) enantiomer in the free, but not the protein-bound form. It thus plays a role in assimilation of oxidized methionines. {ECO:0000269|PubMed:15601707, ECO:0000269|PubMed:2180922}.

## Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.1.8.4.13-RXN|reaction.ecocyc.1.8.4.13-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6277|reaction.ecocyc.RXN0-6277]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-15873|molecule.ecocyc.CPD-15873]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3551|gene.b3551]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P20099`
- `KEGG:ecj:JW5940;eco:b3551;`
- `GeneID:946915;`
- `GO:GO:0009055; GO:0009061; GO:0030151; GO:0030288; GO:0033744; GO:0043546; GO:0050626`
- `EC:1.-.-.-; 1.8.4.13`

## Notes

Biotin sulfoxide reductase (BDS reductase) (BSO reductase) (EC 1.-.-.-) (L-methionine-(S)-sulfoxide reductase) (Met-S-SO reductase) (EC 1.8.4.13)
