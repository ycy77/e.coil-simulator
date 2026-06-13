---
entity_id: "protein.P0AAD4"
entity_type: "protein"
name: "tyrP"
source_database: "UniProt"
source_id: "P0AAD4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:6090409}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tyrP b1907 JW1895"
---

# tyrP

`protein.P0AAD4`

## Static

- Type: `protein`
- Source: `UniProt:P0AAD4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:6090409}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Transports tyrosine across the cytoplasmic membrane (PubMed:6090409). The transport system is energized by the proton motive force (PubMed:6090409). {ECO:0000269|PubMed:6090409}. TyrP is a tyrosine-specific permease. It is a member of the Hydroxy/Aromatic Amino Acid Permease (HAAP) family. Studies, , found a single promoter whose expression was repressed by the TyrR protein in the presence of tyrosine and activated by the TyrR protein in the presence of phenylalanine.

## Biological Role

Catalyzes L-tyrosine:proton symport (reaction.ecocyc.TRANS-RXN-77). Transports L-Tyrosine (molecule.C00082), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Transports tyrosine across the cytoplasmic membrane (PubMed:6090409). The transport system is energized by the proton motive force (PubMed:6090409). {ECO:0000269|PubMed:6090409}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-77|reaction.ecocyc.TRANS-RXN-77]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00082|molecule.C00082]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1907|gene.b1907]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAD4`
- `KEGG:ecj:JW1895;eco:b1907;ecoc:C3026_10825;`
- `GeneID:946412;`
- `GO:GO:0003333; GO:0005886; GO:0015173; GO:0015293; GO:0022857`

## Notes

Tyrosine-specific transport system (Tyrosine permease) (Tyrosine:H(+) symporter)
