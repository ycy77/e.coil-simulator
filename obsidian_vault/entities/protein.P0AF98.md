---
entity_id: "protein.P0AF98"
entity_type: "protein"
name: "lptF"
source_database: "UniProt"
source_id: "P0AF98"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lptF yjgP b4261 JW4218"
---

# lptF

`protein.P0AF98`

## Static

- Type: `protein`
- Source: `UniProt:P0AF98`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex LptBFG involved in the translocation of lipopolysaccharide (LPS) from the inner membrane to the outer membrane. {ECO:0000269|PubMed:18375759}. LptF is an essential inner membrane component of the Lpt lipopolysaccharide (LPS) transport system. LptF contains six predicted transmembrane domains with the C-terminus located in the cytoplasm . lptF is essential . Depletion of LptF (and/or LptG) results in a filamenting phenotype, increased sensitivity to hydrophobic antibiotics and an altered form of LPS; LptFG are required for LPS to reach the outer leaflet of the outer membrane . LptF forms a complex with LptG, LptB and LptC . LptF and LptG each contain a coupling helix which mediates their interaction with LptB; the LptFG coupling helices likely coordinate ATPase activity with LPS extraction from the inner membrane but each appears to have a distinct role (see further ). lptF has been the subject of a pilot study to examine genetic interactions involving essential genes .

## Biological Role

Component of lipopolysaccharide transport system (complex.ecocyc.CPLX0-7992).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex LptBFG involved in the translocation of lipopolysaccharide (LPS) from the inner membrane to the outer membrane. {ECO:0000269|PubMed:18375759}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7992|complex.ecocyc.CPLX0-7992]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4261|gene.b4261]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AF98`
- `KEGG:ecj:JW4218;eco:b4261;ecoc:C3026_22985;`
- `GeneID:75169782;75203518;948795;`
- `GO:GO:0005886; GO:0015920; GO:0016020; GO:0043165; GO:0043190; GO:0055085; GO:1990351`

## Notes

Lipopolysaccharide export system permease protein LptF
