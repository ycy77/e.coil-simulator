---
entity_id: "gene.b3189"
entity_type: "gene"
name: "murA"
source_database: "NCBI RefSeq"
source_id: "gene-b3189"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3189"
  - "murA"
---

# murA

`gene.b3189`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3189`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

murA (gene.b3189) is a gene entity. It encodes murA (protein.P0A749). Encoded protein function: FUNCTION: Cell wall formation (PubMed:1512209). Adds enolpyruvyl to UDP-N-acetylglucosamine (PubMed:1512209, PubMed:20392080). Target for the antibiotic fosfomycin. {ECO:0000269|PubMed:1512209, ECO:0000269|PubMed:20392080}. EcoCyc product frame: UDPNACETYLGLUCOSAMENOLPYRTRANS-MONOMER. EcoCyc synonyms: mrbA, murZ. Genomic coordinates: 3335235-3336494. EcoCyc protein note: UDP-N-acetylglucosamine enolpyruvoyl transferase (MurA) catalyzes the first committed step in the assembly of peptidoglycan . In exponentially growing cells, the intracellular concentration of UDP-N-acetylglucosamine is approximately 100 µM, while the concentration of the MurA product, UDP-N-acetylglucosamine enolpyruvate is only 2 µM . MurA activity is feedback-inhibited by UDP-MurNAc, the product of the second enzyme in the PWY-6387 pathway . The reaction mechanism of the enzyme has been investigated. A tetrahedral adduct can be formed at the active site of the enzyme during catalyis . However, covalent enzyme adduct formation is not required for catalysis . The stereochemical course of the reaction has been investigated . Catalysis involves conformational transitions within the enzyme . MurA is the site of action for the antibiotic fosfomycin...

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A749|protein.P0A749]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010479,ECOCYC:EG11358,GeneID:947703`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3335235-3336494:-; feature_type=gene
