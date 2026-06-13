---
entity_id: "protein.P0A9R4"
entity_type: "protein"
name: "fdx"
source_database: "UniProt"
source_id: "P0A9R4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fdx b2525 JW2509"
---

# fdx

`protein.P0A9R4`

## Static

- Type: `protein`
- Source: `UniProt:P0A9R4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Ferredoxin are iron-sulfur proteins that transfer electrons in a wide variety of metabolic reactions. Although the function of this ferredoxin is unknown it is probable that it has a role as a cellular electron transfer protein. Involved in the in vivo assembly of the Fe-S clusters in a wide variety of iron-sulfur proteins. Ferredoxin (Fdx) contains a [2Fe-2S] cluster and functions in Fe-S cluster assembly . Fdx interacts directly with G7325-MONOMER IscS and supplies one of the two electrons needed for reduction of S0 to IscS. Fdx and G7324-MONOMER IscU compete for overlapping binding sites on IscS . Holo-IscA , holo-GrxD, and the GrxD-BolA heterodimer can transfer an [2Fe-2S] cluster to apo-Fdx in vitro. A crystal structure of Fdx has been solved at 1.7 Å resolution. The [2Fe-2S] cluster is located near the surface of the protein and is coordinated by the Sγ atoms of Cys42, Cys48, Cys51, and Cys87; another cysteine residue, Cys46, is exposed on the surface near the Fe-S cluster . Fdx is synthesized under both aerobic and anaerobic growth conditions . An fdx null mutant strain grows with a significantly increased doubling time compared to wild type . Review: .

## Biological Role

Catalyzes RXN-25087 (reaction.ecocyc.RXN-25087), RXN-25093 (reaction.ecocyc.RXN-25093).

## Enriched Pathways

- `eco00362` Benzoate degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Ferredoxin are iron-sulfur proteins that transfer electrons in a wide variety of metabolic reactions. Although the function of this ferredoxin is unknown it is probable that it has a role as a cellular electron transfer protein. Involved in the in vivo assembly of the Fe-S clusters in a wide variety of iron-sulfur proteins.

## Pathways

- `eco00362` Benzoate degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-25087|reaction.ecocyc.RXN-25087]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-25093|reaction.ecocyc.RXN-25093]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2525|gene.b2525]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9R4`
- `KEGG:ecj:JW2509;eco:b2525;ecoc:C3026_13995;`
- `GeneID:86860651;93774611;947160;`
- `GO:GO:0005829; GO:0009055; GO:0016226; GO:0022900; GO:0046872; GO:0051537; GO:0140647`

## Notes

2Fe-2S ferredoxin
