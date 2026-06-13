---
entity_id: "gene.b4722"
entity_type: "gene"
name: "idlP"
source_database: "NCBI RefSeq"
source_id: "gene-b4722"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4722"
  - "idlP"
---

# idlP

`gene.b4722`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4722`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

idlP (gene.b4722) is a gene entity. It encodes idlP (protein.P0DPC6). Encoded protein function: FUNCTION: A short protein whose stop codon overlaps with the start codon of downstream iraD; its mRNA secondary structure is predicted to fold and sequester the Shine-Dalgarno sequence of iraD. When this protein is expressed the downstream iraD is also expressed due to ribosomal coupling (PubMed:28851853). {ECO:0000269|PubMed:28851853}. EcoCyc product frame: MONOMER0-4390. Genomic coordinates: 4556913-4556996. EcoCyc protein note: The iraD leader peptide is encoded upstream of G7923-MONOMER; its translation is negatively regulated by the EG11447-MONOMER CsrA. The stop codon of the leader peptide overlaps the IraD start codon, and IraD translation is coupled to that of the leader peptide. CsrA thus also negatively regulates IraD translation . IdlP: "iraD leader peptide"

## Biological Role

Repressed by dnaA (protein.P03004), csrA (protein.P69913). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DPC6|protein.P0DPC6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=idlP; function=+
- `represses` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `C` - regulator=DnaA; target=idlP; function=-
- `represses` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `S` - regulator=CsrA; target=idlP; function=-

## External IDs

- `Dbxref:ECOCYC:G0-16685,GeneID:38094980`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4556913-4556996:+; feature_type=gene
