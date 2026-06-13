---
entity_id: "protein.P0A7K2"
entity_type: "protein"
name: "rplL"
source_database: "UniProt"
source_id: "P0A7K2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rplL b3986 JW3949"
---

# rplL

`protein.P0A7K2`

## Static

- Type: `protein`
- Source: `UniProt:P0A7K2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: The binding site for several of the GTPase factors involved in protein synthesis (IF-2, EF-Tu, EF-G and RF3). Is thus essential for accurate translation. Deletion of 1 of the L12 dimers from the ribosome (by deleting the binding site on L10) leads to decreased IF-2 association with the 70S ribosome and decreased stimulation of the GTPase activity of EF-G. {ECO:0000269|PubMed:15989950, ECO:0000269|PubMed:22102582}. MONOMER0-2811 is the N-acetylated form of 50S ribosomal subunit protein L12 .

## Biological Role

Component of 50S ribosomal subunit protein L7/L12 dimer (complex.ecocyc.CPLX0-3955), 50S ribosomal protein complex L8 (complex.ecocyc.CPLX0-3956).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: The binding site for several of the GTPase factors involved in protein synthesis (IF-2, EF-Tu, EF-G and RF3). Is thus essential for accurate translation. Deletion of 1 of the L12 dimers from the ribosome (by deleting the binding site on L10) leads to decreased IF-2 association with the 70S ribosome and decreased stimulation of the GTPase activity of EF-G. {ECO:0000269|PubMed:15989950, ECO:0000269|PubMed:22102582}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3955|complex.ecocyc.CPLX0-3955]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-3956|complex.ecocyc.CPLX0-3956]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3986|gene.b3986]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7K2`
- `KEGG:ecj:JW3949;eco:b3986;ecoc:C3026_21530;`
- `GeneID:86861613;86944525;948489;`
- `GO:GO:0002181; GO:0003729; GO:0003735; GO:0005737; GO:0005829; GO:0006412; GO:0015934; GO:0022625; GO:0042803; GO:0043022`

## Notes

Large ribosomal subunit protein bL12 (50S ribosomal protein L7/L12) (L8)
