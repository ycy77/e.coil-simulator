---
entity_id: "gene.b1131"
entity_type: "gene"
name: "purB"
source_database: "NCBI RefSeq"
source_id: "gene-b1131"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1131"
  - "purB"
---

# purB

`gene.b1131`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1131`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

purB (gene.b1131) is a gene entity. It encodes purB (protein.P0AB89). Encoded protein function: FUNCTION: Catalyzes two reactions in de novo purine nucleotide biosynthesis. Catalyzes the breakdown of 5-aminoimidazole- (N-succinylocarboxamide) ribotide (SAICAR or 2-[5-amino-1-(5-phospho-beta-D-ribosyl)imidazole-4-carboxamido]succinate) to 5-aminoimidazole-4-carboxamide ribotide (AICAR or 5-amino-1-(5-phospho-beta-D-ribosyl)imidazole-4-carboxamide) and fumarate, and of adenylosuccinate (ADS or N(6)-(1,2-dicarboxyethyl)-AMP) to adenosine monophosphate (AMP) and fumarate. {ECO:0000269|PubMed:17531264}.; FUNCTION: (Microbial infection) Catalyzes the conversion of 2-amino-2'-deoxyadenylo-succinate to dZMP and fumarate, when the bacterium is infected by a phage that produces the substrate of this reaction, a step in the synthesis of dZTP (2-amino-2'-deoxyadenosine 5'-triphosphate), which is a nucleotide then used by the phage as a DNA polymerase substrate. {ECO:0000269|PubMed:33926954}. EcoCyc product frame: ASL-MONOMER. EcoCyc synonyms: ade(h), ade. Genomic coordinates: 1190616-1191986.

## Biological Role

Repressed by purR (protein.P0ACP7). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB89|protein.P0AB89]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=purB; function=+
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `S` - regulator=PurR; target=purB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003810,ECOCYC:EG11314,GeneID:945695`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1190616-1191986:-; feature_type=gene
