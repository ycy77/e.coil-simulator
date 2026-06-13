---
entity_id: "protein.P16689"
entity_type: "protein"
name: "phnM"
source_database: "UniProt"
source_id: "P16689"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "phnM b4095 JW4056"
---

# phnM

`protein.P16689`

## Static

- Type: `protein`
- Source: `UniProt:P16689`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of alpha-D-ribose 1-methylphosphonate triphosphate (RPnTP) to form alpha-D-ribose 1-methylphosphonate phosphate (PRPn) and diphosphate. {ECO:0000269|PubMed:22089136}. PhnM catalyzes hydrolysis of CPD0-2479, generating CPD0-2480 and pyrophosphate . PhnM is a member of the amidohydrolase superfamily . phnM is part of an operon that is phosphate starvation-inducible and required for use of phosphonate and phosphite as phosphorous sources . PhnM appeared to be required for carbon-phosphorous lyase activity .

## Biological Role

Catalyzes RXN-17955 (reaction.ecocyc.RXN-17955), RXN0-6733 (reaction.ecocyc.RXN0-6733).

## Enriched Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolysis of alpha-D-ribose 1-methylphosphonate triphosphate (RPnTP) to form alpha-D-ribose 1-methylphosphonate phosphate (PRPn) and diphosphate. {ECO:0000269|PubMed:22089136}.

## Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-17955|reaction.ecocyc.RXN-17955]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6733|reaction.ecocyc.RXN0-6733]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4095|gene.b4095]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16689`
- `KEGG:ecj:JW4056;eco:b4095;ecoc:C3026_22135;`
- `GeneID:948613;`
- `GO:GO:0016810; GO:0019700`
- `EC:3.6.1.63`

## Notes

Alpha-D-ribose 1-methylphosphonate 5-triphosphate diphosphatase (RPnTP diphosphatase) (EC 3.6.1.63)
