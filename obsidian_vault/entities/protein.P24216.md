---
entity_id: "protein.P24216"
entity_type: "protein"
name: "fliD"
source_database: "UniProt"
source_id: "P24216"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Secreted. Bacterial flagellum."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fliD flaV flbC b1924 JW1909"
---

# fliD

`protein.P24216`

## Static

- Type: `protein`
- Source: `UniProt:P24216`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Secreted. Bacterial flagellum.

## Enriched Summary

FUNCTION: Required for the morphogenesis and for the elongation of the flagellar filament by facilitating polymerization of the flagellin monomers at the tip of growing filament. Forms a capping structure, which prevents flagellin subunits (transported through the central channel of the flagellum) from leaking out without polymerization at the distal end. The filament cap lies at the distal, growing end of the flagellar filament and plays a critical role in the assembly of flagellin (FliC) monomers into the growing filament . For a description of flagellar gene nomenclature, including old (fla, flb) and new (flg, flh and fli) symbols, see

## Biological Role

Component of flagellum (complex.ecocyc.CPLX0-7452).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: Required for the morphogenesis and for the elongation of the flagellar filament by facilitating polymerization of the flagellin monomers at the tip of growing filament. Forms a capping structure, which prevents flagellin subunits (transported through the central channel of the flagellum) from leaking out without polymerization at the distal end.

## Pathways

- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7452|complex.ecocyc.CPLX0-7452]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b1924|gene.b1924]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24216`
- `KEGG:ecj:JW1909;eco:b1924;ecoc:C3026_10915;`
- `GeneID:75205830;946428;`
- `GO:GO:0005576; GO:0007155; GO:0009421; GO:0009424; GO:0071973`

## Notes

Flagellar hook-associated protein 2 (HAP2) (Filament cap protein) (Flagellar cap protein)
