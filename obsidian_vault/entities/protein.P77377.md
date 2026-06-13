---
entity_id: "protein.P77377"
entity_type: "protein"
name: "wzxC"
source_database: "UniProt"
source_id: "P77377"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wzxC wzx b2046 JW2031"
---

# wzxC

`protein.P77377`

## Static

- Type: `protein`
- Source: `UniProt:P77377`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

Lipopolysaccharide biosynthesis protein WzxC wzxC is located in a cluster of genes responsible for production of the extracellular polysaccharide, CPD-21504 colanic acid (CA or M antigen) . wzxC encodes a predicted integral membrane protein which may be involved in export of the lipid-linked CA repeat unit . The ΔwzxC mutant of an rcsA overexpressing, CA producing strain of E. coli K-12 MG1655 grows as misshapen rods and spheres and accumulates the pyruvylated hexasaccharide CPD-21522 repeat unit of CA . WzxC single amino acid substitution mutants which have lost substrate specificity and are able to transport lipid II and O-antigen precursors in addition to CA precursors have been isolated; the changes map to regions of the protein located near the periplasmic face of the membrane and may exert their effect through destabilizing the inward-open conformation of the transporter . WzxC may mediate the translocation of lipid III in the absence of functional EG11486-MONOMER WzxE (and see ). WzxC is a member of the Polysaccharide Transporter (PST) family within the MultiDrug/Oligosaccharidyl-lipid/Polysaccharide (MOP) Flippase Superfamily . Nomenclature for genes involved in bacterial polysaccharide synthesis is discussed in

## Biological Role

Catalyzes RXN-22217 (reaction.ecocyc.RXN-22217). Transports hν (molecule.ecocyc.Light).

## Annotation

Lipopolysaccharide biosynthesis protein WzxC

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-22217|reaction.ecocyc.RXN-22217]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2046|gene.b2046]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77377`
- `KEGG:ecj:JW2031;eco:b2046;ecoc:C3026_11520;`
- `GeneID:946581;`
- `GO:GO:0005886; GO:0009103; GO:0009242`

## Notes

Lipopolysaccharide biosynthesis protein WzxC
