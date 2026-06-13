---
entity_id: "protein.P02932"
entity_type: "protein"
name: "phoE"
source_database: "UniProt"
source_id: "P02932"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:2464593}; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "phoE ompE b0241 JW0231"
---

# phoE

`protein.P02932`

## Static

- Type: `protein`
- Source: `UniProt:P02932`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:2464593}; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Uptake of inorganic phosphate, phosphorylated compounds, and some other negatively charged solutes. PhoE is a member of the General Bacterial Porin (GBP) family. These proteins are present in the outer membranes of Gram negative bacteria, mitochondria, and plastids. Induced by phosphate limitation, PhoE facilitates efficient diffusion of phosphate and phosphorus-containing compounds across the outer membrane . PhoE specificity is defined by the pore's composition; PhoE is believed to have a preference for small anions due to a collection of positively charged amino acids near the pore entrance . Therefore PhoE is not a specific transport system, rather, it is a water filled channel allowing for passive diffusion of small molecules (~600 Da). Structural studies indicate that PhoE is a trimer of 16-stranded β-barrel monomers with large loops that fold inside the β-barrel, and the amino terminus faces the periplasm . Charged residues within the constriction zone of the pore may act as voltage gating sensors . PhoE activity is inhibited by ATP which blocks ion flow through the porin . Targeting of PhoE to the Sec-translocase for transport across the inner membrane is SecB-dependent . Protein cross-linking studies indicate the transmembrane form of PhoE interacts with Skp at the periplasmic side of the inner membrane...

## Biological Role

Component of outer membrane porin PhoE (complex.ecocyc.CPLX0-7530).

## Annotation

FUNCTION: Uptake of inorganic phosphate, phosphorylated compounds, and some other negatively charged solutes.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7530|complex.ecocyc.CPLX0-7530]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b0241|gene.b0241]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P02932`
- `KEGG:ecj:JW0231;eco:b0241;ecoc:C3026_01145;ecoc:C3026_23880;`
- `GeneID:93777152;944926;`
- `GO:GO:0009279; GO:0015288; GO:0034220; GO:0046930`

## Notes

Outer membrane porin PhoE (Outer membrane pore protein E)
