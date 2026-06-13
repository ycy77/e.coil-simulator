---
entity_id: "protein.P75958"
entity_type: "protein"
name: "lolE"
source_database: "UniProt"
source_id: "P75958"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lolE ycfW b1118 JW1104"
---

# lolE

`protein.P75958`

## Static

- Type: `protein`
- Source: `UniProt:P75958`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Part of an ATP-dependent transport system LolCDE responsible for the release of lipoproteins targeted to the outer membrane from the inner membrane. Such a release is dependent of the sorting-signal (absence of an Asp at position 2 of the mature lipoprotein) and of LolA. LolE is an inner membrane subunit of the LolCDE lipoprotein release complex . LolE contains 4 predicted transmembrane regions; a large loop region between the first and second transmembrane regions is predicted to be in the periplasm .

## Biological Role

Component of lipoprotein release complex (complex.ecocyc.ABC-62-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of an ATP-dependent transport system LolCDE responsible for the release of lipoproteins targeted to the outer membrane from the inner membrane. Such a release is dependent of the sorting-signal (absence of an Asp at position 2 of the mature lipoprotein) and of LolA.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-62-CPLX|complex.ecocyc.ABC-62-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1118|gene.b1118]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75958`
- `KEGG:ecj:JW1104;eco:b1118;ecoc:C3026_06735;`
- `GeneID:75203704;945665;`
- `GO:GO:0005886; GO:0042953; GO:0043190; GO:0044874; GO:0098797; GO:0140306`

## Notes

Lipoprotein-releasing system transmembrane protein LolE
