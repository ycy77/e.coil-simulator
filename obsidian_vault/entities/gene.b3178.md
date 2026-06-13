---
entity_id: "gene.b3178"
entity_type: "gene"
name: "ftsH"
source_database: "NCBI RefSeq"
source_id: "gene-b3178"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3178"
  - "ftsH"
---

# ftsH

`gene.b3178`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3178`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ftsH (gene.b3178) is a gene entity. It encodes ftsH (protein.P0AAI3). Encoded protein function: FUNCTION: Acts as a processive, ATP-dependent zinc metallopeptidase for both cytoplasmic and membrane proteins. Plays a role in the quality control of integral membrane proteins. Degrades a few membrane proteins that have not been assembled into complexes such as SecY, F(0) ATPase subunit a and YccA, and also cytoplasmic proteins sigma-32, LpxC, KdtA and phage lambda cII protein among others. Degrades membrane proteins in a processive manner starting at either the N- or C-terminus; recognition requires a cytoplasmic tail of about 20 residues with no apparent sequence requirements. It presumably dislocates membrane-spanning and periplasmic segments of the protein into the cytoplasm to degrade them, this probably requires ATP. Degrades C-terminal-tagged cytoplasmic proteins which are tagged with an 11-amino-acid nonpolar destabilizing tail via a mechanism involving the 10SA (SsrA) stable RNA.; FUNCTION: As FtsH regulates the levels of both LpxC and KdtA it is required for synthesis of both the protein and lipid components of lipopolysaccharide (LPS). {ECO:0000269|PubMed:18776015}.; FUNCTION: (Microbial infection) Probably transports the toxic C-terminal region of CdiA from E.coli strain 536, E.cloacae strain ATCC 13047 and of Y...

## Biological Role

Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAI3|protein.P0AAI3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ftsH; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=ftsH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010444,ECOCYC:EG11506,GeneID:947690`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3325001-3326935:-; feature_type=gene
