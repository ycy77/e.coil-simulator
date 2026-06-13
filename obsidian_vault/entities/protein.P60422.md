---
entity_id: "protein.P60422"
entity_type: "protein"
name: "rplB"
source_database: "UniProt"
source_id: "P60422"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rplB b3317 JW3279"
---

# rplB

`protein.P60422`

## Static

- Type: `protein`
- Source: `UniProt:P60422`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: One of the primary rRNA binding proteins (PubMed:3298242). Located near the base of the L1 stalk, it is probably also mobile. Required for association of the 30S and 50S subunits to form the 70S ribosome, for tRNA binding and peptide bond formation (PubMed:8722025). It has been suggested to have peptidyltransferase activity; this is highly controversial. {ECO:0000269|PubMed:10756104, ECO:0000269|PubMed:11013226, ECO:0000269|PubMed:11114255, ECO:0000269|PubMed:12809609, ECO:0000269|PubMed:16272117, ECO:0000269|PubMed:3298242, ECO:0000269|PubMed:8722025}.; FUNCTION: In the E.coli 70S ribosome in the initiation state it has been modeled to make several contacts with the 16S rRNA (forming bridge B7b, PubMed:12809609); these contacts are broken in the model with bound EF-G. {ECO:0000269|PubMed:12809609}. The L2 protein is a component of the 50S subunit of the ribosome and is part of the peptidyltransferase center. L2 is highly evolutionarily conserved . L2 is required for the association of the 30S and 50S subunits ; one end of the elongated L2 protein is located at the intersubunit interface of the 50S subunit . L2 is involved in binding of tRNA to both the A and P sites, and the His229 residue appears to be important for peptidyl-transferase activity of the ribosome . A conserved region within L2 is required for assembly of L16 into the 50S ribosomal subunit...

## Biological Role

Component of 50S ribosomal subunit (complex.ecocyc.CPLX0-3962).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: One of the primary rRNA binding proteins (PubMed:3298242). Located near the base of the L1 stalk, it is probably also mobile. Required for association of the 30S and 50S subunits to form the 70S ribosome, for tRNA binding and peptide bond formation (PubMed:8722025). It has been suggested to have peptidyltransferase activity; this is highly controversial. {ECO:0000269|PubMed:10756104, ECO:0000269|PubMed:11013226, ECO:0000269|PubMed:11114255, ECO:0000269|PubMed:12809609, ECO:0000269|PubMed:16272117, ECO:0000269|PubMed:3298242, ECO:0000269|PubMed:8722025}.; FUNCTION: In the E.coli 70S ribosome in the initiation state it has been modeled to make several contacts with the 16S rRNA (forming bridge B7b, PubMed:12809609); these contacts are broken in the model with bound EF-G. {ECO:0000269|PubMed:12809609}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3962|complex.ecocyc.CPLX0-3962]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b3317|gene.b3317]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P60422`
- `KEGG:ecj:JW3279;eco:b3317;ecoc:C3026_18025;`
- `GeneID:86862285;93778670;947820;`
- `GO:GO:0000027; GO:0002181; GO:0003723; GO:0003735; GO:0005737; GO:0005829; GO:0008270; GO:0016740; GO:0019843; GO:0022625; GO:0032297; GO:1990082`

## Notes

Large ribosomal subunit protein uL2 (50S ribosomal protein L2)
