---
entity_id: "protein.P31069"
entity_type: "protein"
name: "kch"
source_database: "UniProt"
source_id: "P31069"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:8824224}; Multi-pass membrane protein {ECO:0000269|PubMed:8824224}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kch b1250 JW1242"
---

# kch

`protein.P31069`

## Static

- Type: `protein`
- Source: `UniProt:P31069`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:8824224}; Multi-pass membrane protein {ECO:0000269|PubMed:8824224}.

## Enriched Summary

FUNCTION: K(+)-specific ion channel. May play a role in the defense against osmotic shock. {ECO:0000269|PubMed:12912904, ECO:0000269|PubMed:8170937}. Kch is a member of the Voltage-gated Ion Channel (VIC) Superfamily of transporters . The regulation and functional properties of the protein have not been extensively studied; however, comparisons have often been made between Kch and the eukaryotic potassium channel proteins . Kch was solubilized and purified, and the biochemical properties and structure of the protein were examined . The physiological state of Kch is believed to be homotetrameric . Kch was shown to contain an interacting sequence tag corresponding to the oligomerization domain of the protein providing more evidence for oligomerization . The primary structure of Kch as well as experiments with PhoA fusions show the presence of six transmembrane helices with low overall sequence similarity to eukaryotic channels . However, the potassium specific pore region (P-region) is 60-70% identical to corresponding regions in various eukaryotic potassium channel proteins . kch gain-of-function mutants have been isolated which are sensitive to elevated potassium . Suppressor mutations have also been isolated within the K+ filter which rescue these mutants...

## Biological Role

Component of voltage-gated K+ channel (complex.ecocyc.CPLX0-7674).

## Annotation

FUNCTION: K(+)-specific ion channel. May play a role in the defense against osmotic shock. {ECO:0000269|PubMed:12912904, ECO:0000269|PubMed:8170937}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7674|complex.ecocyc.CPLX0-7674]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1250|gene.b1250]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31069`
- `KEGG:ecj:JW1242;eco:b1250;ecoc:C3026_07345;`
- `GeneID:945841;`
- `GO:GO:0005267; GO:0005886; GO:0006813; GO:0032991; GO:0042802; GO:0071805`

## Notes

Voltage-gated potassium channel Kch
