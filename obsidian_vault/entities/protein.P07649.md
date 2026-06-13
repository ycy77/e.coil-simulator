---
entity_id: "protein.P07649"
entity_type: "protein"
name: "truA"
source_database: "UniProt"
source_id: "P07649"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "truA asuC hisT leuK b2318 JW2315"
---

# truA

`protein.P07649`

## Static

- Type: `protein`
- Source: `UniProt:P07649`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Formation of pseudouridine at positions 38, 39 and 40 in the anticodon stem and loop of transfer RNAs. {ECO:0000269|PubMed:17466622}. TruA is the tRNA pseudouridine synthase responsible for catalyzing pseudouridine formation in the anticodon loop of a subset of tRNAs . TruA-mediated pseudouridylation contributes to structural stability of this region of the tRNA and to reading frame maintenance by tRNALeu . Results from site-directed mutagenesis indicate that the reaction mechanism likely does not involve a covalent cysteine intermediate . Instead, the D60 residue is essential for catalytic activity , forming a covalent adduct that can undergo O-acyl hydrolytic cleavage to form the pseudouridine product . The Arg58 residue facilitates flipping of the substrate base into the active site . Pre-steady-state kinetic analysis showed that catalysis, but not substrate binding, is the rate-limiting step . Crystal structures of the enzyme have been solved . TruA is a dimer in the crystal as well as in solution . Modeling of the substrate recognition pathway indicates that the enzyme utilizes the intrinsic flexibility of the tRNA anticodon loop . A truA mutant exhibits a tRNA pseudouridine synthase defect and increased translation errors under conditions of low histidine...

## Biological Role

Component of tRNA pseudouridine38-40 synthase (complex.ecocyc.CPLX0-7728).

## Annotation

FUNCTION: Formation of pseudouridine at positions 38, 39 and 40 in the anticodon stem and loop of transfer RNAs. {ECO:0000269|PubMed:17466622}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7728|complex.ecocyc.CPLX0-7728]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2318|gene.b2318]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07649`
- `KEGG:ecj:JW2315;eco:b2318;ecoc:C3026_12920;`
- `GeneID:946793;`
- `GO:GO:0000049; GO:0009982; GO:0031119; GO:0042803; GO:0106029; GO:0160147`
- `EC:5.4.99.12`

## Notes

tRNA pseudouridine synthase A (EC 5.4.99.12) (tRNA pseudouridine(38-40) synthase) (tRNA pseudouridylate synthase I) (PSU-I) (tRNA-uridine isomerase I)
