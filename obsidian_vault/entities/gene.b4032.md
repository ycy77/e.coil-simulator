---
entity_id: "gene.b4032"
entity_type: "gene"
name: "malG"
source_database: "NCBI RefSeq"
source_id: "gene-b4032"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4032"
  - "malG"
---

# malG

`gene.b4032`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4032`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

malG (gene.b4032) is a gene entity. It encodes malG (protein.P68183). Encoded protein function: FUNCTION: Part of the ABC transporter complex MalEFGK involved in maltose/maltodextrin import. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:2026607, ECO:0000269|PubMed:2155217}. EcoCyc product frame: MALG-MONOMER. Genomic coordinates: 4242626-4243516. EcoCyc protein note: MalG is an integral membrane component of the maltose ABC transporter . A MalG-MalF heterodimer forms the translocation channel of the maltose ABC transporter; the MalG-MalF channel contacts the MalK dimer at the cytoplasmic face of the membrane and the MalE binding protein at the periplasmic face of the membrane MalG contains 6 transmembrane (TM) helices; in a crystal structure of the maltose transporter in complex with MalE, maltose and ATP, an EAA loop located between TM4 and 5 is a major area of contact with the MalK dimer while a C-terminal tail region (residues 290296) packs along the Q loop of one MalK monomer .

## Biological Role

Activated by rpoD (protein.P00579), malT (protein.P06993), fis (protein.P0A6R3), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P68183|protein.P68183]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=malG; function=+
- `activates` <-- [[protein.P06993|protein.P06993]] `RegulonDB` `C` - regulator=MalT; target=malG; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=malG; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=malG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013193,ECOCYC:EG10556,GeneID:948530`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4242626-4243516:-; feature_type=gene
