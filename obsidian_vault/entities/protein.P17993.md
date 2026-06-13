---
entity_id: "protein.P17993"
entity_type: "protein"
name: "ubiG"
source_database: "UniProt"
source_id: "P17993"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:30686758}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ubiG pufX yfaB b2232 JW2226"
---

# ubiG

`protein.P17993`

## Static

- Type: `protein`
- Source: `UniProt:P17993`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:30686758}.

## Enriched Summary

FUNCTION: O-methyltransferase that catalyzes the 2 O-methylation steps in the ubiquinone biosynthetic pathway. {ECO:0000255|HAMAP-Rule:MF_00472, ECO:0000269|PubMed:10419476}. UbiG is an S-adenosyl-L-methionine (SAM)-dependent O-methyltransferase that catalyzes both O-methylation reactions in the biosynthesis of ubiquinone and is a component of the Ubi complex metabolon . The enzyme is mostly cytoplasmic, but also shows some association with the membrane . Purified UbiG binds to liposomes, with preferences for phosphatidylglycerol and cardiolipin . Crystal structures of wild-type and mutant UbiG in complex with S-adenosyl-L-homocysteine (SAH) have been determined . A unique, conserved membrane-binding region was identified and its function confirmed by mutating amino acid residues within this region . Interaction of this region with the cytoplasmic membrane may open a channel that provides access for SAM to its binding site . Liposome-associated UbiG has ~11-fold increased affinity for SAH . However, whether or not the membrane association of UbiG contributes to its catalytic activity has not yet been investigated. The seven ubiquinone biosynthesis proteins UbiE, UbiF, UbiG, UbiH, UbiI, UbiJ, and UbiK form a 1 MDa complex in the cytosol . Gel filtration data showed the apparent molecular mass of UbiG is approximately 50 kDa, suggesting a homodimer...

## Biological Role

Catalyzes 2-octaprenyl-6-hydroxyphenyl methylase (reaction.ecocyc.2-OCTAPRENYL-6-OHPHENOL-METHY-RXN), DHHB-METHYLTRANSFER-RXN (reaction.ecocyc.DHHB-METHYLTRANSFER-RXN). Component of Ubi complex (complex.ecocyc.CPLX0-8301). Bound by Zinc cation (molecule.C00038).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: O-methyltransferase that catalyzes the 2 O-methylation steps in the ubiquinone biosynthetic pathway. {ECO:0000255|HAMAP-Rule:MF_00472, ECO:0000269|PubMed:10419476}.

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.2-OCTAPRENYL-6-OHPHENOL-METHY-RXN|reaction.ecocyc.2-OCTAPRENYL-6-OHPHENOL-METHY-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.DHHB-METHYLTRANSFER-RXN|reaction.ecocyc.DHHB-METHYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-8301|complex.ecocyc.CPLX0-8301]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2232|gene.b2232]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P17993`
- `KEGG:ecj:JW2226;eco:b2232;ecoc:C3026_12470;`
- `GeneID:75172359;75206477;946607;`
- `GO:GO:0005829; GO:0006744; GO:0008168; GO:0008425; GO:0009898; GO:0010420; GO:0032259; GO:0042538; GO:0061542; GO:0102208; GO:0110142; GO:1901611`
- `EC:2.1.1.222; 2.1.1.64`

## Notes

Ubiquinone biosynthesis O-methyltransferase (2-octaprenyl-6-hydroxyphenol methylase) (EC 2.1.1.222) (3-demethylubiquinone-8 3-O-methyltransferase) (EC 2.1.1.64)
