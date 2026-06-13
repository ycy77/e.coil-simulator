---
entity_id: "protein.P76507"
entity_type: "protein"
name: "yfdI"
source_database: "UniProt"
source_id: "P76507"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yfdI b2352 JW5382"
---

# yfdI

`protein.P76507`

## Static

- Type: `protein`
- Source: `UniProt:P76507`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

Uncharacterized protein YfdI yfdG, yfdH and yfdI constitute a three gene cluster within the CPS-53/KpLE1 cryptic prophage . yfdI (also called GtrIVEC) shows significant homology (41% identity and 63% similarity) with gtrIV, encoding a type IV-specific glucosyltransferase in the genome of Shigella flexneri NCTC 8296 . yfdG, yfdH and yfdI mediate partial O-antigen modification when introduced together into S. flexneri serotype Y strain SFL124; yfdI may encode a glucosyltransferase that is specific for the E. coli K-12 O16 O antigen (which differs from the S. flexneri O antigen) . yfdI contains a predicted PD00214 "OxyR" target site; DNase footprinting showed strong binding by oxidized OxyR and weak binding by reduced OxyR to the predicted site within yfdI but no OxyR-regulated transcript was detected . Please note: E. coli K-12 does not produce an O-antigen due to mutations in the rfb region; a reconstructed strain with all rfb genes intact produces an O16 antigen .

## Biological Role

Catalyzes RXN-19362 (reaction.ecocyc.RXN-19362).

## Annotation

Uncharacterized protein YfdI

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-19362|reaction.ecocyc.RXN-19362]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2352|gene.b2352]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76507`
- `KEGG:ecj:JW5382;eco:b2352;ecoc:C3026_13085;`
- `GeneID:946822;`
- `GO:GO:0005886`

## Notes

Uncharacterized protein YfdI
