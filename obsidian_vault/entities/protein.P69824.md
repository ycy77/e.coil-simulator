---
entity_id: "protein.P69824"
entity_type: "protein"
name: "cmtB"
source_database: "UniProt"
source_id: "P69824"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cmtB b2934 JW2901"
---

# cmtB

`protein.P69824`

## Static

- Type: `protein`
- Source: `UniProt:P69824`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II CmtAB PTS system is involved in D-mannitol transport. {ECO:0000250|UniProtKB:P0A0E0}. cmtB encodes a hydrophilic protein with seqence similarity to the EIIA domain of MltA, the mannitol PTS permease . Expression of cmtB from a lac promoter partially complements the growth defect of an E. coli mtlA C-terminal deletion mutant . A solution structure of CmtB shows high similarity with that of the MltA IIA domain although structural differences around the active site are present. Histidine residue 67 is predicted to be the site of phosphorylation .

## Biological Role

Component of mannitol-specific PTS enzyme II CmtBA (complex.ecocyc.CPLX-156).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II CmtAB PTS system is involved in D-mannitol transport. {ECO:0000250|UniProtKB:P0A0E0}.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-156|complex.ecocyc.CPLX-156]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2934|gene.b2934]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69824`
- `KEGG:ecj:JW2901;eco:b2934;ecoc:C3026_16065;`
- `GeneID:75173040;75205230;945125;`
- `GO:GO:0005737; GO:0009401; GO:0016301; GO:0090585`

## Notes

Mannitol-specific cryptic phosphotransferase enzyme IIA component (EIIA-Mtl) (EIII-Mtl) (PTS system mannitol-specific EIIA component)
