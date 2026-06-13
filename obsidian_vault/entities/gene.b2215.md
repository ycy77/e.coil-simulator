---
entity_id: "gene.b2215"
entity_type: "gene"
name: "ompC"
source_database: "NCBI RefSeq"
source_id: "gene-b2215"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2215"
  - "ompC"
---

# ompC

`gene.b2215`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2215`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ompC (gene.b2215) is a gene entity. It encodes ompC (protein.P06996). Encoded protein function: FUNCTION: Forms pores that allow passive diffusion of small molecules across the outer membrane.; FUNCTION: (Microbial infection) Supports colicin E5 entry in the absence of its major receptor OmpF. {ECO:0000305|PubMed:27723824}.; FUNCTION: (Microbial infection) A mixed OmpC-OmpF heterotrimer is the outer membrane receptor for toxin CdiA-EC536; polymorphisms in extracellular loops 4 and 5 of OmpC confer susceptibility to CdiA-EC536-mediated toxicity. {ECO:0000269|PubMed:27723824}. EcoCyc product frame: EG10670-MONOMER. EcoCyc synonyms: meoA, par. Genomic coordinates: 2311646-2312749. EcoCyc protein note: OmpC is a general outer membrane (OM) porin which mediates the non-specific diffusion of small solutes such as sugars, ions and amino acids; the major non-specific OM porins of E. coli K-12 (OmpC and CPLX0-7534 "OmpF") are typically defined by an exclusion limit based on substrate mass (~600 daltons) but there are large differences in penetration rates within solutes due to factors such as size, hydrophobicity and charge (discussed in ). OmpC acts as a receptor for bacteriophages 434, T4 and Bp7 (see and further ). Purified OmpC reconstituted into artificial lipid bilayer membranes forms an ion permeable channel with a slight preference for cations...

## Biological Role

Repressed by micC (gene.b4427), lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), ompR (protein.P0AA16), cpxR (protein.P0AE88).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06996|protein.P06996]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=ompC; function=+
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `C` - regulator=OmpR; target=ompC; function=+
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=ompC; function=+
- `represses` <-- [[gene.b4427|gene.b4427]] `RegulonDB` `S` - regulator=MicC; target=ompC; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=ompC; function=-

## External IDs

- `Dbxref:ECOCYC:EG10670,GeneID:946716`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2311646-2312749:-; feature_type=gene
