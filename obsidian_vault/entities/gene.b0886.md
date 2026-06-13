---
entity_id: "gene.b0886"
entity_type: "gene"
name: "cydC"
source_database: "NCBI RefSeq"
source_id: "gene-b0886"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0886"
  - "cydC"
---

# cydC

`gene.b0886`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0886`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cydC (gene.b0886) is a gene entity. It encodes cydC (protein.P23886). Encoded protein function: FUNCTION: Part of the ABC transporter complex CydDC that exports the reduced low-molecular-weight thiols cysteine and glutathione to the periplasm (PubMed:12393891, PubMed:16040611). Export of these thiol-containing redox-active molecules may be crucial for redox homeostasis in the periplasm, permitting correct assembly of various respiratory complexes and formation of correct disulfide bonds in periplasmic and secreted proteins (Probable). CydC contains transmembrane domains (TMD), which form a pore in the inner membrane, and an ATP-binding domain (NBD), which is responsible for energy generation (PubMed:24958725). Required for the assembly of functional cytochrome bd-type quinol oxidases and periplasmic c-type cytochromes (PubMed:15470119, PubMed:3032907, PubMed:7934832, PubMed:8181727). Overexpression of CydDC under anaerobic conditions also results in the formation of a heme biosynthesis-derived pigment, P-574 (PubMed:12375104). CydDC binds heme b, but heme is probably not transported by the complex and instead has a role in regulating ATPase activity (PubMed:24958725)...

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), arcA (protein.P0A9Q1).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23886|protein.P23886]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cydC; function=+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=cydC; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003012,ECOCYC:EG10012,GeneID:945504`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:927474-929195:-; feature_type=gene
