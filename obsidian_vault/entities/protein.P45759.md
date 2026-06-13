---
entity_id: "protein.P45759"
entity_type: "protein"
name: "gspE"
source_database: "UniProt"
source_id: "P45759"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:Q00512}. Note=Membrane association is not an intrinsic property but requires the GspL gene product. {ECO:0000250|UniProtKB:Q00512}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gspE yheG b3326 JW3288"
---

# gspE

`protein.P45759`

## Static

- Type: `protein`
- Source: `UniProt:P45759`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250|UniProtKB:Q00512}. Note=Membrane association is not an intrinsic property but requires the GspL gene product. {ECO:0000250|UniProtKB:Q00512}.

## Enriched Summary

FUNCTION: ATPase component of the type II secretion system required for the energy-dependent secretion of extracellular factors such as proteases and toxins from the periplasm. Acts as a molecular motor to provide the energy that is required for assembly of the pseudopilus and the extrusion of substrates generated in the cytoplasm. {ECO:0000250|UniProtKB:Q00512}. E. coli K-12 contains a cluster of genes (gsp) predicted to encode the components of a type II secretion system; the cluster consists of two divergent operons TU0-14374 gspC-O and TU-8433 gspAB which are transcriptionally repressed by PD00288 nucleoid-structuring protein H-NS under standard laboratory conditions . Overexpression of the full cluster supports secretion of (plasmid expressed) EG11237-MONOMER and (plasmid expressed) G7706-MONOMER pseudopilin GspG in a hns mutant strain . gspE encodes the cytoplasmic ATPase of gram-negative type II secretion systems (see ). gsp: general secretory pathway

## Biological Role

Component of type II secretion system (complex.ecocyc.CPLX0-3382).

## Enriched Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: ATPase component of the type II secretion system required for the energy-dependent secretion of extracellular factors such as proteases and toxins from the periplasm. Acts as a molecular motor to provide the energy that is required for assembly of the pseudopilus and the extrusion of substrates generated in the cytoplasm. {ECO:0000250|UniProtKB:Q00512}.

## Pathways

- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3382|complex.ecocyc.CPLX0-3382]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3326|gene.b3326]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45759`
- `KEGG:ecj:JW3288;eco:b3326;ecoc:C3026_18070;`
- `GeneID:947823;`
- `GO:GO:0005524; GO:0005886; GO:0008564; GO:0015627; GO:0015628; GO:0016887; GO:0046872`
- `EC:7.4.2.8`

## Notes

Putative type II secretion system protein E (T2SS protein E) (EC 7.4.2.8) (Putative general secretion pathway protein E) (Type II traffic warden ATPase)
