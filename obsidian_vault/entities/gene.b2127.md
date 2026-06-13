---
entity_id: "gene.b2127"
entity_type: "gene"
name: "mlrA"
source_database: "NCBI RefSeq"
source_id: "gene-b2127"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2127"
  - "mlrA"
---

# mlrA

`gene.b2127`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2127`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mlrA (gene.b2127) is a gene entity. It encodes mlrA (protein.P33358). Encoded protein function: FUNCTION: Activates transcription of csgD, the master regulator of biofilm formation, by binding to its promoter region (PubMed:11489123, PubMed:20874755). Also controls the transcription of cadC and ibaG (PubMed:20874755). Part of a signaling cascade that regulates curli biosynthesis. The cascade is composed of two c-di-GMP control modules, in which c-di-GMP controlled by the DgcE/PdeH pair (module I) regulates the activity of the DgcM/PdeR pair (module II), which in turn regulates activity of the transcription factor MlrA (PubMed:23708798). {ECO:0000269|PubMed:11489123, ECO:0000269|PubMed:20874755, ECO:0000269|PubMed:23708798}. EcoCyc product frame: EG12008-MONOMER. EcoCyc synonyms: yehV. Genomic coordinates: 2214866-2215597. EcoCyc protein note: MlrA is a regulator of curli production in an avian pathogenic Escherichia coli strain and in Salmonella enterica serovar Typhimurium . Shiga toxin-encoding prophages have been observed to integrate at the mlrA gene of enterohemorrhagic E. coli . MlrA is a member of the MerR family, containing the conserved N-terminal DNA-binding domain present in members of this family...

## Biological Role

Repressed by fliZ (protein.P52627). Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33358|protein.P33358]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mlrA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=mlrA; function=+
- `represses` <-- [[protein.P52627|protein.P52627]] `RegulonDB` `C` - regulator=FliZ; target=mlrA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007030,ECOCYC:EG12008,GeneID:949029`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2214866-2215597:+; feature_type=gene
