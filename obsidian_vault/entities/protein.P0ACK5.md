---
entity_id: "protein.P0ACK5"
entity_type: "protein"
name: "deoR"
source_database: "UniProt"
source_id: "P0ACK5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "deoR nucR b0840 JW0824"
---

# deoR

`protein.P0ACK5`

## Static

- Type: `protein`
- Source: `UniProt:P0ACK5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: This protein is one of the repressors that regulate the expression of deoCABD genes, which encode nucleotide and deoxy ribonucleotide catabolizing enzymes. It also negatively regulates the expression of nupG (a transport protein) and tsx (a pore-forming protein). The inducer is deoxyribose-5-phosphate. The transcriptional repressor DeoR, for "Deoxyribose Regulator," is involved in the negative expression of genes related to transport and catabolism of deoxyribonucleoside nucleotides . A transposon insertion mutation in the deoR gene produces cellular susceptibility to the antibiotic trimethoprim . On the other hand, inhibition of deoR expression by CRISPRi reduced cellular fitness under treatment with the antibiotic carbonyl cyanide 3-chlorophenylhydrazone (CCCP) . DeoR belongs to the DeoR family of transcriptional regulators . This protein consists of two domains, an amino-terminal domain that contains a potential helix-turn-helix DNA-binding motif and a carboxy-terminal domain involved in the oligomerization and the recognition of a possible co-inducer . DeoR is an octamer in solution and it forms multiple complexes (oligomers) in its target promoters; the cooperative binding of this regulator to different tandem inverted repeat sequences generates a repression DNA loop...

## Annotation

FUNCTION: This protein is one of the repressors that regulate the expression of deoCABD genes, which encode nucleotide and deoxy ribonucleotide catabolizing enzymes. It also negatively regulates the expression of nupG (a transport protein) and tsx (a pore-forming protein). The inducer is deoxyribose-5-phosphate.

## Outgoing Edges (4)

- `represses` --> [[gene.b4381|gene.b4381]] `RegulonDB` `S` - regulator=DeoR; target=deoC; function=-
- `represses` --> [[gene.b4382|gene.b4382]] `RegulonDB` `S` - regulator=DeoR; target=deoA; function=-
- `represses` --> [[gene.b4383|gene.b4383]] `RegulonDB` `S` - regulator=DeoR; target=deoB; function=-
- `represses` --> [[gene.b4384|gene.b4384]] `RegulonDB` `S` - regulator=DeoR; target=deoD; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0840|gene.b0840]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACK5`
- `KEGG:ecj:JW0824;eco:b0840;ecoc:C3026_05255;`
- `GeneID:75170909;945453;`
- `GO:GO:0000987; GO:0006355; GO:0098531; GO:2000143`

## Notes

Deoxyribose operon repressor
