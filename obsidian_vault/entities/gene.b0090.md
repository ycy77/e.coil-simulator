---
entity_id: "gene.b0090"
entity_type: "gene"
name: "murG"
source_database: "NCBI RefSeq"
source_id: "gene-b0090"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0090"
  - "murG"
---

# murG

`gene.b0090`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0090`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

murG (gene.b0090) is a gene entity. It encodes murG (protein.P17443). Encoded protein function: FUNCTION: Cell wall formation (PubMed:1649817). Catalyzes the transfer of a GlcNAc subunit on undecaprenyl-pyrophosphoryl-MurNAc-pentapeptide (lipid intermediate I) to form undecaprenyl-pyrophosphoryl-MurNAc-(pentapeptide)GlcNAc (lipid intermediate II) (PubMed:12538870, PubMed:1649817). Strongly prefers UDP to CDP, GDP, ADP and TDP (PubMed:12538870). {ECO:0000269|PubMed:12538870, ECO:0000269|PubMed:1649817}. EcoCyc product frame: NACGLCTRANS-MONOMER. Genomic coordinates: 99644-100711. EcoCyc protein note: The murG gene codes for the N-acetylglucosaminyl transferase responsible for the final intracellular step of peptidoglycan subunit assembly. The transferase is associated with the cytoplasmic face of the inner membrane. Therefore, the entire peptidoglycan subunit is assembled before transport across the cytoplasmic membrane . The crystal structures of MurG by itself to a resolution of 1.9 Å and in a complex with its substrate UDP-GlcNAc to a resolution of 2.5 Å have been determined by X-ray crystallography. A temperature sensitive MurG mutant fails to localize to cell-division sites resulting in cell lysis...

## Biological Role

Repressed by pdhR (protein.P0ACL9), mraZ (protein.P22186).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01502` Vancomycin resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P17443|protein.P17443]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=murG; function=-
- `represses` <-- [[protein.P22186|protein.P22186]] `RegulonDB` `C` - regulator=MraZ; target=murG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000322,ECOCYC:EG10623,GeneID:946321`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:99644-100711:+; feature_type=gene
