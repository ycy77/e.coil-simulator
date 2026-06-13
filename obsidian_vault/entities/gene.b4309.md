---
entity_id: "gene.b4309"
entity_type: "gene"
name: "nanS"
source_database: "NCBI RefSeq"
source_id: "gene-b4309"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4309"
  - "nanS"
---

# nanS

`gene.b4309`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4309`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nanS (gene.b4309) is a gene entity. It encodes nanS (protein.P39370). Encoded protein function: FUNCTION: Probably catalyzes the hydrolysis of the 9-O-acetyl group of 9-O-acetyl-N-acetylneuraminate (Neu5,9Ac2). Is required for growth of E.coli on Neu5,9Ac2, an alternative sialic acid commonly found in mammalian host mucosal sites, in particular in the human intestine. {ECO:0000269|PubMed:19749043}. EcoCyc product frame: G7919-MONOMER. EcoCyc synonyms: yjhS. Genomic coordinates: 4536614-4537594. EcoCyc protein note: N-ACETYL-9-O-ACETYLNEURAMINATE (Neu5,9Ac2) is a commonly occurring sialic acid in the human intestine and can be utilized as the sole source of carbon by E. coli. NanS is predicted to be periplasmic and catalyzes the hydrolysis of the 9-O-acetyl group of Neu5,9Ac2, thereby liberating N-ACETYLNEURAMINATE (Neu5Ac) . Earlier, the enzyme from E. coli O157:H7, whose amino acid sequence is 98% identical to that of K-12 MG1655, has been structurally and biochemically characterized. The Ser19 and His301 residues that were found to be essential for catalysis are conserved. Growth of E. coli on Neu5,9Ac2 requires nanS . nanS is not required for growth on glycerol minimal medium ; an earlier finding that nanS was required for growth on glycerol () may have been due to the particular strain used in that study...

## Biological Role

Repressed by nanR (protein.P0A8W0), nagC (protein.P0AF20). Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39370|protein.P39370]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=nanS; function=+
- `represses` <-- [[protein.P0A8W0|protein.P0A8W0]] `RegulonDB` `C` - regulator=NanR; target=nanS; function=-
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `C` - regulator=NagC; target=nanS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014130,ECOCYC:G7919,GeneID:948835`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4536614-4537594:-; feature_type=gene
