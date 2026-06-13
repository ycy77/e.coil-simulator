---
entity_id: "protein.P0A6A8"
entity_type: "protein"
name: "acpP"
source_database: "UniProt"
source_id: "P0A6A8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "acpP b1094 JW1080"
---

# acpP

`protein.P0A6A8`

## Static

- Type: `protein`
- Source: `UniProt:P0A6A8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Carrier of the growing fatty acid chain in fatty acid biosynthesis. Acyl carrier protein (ACP) plays an important role in fatty acid biosynthesis. It carries fatty acid chains via a thioester linkage to a PANTETHEINE-P prosthetic group as the chains are elongated. There is also evidence that it has a function in the biosynthesis of membrane-derived oligosaccharides. ACP and its acylated forms interact with at least 12 different TAX-562 enzymes . ACP is the most abundant protein in TAX-562, with about 1.5 million molecules per cell . ACP contains a PANTETHEINE-P moiety (as does Coenzyme A) as the reactive unit, attached to the ACP protein through a serine side chain. The HOLO-ACP-SYNTH-CPLX enzyme (encoded by EG10247) transfers the PANTETHEINE-P moiety of CO-A to the EG50003-MONOMER to form ACP-MONOMER, which is the active form of the carrier in lipid synthesis . Acyl carrier protein (ACP) plays an important role in fatty acid biosynthesis. It carries fatty acid chains via a thioester linkage to a PANTETHEINE-P prosthetic group as the chains are elongated. There is also evidence that it has a function in the biosynthesis of membrane-derived oligosaccharides. ACP and its acylated forms interact with at least 12 different TAX-562 enzymes . ACP is the most abundant protein in TAX-562, with about 1.5 million molecules per cell...

## Enriched Pathways

- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Carrier of the growing fatty acid chain in fatty acid biosynthesis.

## Pathways

- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `represses` --> [[reaction.ecocyc.HOLO-ACP-SYNTH-RXN|reaction.ecocyc.HOLO-ACP-SYNTH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-1381|reaction.ecocyc.RXN-1381]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `encodes` <-- [[gene.b1094|gene.b1094]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6A8`
- `KEGG:ecj:JW1080;eco:b1094;ecoc:C3026_06615;`
- `GeneID:944805;98387866;99776460;`
- `GO:GO:0000035; GO:0000036; GO:0005737; GO:0005829; GO:0006633; GO:0008289; GO:0008610; GO:0009245; GO:0009410; GO:0016020; GO:0031177`

## Notes

Acyl carrier protein (ACP) (Cytosolic-activating factor) (CAF) (Fatty acid synthase acyl carrier protein)
