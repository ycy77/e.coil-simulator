---
entity_id: "protein.P0A7W7"
entity_type: "protein"
name: "rpsH"
source_database: "UniProt"
source_id: "P0A7W7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpsH b3306 JW3268"
---

# rpsH

`protein.P0A7W7`

## Static

- Type: `protein`
- Source: `UniProt:P0A7W7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: One of the primary rRNA binding proteins, it binds directly to 16S rRNA central domain where it helps coordinate assembly of the platform of the 30S subunit. {ECO:0000250}.; FUNCTION: Protein S8 is a translational repressor protein, it controls the translation of the spc operon by binding to its mRNA. {ECO:0000269|PubMed:6262737}. The S8 protein is a component of the 30S subunit of the ribosome and also functions in the post-transcriptional regulation of the ribosomal protein genes encoded in the spc operon. The S8 protein binds to 16S rRNA in the absence of other ribosomal proteins . S8 binding is not absolutely required for assembly of the 30S ribosomal subunit platform, but it influences the organization of the 16S rRNA central domain . Sites within 16S rRNA where S8 interacts have been determined , and the secondary and tertiary structure of the binding region has been investigated . The unique cysteine residue present in S8 is essential for 16S rRNA binding , although it may not be involved in RNA recognition . Other sequence determinants important for 16S rRNA binding have been investigated . The affinity of S8 for 16S rRNA and thus the stability of the complex is correlated with the optimal growth temperature of various organisms...

## Biological Role

Component of 30S ribosomal subunit (complex.ecocyc.CPLX0-3953).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: One of the primary rRNA binding proteins, it binds directly to 16S rRNA central domain where it helps coordinate assembly of the platform of the 30S subunit. {ECO:0000250}.; FUNCTION: Protein S8 is a translational repressor protein, it controls the translation of the spc operon by binding to its mRNA. {ECO:0000269|PubMed:6262737}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (13)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3953|complex.ecocyc.CPLX0-3953]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b3299|gene.b3299]] `RegulonDB` `S` - regulator=RpsH; target=rpmJ; function=-
- `represses` --> [[gene.b3300|gene.b3300]] `RegulonDB` `S` - regulator=RpsH; target=secY; function=-
- `represses` --> [[gene.b3301|gene.b3301]] `RegulonDB` `S` - regulator=RpsH; target=rplO; function=-
- `represses` --> [[gene.b3302|gene.b3302]] `RegulonDB` `S` - regulator=RpsH; target=rpmD; function=-
- `represses` --> [[gene.b3303|gene.b3303]] `RegulonDB` `S` - regulator=RpsH; target=rpsE; function=-
- `represses` --> [[gene.b3304|gene.b3304]] `RegulonDB` `S` - regulator=RpsH; target=rplR; function=-
- `represses` --> [[gene.b3305|gene.b3305]] `RegulonDB` `S` - regulator=RpsH; target=rplF; function=-
- `represses` --> [[gene.b3306|gene.b3306]] `RegulonDB` `S` - regulator=RpsH; target=rpsH; function=-
- `represses` --> [[gene.b3307|gene.b3307]] `RegulonDB` `S` - regulator=RpsH; target=rpsN; function=-
- `represses` --> [[gene.b3308|gene.b3308]] `RegulonDB` `S` - regulator=RpsH; target=rplE; function=-
- `represses` --> [[gene.b3309|gene.b3309]] `RegulonDB` `S` - regulator=RpsH; target=rplX; function=-
- `represses` --> [[gene.b3310|gene.b3310]] `RegulonDB` `S` - regulator=RpsH; target=rplN; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3306|gene.b3306]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7W7`
- `KEGG:ecj:JW3268;eco:b3306;ecoc:C3026_17970;`
- `GeneID:86862296;93778681;947802;`
- `GO:GO:0000028; GO:0002181; GO:0003735; GO:0005737; GO:0005829; GO:0006417; GO:0019843; GO:0022627; GO:0043488`

## Notes

Small ribosomal subunit protein uS8 (30S ribosomal protein S8)
