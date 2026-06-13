---
entity_id: "gene.b3729"
entity_type: "gene"
name: "glmS"
source_database: "NCBI RefSeq"
source_id: "gene-b3729"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3729"
  - "glmS"
---

# glmS

`gene.b3729`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3729`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glmS (gene.b3729) is a gene entity. It encodes glmS (protein.P17169). Encoded protein function: FUNCTION: Catalyzes the first step in hexosamine metabolism, converting fructose-6P into glucosamine-6P using glutamine as a nitrogen source. EcoCyc product frame: L-GLN-FRUCT-6-P-AMINOTRANS-MONOMER. Genomic coordinates: 3911839-3913668. EcoCyc protein note: L-glutamine:D-fructose-6-phosphate aminotransferase, or GFAT, catalyzes the first step in hexosamine biosynthesis. The enzyme uses a nucleophilic attack by the thiol group of Cys1 on the δ-carbonyl group of glutamine to form ammonia, which is then channeled through the enzyme to the acceptor group on fructose-6-phosphate. The enzyme can not use exogenous ammonia as the nitrogen donor . The N-terminal domain contains the glutamine amidohydrolase activity, and the C-terminal domain contains the ketose/aldose isomerase activity . Crystal structures of the isolated domains and the full length enzyme have been solved . An 18 Å hydrophobic channel provides a conduit for the transfer of ammonia from the glutamine amidohydrolase active site to the isomerase active site . Molecular dynamics simulations and kinetic analysis of mutants identified roles for W74, A602 and V605 in the opening and closing of the ammonia channel . Major structural changes occur during the catalytic cycle...

## Biological Role

Repressed by nagC (protein.P0AF20). Activated by rpoD (protein.P00579), nagC (protein.P0AF20).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P17169|protein.P17169]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=glmS; function=+
- `activates` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `C` - regulator=NagC; target=glmS; function=-+
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `C` - regulator=NagC; target=glmS; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0012198,ECOCYC:EG10382,GeneID:948241`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3911839-3913668:-; feature_type=gene
