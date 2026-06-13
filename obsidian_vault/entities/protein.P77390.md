---
entity_id: "protein.P77390"
entity_type: "protein"
name: "citC"
source_database: "UniProt"
source_id: "P77390"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "citC ybeO b0618 JW0610"
---

# citC

`protein.P77390`

## Static

- Type: `protein`
- Source: `UniProt:P77390`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Acetylation of prosthetic group (2-(5''-phosphoribosyl)-3'-dephosphocoenzyme-A) of the gamma subunit of citrate lyase. Citrate lyase synthetase activates citrate lyase by acetylation . The actual site of acetylation is the prosthetic group of the acyl-carrier protein, or γ, subunit.

## Biological Role

Catalyzes CITC-RXN (reaction.ecocyc.CITC-RXN).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Acetylation of prosthetic group (2-(5''-phosphoribosyl)-3'-dephosphocoenzyme-A) of the gamma subunit of citrate lyase.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.CITC-RXN|reaction.ecocyc.CITC-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0618|gene.b0618]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77390`
- `KEGG:ecj:JW0610;eco:b0618;ecoc:C3026_03090;`
- `GeneID:75170622;75205020;945231;`
- `GO:GO:0005524; GO:0008771; GO:0016747`
- `EC:6.2.1.22`

## Notes

[Citrate [pro-3S]-lyase] ligase (EC 6.2.1.22) (Acetate:SH-citrate lyase ligase) (Citrate lyase synthetase)
