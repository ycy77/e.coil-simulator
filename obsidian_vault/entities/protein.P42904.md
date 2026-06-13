---
entity_id: "protein.P42904"
entity_type: "protein"
name: "agaV"
source_database: "UniProt"
source_id: "P42904"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "agaV yhaY b3133 JW3102"
---

# agaV

`protein.P42904`

## Static

- Type: `protein`
- Source: `UniProt:P42904`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in N-acetylgalactosamine transport. Sequence analysis indicates that agaV encodes a protein with similarity to the IIB domain of the PTS Enzymes II specific for mannose. agaV has sequence similarity with EG12769 "agaB". agaV contains a conserved histidine residue (His15) . E. coli contains a cluster of genes (agaZVWEFASYBCDI) responsible for the uptake and metabolism of D-galactosamine (GalN or Gam) and N-acetyl-D-galactosamine (GalNAc or Aga). However, in strain K-12 there is a deletion of the region from agaW' to 'agaA and the organism is unable to utilize GalN and GalNAc as sole carbon sources . AgaVWEF, the GalNAc PTS permease, belongs to the functional superfamily of the PEP-dependent, sugar transporting phosphotransferase system (PTSsugar). When all of its components are present, AgaVWEF takes up exogenous GalNAc, releasing the phosphate ester into the cytoplasm in preparation for metabolism . AgaV is an Enzyme IIBAga. AgaW is a truncated Enzyme IICAga. agaE and agaF encoding Enzymes IIDAga and IIAAga/Gam, respectively, have been deleted...

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in N-acetylgalactosamine transport.

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b3133|gene.b3133]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P42904`
- `KEGG:ecj:JW3102;eco:b3133;ecoc:C3026_17075;`
- `GeneID:75203751;947648;`
- `GO:GO:0005737; GO:0008982; GO:0009401; GO:0016301`
- `EC:2.7.1.-`

## Notes

N-acetylgalactosamine-specific phosphotransferase enzyme IIB component 2 (EC 2.7.1.-) (EIIB-Aga') (PTS system N-acetylgalactosamine-specific EIIB component 2)
