---
entity_id: "protein.P03014"
entity_type: "protein"
name: "pinE"
source_database: "UniProt"
source_id: "P03014"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pinE pin b1158 JW1144"
---

# pinE

`protein.P03014`

## Static

- Type: `protein`
- Source: `UniProt:P03014`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: This protein catalyzes the inversion of an 1800-bp E.coli DNA fragment, the P region, which can exist in either orientation. The function of the inversion is not yet clear. Pin is a site-specific DNA recombinase that is a part of the e14 prophage element. Pin is a site-specific DNA recombinase, similar to the Gin recombinase of phage Mu. It is responsible for the inversion of the P region, an adjacent chunk of DNA containing EG12877, G6598, EG11120 and G6599 . Pin is part of e14, a UV-excisable element that is probably the remains of a prophage . Pin allows phase variation when Salmonella H1 and H2 regions are artificially introduced into E. coli .

## Biological Role

Catalyzes RXN0-5100 (reaction.ecocyc.RXN0-5100).

## Annotation

FUNCTION: This protein catalyzes the inversion of an 1800-bp E.coli DNA fragment, the P region, which can exist in either orientation. The function of the inversion is not yet clear.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5100|reaction.ecocyc.RXN0-5100]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1158|gene.b1158]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P03014`
- `KEGG:ecj:JW1144;eco:b1158;`
- `GeneID:945721;`
- `GO:GO:0000150; GO:0003677; GO:0006310; GO:0015074; GO:0016787; GO:0016874`
- `EC:3.1.22.-; 6.5.1.-`

## Notes

Serine recombinase PinE (EC 3.1.22.-) (EC 6.5.1.-) (DNA-invertase PinE) (DNA-invertase from lambdoid prophage e14) (Site-specific recombinase PinE)
