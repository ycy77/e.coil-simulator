---
entity_id: "protein.P0C8J8"
entity_type: "protein"
name: "gatZ"
source_database: "UniProt"
source_id: "P0C8J8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gatZ b2095 JW2082"
---

# gatZ

`protein.P0C8J8`

## Static

- Type: `protein`
- Source: `UniProt:P0C8J8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Component of the tagatose-1,6-bisphosphate aldolase GatYZ that is required for full activity and stability of the Y subunit. Could have a chaperone-like function for the proper and stable folding of GatY. When expressed alone, GatZ does not show any aldolase activity. Is involved in the catabolism of galactitol. {ECO:0000269|PubMed:11976750, ECO:0000269|PubMed:8955298}. The GatZ protein has no catalytic activity, but may stabilize the tagatose-1,6-bisphosphate aldolase TAGAALDOL2-MONOMER GatY as a heterodimer. GatZ appears to be required for full activity of GatY, and thus may have a chaperone-like function . However, E. coli's gatZ gene shows high sequence similarity for genes with tagatose-6-phosphate epimerase activity in other Gram negative bacteria: the gatZ of TAX-571, the tagE gene of TAX-382 and the agaZ of TAX-358 . Structural analysis with AlphaFold and Rosetta predicted a structure with a Zn2+ cofactor and conserved amino acid residues in an active site that is structurally similar and mechanistically consistent with known C4 epimerases; another putative tagatose-1,6-bisphosphate aldolase chaperone G7631-MONOMER KbaZ also had similar predicted structure and mechanisms...

## Biological Role

Catalyzes RXN-18477 (reaction.ecocyc.RXN-18477). Bound by Zinc cation (molecule.C00038).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Component of the tagatose-1,6-bisphosphate aldolase GatYZ that is required for full activity and stability of the Y subunit. Could have a chaperone-like function for the proper and stable folding of GatY. When expressed alone, GatZ does not show any aldolase activity. Is involved in the catabolism of galactitol. {ECO:0000269|PubMed:11976750, ECO:0000269|PubMed:8955298}.

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `activates` --> [[reaction.ecocyc.TAGAALDOL-RXN|reaction.ecocyc.TAGAALDOL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` --> [[reaction.ecocyc.RXN-18477|reaction.ecocyc.RXN-18477]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2095|gene.b2095]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0C8J8`
- `KEGG:ecj:JW2082;eco:b2095;`
- `GeneID:946641;`
- `GO:GO:0005886; GO:0008047; GO:0009401; GO:0019402; GO:1902494; GO:2001059`

## Notes

D-tagatose-1,6-bisphosphate aldolase subunit GatZ
