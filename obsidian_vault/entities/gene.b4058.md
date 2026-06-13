---
entity_id: "gene.b4058"
entity_type: "gene"
name: "uvrA"
source_database: "NCBI RefSeq"
source_id: "gene-b4058"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4058"
  - "uvrA"
---

# uvrA

`gene.b4058`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4058`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uvrA (gene.b4058) is a gene entity. It encodes uvrA (protein.P0A698). Encoded protein function: FUNCTION: The UvrABC repair system catalyzes the recognition and processing of DNA lesions. UvrA is an ATPase and a DNA-binding protein. A damage recognition complex composed of 2 UvrA and 2 UvrB subunits scans DNA for abnormalities. When the presence of a lesion has been verified by UvrB, the UvrA molecules dissociate. {ECO:0000255|HAMAP-Rule:MF_00205}. EcoCyc product frame: EG11061-MONOMER. EcoCyc synonyms: dar, dinE. Genomic coordinates: 4271049-4273871. EcoCyc protein note: uvrA encodes one of the three key proteins of the nucleotide excision repair (NER) pathway. UvrA forms homodimers in the presence of ATP , and at physiological concentrations UvrA associaties with UvrB to form a UvrA2B complex in an ATP-dependent interaction . UvrA binds DNA as a dimer with a strong preference for DNA ends . uvrA insertion mutants were identified in a genetic screen for genes that are important for survival of exposure to ionizing radiation (IR). A uvrA deletion mutant has a substantial decrease in IR survival . Deletion of uvrA results in a significant decrease in persister fraction following fluoroquinolone treatment; the absence of uvrA impedes persister awakening .

## Biological Role

Repressed by arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03420` Nucleotide excision repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A698|protein.P0A698]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=uvrA; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=uvrA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013290,ECOCYC:EG11061,GeneID:948559`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4271049-4273871:-; feature_type=gene
