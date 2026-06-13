---
entity_id: "protein.P33590"
entity_type: "protein"
name: "nikA"
source_database: "UniProt"
source_id: "P33590"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nikA b3476 JW3441"
---

# nikA

`protein.P33590`

## Static

- Type: `protein`
- Source: `UniProt:P33590`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Involved in a nickel transport system, probably represents the nickel binder. NikA is the periplasmic binding protein of a high affinity nickel uptake system. The endogenous ligand for NikA is suggested to be a CPD0-2714 Ni-(L-His)2 complex. Purified NikA is monomeric and binds one atom of nickel per molecule of protein with a Kd of less than 0.1μM; purified NikA binds Ni2+ with at least 10-fold higher affinity than for other divalent metals . Purified NikA binds nickel selctively over cobalt with a Kd of 1µM for Ni2+ and 246µM for Co2+ . NikA mediates Tar dependent nickel-repellent chemotaxis . Purified, crystallized NikA consists of two lobes connected by a hinge; a hydrophobic pocket shaped to fit a penta-coordinate-hydrated nickel ion [Ni(H2O)52] forms the ligand binding site; nickel does not form direct contacts with NikA but hydrogen bonds to a coordinating water molecule; nickel remains accessible to solvent while bound to NikA . The details of this binding site were later challenged by who reported that NikA (aerobically overexpressed and purified in the presence of EDTA) binds Fe(III)EDTA(H2O)- with high affinity and suggested that NikA would transport nickel complexed to a chemically similar metallophore (possibly butane-1,2,4-tricarboxylate ) in vivo. Ni2+ binds a natural metallophore; His416 is the only direct metal-NikA contact...

## Biological Role

Component of Ni(2+) ABC transporter (complex.ecocyc.ABC-20-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Involved in a nickel transport system, probably represents the nickel binder.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-20-CPLX|complex.ecocyc.ABC-20-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3476|gene.b3476]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33590`
- `KEGG:ecj:JW3441;eco:b3476;ecoc:C3026_18825;`
- `GeneID:947981;`
- `GO:GO:0015675; GO:0015833; GO:0016020; GO:0016151; GO:0020037; GO:0030288; GO:0042597; GO:0046914; GO:0050919; GO:0051540; GO:0055052; GO:0098716; GO:1904680`

## Notes

Nickel-binding periplasmic protein
