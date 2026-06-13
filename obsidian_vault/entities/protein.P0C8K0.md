---
entity_id: "protein.P0C8K0"
entity_type: "protein"
name: "kbaZ"
source_database: "UniProt"
source_id: "P0C8K0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kbaZ agaZ yhaX b3132 JW3101"
---

# kbaZ

`protein.P0C8K0`

## Static

- Type: `protein`
- Source: `UniProt:P0C8K0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Component of the tagatose-1,6-bisphosphate aldolase KbaYZ that is required for full activity and stability of the Y subunit. Could have a chaperone-like function for the proper and stable folding of KbaY. When expressed alone, KbaZ does not show any aldolase activity. {ECO:0000269|PubMed:11976750}. The KbaZ protein has no catalytic activity, but may stabilize the tagatose-1,6-bisphosphate aldolase CPLX0-240 KbaY. KbaZ appears to be required for full activity of KbaY, and thus may have a chaperone-like function . However like E. coli's other putative tagatose-1,6-bisphosphate aldolase chaperone G7128-MONOMER GatZ, structural analysis of KbaZ with AlphaFold and Rosetta predicted a structure with a Zn2+ cofactor and conserved amino acid residues in an active site that is structurally similar and mechanistically consistent with known C4 epimerases . Overexpression of kbaYZ has been shown to complement mutations to gatYZ . KbaZ is able to produce D-tagatose in the triple mutant ΔpfkAΔzwfΔgatZ when G7187-MONOMER is present to dephosphorylate D-tagatose-6-P to D-tagatose .

## Biological Role

Catalyzes RXN-18477 (reaction.ecocyc.RXN-18477). Bound by Zinc cation (molecule.C00038).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Component of the tagatose-1,6-bisphosphate aldolase KbaYZ that is required for full activity and stability of the Y subunit. Could have a chaperone-like function for the proper and stable folding of KbaY. When expressed alone, KbaZ does not show any aldolase activity. {ECO:0000269|PubMed:11976750}.

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `activates` --> [[reaction.ecocyc.TAGAALDOL-RXN|reaction.ecocyc.TAGAALDOL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` --> [[reaction.ecocyc.RXN-18477|reaction.ecocyc.RXN-18477]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3132|gene.b3132]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0C8K0`
- `KEGG:ecj:JW3101;eco:b3132;ecoc:C3026_17070;`
- `GeneID:947637;`
- `GO:GO:0005886; GO:0005975; GO:0008047; GO:0009401; GO:1902494; GO:2001059`

## Notes

D-tagatose-1,6-bisphosphate aldolase subunit KbaZ
